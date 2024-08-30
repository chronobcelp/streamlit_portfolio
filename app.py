import streamlit as st
import pandas as pd

st.header('レッスン4: データ⼊⼒と表⽰')
# テキスト⼊⼒
name = st.text_input('あなたの名前を⼊⼒してください')
if name:
   st.write(f'こんにちは、{name}さん！')   

# 数値⼊⼒
age = st.number_input('あなたの年齢を⼊⼒してください', min_value=0,
max_value=120, value=20)
st.write(f'あなたは{age}歳です。')   

# ⽇付⼊⼒
date = st.date_input('⽇付を選択してください')
st.write(f'選択された⽇付: {date}')

# サンプルデータの作成
data = {
'名前': ['太郎', '花⼦', '⼀郎'],
'年齢': [25, 30, 35],
'都市': ['東京', '⼤阪', '福岡']
}
df = pd.DataFrame(data)
# データフレームの表⽰
st.subheader('データフレームの表⽰')
st.dataframe(df)

# 表の表⽰
st.subheader('表の表⽰')
st.table(df)