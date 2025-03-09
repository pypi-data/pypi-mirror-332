from argparse import ArgumentParser
from decimal import Decimal
from tempfile import gettempdir
from exiftool.exceptions import ExifToolExecuteError
from os import chmod
from PIL import Image
from magic import from_file
from typing import Any
from tzlocal import get_localzone
from zoneinfo import ZoneInfo
from datetime import datetime
from json import loads
from re import sub, search, IGNORECASE
from exiftool import ExifToolHelper
from os import makedirs, walk
from os.path import exists, join
from dataclasses import dataclass
from shutil import copy

from takeout_prepper.parsing import dir_path


@dataclass
class Asset:
    filename: str
    absolute_input_path: str
    relative_parent: str
    absolute_metadata_path: str


@dataclass
class ExtractedMetadata:
    date_taken: datetime
    latitude: Decimal | None
    longitude: Decimal | None


@dataclass
class InferredTimezone:
    tzinfo: Any  # tzinfo
    fell_back_to_system_timezone: bool


@dataclass
class ProcessingOutcome:
    exif_added: bool
    exif_modified: bool
    fell_back_to_system_timezone: bool
    detected_input_file_corruption: bool


def _match_metadata_file(root: str, filename_to_test: str) -> str | None:
    joined_path = join(root, f"{filename_to_test}.json")
    if exists(joined_path):
        return joined_path
    return None


def _find_metadata_path(root: str, filename: str) -> str:
    if filename_match := _match_metadata_file(root, filename):
        return filename_match

    # Takeout seems to use a max filename length of 51 characters
    filename_to_test = filename[0:46]
    if filename_match := _match_metadata_file(root, filename_to_test):
        return filename_match

    # JSON files never seem to include an '-edited' suffix
    filename_to_test = sub(r"-edited(\.[a-zA-Z]+)$", r"\1", filename)[0:46]
    if filename_match := _match_metadata_file(root, filename_to_test):
        return filename_match

    # Sometimes the -edited suffix gets chopped off for the 51-char limit
    filename_to_test = sub(
        r"(?:-(?:e(?:d(?:i(?:t(?:e(?:d)?)?)?)?)?)?)?(\.[a-zA-Z]+)$", r"\1", filename
    )[0:46]
    if filename_match := _match_metadata_file(root, filename_to_test):
        return filename_match

    raise Exception(f"No corresponding metadata file found for {root}/{filename}")


def find_assets(input_directory: str):
    for root, dirs, files in walk(input_directory):
        for name in files:
            if not search(r"\.(html|json|mp)$", name, flags=IGNORECASE):
                if name.endswith(".MP4"):
                    jpg_equivalent = sub(r"\.mp4$", ".jpg", name)

                    if exists(join(root, jpg_equivalent)):
                        print(
                            f"Ignoring {name} because it's auxiliary footage to {jpg_equivalent}"
                        )
                        continue

                metadata_path = _find_metadata_path(root, name)

                yield Asset(
                    filename=name,
                    absolute_input_path=join(root, name),
                    relative_parent=root[len(input_directory) :],
                    absolute_metadata_path=metadata_path,
                )


def _infer_preferred_timezone(filename: str, original_exif: Any) -> InferredTimezone:
    # Ideally, use the timezone from the original asset
    try:
        original_timestamp = datetime.strptime(
            f"{original_exif['EXIF:DateTimeOriginal']}{original_exif['EXIF:OffsetTimeOriginal']}",
            "%Y:%m:%d %H:%M:%S%z",
        )
        return InferredTimezone(
            tzinfo=original_timestamp.tzinfo, fell_back_to_system_timezone=False
        )
    except KeyError:
        return InferredTimezone(
            tzinfo=get_localzone(), fell_back_to_system_timezone=True
        )


def _extract_metadata(absolute_metadata_path: str) -> ExtractedMetadata:
    with open(absolute_metadata_path, "r") as metadata_handle:
        json_payload = loads(metadata_handle.read())

    # Warning: these timestamps are not actually UTC-encoded, so we have to parse them
    # the hard way. strptime doesn't store timezone, so scrape it manually.
    raw_asset_taken_time = json_payload["photoTakenTime"]["formatted"]
    asset_taken_time = datetime.strptime(
        raw_asset_taken_time, "%b %d, %Y, %I:%M:%S %p %Z"
    )
    timezone_matcher = search(r"\b(\w+)$", json_payload["photoTakenTime"]["formatted"])
    assert timezone_matcher, json_payload["photoTakenTime"]["formatted"]
    raw_timezone = timezone_matcher.groups()[0]
    asset_taken_time = asset_taken_time.replace(tzinfo=ZoneInfo(raw_timezone))

    latitude = None
    longitude = None
    raw_latitude = json_payload["geoData"]["latitude"]
    raw_longitude = json_payload["geoData"]["longitude"]
    if raw_latitude:
        latitude = Decimal(raw_latitude)
    if raw_longitude:
        longitude = Decimal(raw_longitude)

    return ExtractedMetadata(
        date_taken=asset_taken_time,
        latitude=latitude,
        longitude=longitude,
    )


def _determine_exif_added_modified_status(
    exif_current: dict, exif_new: dict
) -> tuple[bool, bool]:
    # Never remove EXIF keys
    assert set(exif_current.keys()) <= set(exif_new.keys())

    exif_added = len(exif_current.keys()) < len(exif_new.keys())
    if exif_current != exif_new:
        for key in exif_current.keys():
            if key != "SourceFile" and exif_current[key] != exif_new[key]:
                return exif_added, True

    return exif_added, False


def _process_asset(
    asset: Asset, target_root: str, exif_helper: ExifToolHelper
) -> ProcessingOutcome:
    TAGS_TO_COMPARE = [
        "EXIF:DateTimeOriginal",
        "EXIF:OffsetTimeOriginal",
        "QuickTime:CreateDate",
        "GPSLatitude",
        "GPSLongitude",
    ]
    detected_file_corruption = False
    target_filename = join(target_root, asset.relative_parent, asset.filename)
    extracted_metadata = _extract_metadata(asset.absolute_metadata_path)

    exif_current = exif_helper.get_tags(
        files=[asset.absolute_input_path],
        tags=TAGS_TO_COMPARE,
    )[0]

    # Shift date taken to preferred timezone
    inferred_timezone = _infer_preferred_timezone(
        asset.absolute_input_path, exif_current
    )
    asset_taken_time = extracted_metadata.date_taken.astimezone(
        inferred_timezone.tzinfo
    )

    # Take offset from preferred timezone to save it along the local timestamp
    offset = asset_taken_time.strftime("%z")
    transformed_offset = f"{offset[0:3]}:{offset[3:5]}"

    exiftool_params = ["-o", target_filename]
    tags_to_write = {
        "EXIF:DateTimeOriginal": asset_taken_time.strftime("%Y:%m:%d %H:%M:%S"),
        "EXIF:OffsetTimeOriginal": transformed_offset,
        "QuickTime:CreateDate": f"{asset_taken_time.strftime('%Y:%m:%d %H:%M:%S')}{transformed_offset}",
    }
    if extracted_metadata.latitude and extracted_metadata.longitude:
        tags_to_write["GPSLatitude"] = str(extracted_metadata.latitude)
        tags_to_write["GPSLatitudeRef"] = (
            "N" if extracted_metadata.latitude >= 0 else "S"
        )
        tags_to_write["GPSLongitude"] = str(extracted_metadata.longitude)
        tags_to_write["GPSLongitudeRef"] = (
            "E" if extracted_metadata.latitude >= 0 else "W"
        )

    try:
        exif_helper.set_tags(
            files=[asset.absolute_input_path],
            tags=tags_to_write,
            params=exiftool_params,
        )
    except ExifToolExecuteError as e:
        print(f"Error writing EXIF for {asset.filename}. Retrying with -m. {e.stderr}")
        exif_helper.set_tags(
            files=[asset.absolute_input_path],
            tags=tags_to_write,
            params=exiftool_params + ["-m"],
        )
        detected_file_corruption = True
    exif_new = exif_helper.get_tags(
        files=[target_filename],
        tags=TAGS_TO_COMPARE,
    )[0]

    added, modified = _determine_exif_added_modified_status(exif_current, exif_new)
    return ProcessingOutcome(
        exif_added=added,
        exif_modified=modified,
        fell_back_to_system_timezone=inferred_timezone.fell_back_to_system_timezone,
        detected_input_file_corruption=detected_file_corruption,
    )


def _print_assets_if_verbose(verbose: bool, assets: list[Asset]):
    if verbose:
        for asset in assets:
            print(f" - {asset.relative_parent}/{asset.filename}")


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "input_directory", type=dir_path, help="Your unzipped Google Photos folder"
    )
    parser.add_argument(
        "output_directory",
        help="Output folder for modified pictures",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Be more verbose about actions that were taken",
    )
    args = parser.parse_args()

    try:
        makedirs(args.output_directory)
    except FileExistsError:
        print(f"Directory {args.output_directory} exists. Aborting for safety reasons.")
        exit(1)

    assets_with_exif_added = []
    assets_with_exif_modified = []
    assets_with_exif_unsupported = []
    assets_converted_to_jpg = []
    assets_normalized_jpg_extension = []
    assets_with_timezone_fallback = []
    assets_with_input_file_corruption = []
    assets_handled = 0

    with ExifToolHelper() as exif_helper:
        for i, asset in enumerate(find_assets(args.input_directory)):
            if i % 50 == 0 and i > 0:
                print(f"Processed {i} assets so far")

            makedirs(join(args.output_directory, asset.relative_parent), exist_ok=True)

            # Sometimes images have the wrong extension
            # Outsmart the files
            inferred_mimetype = from_file(asset.absolute_input_path, mime=True)

            try:
                if inferred_mimetype == "image/png":
                    png_asset = Image.open(asset.absolute_input_path)
                    png_asset = png_asset.convert("RGB")
                    jpgified_path = join(
                        gettempdir(),
                        sub(r"\.png$", ".jpg", asset.filename, flags=IGNORECASE),
                    )
                    png_asset.save(jpgified_path)
                    jpgified_asset = Asset(
                        absolute_input_path=jpgified_path,
                        absolute_metadata_path=asset.absolute_metadata_path,
                        filename=sub(
                            r"\.png", ".jpg", asset.filename, flags=IGNORECASE
                        ),
                        relative_parent=asset.relative_parent,
                    )
                    outcome = _process_asset(
                        jpgified_asset, args.output_directory, exif_helper
                    )
                    assets_converted_to_jpg.append(asset)
                elif inferred_mimetype == "image/jpeg" and not search(
                    r"\.dng$", asset.filename
                ):
                    # If file extension doesn't match, copy file to temporary location with JPG extension so exiftool doesn't panic
                    rewritten_asset = asset
                    if not search(r"\.jpe?g$", asset.filename, flags=IGNORECASE):
                        normalized_filename = f"{asset.filename}.jpg"
                        auxiliary_path = join(gettempdir(), normalized_filename)
                        copy(asset.absolute_input_path, auxiliary_path)
                        chmod(auxiliary_path, 0o700)
                        rewritten_asset = Asset(
                            absolute_input_path=auxiliary_path,
                            filename=normalized_filename,
                            absolute_metadata_path=asset.absolute_metadata_path,
                            relative_parent=asset.relative_parent,
                        )
                        assets_normalized_jpg_extension.append(asset)

                    outcome = _process_asset(
                        rewritten_asset, args.output_directory, exif_helper
                    )
                elif search(
                    r"\.(mp4|mov|m4v)$", asset.filename, IGNORECASE
                ) and inferred_mimetype in ["video/mp4", "video/quicktime"]:
                    outcome = _process_asset(asset, args.output_directory, exif_helper)
                else:
                    copy(
                        asset.absolute_input_path,
                        join(
                            args.output_directory, asset.relative_parent, asset.filename
                        ),
                    )
                    assets_with_exif_unsupported.append(asset)
                    if args.verbose:
                        print(
                            f"Cannot process EXIF for {asset.absolute_input_path} ({inferred_mimetype})"
                        )
                    continue
            except ExifToolExecuteError as e:
                print(f"Error from exiftool: {e.stderr}")
                raise e

            if outcome.exif_added:
                assets_with_exif_added.append(asset)
            if outcome.exif_modified:
                assets_with_exif_modified.append(asset)
            if outcome.fell_back_to_system_timezone:
                assets_with_timezone_fallback.append(asset)
            if outcome.detected_input_file_corruption:
                assets_with_input_file_corruption.append(asset)
            assets_handled += 1

    print(f"{len(assets_with_exif_added)} assets had missing EXIF tags that were added")
    _print_assets_if_verbose(args.verbose, assets_with_exif_added)
    print(
        f"{len(assets_with_exif_modified)} assets had existing EXIF tags that were modified"
    )
    _print_assets_if_verbose(args.verbose, assets_with_exif_modified)
    print(
        f"{len(assets_with_exif_unsupported)} assets did not support writing EXIF data"
    )
    _print_assets_if_verbose(args.verbose, assets_with_exif_unsupported)
    print(f"{len(assets_converted_to_jpg)} assets were converted to JPG")
    _print_assets_if_verbose(args.verbose, assets_converted_to_jpg)
    print(
        f"{len(assets_normalized_jpg_extension)} assets with mimetype image/jpeg were corrected to have JPG extension"
    )
    _print_assets_if_verbose(args.verbose, assets_normalized_jpg_extension)
    print(
        f"{len(assets_with_timezone_fallback)} assets did not have a preferred display timezone"
        " offset information present, so we assumed system timezone"
    )
    _print_assets_if_verbose(args.verbose, assets_with_timezone_fallback)
    print(
        f"{len(assets_with_input_file_corruption)} assets with file corruption were handled"
    )
    _print_assets_if_verbose(args.verbose, assets_with_input_file_corruption)
    print(f"{assets_handled} assets were handled")
