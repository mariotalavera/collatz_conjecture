import streamlit as st
import numpy as np
import pandas as pd
import time

min_value=5
max_value=27
cur_value=6

def compute():
	i = num_beg
	while i <= num_end:
		st.write('Testing number ',i)

		if i == 1:
			print("We have reached 4-2-1 Loop!")
			return 1
		else:
			if i % 2: 
				# If i is odd
				# doOdd(i, iteration, number_evaluated)
				'peep'
			else:
				# Number is even
				# doEven(i, iteration, number_evaluated)
				'poop'
		i += 1

# Display Starts Here
st.title('The Collatz Conjecture')

st.write('Welcome to the Collatz Conjecture Head Scratcher.')

left_column, right_column = st.beta_columns(2)

with left_column:
	num_beg = st.number_input('Beginning Number', min_value=min_value, max_value=max_value, value=cur_value)
	num_end = st.number_input('Ending Number', min_value=min_value, max_value=max_value, value=max_value)

with right_column:
	st.write('Selected number range is from ', num_beg, ' to ' , num_end, '.')
	st.write('\n')

# Single Canvas, no columns
if st.button('Compute Collatz'):
	compute()
# Display Ends Here




# ############################
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

# st.line_chart(df)