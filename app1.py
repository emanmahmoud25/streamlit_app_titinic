import streamlit as st

st.set_page_config(
    page_title="My First App",
    page_icon="🚀"
)

st.title("My First Streamlit App")

st.write("Welcome to my application!")

name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello, {name}!")

if st.button("Click Me"):
    st.balloons()

#################################333
st.radio("Select a number:", [1, 2, 3, 4, 5],index=0)
checked = st.checkbox("Check me!")
if checked:
    st.write("You checked the box!")

###################################333
with st.form('Search Form'):
     name = st.text_input("Search")
     classes=st.multiselect("Select classes",[1,2,3,4,5],default=[1,2,3])
     ages=st.slider("Select age range", 0, 100, (25, 75))
     submitted = st.form_submit_button("Submit")
if submitted:
        st.write(f'you searched for: {name} in classes: {classes} and age range: {ages}')
#################################################################


    
