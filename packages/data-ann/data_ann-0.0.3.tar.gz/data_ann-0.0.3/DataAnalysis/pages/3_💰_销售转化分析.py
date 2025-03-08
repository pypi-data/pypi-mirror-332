import streamlit as st
from datetime import date
from services.sales import SalesAnalysisService
from common.utils import DateUtils
import plotly.graph_objects as go

# 页面配置
st.set_page_config(page_title="销售转化分析", page_icon="💰", layout="wide")

# 创建服务实例
service = SalesAnalysisService()

# 页面标题
st.title("💰 销售转化分析")

# 日期选择
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("开始日期", date.today().replace(day=1))
with col2:
    end_date = st.date_input("结束日期", date.today())

# 验证日期范围
if not DateUtils.validate_date_range(start_date, end_date):
    st.error("请选择有效的日期范围")
    st.stop()

# 确认按钮
if st.button("确认分析", type="primary"):
    # 获取销售指标数据
    metrics = service.get_sales_metrics(start_date, end_date)
    
    # 创建三列布局显示核心指标
    col1, col2, col3 = st.columns(3)
    
    # 订单指标
    with col1:
        st.subheader("📦 订单指标")
        st.metric("订单提交量", metrics['order_metrics']['total_orders'])
        st.metric("订单总金额", metrics['order_metrics']['total_amount'])
        st.metric("下单用户数", metrics['order_metrics']['total_users'])
    
    # 支付指标
    with col2:
        st.subheader("💳 支付指标")
        st.metric("支付订单量", metrics['payment_metrics']['paid_orders'])
        st.metric("支付金额", metrics['payment_metrics']['paid_amount'])
        st.metric("支付用户数", metrics['payment_metrics']['paid_users'])
    
    # 性能指标
    with col3:
        st.subheader("📊 性能指标")
        st.metric("取消订单量", metrics['performance_metrics']['cancelled_orders'])
        st.metric("复购率", metrics['performance_metrics']['repurchase_rate'])
        st.metric("客单价", metrics['performance_metrics']['average_order_value'])
    
    # 销售趋势分析
    st.subheader("📈 销售趋势分析")
    trend_data = service.get_daily_sales_trend(start_date, end_date)
    
    # 创建销售趋势图
    fig = go.Figure()
    
    # 添加订单量曲线
    fig.add_trace(go.Scatter(
        x=trend_data['dates'],
        y=trend_data['orders'],
        name='订单量',
        mode='lines+markers',
        line=dict(color='rgb(26, 118, 255)')
    ))
    
    # 添加销售金额曲线
    fig.add_trace(go.Scatter(
        x=trend_data['dates'],
        y=trend_data['amounts'],
        name='销售金额',
        mode='lines+markers',
        line=dict(color='rgb(55, 83, 109)'),
        yaxis='y2'
    ))
    
    # 更新布局
    fig.update_layout(
        title='每日销售趋势',
        xaxis_title='日期',
        yaxis_title='订单量',
        yaxis2=dict(
            title='销售金额',
            overlaying='y',
            side='right'
        ),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)