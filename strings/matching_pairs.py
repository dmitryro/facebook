import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
  # Write your code here
  if s == t:
    return len(s) - 2
  
  unmatched_pairs = set()
  unmatched_in_t = set()
  unmatched_in_s = set()
  count = 0
  found_perfect_swap = False
  partial_swap = False

  for i in range(len(s)):
    if s[i] == t[i]:
      count += 1
    if found_perfect_swap:
      # No need to keep looking for swaps
      continue

    if s[i] != t[i]:
      unmatched_pairs.add((s[i], t[i]))
      unmatched_in_t.add(t[i])
      unmatched_in_s.add(s[i])
      # If we found the inverse pair, perfect swap
      if (t[i], s[i]) in unmatched_pairs:
        found_perfect_swap = True
      # Otherwise see if we have a "partial swap"
      elif s[i] in unmatched_in_t or t[i] in unmatched_in_s:
        partial_swap = True

  if found_perfect_swap:
    return count + 2
  elif partial_swap:
    return count + 1  
  











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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
