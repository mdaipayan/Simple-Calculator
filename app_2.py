import streamlit as st

# Set up the app title and layout
st.title("🔢 Simple Calculator")
st.write("A basic arithmetic tool built with Streamlit.")

# Create two columns for input numbers
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Dropdown for operation selection
operation = st.selectbox("Choose an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Calculation logic
result = 0
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
            result = None

    # Display the result
    if result is not None:
        st.success(f"The result is: {result}")
