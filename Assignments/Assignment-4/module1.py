# Eraram Sai Teja Goud (PFS-22)
def binary_to_decimal():
  return '''
  ***binary to decimal***

  n=int(input("Enter Number: "))
  s=str(n)
  i=len(s)-1
  res=0
  for j in s:
    res=res+int(j)*(2**i)
    i=i-1
  print(res)
  ==========================================
  Testcase-1:
  Enter Number: 1010
  output:
  10
  ------------------------------------------
  Testcase-2:
  Enter Number: 1000
  output:
  8
  ===========================================
  '''

def binary_search():
  return '''
  ***binary search***

  arr=list(map(int,input("Enter elements").split()))
  arr.sort()
  key=int(input("Enter the key to search: "))
  n=len(arr)
  l=0
  h=n-1
  while l<=h:
    m=(l+h)//2
    if key==ar[m]:
      print("Key found at index:",m)
      break
    elif key<ar[m]:
    h=m-1
    else:
      l=m+1
  else:
    print("key not found")
  ==========================================
  Testcase-1:
  Enter elements: 2 4 5 7 8
  Enter the key to search: 4
  output:
  Key found at index: 1
  ------------------------------------------
  Testcase-2:
  Enter elements: 10 20 30 40
  Enter the key to search: 25
  output:
  Key not found
  ===========================================
  '''

def Linear_search():
  return '''
  ***Linear search***

  arr = list(map(int, input("Enter elements: ").split()))
  key = int(input("Enter the key to search: "))

  found = False
  for i in range(len(arr)):
      if arr[i] == key:
          print("Key found at index", i)
          found = True
          break

  if not found:
      print("Key not found")
 ==========================================
  Testcase-1:
  Enter elements: 2 4 5 7 8
  Enter the key to search: 5
  output:
  Key found at index: 2
  ------------------------------------------
  Testcase-2:
  Enter elements: 1 3 5 7
  Enter the key to search: 4
  output:
  Key not found
===========================================
  '''

def bubble_sort():
  return '''
  ****Bubble Sort*****

  arr = list(map(int, input("Enter elements: ").split()))
  n = len(arr)
  for i in range(n):
      for j in range(0, n - i - 1):
          if arr[j] > arr[j + 1]:
              arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

  print("Sorted array:", arr)
 ==========================================
  Testcase-1:
  Enter elements: 5 1 4 2 8
  output:
  Sorted array: [1, 2, 4, 5, 8]
  ------------------------------------------
  Testcase-2:
  Enter elements: 9 3 7 1 6
  output:
  Sorted array: [1, 3, 6, 7, 9]
===========================================
  '''

def selection_sort():
  return '''
  ***selection sort***
  arr = list(map(int, input("Enter elements: ").split()))
  n = len(arr)

  for i in range(n):
      min_idx = i
      for j in range(i + 1, n):
          if arr[j] < arr[min_idx]:
              min_idx = j
      arr[i], arr[min_idx] = arr[min_idx], arr[i]

  print("Sorted array:", arr)
===========================================
  Testcase-1:
  Enter elements: 64 25 12 22 11
  output:
  Sorted array: [11, 12, 22, 25, 64]
  ------------------------------------------
  Testcase-2:
  Enter elements: 10 5 3 8 2
  output:
  Sorted array: [2, 3, 5, 8, 10]
===========================================
  '''

def insertion_sort():
  return '''
  ***insertion sort***
  arr = list(map(int, input("Enter elements: ").split()))
  n = len(arr)

  for i in range(1, n):
      key = arr[i]
      j = i - 1
      while j >= 0 and arr[j] > key:
          arr[j + 1] = arr[j]
          j -= 1
      arr[j + 1] = key

  print("Sorted array:", arr)
===========================================
  Testcase-1:
  Enter elements: 64 25 12 22 11
  output:
  Sorted array: [11, 12, 22, 25, 64]
  ------------------------------------------
  Testcase-2:
  Enter elements: 10 5 3 8 2
  output:
  Sorted array: [2, 3, 5, 8, 10]
===========================================
  '''

def quick_sort():
  return '''
  ***quick sort***
  def quicksort(arr):
      if len(arr) <= 1:
          return arr

      pivot = arr[0]
      left = []
      right = []

      for i in range(1, len(arr)):
          if arr[i] <= pivot:
              left.append(arr[i])
          else:
              right.append(arr[i])

      sorted_left = quicksort(left)
      sorted_right = quicksort(right)

      return sorted_left + [pivot] + sorted_right

  arr = list(map(int, input("Enter elements: ").split()))
  arr = quicksort(arr)
  print("Sorted array:", arr)
===========================================
  Testcase-1:
  Enter elements: 64 25 12 22 11
  output:
  Sorted array: [11, 12, 22, 25, 64]
  ------------------------------------------
  Testcase-2:
  Enter elements: 10 5 3 8 2
  output:
  Sorted array: [2, 3, 5, 8, 10]
===========================================
  '''

def reverse_array():
  return '''
  ***reverse array using two pointers***
  arr = list(map(int, input("Enter elements: ").split()))
  left = 0
  right = len(arr) - 1

  while left < right:
      arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -= 1

  print("Reversed array:", arr)
===========================================
  Testcase-1:
  Enter elements: 1 2 3 4 5
  output:
  Reversed array: [5, 4, 3, 2, 1]
  ------------------------------------------
  Testcase-2:
  Enter elements: 10 20 30 40
  output:
  Reversed array: [40, 30, 20, 10]
===========================================
  '''

#Find Pairs with Given Sum from a List
def find_pairs_with_sum():
  return '''
  ***find pairs with a given sum***
  lst = list(map(int, input("Enter list elements: ").split()))
  tar = int(input("Target sum: "))
  res = []

  while lst:
      f = lst[0]
      s = tar - f
      lst.remove(f)
      if s in lst:
          res.append((f, s))
          lst.remove(s)

  if res:
      print(f"Pairs with sum {tar}: ", end="")
      for pair in res:
          print(pair, end=" ")
      print()
  else:
      print(f"No pairs found with sum {tar}.")

===========================================
  Testcase-1:
  Enter list elements: 2 4 3 5 7 8
  Target sum: 10
  output:
  Pairs with sum 10: (2, 8) (3, 7)
------------------------------------------
  Testcase-2:
  Enter list elements: 1 9 6 4 5 3 7
  Target sum: 10
  output:
  Pairs with sum 10: (1, 9) (6, 4) (3, 7)
===========================================
  '''

#Sum of All Digits Until Single Digit
def sum_to_single_digit():
  return '''
  ***sum of all digits until a single digit***
  num = int(input("Enter the number: "))
  tot_sum = num

  while tot_sum > 9:
      cur_sum = 0
      while num > 0:
          cur_sum += num % 10
          num = num // 10
      tot_sum = cur_sum
      num = cur_sum

  print(f'Single digit: {tot_sum}')
===========================================
  Testcase-1:
  Enter the number: 9875
  output:
  Single digit: 2
  ------------------------------------------
  Testcase-2:
  Enter the number: 123456
  output:
  Single digit: 3
===========================================
  '''


#String Compression (Run-Length Encoding)aaabbc  a3b2c1
def string_compression():
  return '''
  ***string compression (run-length encoding)***
  s = input("Enter a string: ")

  compressed = ""
  count = 1

  for i in range(1, len(s)):
      if s[i] == s[i - 1]:
          count += 1
      else:
          compressed += s[i - 1] + str(count)
          count = 1

  compressed += s[-1] + str(count)

  print("Compressed string:", compressed)

===========================================
  Testcase-1:
  Enter a string: aaabbc
  output:
  Compressed string: a3b2c1
  ------------------------------------------
  Testcase-2:
  Enter a string: xxxyyyzz
  output:
  Compressed string: x3y3z2
===========================================
  '''

#Find the First Repeated Character in a String
def first_repeated_char():
  return '''
  ***first repeated character in a string***
  st = input("Enter a string: ")
  s = set()

  for i in st:
      if i in s:
          print('First repeated character:', i)
          break
      else:
          s.add(i)

===========================================
  Testcase-1:
  Enter a string: abcadef
  output:
  First repeated character: a
  ------------------------------------------
  Testcase-2:
  Enter a string: python
  output:
  (No output, as no character is repeated)
===========================================
  '''



def multiply_matrices():
  return '''
  ***multiply two matrices***
  def input_matrix(rows, cols):
      print(f"Enter elements for a {rows}x{cols} matrix:")
      matrix = []
      for i in range(rows):
          row = list(map(int, input().split()))
          if len(row) != cols:
              print("Invalid number of columns. Try again.")
              return None
          matrix.append(row)
      return matrix

  r1 = int(input("Enter rows of first matrix: "))
  c1 = int(input("Enter columns of first matrix: "))
  r2 = int(input("Enter rows of second matrix: "))
  c2 = int(input("Enter columns of second matrix: "))

  if c1 != r2:
      print("Matrix multiplication not possible. Columns of first must equal rows of second.")
  else:
      print("First matrix:")
      A = input_matrix(r1, c1)
      print("Second matrix:")
      B = input_matrix(r2, c2)

      result = [[0 for _ in range(c2)] for _ in range(r1)]

      for i in range(r1):
          for j in range(c2):
              for k in range(c1):
                  result[i][j] += A[i][k] * B[k][j]

      print("Resultant matrix:")
      for row in result:
          print(*row)

===========================================
  Testcase-1:
  Enter rows of first matrix: 2
  Enter columns of first matrix: 2
  Enter rows of second matrix: 2
  Enter columns of second matrix: 2
  First matrix:
  1 2
  3 4
  Second matrix:
  5 6
  7 8
  output:
  Resultant matrix:
  19 22
  43 50
  ------------------------------------------
  Testcase-2:
  Enter rows of first matrix: 2
  Enter columns of first matrix: 3
  Enter rows of second matrix: 3
  Enter columns of second matrix: 2
  First matrix:
  1 2 3
  4 5 6
  Second matrix:
  7 8
  9 10
  11 12
  output:
  Resultant matrix:
  58 64
  139 154
===========================================
  '''

#Roman to Integer
def roman_to_integer():
  return '''
  ***roman to integer***
  rtoi = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  s = input("Enter Roman numeral: ").upper()

  total = 0
  i = 0
  n = len(s)

  while i < n:
      if i < n - 1 and rtoi[s[i]] < rtoi[s[i + 1]]:
          total += rtoi[s[i + 1]] - rtoi[s[i]]
          i += 2
      else:
          total += rtoi[s[i]]
          i += 1

  print("Integer value:", total)

===========================================
  Testcase-1:
  Enter Roman numeral: IX
  output:
  Integer value: 9
  ------------------------------------------
  Testcase-2:
  Enter Roman numeral: MCMXCIV
  output:
  Integer value: 1994
===========================================
  '''


#Integer to roman
def integer_to_roman():
  return '''
  ***integer to roman***
  val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

  num = int(input("Enter an integer (1 to 3999): "))
  roman = ""

  for i in range(len(val)):
      while num >= val[i]:
          roman += syms[i]
          num -= val[i]

  print("Roman numeral:", roman)

===========================================
  Testcase-1:
  Enter an integer: 9
  output:
  Roman numeral: IX
  ------------------------------------------
  Testcase-2:
  Enter an integer: 1994
  output:
  Roman numeral: MCMXCIV
===========================================
  '''



def all_diagonals_bottom_left_to_top_right():
  return '''
  ***all diagonals from bottom-left to top-right***
  def input_matrix(n):
      print(f"Enter elements for a {n}x{n} matrix:")
      matrix = []
      for i in range(n):
          row = list(map(int, input().split()))
          if len(row) != n:
              print("Invalid number of elements. Try again.")
              return None
          matrix.append(row)
      return matrix

  n = int(input("Enter size of square matrix: "))
  mat = input_matrix(n)

  if mat:
      print("Diagonals from bottom-left to top-right:")
      # Lower half diagonals including the main diagonal
      for i in range(n - 1, -1, -1):
          row = i
          col = 0
          while row < n and col < n:
              print(mat[row][col], end=" ")
              row += 1
              col += 1
          print()

      # Upper half diagonals
      for j in range(1, n):
          row = 0
          col = j
          while row < n and col < n:
              print(mat[row][col], end=" ")
              row += 1
              col += 1
          print()

===========================================
  Testcase-1:
  Enter size of square matrix: 3
  Enter elements:
  1 2 3
  4 5 6
  7 8 9
  output:
  Diagonals from bottom-left to top-right:
  7
  4 8
  1 5 9
  2 6
  3
  ------------------------------------------
  Testcase-2:
  Enter size of square matrix: 2
  Enter elements:
  10 20
  30 40
  output:
  Diagonals from bottom-left to top-right:
  30
  10 40
  20
===========================================
  '''

def max_product_subarray_kadane():
  return '''
  **Maximum Product Subarray - Kadane's Variation**

  arr = list(map(int, input("Enter array elements separated by space: ").split()))
  max_prod = arr[0]
  min_prod = arr[0]
  result = arr[0]

  for i in range(1, len(arr)):
    if arr[i] < 0:
      max_prod, min_prod = min_prod, max_prod

    max_prod = max(arr[i], max_prod * arr[i])
    min_prod = min(arr[i], min_prod * arr[i])

    result = max(result, max_prod)

  print("Maximum Product Subarray is:", result)
  ==========================================
  Testcase-1:
  Enter array elements separated by space: 2 3 -2 4
  Output:
  Maximum Product Subarray is: 6
  ------------------------------------------
  Testcase-2:
  Enter array elements separated by space: -2 0 -1
  Output:
  Maximum Product Subarray is: 0
  ===========================================
  '''

def largest_word_in_string():
  return '''
  **Find the Largest Word in a String**

  s = input("Enter a sentence: ")
  words = s.split()
  max_word = ""
  for word in words:
    if len(word) > len(max_word):
      max_word = word

  print("The largest word is:", max_word)
  ==========================================
  Testcase-1:
  Enter a sentence: I love programming in Python
  Output:
  The largest word is: programming
  ------------------------------------------
  Testcase-2:
  Enter a sentence: This is a test sentence
  Output:
  The largest word is: sentence
  ===========================================
  '''


def replace_elements_with_rank():
  return '''
  **Replace Elements by Their Rank in the Array (No List Comprehension)**

  arr = list(map(int, input("Enter array elements separated by space: ").split()))
  unique = []
  for num in arr:
    if num not in unique:
      unique.append(num)
  unique.sort()

  rank_map = {}
  rank = 1
  for num in unique:
    rank_map[num] = rank
    rank += 1

  ranked_arr = []
  for num in arr:
    ranked_arr.append(rank_map[num])

  print("Ranked array:", ranked_arr)
  ==========================================
  Testcase-1:
  Enter array elements separated by space: 40 10 20 30
  Output:
  Ranked array: [4, 1, 2, 3]
  ------------------------------------------
  Testcase-2:
  Enter array elements separated by space: 100 100 50 10
  Output:
  Ranked array: [3, 3, 2, 1]
  ===========================================
  '''


def move_zeroes_to_left():
  return '''
  **Move All Zeroes in the Array to the Left**

  arr = list(map(int, input("Enter array elements separated by space: ").split()))
  result = []
  zero_count = 0

  for num in arr:
    if num == 0:
      zero_count += 1
    else:
      result.append(num)

  for _ in range(zero_count):
    result.insert(0, 0)

  print("Array after moving zeroes to the left:", result)
  ==========================================
  Testcase-1:
  Enter array elements separated by space: 1 0 2 0 3 4
  Output:
  Array after moving zeroes to the left: [0, 0, 1, 2, 3, 4]
  ------------------------------------------
  Testcase-2:
  Enter array elements separated by space: 0 0 0 1
  Output:
  Array after moving zeroes to the left: [0, 0, 0, 1]
  ===========================================
  '''
