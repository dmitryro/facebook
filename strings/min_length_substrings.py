import math
# Add any extra import statements you may need here
import collections

# Add any helper functions you may need here


def min_length_substring(s, t):
  # Write your code here
    c=collections.Counter(t)
    curr=collections.Counter()
    left=0
    minLength=float('inf')

    def check(sc, tc):
        for k in tc:
           if sc[k] < tc[k]:
               return False
        return True
      
    for right in range(len(s)):
        curr[s[right]] += 1 
        while check(curr, c):
            minLength=min(minLength, right-left+1)
            curr[s[left]]-=1
            if curr[s[left]]==0:
                del curr[s[left]]
            left+=1
    return minLength if minLength!=float('inf') else -1

	











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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

	# Add your own test cases here
