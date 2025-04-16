# Eraram Sai Teja Goud (PFS-22)


# 1. Course ID (int)
course_id = int(input("Enter Course ID: "))

# 2. Course Name (str)
course_name = input("Enter Course Name: ")

# 3. Course Fee (float)
fee = float(input("Enter Course Fee (₹): "))

# 4. Technologies Covered (list)
tech_input = input("Enter Technologies Covered (comma-separated): ")
technologies = [tech.strip() for tech in tech_input.split(",")]

# 5. Batch Details (tuple) – Available Seats and Filled Seats
available = int(input("Enter Available Seats: "))
filled = int(input("Enter Filled Seats: "))
batch_details = (available, filled)

# 6. Discount Percentage (float)
discount = float(input("Enter Discount Percentage: "))

# 7. Course Features (set)
features_input = input("Enter Course Features (comma-separated): ")
features = set(f.strip() for f in features_input.split(","))

# 8. Institute Branch Details (dict)
branch_name = input("Enter Branch Name: ")
branch_contact = input("Enter Branch Contact Number: ")
branch_location = input("Enter Branch Location: ")
branch_info = {
    "name": branch_name,
    "contact": branch_contact,
    "location": branch_location
}


#  ***Display Course Details Using Different Formatting Methods****

print("\n" + "-"*45)
print("CODEGNAN COURSE DETAILS FORMATTED OUTPUT")
print("-"*45)

# 1. Using Comma Separation (sep=',')
print("Course ID, Name, Fee:", course_id, course_name, fee, sep=", ")

# 2. Using Percentage Formatting (% operator)
print("Discount Available: %.2f%%" % discount)

# 3. Using f-strings
print(f"Course Name: {course_name}")
print(f"Course Fee: ₹{fee}")
print(f"Discount: {discount}%")
print(f"Batch Info: {batch_details[0]} Seats Available | {batch_details[1]} Filled")

# 4. Using .format() method
print("Branch Details: Name - {}, Contact - {}, Location - {}".format(
    branch_info['name'], branch_info['contact'], branch_info['location']
))


print("\nTechnologies Covered:", technologies)
print("Course Features:", features)
