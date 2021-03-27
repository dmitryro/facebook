import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOperations(arr):
    # Write your code here
    n = 0
    
    for i in range(len(arr)): # assign i every value in the array
  
    # i is the value, j is the list position
    #using .index() we can return the position of a value
      
    #Essentially, we are assigning the value and position to seperate objects (i, j).
        j = arr.index(min(arr[i:])) # j will store the current position of the value we are going to swith
    
        if j != i: #if the current position and current value do no match then
        
        #this is the fascinating part of this algorithm:
            arr = arr[:i] + [ v for v in reversed( arr[i:j+1] ) ] + arr[ j+1: ]
        
        #a nice way to visually see what is happening:
           
            n += 1
      
    return n
	











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
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  # Add your own test cases here
  
