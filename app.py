import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header('レッスン6: 棒グラフ(plotly,go)の作成')
# サンプルデータの作成
data = {
'製品': ['A', 'B', 'C', 'D', 'E'],
'売上': [300, 400, 200, 600, 500],
'利益': [30, 60, 20, 100, 80]
}
df = pd.DataFrame(data)
st.write('サンプルデータ:')
st.dataframe(df)

# 基本的な棒グラフの作成
fig = go.Figure()
fig.add_trace(go.Bar(x=df['製品'], y=df['売上'], name='売上'))
fig.add_trace(go.Bar(x=df['製品'], y=df['利益'], name='利益'))
fig.update_layout(title='製品別の売上と利益',
xaxis_title='製品',
yaxis_title='⾦額（万円）',
barmode='group')
st.plotly_chart(fig)

# カスタマイズされた棒グラフの作成
fig = go.Figure()
fig.add_trace(go.Bar(x=df['製品'], y=df['売上'], name='売上',
marker_color='blue'))
fig.add_trace(go.Bar(x=df['製品'], y=df['利益'], name='利益',
marker_color='red'))
fig.update_layout(
title='製品別の売上と利益⽐較',
xaxis_title='製品',
yaxis_title='⾦額（万円）',
barmode='group',
font=dict(family="Meiryo", size=12),
legend=dict(orientation="h", yanchor="bottom", y=1.02,
xanchor="right", x=1),
hovermode="x unified"
)
fig.update_traces(texttemplate='%{y}', textposition='outside')
fig.update_yaxes(range=[0, max(df['売上'].max(), df['利益'].max()) * 1.1])
st.plotly_chart(fig)