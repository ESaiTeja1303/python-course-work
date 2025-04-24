import random

print("===== Welcome to Python BookMyShow =====")

users = []
locations = ["Hyderabad", "Mumbai", "Delhi", "Bangalore"]
categories = {
    "Movies": ["Batman", "RRR", "Inception"],
    "Events": ["Comic Con", "Tech Summit"],
    "Plays": ["Hamlet", "Phantom of the Opera"],
    "Sports": ["Cricket Match", "Football Final"],
    "Activities": ["Bowling", "Paintball"]
}
prices = {
    "Batman": 200, "RRR": 180, "Inception": 250,
    "Comic Con": 150, "Tech Summit": 200,
    "Hamlet": 300, "Phantom of the Opera": 350,
    "Cricket Match": 400, "Football Final": 350,
    "Bowling": 100, "Paintball": 150
}
bookings = []
logged_in = False
current_user = None
current_location = None

# Registration/Login
while not logged_in:
    print("\n1. Register\n2. Login")
    choice = input("Select option: ")

    if choice == "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")

        exists = any(u["username"] == username for u in users)
        if exists:
            print("Username already exists. Try another.")
        else:
            users.append({"username": username, "password": password, "bookings": []})
            print("Registered successfully. Please login now.")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                logged_in = True
                current_user = user
                print("Login successful! Welcome", username)
                break
        if not logged_in:
            print("Invalid credentials.")

# Select location
print("\nAvailable Locations:")
for i, loc in enumerate(locations, start=1):
    print(f"{i}. {loc}")
loc_choice = int(input("Select your location: "))
current_location = locations[loc_choice - 1]
print(f"Location set to {current_location}")

# Main Menu
while True:
    print("\n===== BookMyShow Menu =====")
    print("1. View Categories")
    print("2. Book Tickets")
    print("3. View My Bookings")
    print("4. Logout")

    option = input("Select an option: ")

    if option == "1":
        print("\n--- Categories Available ---")
        for cat, shows in categories.items():
            print(f"\n{cat}:")
            for show in shows:
                print(f"  - {show} | ₹{prices[show]}")
    
    elif option == "2":
        print("\n--- Book Tickets ---")
        print("Categories:")
        cat_list = list(categories.keys())
        for i, cat in enumerate(cat_list, start=1):
            print(f"{i}. {cat}")
        cat_choice = int(input("Select category: "))
        selected_cat = cat_list[cat_choice - 1]

        print(f"\nAvailable in {selected_cat}:")
        for i, show in enumerate(categories[selected_cat], start=1):
            print(f"{i}. {show} | ₹{prices[show]}")
        show_choice = int(input("Select a show: "))
        selected_show = categories[selected_cat][show_choice - 1]
        ticket_count = int(input("How many tickets?: "))
        total_amount = prices[selected_show] * ticket_count

        print(f"\nTotal Amount: ₹{total_amount}")
        confirm = input("Proceed to payment? (yes/no): ")
        if confirm.lower() == "yes":
            # Simulate payment
            if random.choice([True, True, True, False]):  
                print("Payment Successful ✅")
                booking_info = {
                    "category": selected_cat,
                    "show": selected_show,
                    "tickets": ticket_count,
                    "total": total_amount,
                    "location": current_location
                }
                current_user["bookings"].append(booking_info)
                print(f"🎟️ Booking Confirmed for {selected_show} in {current_location}!")
            else:
                print("Payment Failed ❌ Try again.")
        else:
            print("Booking cancelled.")

    elif option == "3":
        print("\n--- Your Bookings ---")
        if not current_user["bookings"]:
            print("No bookings yet.")
        else:
            for i, b in enumerate(current_user["bookings"], start=1):
                print(f"\nBooking {i}:")
                print(f"  Category: {b['category']}")
                print(f"  Show: {b['show']}")
                print(f"  Tickets: {b['tickets']}")
                print(f"  Total: ₹{b['total']}")
                print(f"  Location: {b['location']}")

    elif option == "4":
        print("Logged out. Thank you for using BookMyShow!")
        break

    else:
        print("Invalid option.")
