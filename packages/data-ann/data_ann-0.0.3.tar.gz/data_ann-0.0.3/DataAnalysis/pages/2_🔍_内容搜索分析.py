import streamlit as st
from services.search import SearchAnalysisService
import plotly.graph_objects as go
import plotly.express as px

# 页面配置
st.set_page_config(page_title="内容搜索分析", page_icon="🔍", layout="wide")

# 创建服务实例
service = SearchAnalysisService()

# 页面标题
st.title("🔍 内容搜索分析")

# 创建两列布局
col1, col2 = st.columns(2)

# 每日搜索统计
with col1:
    st.subheader("📅 每日搜索统计")
    daily_stats = service.get_daily_search_stats()
    
    # 创建每日搜索趋势图
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily_stats['dates'],
        y=daily_stats['values'],
        mode='lines+markers',
        name='每日搜索量',
        line=dict(color='rgb(26, 118, 255)')
    ))
    fig.update_layout(
        title='每日搜索趋势',
        xaxis_title='日期',
        yaxis_title='搜索次数'
    )
    st.plotly_chart(fig, use_container_width=True)

# 每月搜索统计
with col2:
    st.subheader("📊 每月搜索统计")
    monthly_stats = service.get_monthly_search_stats()
    
    # 创建每月搜索趋势图
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=monthly_stats['dates'],
        y=monthly_stats['values'],
        name='每月搜索量',
        marker_color='rgb(55, 83, 109)'
    ))
    fig.update_layout(
        title='每月搜索趋势',
        xaxis_title='月份',
        yaxis_title='搜索次数'
    )
    st.plotly_chart(fig, use_container_width=True)

# 热门搜索关键词分析
st.subheader("🔥 热门搜索关键词")

# 设置显示的关键词数量
top_n = st.slider("选择显示的关键词数量", min_value=5, max_value=20, value=10)

# 获取热门关键词数据
popular_keywords = service.get_popular_keywords(limit=top_n)

# 创建热门关键词图表
fig = go.Figure(data=[go.Bar(
    x=list(popular_keywords.keys()),
    y=list(popular_keywords.values()),
    marker_color='rgb(26, 118, 255)'
)])
fig.update_layout(
    title='热门搜索关键词统计',
    xaxis_title='关键词',
    yaxis_title='搜索次数',
    xaxis_tickangle=-45
)
st.plotly_chart(fig, use_container_width=True)

# 关键词搜索趋势分析
st.subheader("📈 关键词搜索趋势分析")

# 选择要分析的关键词
selected_keyword = st.selectbox(
    "选择要分析的关键词",
    options=list(popular_keywords.keys())
)

# 获取并显示选中关键词的搜索趋势
if selected_keyword:
    trend_data = service.get_search_trends(selected_keyword)
    
    # 创建搜索趋势图
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=trend_data['dates'],
        y=trend_data['values'],
        mode='lines+markers',
        name=f'{selected_keyword}的搜索趋势',
        line=dict(color='rgb(55, 83, 109)')
    ))
    fig.update_layout(
        title=f'{selected_keyword} 的搜索趋势分析',
        xaxis_title='日期',
        yaxis_title='搜索次数'
    )
    st.plotly_chart(fig, use_container_width=True)