import streamlit as st
import requests

# Defining Page Title,Icon
st.set_page_config(
    page_title="Random Facts Generator",
    page_icon="data:image/png;base64,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",
    menu_items={
        "About":"Unlock the secrets of time, date and numbers with factfusion. Immerse yourself in a world where each visit promises a new discovery—from quirky number quirks to historical milestones and unforgettable dates."
    }
)


t1,t2,t3=st.tabs(["Number Fact","Date Fact","Year Fact"])

with t1:
    st.write("<h3>Unlock the mysteries of numbers with our <span style='color:#fcba03;'> Random Number</span> Fact Generator!</h3>",unsafe_allow_html=True)
    btn1=st.button(":orange[Generate]")
    if btn1:
        try:
            data1=requests.get("http://numbersapi.com/random/trivia")
            st.write(f"<h3 style='color:#FF5580;'>{data1.text}</h3>",unsafe_allow_html=True)
        except:
             st.toast("Network Error",icon="🔌")

with t2:
    st.write("<h3>Step into the time machine and discover fascinating facts and events that occurred on a <span style='color:#6FDCE3'>Random Date</span> in history.</h3>",unsafe_allow_html=True)
    btn2=st.button(":green[Generate]",key=1)
    if btn2:
        try:
            data2=requests.get("http://numbersapi.com/random/date")
            st.write(f"<h3 style='color: #FF7D29;'>{data2.text}</h3>",unsafe_allow_html=True)
        except:
             st.toast("Network Error",icon="🔌")

with t3:
    st.write("<h3>Step into the vault and discover fascinating facts and events that shaped a <span style='color:#EE4E4E'>Random Year</span> in history.</h3>",unsafe_allow_html=True)
    btn3=st.button(":violet[Generate]",key=2)
    if btn3:
        try:
            data3=requests.get("http://numbersapi.com/random/year")
            st.write(f"<h3 style='color:#E58E26;'>{data3.text}</h3>",unsafe_allow_html=True)
        except:
             st.toast("Network Error",icon="🔌")
