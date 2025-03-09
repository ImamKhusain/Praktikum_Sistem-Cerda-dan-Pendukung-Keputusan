import streamlit as st
import pandas as pd
# import matplotlib.pylot as plt

st.text('ini text')
st.write('Adi Gamon')

df = pd.DataFrame({
    'nama' : ['Imam', 'Affan'],
    'umur' : [21,22]
})

st.dataframe(df)

#fitur inetraktif
#BUTTON
if st.button('LOGIN') :
    st.write('Adi Gamon')

# SLIDER (label, min val, max val, default)
nilai = st.slider('slider', 1, 100, 50)
st.write(f'Tingkat Kecerdasan {nilai}')

#SELECT BOX (label, option, index(nilai default))
pilihan = st.selectbox('pilih buah', ['apel', 'anggur', 'pisang'], index=2)
st.write(f'pilihanku {pilihan}')

#NUMBER INPUT (label, min val, max val)
st.number_input('angka', 1, 10)

#TEXT INPUT
st.text_input('nama', placeholder='ketikkan nama', value='Hello')

#STATUS TEKS
st.success('berhasil', icon='😊')
st.error('gagal')

# EXPANDER
with st.expander('lihat'):
    st.write('Aku Lapar')
    st.number_input('angka')
    st.button('submit')

# COLOM
col1, col2, = st.columns(2)
with col1:
    st.write('kolom1')
    st.write('Hello')
with col2:
    st.write('kolom2')
    st.write('Jadi Gini Doang')

# TABS
tab1, tab2 = st.tabs(['TAB 1', 'TAB 2'])
with tab1:
    st.write('ini adalah tab 1')
with tab2:
    st.write('ini second choice')


st.title("Aplikasi Penjumlahan dan Perkalian")
# Input angka
angka1 = st.number_input("Masukkan Angka 1", min_value=0, value=0)
angka2 = st.number_input("Masukkan Angka 2", min_value=0, value=0)
# Tombol untuk operasi
if st.button("Kali"):
    hasil = angka1 * angka2
    st.success(f"Hasil perkalian: {hasil}")
if st.button("Bagi"):
    if angka2 != 0:
        hasil = angka1 / angka2
        st.success(f"Hasil pembagian: {hasil}")
    else:
        st.error("Angka 2 tidak boleh 0 untuk pembagian!")
