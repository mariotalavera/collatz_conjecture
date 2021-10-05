import streamlit as st
import csv
# import numpy as np
import pandas as pd
import altair as alt

# import time

min_value=1 	# n
max_value=999 	# numbers_to_rty
cur_value=6 	# 
# n = min_value

def conjecture():
	n = num_beg       
	numbers_to_try = num_end
	iteration = 1 

	# Lets create a CSV file to save our work
	with open('soln.csv','w') as file:
		field_names = ['Number', 'X', 'Y']
		writer = csv.DictWriter(file, fieldnames=field_names)
		writer.writeheader()
		file.close()


	# While current number is not last number
	while n <= numbers_to_try:
		number_evaluated = n
		# st.write('Testing ', n)
		doCollatz(n, iteration, number_evaluated)
		n += 1
	else:
		# left_column.write("\nDone! We have reached our last number.\n")

		df = pd.read_csv('soln.csv') # .set_index('X')

		df2 = df.pivot(index='X', columns="Number", values="Y")
		st.write(df2.style.highlight_max(axis=0))
		st.write('\n')

		c = alt.Chart(df).mark_line(point=True).encode(
		    x='X:N',
		    y='Y:Q',
		    color='Number:N', tooltip=['Number','Y']
		).properties(
		    width=960,
		    height=540
		    )
		# st.altair_chart(c,use_container_width=True)
		st.altair_chart(c)

def doCollatz(number, iteration, number_evaluated):
	if number == 1:
		# st.write("We have reached 4-2-1 Loop!")
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

def recordStep(number, iteration, number_evaluated):
	# st.write(' x =', iteration, ', y =', number)
	measurement = [number_evaluated, iteration, number]
	with open('soln.csv','a') as file:
		writer = csv.writer(file)
		writer.writerow(measurement)
		file.close()

# Display Starts Here
st.title('The Collatz Conjecture')

st.write('Welcome to the Collatz Conjecture Head Scratcher.')

left_column, right_column = st.beta_columns(2)

# Sidecar
num_beg = st.sidebar.number_input('Beginning Number', min_value=min_value, max_value=max_value, value=cur_value)
num_end = st.sidebar.number_input('Ending Number', min_value=min_value, max_value=max_value, value=cur_value)

st.sidebar.write('Selected number range is from ', num_beg, ' to ' , num_end)

if st.sidebar.button('Conjecture'):
	st.sidebar.write('Conjecturing!\n')
	conjecture()

# Left column
with left_column:
	st.write('\n')

# Right column
with right_column:
	st.write('\n')

# Display Ends Here