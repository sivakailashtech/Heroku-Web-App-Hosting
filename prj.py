import streamlit as st
st.title("TDS Graded Assignment 8")
st.subheader("odd or even number checking Web App by Siva Kailash (21f1002374)")
placeholder_Number = st.empty()
n = placeholder_Number.number_input('Enter Number')
n=int(n)
if (n % 2) == 0:
	st.write("your number is even")
else:
	st.write("your number is odd")
