# 環境変数の読み込み
from dotenv import load_dotenv
load_dotenv()

# StreamlitとLangChainのインポート
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# LLMに質問する関数の定義
def Answer_expert(input_message, expert_type):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    if expert_type == "Webアプリの専門家":
        system_content = "あなたはWebアプリの専門家です。"
        ai_intro = "私はWebアプリの専門家ChatOpenAIです。ご質問にお答えします。"
    elif expert_type == "健康の専門家":
        system_content = "あなたは健康の専門家です。"
        ai_intro = "私は健康の専門家ChatOpenAIです。ご質問にお答えします。"
    else:
        system_content = "あなたは資産運用の専門家です。"
        ai_intro = "私は資産運用の専門家ChatOpenAIです。ご質問にお答えします。"

    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=input_message),
        AIMessage(content=ai_intro),
    ]

    result = llm(messages)
    return(result.content)


# メイン処理
st.title("My Streamlit LLM App")
st.write("### ◻️Webアプリの専門家への質問")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;Webアプリケーション全般についての質問を受け付けております。")
st.write("### ◻️健康の専門家への質問")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;健康に関する質問を受け付けております。")
st.write("### ◻️資産運用の専門家への質問")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;資産運用に関する質問を受け付けております。")

st.divider()

select_item = st.radio(
    "専門家を選択してください",
    ("Webアプリの専門家", "健康の専門家", "資産運用の専門家")
)

st.divider()

if select_item == "Webアプリの専門家":
    input_message = st.text_input("入力フォームにテキストを入力し、「質問する」ボタンを押すことで専門家からの回答を得ることができます。")

elif select_item == "健康の専門家":
    input_message = st.text_input("入力フォームにテキストを入力し、「質問する」ボタンを押すことで専門家からの回答を得ることができます。")

else:
    input_message = st.text_input("入力フォームにテキストを入力し、「質問する」ボタンを押すことで専門家からの回答を得ることができます。")

if st.button("質問する"):
    st.divider()

    if select_item == "Webアプリの専門家":
        if input_message:
            st.write("専門家からの回答: ", Answer_expert(input_message, select_item))
        else:
            st.error("質問を入力してから「質問する」ボタンを押してください。")

    elif select_item == "健康の専門家":
        if input_message:
            st.write("専門家からの回答: ", Answer_expert(input_message, select_item))
        else:
            st.error("質問を入力してから「質問する」ボタンを押してください。")

    else:
        if input_message:
            st.write("専門家からの回答: ", Answer_expert(input_message, select_item))
        else:
            st.error("質問を入力してから「質問する」ボタンを押してください。")