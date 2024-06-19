import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import time

# 设置Streamlit应用程序的标题
st.set_page_config(page_title="streamlit WebUI", layout="wide")

st.sidebar.title("智慧校园")
st.write("欢迎使用湖南工商大学智慧校园助手！")

menu1 = "智慧校园智能对话框"

with st.sidebar:
    menu = option_menu("智慧校园", [menu1],
        icons=['house', "list-task"],
        menu_icon="cast", default_index=0)

def main():
    if menu == menu1:
        # 使用 st.markdown 来创建一个可点击的标题
        st.markdown('<h2><a href="http://www.hutb.edu.cn/" target="_blank">湖南工商大学</a></h2>', unsafe_allow_html=True)
        showLLMChatbot()

def showLLMChatbot():
    st.title("智慧校园")
    st.caption("至诚至信，为实为新。")

    info = st.text_input("输入你的问题：")
    if info:
        st.write("用户: " + info)
        st.write("商: 我是湖南工商大学智慧校园助手！")

if __name__ == '__main__':
    main()
