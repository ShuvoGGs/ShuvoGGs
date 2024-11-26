import streamlit as st
st.title("My App")

st.header('Mobile Number Validation')
st.write('Enter a mobile number and validate')
st.write('')
input_mob = st.text_input('Enter a Mobile Number')

if input_mob:
	st.subheader('report')

#show image
image_path_1= r'Image/a.jpg'
st.image(image_path_1)