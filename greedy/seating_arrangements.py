import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOverallAwkwardness(arr):
  # Write your code here
  max_dist = 0
  arr.sort()
  for i in range(len(arr)):
    if i == 0:
        right = left = arr[0]
        continue
    if i % 2 == 0:
      max_dist = max(max_dist, arr[i] - right)
      right = arr[i]
    else:
      max_dist = max(max_dist, arr[i] - left)
      left = arr[i]
  return max_dist











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 10, 6, 8]
  expected_1 = 4
  output_1 = minOverallAwkwardness(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2, 5, 3, 7]
  expected_2 = 4
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
