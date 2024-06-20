import streamlit as st
from streamlit_option_menu import option_menu
import requests

st.set_page_config(page_title="streamlit WebUI", layout="wide")

st.sidebar.title("智慧校园")
st.write("欢迎使用湖南工商大学智慧校园助手！")

menu1 = "智慧校园智能对话框"
menu2 = "课表查询"
menu3 = "学校班车信息"
menu4 = "校园风景"

with st.sidebar:
    menu = option_menu("智慧校园", [menu1, menu2, menu3, menu4],
        icons=['chat', 'calendar', 'bus', 'image'],
        menu_icon="cast", default_index=0)

def query_zhizhu_api(question):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    headers = {
        "Authorization": "Bearer f98c361b47c3be0e51876e6895847ac9.xQrpLy1oLpYBPlXY",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "glm-4",
        "messages": [
            {"role": "assistant", "content": "我是智慧校园助手"},
            {"role": "user", "content": question},
        ],
        "top_p": 0.7,
        "temperature": 0.9,
        "stream": False,
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "抱歉，我无法获取答案。"

def showLLMChatbot():
    st.title("智慧校园")
    st.caption("至诚至信，为实为新。")

    info = st.text_input("输入你的问题：")
    if info:
        st.write("用户: " + info)
        answer = query_zhizhu_api(info)
        st.write("智慧校园助手: " + answer)

def showCourseSchedule():
    st.title("课表查询")
    st.caption("查询你的课程安排。")
    st.image("kebiao.png", caption="课程表")

def showBusInfo():
    st.title("学校班车信息")
    st.caption("查看学校班车的时刻表。")
    st.image("car.jpg", caption="班车时刻表")

def showCampusScenes():
    st.title("校园风景")
    st.caption("欣赏湖南工商大学的美丽校园。")
    st.image("hutb.jpg", caption="校园风景")

def main():
    if menu == menu1:
        st.markdown('<h2><a href="http://www.hutb.edu.cn/" target="_blank">湖南工商大学</a></h2>', unsafe_allow_html=True)
        showLLMChatbot()
    elif menu == menu2:
        showCourseSchedule()
    elif menu == menu3:
        showBusInfo()
    elif menu == menu4:
        showCampusScenes()

if __name__ == '__main__':
    main()
