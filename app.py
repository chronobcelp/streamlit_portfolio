import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

st.header('レッスン9: セッション状態の管理')
if 'count' not in st.session_state:
    st.session_state.count = 0
st.write(f"現在のカウント: {st.session_state.count}")
if st.button('カウントアップ'):
    st.session_state.count += 1
    st.rerun()
    
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""

user_name = st.text_input("ユーザー名", value=st.session_state.user_name)
user_email = st.text_input("メールアドレス",
value=st.session_state.user_email)

if st.button("ユーザー情報を保存"): 
    st.session_state.user_name = user_name
    st.session_state.user_email = user_email
    st.success("ユーザー情報が保存されました！")

st.write(f"セッションに保存されたユーザー名: {st.session_state.user_name}")
st.write(f"セッションに保存されたメールアドレス: {st.session_state.user_email}")

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['商品', '価格'])
product = st.text_input("商品名を⼊⼒")
price = st.number_input("価格を⼊⼒", min_value=0)

if st.button("商品データを追加"):
    new_data = pd.DataFrame({'商品': [product], '価格': [price]})
    st.session_state.df = pd.concat([st.session_state.df, new_data],ignore_index=True)

st.write("現在の商品データ:")
st.write(st.session_state.df)

if st.button("データをリセット"):
    st.session_state.df = pd.DataFrame(columns=['商品', '価格'])
    st.rerun()