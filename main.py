import streamlit as st
import datetime
import time
st.markdown("<h1 style='text-align: center; color: green;'>game password</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>"
"Придумай пароль!</p>", unsafe_allow_html=True)
st.markdown('*начнём игру?*')
current = time.localtime()
hour = time.strftime('%H')
date = time.strftime('%d')
day = time.strftime('%A')

def check(password):
    count_s_symbol = 0
    count_num = 0
    count_lower = 0
    count_upper = 0
    for symbol in password:
        if symbol in '[!"№%:,.;()_-+=/?}{\|<~>$@#%^&*':
            count_s_symbol += 1
        if symbol in '1234567890':
            count_num += 1
        if symbol in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            count_lower += 1
        if symbol in 'qwertyuiopasdfghjklzxcvbnm':
            count_upper += 1
    if len(password) < 15:
        st.text('Пароль должен содержать как минимум 15 символов')
    elif len(password) > 70:
        st.text('Пароль должен содержать максимум 70 символов')
    elif '11.12.2008' not in password:
            st.text('Пароль должен содержать мою дату рождения')
    elif 'plie' not in password:
        st.text('Пароль должен содержать название движения в балете')
    elif '1991' in password:
        st.text('Пароль не должен содержать год распада СССР')
    elif hour not in password:
        st.text('Пароль должен содержать текущий час')
    elif date not in password:
        st.text('Пароль должен содержать текущию дату')
    elif day not in password:
        st.text('Пароль должен содержать название дня недели')
    elif count_s_symbol < 2:
        st.markdown('Пароль должен содержать один спец. символ')
    elif count_num < 4:
        st.text('Пароль должен содержать как минимум 4 цифры')
    elif count_lower < 3:
        st.text('Пароль должен содержать две заглавных англ. букв')

    else:
        st.text('Поздравляю, ваш пароль подходит! Только не забудьте его;D')



password = st.text_input('Введите пароль', max_chars=70, type='password')

check(password)