import streamlit as st
import pickle
st.subheader('Iris Flower Identification App')
sl=st.number_input('Enter Sepal Length')
sw=st.number_input('Enter Sepal Width')   
pl=st.number_input('Enter Petal Length')
pw=st.number_input('Enter Petal Width')
button=st.button('Predict')

if button:
    knn=pickle.load(open('iris.pkl','rb'))
    prediction=knn.predict([[sl,sw,pl,pw]])
    st.write('The predicted species is:',{prediction[0]})