import numpy as np
import pandas as pd
import streamlit as st
from datetime import date

from pandas import DataFrame

from services.behavior import BehaviorAnalysisService
from common.utils import DateUtils, calculate_duration
import plotly.graph_objects as go
import plotly.express as px

# 页面配置
st.set_page_config(page_title="用户行为分析", page_icon="👤", layout="wide")

# 创建服务实例
service = BehaviorAnalysisService()

# 页面标题
st.title("👤 用户行为分析")

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
    # 事件分析数据获取和验证
    event_data = service.get_event_analysis(start_date, end_date)
    if not event_data:
        st.error("未获取到有效的用户分析数据")
        st.stop()
    
    user_data = event_data.get_user_all()
    if not user_data:
        st.error("未获取到有效的用户行为数据")
        st.stop()
    df = pd.DataFrame([{
        '用户ID': user.user_id,
        '行为类型': user.module,
        '详情': user.description,
        '时间': pd.to_datetime(user.create_time),
        '停留时间': None
    } for user in user_data])
    df = calculate_duration(df)
    if df.empty:
        st.error("计算用户停留时间失败")
        st.stop()

    # 创建三列布局
    col1, col2 = st.columns(2)

    # # 事件分析
    # with col1:
    #     st.subheader("📊 事件分析")
    #     # 创建事件分析图表
    #     fig = go.Figure()
    #     fig.add_trace(go.Bar(
    #         name='事件次数',
    #         x=event_data['event_types'],
    #         y=event_data['event_counts'],
    #         marker_color='rgb(55, 83, 109)'
    #     ))
    #     fig.add_trace(go.Bar(
    #         name='用户数',
    #         x=event_data['event_types'],
    #         y=event_data['user_counts'],
    #         marker_color='rgb(26, 118, 255)'
    #     ))
    #     fig.update_layout(
    #         title='事件分析统计',
    #         xaxis_title='事件类型',
    #         yaxis_title='数量',
    #         barmode='group'
    #     )
    #     st.plotly_chart(fig, use_container_width=True)
    #
    # # 漏斗分析数据获取和验证
    # stages = ['浏览', '加入购物车', '提交订单', '支付成功']
    # funnel_data = end_date.get_funnel_data()
    # if not funnel_data or not funnel_data.get('stages') or not funnel_data.get('values'):
    #     st.error("未获取到有效的漏斗分析数据")
    #     st.stop()
    #
    # # 漏斗分析
    # with col2:
    #     st.subheader("🔄 漏斗分析")
    #     # 创建漏斗图
    #     fig = go.Figure(go.Funnel(
    #         y=funnel_data['stages'],
    #         x=funnel_data['values'],
    #         textinfo="value+percent initial"
    #     ))
    #     fig.update_layout(title='用户转化漏斗')
    #     st.plotly_chart(fig, use_container_width=True)
    #
    # # 留存分析数据获取和验证
    # retention_data = service.get_retention_analysis(start_date, end_date)
    # if retention_data is None or retention_data.empty:
    #     st.error("未获取到有效的留存分析数据")
    #     st.stop()
    #
    # # 留存分析
    # st.subheader("📈 留存分析")
    # # 创建留存率热力图
    # fig = px.line(
    #     retention_data,
    #     x=retention_data.index,
    #     y=retention_data.columns[0],
    #     title='用户留存率趋势'
    # )
    # st.plotly_chart(fig, use_container_width=True)
    #
    # # 用户路径分析数据获取和验证
    # path_data = service.get_user_path_analysis(start_date, end_date)
    # if not path_data:
    #     st.error("未获取到有效的用户路径数据")
    #     st.stop()
    #
    # # 用户路径分析
    # st.subheader("🛣️ 用户行为路径")
    # # 展示用户路径数据
    # for user_path in path_data[:5]:  # 只显示前5个用户的路径
    #     with st.expander(f"用户 {user_path['user_id']} 的行为路径"):
    #         for event in user_path['path']:
    #             st.write(f"事件: {event['event']} | 时间: {event['date']} | 停留时长: {event['duration']}秒")
    #
    # # 用户标签分析数据获取和验证
    # tags_data = service.get_user_tags(start_date, end_date)
    # if not tags_data:
    #     st.error("未获取到有效的用户标签数据")
    #     st.stop()
    #
    # # 用户标签分析
    # st.subheader("🏷️ 用户标签分析")
    # # 创建标签分布图
    # fig = go.Figure(data=[go.Pie(
    #     labels=list(tags_data.keys()),
    #     values=list(tags_data.values()),
    #     hole=.3
    # )])
    # fig.update_layout(title='用户标签分布')
    # st.plotly_chart(fig, use_container_width=True)

    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    import plotly.express as px

    # 假设 df 是你的数据
    df = pd.DataFrame([{
        '用户ID': user.user_id,
        '行为类型': user.module,
        '详情': user.description,
        '时间': pd.to_datetime(user.create_time),
        '停留时间': None
    } for user in user_data])

    # 1. 事件分析
    with st.container():
        st.subheader("📊 事件分析")

        # 事件频率统计
        event_counts = df['行为类型'].value_counts().reset_index(name='次数')
        event_data = {
            'event_types': event_counts['行为类型'],
            'event_counts': event_counts['次数'],
            'user_counts': df.groupby('行为类型')['用户ID'].nunique().values  # 每个事件的独立用户数
        }

        # 创建事件分析图表
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='事件次数',
            x=event_data['event_types'],
            y=event_data['event_counts'],
            marker_color='rgb(55, 83, 109)'
        ))
        fig.add_trace(go.Bar(
            name='用户数',
            x=event_data['event_types'],
            y=event_data['user_counts'],
            marker_color='rgb(26, 118, 255)'
        ))
        fig.update_layout(
            title='事件分析统计',
            xaxis_title='事件类型',
            yaxis_title='数量',
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)

    # 2. 漏斗分析
    with st.container():
        st.subheader("📉 漏斗分析")

        # 漏斗分析（示例：注册->浏览->支付）
        funnel_steps = ['注册', '浏览', '支付']
        step_users = []
        current_users = set()
        for step in funnel_steps:
            current_users = current_users.intersection(df[df['行为类型'] == step]['用户ID']) if step_users else \
                set(df[df['行为类型'] == step]['用户ID'])
            step_users.append(current_users)
        funnel_data = pd.DataFrame({
            '步骤': funnel_steps,
            '用户数': [len(users) for users in step_users]
        })

        # 绘制漏斗图
        fig = px.funnel(funnel_data, x='用户数', y='步骤', title='转化漏斗分析')
        st.plotly_chart(fig, use_container_width=True)

    # 3. 留存分析
    with st.container():
        st.subheader("📈 留存分析")

        # 留存分析（以注册为初始事件）
        registered = df[df['行为类型'] == '注册'][['用户ID', '时间']].drop_duplicates('用户ID')
        merged = df.merge(registered, on='用户ID', suffixes=('', '_注册'))
        merged['天数差异'] = (merged['时间'] - merged['时间_注册']).dt.days

        # 计算留存数据
        retention = merged[merged['天数差异'] >= 0].groupby('天数差异')['用户ID'].nunique().reset_index(name='用户数')

        # 计算总注册用户数
        total_registered_users = registered['用户ID'].nunique()

        # 直接计算留存率，无需合并
        retention['留存率'] = retention['用户数'] / total_registered_users

        # 绘制留存曲线
        fig = px.line(retention, x='天数差异', y='留存率', title='留存率曲线', markers=True)
        fig.update_layout(xaxis_title='注册后天数', yaxis_title='留存率')
        st.plotly_chart(fig, use_container_width=True)

    # 4. 用户行为路径分析
    with st.container():
        st.subheader("🛤️ 用户行为路径分析")
        import networkx as nx

        # 生成行为转移矩阵
        df['下一个行为类型'] = df.groupby('用户ID')['行为类型'].shift(-1)
        edges = df.groupby(['行为类型', '下一个行为类型']).size().reset_index(name='数量')
        edges = edges.rename(columns={'行为类型': '来源', '下一个行为类型': '目标'})
        edges.dropna(subset=['目标'], inplace=True)

        # 创建网络图
        G = nx.from_pandas_edgelist(edges, source='来源', target='目标', edge_attr='数量', create_using=nx.DiGraph())

        # 绘制网络图
        pos = nx.spring_layout(G)  # 布局算法
        edge_trace = []
        for edge in G.edges(data=True):
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_trace.append(go.Scatter(
                x=[x0, x1, None], y=[y0, y1, None],
                line=dict(width=edge[2]['数量'] / edges['数量'].max() * 10, color='#888'),
                hoverinfo='none',
                mode='lines'
            ))

        node_trace = go.Scatter(
            x=[], y=[], text=[], mode='markers+text', hoverinfo='text',
            marker=dict(size=10, color='lightblue'),
            textposition="top center"
        )

        for node in G.nodes():
            x, y = pos[node]
            node_trace['x'] += (x,)
            node_trace['y'] += (y,)
            node_trace['text'] += (node,)

        fig = go.Figure(data=edge_trace + [node_trace],
                        layout=go.Layout(
                            title='用户行为路径网络图',
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                        ))
        st.plotly_chart(fig, use_container_width=True)

    # 5. 标签分析
    with st.container():
        st.subheader("🏷️ 用户标签分析")

        # 最近一次活跃时间标签
        current_time = df['时间'].max()
        user_last_active = df.groupby('用户ID')['时间'].max().reset_index()
        user_last_active['最近活跃天数'] = (current_time - user_last_active['时间']).dt.days
        user_last_active['活跃度标签'] = pd.cut(user_last_active['最近活跃天数'],
                                                bins=[0, 3, 7, 30, np.inf],
                                                labels=['极高', '高', '中', '低'])

        # 活跃度标签分布
        active_tag_counts = user_last_active['活跃度标签'].value_counts().reset_index(name='用户数')
        fig = px.bar(active_tag_counts, x='活跃度标签', y='用户数', title='用户活跃度标签分布')
        st.plotly_chart(fig, use_container_width=True)

        # # 购买行为标签
        # has_purchased = df[df['行为类型'] == '支付' or df['行为类型']=="普通支付"]['用户ID'].unique()
        # user_last_active['是否购买'] = user_last_active['用户ID'].isin(has_purchased).map({True: '是', False: '否'})
        #
        # # 购买行为标签分布
        # purchase_tag_counts = user_last_active['是否购买'].value_counts().reset_index(name='用户数')
        # fig = px.pie(purchase_tag_counts, values='用户数', names='是否购买', title='用户购买行为分布')
        # st.plotly_chart(fig, use_container_width=True)

        # 购买行为标签
        has_purchased = df[(df['行为类型'] == '支付') | (df['行为类型'] == '普通支付')]['用户ID'].unique()

        # 添加购买行为标签
        user_last_active['是否购买'] = user_last_active['用户ID'].isin(has_purchased).map({True: '是', False: '否'})

        # 购买行为标签分布
        purchase_tag_counts = user_last_active['是否购买'].value_counts().reset_index(name='用户数')
        fig = px.pie(purchase_tag_counts, values='用户数', names='是否购买', title='用户购买行为分布')
        st.plotly_chart(fig, use_container_width=True)