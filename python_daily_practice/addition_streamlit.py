# import streamlit as st
# st.set_page_config(page_title="Number Addition",page_icon="➕",layout="centered")
# st.title("Addition of Two Numbers")
# st.caption("Enter two number will return additon of them")
# form=st.form("add_form")
# num1=form.number_input("First Number")
# num2=form.number_input("Second Number")
# submitted=form.form_submit_button("Calculate Sum")
# if submitted:
#     result=num1+num2
#     st.divider()
#     st.success(F"sum{result}")
#     st.metric(label="Result",value=result)

# for i in range(1,11):
#     st.write(f"2 * {i} = {2*i}")

import streamlit as st
st.set_page_config(page_title="multiplication of numbers",page_icon="✖️",layout="centered")
st.title("multiplication of numbers")
st.caption("product of two numbers in result")
form=st.form("add_form")
num1=form.number_input("enter first number")
num2=form.number_input("enter second number")
submitted=form.form_submit_button("calculate product")
if submitted:
    Result=num1*num2
    st.divider()
    st.success(f"product{Result}")
    st.metric(label="Result",value=Result)
    
