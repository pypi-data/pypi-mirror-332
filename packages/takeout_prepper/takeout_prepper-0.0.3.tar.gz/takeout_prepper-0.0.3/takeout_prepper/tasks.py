from argparse import ArgumentParser, FileType
from json import load
from datetime import datetime, timezone

ICS_TEMPLATE = """BEGIN:VTODO
UID:{item_id}
DUE:{due}
STATUS:{mapped_status}
LAST-MODIFIED:{due}
DTSTAMP:{due}
SUMMARY:{summary}
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER;RELATED=END:PT0S
END:VALARM
END:VTODO"""


def _render_item(item: dict) -> str:
    timestamp: datetime | None = None
    if "due" in item:
        timestamp = datetime.fromisoformat(item["due"])
    if "completed" in item:
        timestamp = datetime.fromisoformat(item["completed"])
    assert timestamp
    mapped_status = {
        "needsAction": "NEEDS-ACTION",
        "completed": "COMPLETED",
    }[item["status"]]

    return ICS_TEMPLATE.format(
        item_id=item["id"],
        summary=item["title"],
        mapped_status=mapped_status,
        due=timestamp.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
    )


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "input", type=FileType("r"), help="Input JSON file from Google Tasks"
    )
    parser.add_argument(
        "output", type=FileType("w"), help="Output ICS file containing a task list"
    )
    parser.add_argument(
        "--tz",
        required=True,
        help='Which timezone the ICS file should be displayed in (e.g. "Europe/Berlin").',
    )
    args = parser.parse_args()

    data = load(args.input)

    args.output.write("BEGIN:VCALENDAR\n")
    args.output.write("VERSION:2.0\n")
    args.output.write("PRODID:-//Nextcloud Tasks v0.16.1\n")
    args.output.write(f"X-WR-CALNAME:{data['items'][0]['title']}\n")
    args.output.write("BEGIN:VTIMEZONE\n")
    args.output.write(f"TZID:{args.tz}\n")
    args.output.write("END:VTIMEZONE\n")

    items_written = 0
    for item in data["items"][0]["items"]:
        item = _render_item(item)
        args.output.write(f"{item}\n")
        items_written += 1

    args.output.write("END:VCALENDAR")

    print(f"Written {items_written} task items to {args.output.name}.")
    print(
        "Keep in mind that recurring tasks are not handled properly. See README for further info."
    )
