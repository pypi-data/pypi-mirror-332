from argparse import ArgumentParser, FileType


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "input", type=FileType("r"), help="Input ICS file from Google Calendar"
    )
    parser.add_argument(
        "output", type=FileType("w"), help="Output ICS file to ingest into another tool"
    )
    args = parser.parse_args()

    events_written = 0
    created_timestamp_corrections = 0
    alarm_action_corrections = 0
    alarm_trigger_corrections = 0
    for line in args.input:
        if line == "CREATED:00010101T000000Z\n":
            line = "CREATED:19700101T000000Z\n"
            created_timestamp_corrections += 1
        if line == "ACTION:NONE\n":
            line = "ACTION:DISPLAY\n"
            alarm_action_corrections += 1
        elif line == "TRIGGER;VALUE=DATE-TIME:19760401T005545Z\n":
            line = "TRIGGER:-PT10M\n"
            alarm_trigger_corrections += 1

        args.output.write(line)

        if line == "BEGIN:VEVENT\n":
            events_written += 1

    print(f"Corrected {created_timestamp_corrections} invalid created timestamps.")
    print(f"Corrected {alarm_action_corrections} empty alarm actions (ACTION:NONE).")
    print(
        f"Corrected {alarm_trigger_corrections} incorrect alarm triggers (triggers for the year 1976)."
    )
    print(f"Wrote {events_written} events to {args.output.name}.")
