import streamlit as st
import requests

t1,t2,t3=st.tabs(["Number Fact","Date Fact","Year Fact"])

with t1:
    data1=requests.get("http://numbersapi.com/random/trivia")
    st.markdown("<h1 style='color:#fcba03;'>Random Number Fact Generator</h1>",unsafe_allow_html=True)
    btn1=st.button(":blue[Generate]")
    if btn1:
        st.write(f"<h3 style='color: #DA70D6;'>{data1.text}</h3>",unsafe_allow_html=True)

with t2:
    data2=requests.get("http://numbersapi.com/random/date")
    st.markdown("<h1 style='color: #FF6347;'>Random Date Fact Generator</h1>",unsafe_allow_html=True)
    btn2=st.button(":violet[Generate]",key=1)
    if btn2:
        st.write(f"<h3 style='color:  #F08080;'>{data2.text}</h3>",unsafe_allow_html=True)

with t3:
    data3=requests.get("http://numbersapi.com/random/year")
    st.markdown("<h1 style='color:#DB7093;'>Random Year Fact Generator</h1>",unsafe_allow_html=True)
    btn3=st.button(":green[Generate]",key=2)
    if btn3:
        st.write(f"<h3 style='color:#E58E26;'>{data3.text}</h3>",unsafe_allow_html=True)
