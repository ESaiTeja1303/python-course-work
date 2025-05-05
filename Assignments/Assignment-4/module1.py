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
