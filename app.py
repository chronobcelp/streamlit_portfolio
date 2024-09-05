import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header('レッスン7: 円グラフ(plotly,go)の作成')
# サンプルデータの作成
data = {
'商品': ['A', 'B', 'C', 'D', 'E'],
'売上': [300, 200, 180, 150, 120]
}
df = pd.DataFrame(data)
st.write('サンプルデータ:')
st.dataframe(df)

# 基本的な円グラフの作成
fig = go.Figure(data=[go.Pie(labels=df['商品'], values=df['売上'])])
fig.update_layout(title='商品別売上⽐率')
st.plotly_chart(fig)

# カスタマイズされた円グラフの作成
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen',
'lightcoral']
fig = go.Figure(data=[go.Pie(labels=df['商品'],
values=df['売上'],
hole=.3,
marker=dict(colors=colors,
line=dict(color='#000000',
width=2)))])
fig.update_traces(textposition='inside',
textinfo='percent+label',
hoverinfo='label+value+percent',
textfont_size=14)
fig.update_layout(
title='商品別売上⽐率（詳細版）',
font=dict(family="Meiryo", size=12),
legend=dict(orientation="h", yanchor="bottom", y=1.02,
xanchor="right", x=1),
annotations=[dict(text='総売上', x=0.5, y=0.5, font_size=20,
showarrow=False)]
)
st.plotly_chart(fig)