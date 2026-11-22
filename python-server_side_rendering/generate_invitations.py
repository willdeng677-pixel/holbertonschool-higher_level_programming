#!/usr/bin/python3


def generate_invitations(template, attendees):
    """Generate personalized invitation files."""

    # Check that template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check that attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):

        # Replace missing values with N/A
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Create output file
        filename = f"output_{index}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(invitation)

        print(f"Generated {filename}")


# Read the template file
with open("template.txt", "r", encoding="utf-8") as file:
    template = file.read()

# Define attendees
attendees = [
    {
        "name": "John",
        "event_title": "Python Conference",
        "event_date": "December 10, 2026",
        "event_location": "Sydney"
    },
    {
        "name": "Mary",
        "event_title": "Tech Meetup",
        "event_date": "December 15, 2026",
        "event_location": "Melbourne"
    },
    {
        "name": "David",
        "event_title": "Coding Workshop",
        "event_location": "Brisbane"
    }
]

# Generate invitations
generate_invitations(template, attendees)
