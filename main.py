import csv
import os
import random
import shutil
import sys
from pathlib import Path

# Pointer to the relevant CSV file
CSV_FILE = "demo.csv"


def delete_old_data(directory):
    """Delete old game data if the user confirms."""
    if os.path.exists(directory):
        confirm = input(
            f"Directory '{directory}' exists. Do you want to delete old game data? (y/n): ").strip().lower()
        if confirm == 'y':
            shutil.rmtree(directory)
            print(f"Deleted old game data in '{directory}'.")
        if confirm == 'n':
            sys.exit()
        if confirm not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            delete_old_data(directory)


def read_csv(file_path):
    """Read the CSV file and return a list of participants."""
    participants = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row if it exists
        for row in reader:
            if len(row) >= 2:
                participants.append({'name': row[0].strip(), 'group': row[1].strip()})
    return participants


def assign_recipients(participants):
    """Assign Secret Santa recipients within the same group."""
    group_mapping = {}
    for participant in participants:
        group = participant['group']
        if group not in group_mapping:
            group_mapping[group] = []
        group_mapping[group].append(participant['name'])

    assignments = {}
    for group, names in group_mapping.items():
        shuffled = names[:]
        random.shuffle(shuffled)
        for giver, recipient in zip(names, shuffled):
            while giver == recipient:  # Ensure no one is assigned to themselves
                random.shuffle(shuffled)
                recipient = shuffled[names.index(giver)]
            assignments[giver] = recipient

    return assignments


def generate_html_files(assignments, participants, directory):
    """Generate HTML files for each participant."""
    os.makedirs(directory, exist_ok=True)

    for participant in participants:
        name = participant['name']
        group = participant['group']
        recipient = assignments[name]

        html_content = f"""
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>Secret Santa for {name}</title>
        </head>
        <body>
            <h1>{directory} Secret Santa</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Group:</strong> {group}</p>
            <p><strong>Your Secret Santa Recipient:</strong> {recipient}</p>
        </body>
        </html>
        """
        file_name = f"{directory}/{name}_{group}.html"
        with open(file_name, 'w') as html_file:
            html_file.write(html_content)


if __name__ == "__main__":
    if not os.path.exists(CSV_FILE):
        print(f"CSV file '{CSV_FILE}' not found. Please make sure the file exists.")
        exit(1)

    output_directory = Path(CSV_FILE).stem  # Use CSV file name without extension as directory name
    delete_old_data(output_directory)

    participants = read_csv(CSV_FILE)
    if not participants:
        print("No participants found in the CSV file.")
        exit(1)

    assignments = assign_recipients(participants)
    generate_html_files(assignments, participants, output_directory)

    print(f"Secret Santa game setup complete! Files are saved in the '{output_directory}' directory.")

