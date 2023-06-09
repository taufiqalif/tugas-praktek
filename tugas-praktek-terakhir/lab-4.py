import streamlit as st
from sklearn import linear_model
import pandas as pd
import numpy as np
# import seaborn as sns

import pickle
# import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

# model = st.text_input('Input Model Mobil')
year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input pajak Mobil')
mpg = st.number_input('Input Komsumsi BBM Mobil')
engineSize = st.number_input('Input EngineSize Mobil')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    # a = predict*19000
    st.subheader('Estimasi Harga Mobil Bekas Dalam Rupiah')
    st.write(predict*19000)
    # st.write('Estimasi Harga Mobil Bekas dalam Ponds : ', predict)
    # st.write('Estimasi Harga Mobil Bekas dalam Rupiah :', predict*19000)
