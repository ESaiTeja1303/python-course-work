import os
import re


os.chdir('c:/Users/ERARAM SAI TEJA GOUD/OneDrive/Desktop/Python Class practice/Assignments/Assignment-5')
# Directory to store medical reports
REPORTS_DIR = "patient_reports"

# Ensure the directory exists
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

# Sample keywords to indicate seriousness of condition
serious_conditions = [
    'cancer', 'tumor', 'stroke', 'heart attack', 'seizure',
    'coma', 'failure', 'critical', 'emergency', 'intensive'
]
minor_conditions = [
    'headache', 'cold', 'fever', 'cough', 'fatigue',
    'allergy', 'sore throat', 'nausea', 'dizziness'
]

def analyze_severity(content):
    serious_found = re.findall(r'\b(?:' + '|'.join(serious_conditions) + r')\b', content, re.IGNORECASE)
    minor_found = re.findall(r'\b(?:' + '|'.join(minor_conditions) + r')\b', content, re.IGNORECASE)

    print("\nKeywords indicating serious conditions found:", serious_found)
    print("Keywords indicating minor conditions found:", minor_found)

    if len(serious_found) > len(minor_found):
        print("Report Analysis: Serious Condition")
    elif len(minor_found) > len(serious_found):
        print("Report Analysis: Minor Condition")
    else:
        print("Report Analysis: Inconclusive")

def analyze_report():
    print("\n--- Analyze Patient Reports ---")
    choice = input("Analyze a specific report or all reports? (specific/all): ").strip().lower()

    if choice == "specific":
        filename = input("Enter the report filename: ").strip()
        filepath = os.path.join(REPORTS_DIR, filename)
        try:
            with open(filepath, 'r') as file:
                content = file.read()
                print("\n--- Report Content ---")
                print(content)
                analyze_severity(content)
        except FileNotFoundError:
            print("File not found.")
    elif choice == "all":
        files = os.listdir(REPORTS_DIR)
        if not files:
            print("No reports to analyze.")
            return
        for filename in files:
            filepath = os.path.join(REPORTS_DIR, filename)
            with open(filepath, 'r') as file:
                content = file.read()
                print(f"\nAnalyzing Report: {filename}")
                print("--------------------------")
                analyze_severity(content)
    else:
        print("Invalid choice.")

def create_report():
    print("\n--- Create a New Medical Report ---")
    filename = input("Enter a filename for the report: ").strip()
    content = input("Enter the report content:\n")

    filepath = os.path.join(REPORTS_DIR, filename)
    with open(filepath, 'w') as file:
        file.write(content)
    print("Report created successfully.")

def modify_report():
    print("\n--- Modify an Existing Report ---")
    files = os.listdir(REPORTS_DIR)
    if not files:
        print("No reports available.")
        return

    print("Available Reports:")
    for f in files:
        print(f"- {f}")

    filename = input("Enter the filename to modify: ").strip()
    filepath = os.path.join(REPORTS_DIR, filename)

    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, 'r') as file:
        old_content = file.read()
        print("\n--- Current Report Content ---")
        print(old_content)

    new_content = input("\nEnter the updated content:\n")
    with open(filepath, 'w') as file:
        file.write(new_content)
    print("Report updated successfully.")

def main():
    print("Medical Reports Analyzer")

    while True:
        print("\nMenu:")
        print("1. Analyze Reports")
        print("2. Create New Report")
        print("3. Modify Existing Report")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        try:
            if choice == '1':
                analyze_report()
            elif choice == '2':
                create_report()
            elif choice == '3':
                modify_report()
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please choose between 1 and 4.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
