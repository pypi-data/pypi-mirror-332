import streamlit as st
from datetime import date

def show_page():
    # 页面专属配置（不影响其他页面）
    st.markdown("# 欢迎使用数据分析平台 🚀")
    # 全局状态初始化
    if 'start_date' not in st.session_state:
        st.session_state.start_date = date.today()
    if 'end_date' not in st.session_state:
        st.session_state.end_date = date.today()
    
    # 全局侧边栏控件（显示在左侧导航下方）
    with st.sidebar:
        # 显示在用户行为分析和销售转化分析页面
        current_page = st.session_state.get("current_page")
        if current_page in ["👤 用户行为分析", "💰 销售转化分析"]:
            st.subheader("⏰ 时间范围选择")
            start = st.date_input("开始日期", value=st.session_state.start_date)
            end = st.date_input("结束日期", value=st.session_state.end_date)
            
            if st.button("应用筛选", type="primary"):
                st.session_state.start_date = start
                st.session_state.end_date = end
                st.rerun()
        
        # 显示在所有页面的附加信息
        st.markdown("---")
        st.caption("系统版本: v1.0.0")

    # 功能模块介绍
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("👥 用户行为分析")
            st.markdown("""
            - 用户轨迹追踪
            - 停留时间分析
            - 行为漏斗模型
            """)
        
        with col2:
            st.subheader("🔍 内容搜索分析")
            st.markdown("""
            - 实时搜索统计
            - 关键词热度榜
            - 月度趋势报告
            """)
        
        with col3:
            st.subheader("💰 销售转化分析")
            st.markdown("""
            - 支付成功率监控
            - 复购率分析
            - 客单价分布
            """)


# 通过页面名称设置当前页面状态
if __name__ == "__main__":
    st.session_state.current_page = "Home"
    show_page()