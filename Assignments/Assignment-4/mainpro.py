# Eraram Sai Teja Goud (PFS-22)
import module1 as m

def display_menu():
    print("\nSelect an option:")
    print("1. Binary to Decimal")
    print("2. Binary Search")
    print("3. Linear Search")
    print("4. Bubble Sort")
    print("5. Selection Sort")
    print("6. Insertion Sort")
    print("7. Quick Sort")
    print("8. Reverse Array")
    print("9. Find Pairs with Given Sum")
    print("10. Sum of All Digits Until Single Digit")
    print("11. String Compression (Run-Length Encoding)")
    print("12. Find the First Repeated Character in a String")
    print("13. Multiply Two Matrices")
    print("14. Roman to Integer")
    print("15. Integer to Roman")
    print("16. All Diagonals (Bottom-Left to Top-Right)")
    print("17. Max product subarray kadane")
    print("18. Largest word in string")
    print("19. Replace elements with rank")
    print("20. Move all zeroes to left in array")
    print("0. Exit")


while True:
    display_menu()
    option = int(input("\nEnter your choice: "))

    if option == 1:
        print(m.binary_to_decimal())
    elif option == 2:
        print(m.binary_search())
    elif option == 3:
        print(m.Linear_search())
    elif option == 4:
        print(m.bubble_sort())
    elif option == 5:
        print(m.selection_sort())
    elif option == 6:
        print(m.insertion_sort())
    elif option == 7:
        print(m.quick_sort())
    elif option == 8:
        print(m.reverse_array())
    elif option == 9:
        print(m.find_pairs_with_sum())
    elif option == 10:
        print(m.sum_to_single_digit())
    elif option == 11:
        print(m.string_compression())
    elif option == 12:
        print(m.first_repeated_char())
    elif option == 13:
        print(m.multiply_matrices())
    elif option == 14:
        print(m.roman_to_integer())
    elif option == 15:
        print(m.integer_to_roman())
    elif option == 16:
        print(m.all_diagonals_bottom_left_to_top_right())
    elif option == 17:
        print(m.max_product_subarray_kadane())
    elif option == 18:
        print(m.largest_word_in_string())
    elif option == 19:
        print(m.replace_elements_with_rank())
    elif option == 20:
        print(m.move_zeroes_to_left())
    elif option == 0:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")


