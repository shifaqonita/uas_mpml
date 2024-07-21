import pickle
import streamlit as st

# membaca model
resto_model = pickle.load(open('resto_model.sav', 'rb'))

#judul web
st.title('Prediksi Profitability')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    RestaurantID = st.text_input ('input RestaurantID')

with col2 :
    MenuCategory = st.text_input ('input MenuCategory')

with col1 :
    MenuItem = st.text_input ('input MenuItem')

with col2 :
    Price = st.text_input ('input Price')


# code untuk prediksi
resto_pred = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Profitability'):
    resto_prediction = resto_model.predict([[RestaurantID, MenuCategory, MenuItem, Price]])

    if(resto_prediction[0] == 0):
        resto_pred = 'Low' 
    elif(resto_prediction[0] == 1):
        resto_pred = 'Medium'
    else:
        resto_pred = 'High'
st.success(resto_pred)
