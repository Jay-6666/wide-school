import streamlit as st
from streamlit_option_menu import option_menu
import requests

# 设置Streamlit应用程序的标题
st.set_page_config(page_title="streamlit WebUI", layout="wide")

st.sidebar.title("智慧校园")
st.write("欢迎使用湖南工商大学智慧校园助手！")

menu1 = "智慧校园智能对话框"

with st.sidebar:
    menu = option_menu("智慧校园", [menu1],
        icons=['house', "list-task"],
        menu_icon="cast", default_index=0)

def query_zhizhu_api(question):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"  # 替换为智谱清言API的实际URL
    headers = {
        "Authorization": "Bearer f98c361b47c3be0e51876e6895847ac9.xQrpLy1oLpYBPlXY",  # 替换为你的API密钥
        "Content-Type": "application/json"
    }
    payload = {
        "model": "glm-4",
        "messages": [
            {"role": "assistant", "content": "我是智慧校园助手商专"},
            {"role": "user", "content": question},
        ],
        "top_p": 0.7,
        "temperature": 0.9,
        "stream": False,
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]  # 根据API返回的结构提取答案
    else:
        return "抱歉，我无法获取答案。"

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
        answer = query_zhizhu_api(info)
        st.write("商: " + answer)

if __name__ == '__main__':
    main()
