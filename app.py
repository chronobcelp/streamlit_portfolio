import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header('レッスン5: 折れ線グラフ(plotly,go)の作成')
# サンプルデータの作成
data = {
'⽉': ['1⽉', '2⽉', '3⽉', '4⽉', '5⽉', '6⽉'],
'売上': [100, 120, 140, 180, 200, 210],
'利益': [20, 25, 30, 40, 50, 55]
}
df = pd.DataFrame(data)
st.write('サンプルデータ:')
st.dataframe(df)

# 基本的な折れ線グラフの作成
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['⽉'], y=df['売上'], mode='lines+markers',
name='売上'))
fig.add_trace(go.Scatter(x=df['⽉'], y=df['利益'], mode='lines+markers',
name='利益'))
fig.update_layout(title='⽉別売上と利益',
xaxis_title='⽉',
yaxis_title='⾦額（万円）')
st.plotly_chart(fig)

# カスタマイズされた折れ線グラフの作成
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['⽉'], y=df['売上'], mode='lines+markers',
name='売上', line=dict(color='blue', width=2)))
fig.add_trace(go.Scatter(x=df['⽉'], y=df['利益'], mode='lines+markers',
name='利益', line=dict(color='red', width=2)))
fig.update_layout(
title='⽉別売上と利益の推移',
xaxis_title='⽉',
yaxis_title='⾦額（万円）',
font=dict(family="Meiryo", size=12),
legend=dict(orientation="h", yanchor="bottom", y=1.02,
xanchor="right", x=1),
hovermode="x unified"
)

fig.update_xaxes(tickangle=45)
fig.update_yaxes(zeroline=True, zerolinewidth=2,
zerolinecolor='lightgrey')
st.plotly_chart(fig)