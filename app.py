import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

st.header('レッスン8: キャッシュを使⽤したパフォーマンス最適化')
def generate_large_dataset():
# ⼤きなデータセットを⽣成（約10秒かかる）
    data = pd.DataFrame(np.random.randn(1000000, 5), columns=['A', 'B','C', 'D', 'E'])
    return data

@st.cache_data
def load_data_cached():
    return generate_large_dataset()

def load_data_uncached():
    return generate_large_dataset()

st.subheader("キャッシュなしの場合")
start_time = time.time()
data_uncached = load_data_uncached()
end_time = time.time()
st.write(f"データ読み込み時間: {end_time - start_time:.2f} 秒")
st.write(data_uncached.head())

st.subheader("キャッシュありの場合")
start_time = time.time()
data_cached = load_data_cached()
end_time = time.time()
st.write(f"データ読み込み時間: {end_time - start_time:.2f} 秒")
st.write(data_cached.head())
st.write("キャッシュありの場合、2回⽬以降の読み込みは⾮常に⾼速になります。") ,

@st.cache_resource
def load_large_dataset():
    return pd.DataFrame(
np.random.randn(1000000, 5),
columns=['A', 'B', 'C', 'D', 'E']
)

st.subheader("⼤規模データセットの処理")
start_time = time.time()
large_data = load_large_dataset()
end_time = time.time()
st.write(f"⼤規模データセット読み込み時間: {end_time - start_time:.2f} 秒")
st.write(f"データセットの形状: {large_data.shape}")
st.write(large_data.head())

@st.cache_data(ttl=10)
def get_current_time():
    return pd.Timestamp.now()
st.subheader("キャッシュの無効化")
st.write("現在時刻（10秒ごとに更新）:")
st.write(get_current_time())