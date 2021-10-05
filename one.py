"""The Collatz Conjecture is the simplest math problem no one can solve.""" 
"""https://www.youtube.com/watch?v=094y1Z2wpJg"""

import csv

# TODO - rename soln.csv to proper timestamped filename.
# TODO - do streamlit app all in one page

def main():
  """Loop numbers and calculate their sequence to 4 2 1 Loop"""
  print("\nWelcome to the Collatz Conjecture Head Scratcher.")

  n = 0         
  numbers_to_try = 7
  iteration = 1 

  # Lets create a CSV file to save our work
  with open('soln.csv','w') as file:
    field_names = ["Number", "X", "Y"]
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    file.close()

  # While current number is not last number
  while n < numbers_to_try:
    n += 1
    number_evaluated = n
    print("\nTesting the number " + str(n) + ".")
    doCollatz(n, iteration, number_evaluated)
  else:
    print("\nDone! We have reached our last number.\n")

def doCollatz(number, iteration, number_evaluated):

  if number == 1:
    print("We have reached 4-2-1 Loop!")
    return 1
  else:
    if number % 2: 
      # If number is odd
      doOdd(number, iteration, number_evaluated)
    else:
      # Number is even
      doEven(number, iteration, number_evaluated)

def doOdd(number, iteration, number_evaluated):
  number = (number * 3) + 1
  recordStep(number, iteration, number_evaluated)
  iteration += 1
  return doCollatz(number, iteration, number_evaluated)

def doEven(number, iteration, number_evaluated):
  number = number / 2
  recordStep(number, iteration, number_evaluated)
  iteration += 1
  return doCollatz(number, iteration, number_evaluated)

""" Record value"""
def recordStep(number, iteration, number_evaluated):
  print(" x=" + str(iteration) +  " y=" + str(number))
  measurement = [number_evaluated, iteration, number]
  with open('soln.csv','a') as file:
    writer = csv.writer(file)
    writer.writerow(measurement)
    file.close()

if __name__ == '__main__':
    main()



