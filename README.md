# Secret Santa Administrator Program

Ever tried running a Secret Santa game and someone has to be the brave soul to create the pairings? I used to, then I wrote this. 

This Python program facilitates the management of a Secret Santa game among friends or colleagues. It assigns participants within the same group to one another randomly and generates personalized HTML pages for each participant with their assignment. These HTML files can be shared via email or messaging apps, and allow the organizer to keep himself from seeing the pairings.

---

## Features
- **CSV-based Input**: Reads participants' names and group information from a CSV file.
- **Group-specific Matching**: Ensures that each participant is matched with someone within their designated group.
- **Self-exclusion**: Prevents participants from being matched with themselves.
- **HTML Output**: Creates an individual HTML file for each participant showing their assigned recipient.
- **Dynamic Directory Handling**: Automatically names the output directory after the CSV file and allows for old game data cleanup.

---

## Prerequisites
- Python 3.x installed on your system.
- A CSV file containing participants and their group names.

### Example CSV Format:
```csv
Name,Group
Alice,Team A
Bob,Team A
Charlie,Team B
Dana,Team B
```

---

## How to Use

1. **Set up the CSV File**:
   - Update the `CSV_FILE` variable at the top of the script with the path to your CSV file.

2. **Run the Program**:
   ```bash
   python main.py
   ```

3. **Old Data Handling**:
   - If a directory with the same name as the CSV file exists, the program will prompt you to delete old game data before proceeding.

4. **Check Output**:
   - The program generates HTML files in a directory named after the CSV file (without its extension). Each file is named based on the participant's name and group.

### Example Output Directory Structure:
```
secret_santa/
├── Alice_Team_A.html
├── Bob_Team_A.html
├── Charlie_Team_B.html
├── Dana_Team_B.html
```

---

## Program Details

### Key Functionalities:
- **`delete_old_data(directory)`**: Deletes existing game data upon user confirmation.
- **`read_csv(file_path)`**: Reads the CSV file and parses participants' names and groups.
- **`assign_recipients(participants)`**: Randomly assigns gift recipients within each group.
- **`generate_html_files(assignments, participants, directory)`**: Creates personalized HTML files for each participant.

---

## Customization
- To change the output format or file structure, modify the `generate_html_files` function.
- Update the `CSV_FILE` variable to point to a different CSV file for new games.

---

## Troubleshooting

1. **CSV File Not Found**:
   - Ensure the file path specified in the `CSV_FILE` variable is correct.

2. **No Participants Found**:
   - Verify the CSV file is properly formatted and not empty.

3. **Directory Already Exists**:
   - If you want to reuse the same CSV file, confirm the deletion of old data when prompted.

---

## License
This program is provided "as-is" with no warranty. Feel free to modify and use it as needed.

---

## Author
Nick Troiano
---

Happy gifting! 🎁

