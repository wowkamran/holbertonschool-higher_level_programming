#!/usr/bin/python3
"""
Module to generate personalized invitation files from a template and a list of attendee dictionaries.
"""

import os


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template for a list of attendees.

    Parameters:
    - template (str): The template string with placeholders.
    - attendees (list): List of dictionaries with attendee information.

    Behavior:
    - Validates input types and contents.
    - Replaces missing values with 'N/A'.
    - Writes output files named output_1.txt, output_2.txt, etc.
    """
    # Validate types
    if not isinstance(template, str):
        print(f"Error: template should be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees should be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Define placeholders expected in template
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        invitation_text = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation_text = invitation_text.replace(f"{{{key}}}", str(value))

        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(invitation_text)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
