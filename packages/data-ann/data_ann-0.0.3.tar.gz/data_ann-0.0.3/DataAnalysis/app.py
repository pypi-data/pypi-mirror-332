import streamlit as st
from datetime import date

def main():
    # 全局页面配置（所有页面生效）
    st.set_page_config(
        page_title="数据分析平台",
        layout="wide",
        page_icon="📊"
    )
    
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

if __name__ == "__main__":
    main()