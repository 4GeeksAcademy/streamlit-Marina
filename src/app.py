# your code here
import streamlit as st

st.title('Hiring chance predictor')

st.write('Welcome to our page! Please insert your data and we will predict your hiring chances in a new job!')

studies = st.selectbox('Please select your level of studies', ('No studies', 
                                                 'Preschool (early childhood education)', 
                                                 'Elementary school', 'Middle school', 
                                                 'High school', 
                                                 'Other studies', 
                                                 'Higher education (Bachelor’s degree)',
                                                 'Master’s degree',
                                                'Ph.D.'))

choice = st.radio('Do you have any former experience in the job you are applying for?', ('No', 'Yes'))

if choice == 'Yes':
    experience = st.selectbox('Please select for how many years:', ('Less than one year', '1-3', '3-6', '6-10', 'More than 10 years'))

languages = st.multiselect('Which Programming Languages are you able to use?', 
                         ['Python', 'JavaScript',
                         'SQL', 'JSON', 'XML', 'C++', 'Java'])

libraries = st.multiselect('Which of these libraries are you familiar with?', ['None', 'Pandas', 'Matplotlib', 'Numpy', 'TensorFlow' ])

environments = st.multiselect('Please select which development environments are you familiar with:',
                              ['React', 'Ruby', 'Linux', 'Wordpress', '.Net', 'AndroidStudio'])

english = st.select_slider('Please select your English level', ('None', 'Basic', 'Intermediate', 'Advanced', 'Native'))

languages = st.text_input('Please write down the languages you can speak: ')

if ((choice == 'Yes' and experience != '')):
    if st.button('Predict!'):
        st.switch_page('pages/prediction.py')