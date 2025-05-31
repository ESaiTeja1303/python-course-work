import os
import re

os.chdir('c:/Users/ERARAM SAI TEJA GOUD/OneDrive/Desktop/Python Class practice/class work/work_file')
# Directory for storing notes
NOTES_DIR = "usernotes"

# Ensure notes directory exists
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

# Basic sentiment word lists
positive_words = ['good', 'happy', 'great', 'excellent', 'fantastic', 'positive', 'love']
negative_words = ['bad', 'sad', 'terrible', 'horrible', 'negative', 'hate', 'angry']

def analyze_sentiment(content):
    # Use regex to find sentiment words
    pos_found = re.findall(r'\b(?:' + '|'.join(positive_words) + r')\b', content, re.IGNORECASE)
    neg_found = re.findall(r'\b(?:' + '|'.join(negative_words) + r')\b', content, re.IGNORECASE)

    print(f"\n[+] Positive Words Found: {pos_found}")
    print(f"[-] Negative Words Found: {neg_found}")
    
    if len(pos_found) > len(neg_found):
        print("🔎 Sentiment: Positive")
    elif len(neg_found) > len(pos_found):
        print("🔎 Sentiment: Negative")
    else:
        print("🔎 Sentiment: Neutral")

def analyze_note():
    print("\n--- Analyze Notes ---")
    choice = input("Analyze a specific note or all? (specific/all): ").strip().lower()

    if choice == "specific":
        filename = input("Enter the filename: ").strip()
        filepath = os.path.join(NOTES_DIR, filename)
        try:
            with open(filepath, 'r') as file:
                content = file.read()
                print("\n--- Note Content ---\n" + content)
                analyze_sentiment(content)
        except FileNotFoundError:
            print("❌ File not found.")
    elif choice == "all":
        files = os.listdir(NOTES_DIR)
        if not files:
            print("📂 No notes to analyze.")
            return
        for filename in files:
            filepath = os.path.join(NOTES_DIR, filename)
            with open(filepath, 'r') as file:
                content = file.read()
                print(f"\n📄 {filename}")
                print("-------------------")
                analyze_sentiment(content)
    else:
        print("❌ Invalid choice.")

def create_note():
    print("\n--- Create a New Note ---")
    filename = input("Enter a filename: ").strip()
    content = input("Enter the content for the note:\n")
    
    filepath = os.path.join(NOTES_DIR, filename)
    with open(filepath, 'w') as file:
        file.write(content)
    print("✅ Note created successfully.")

def modify_note():
    print("\n--- Modify Existing Note ---")
    files = os.listdir(NOTES_DIR)
    if not files:
        print("📂 No notes to modify.")
        return
    print("📄 Available Notes:")
    for f in files:
        print(f"- {f}")

    filename = input("Enter the filename to modify: ").strip()
    filepath = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(filepath):
        print("❌ File not found.")
        return

    with open(filepath, 'r') as file:
        old_content = file.read()
        print("\n--- Current Content ---\n" + old_content)

    new_content = input("\nEnter the new content:\n")
    with open(filepath, 'w') as file:
        file.write(new_content)
    print("✅ Note updated successfully.")

def main():
    print("📘 Welcome to Intelligent Notes Management System 📘")

    while True:
        print("\n--- Menu ---")
        print("1. Analyze Notes")
        print("2. Create New Note")
        print("3. Modify Existing Note")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()

        try:
            if choice == '1':
                analyze_note()
            elif choice == '2':
                create_note()
            elif choice == '3':
                modify_note()
            elif choice == '4':
                print("👋 Exiting... Goodbye!")
                break
            else:
                print("❌ Invalid option. Please choose 1-4.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()






