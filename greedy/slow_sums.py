import math
# Add any extra import statements you may need here
dp = {}

# Add any helper functions you may need here


def getTotalTime(arr):
  # Write your code here
  n = len(arr)
  sums = [0]*(n+1)
  for i in range(1,n+1):
    sums[i] = sums[i-1] + arr[i-1]
  D = [[0]*n for _ in range(n)]
  for i in range(1,n):
    D[i-1][i] = arr[i-1]+arr[i]
  for i in range(n-3,-1,-1):
    for j in range(i+2,n):
      for k in range(i,j):
        D[i][j] = max(D[i][j], D[i][k]+D[k+1][j] + sums[k+1]-sums[i] + sums[j+1]-sums[k+1])
  return D[0][n-1]
  
  









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
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
