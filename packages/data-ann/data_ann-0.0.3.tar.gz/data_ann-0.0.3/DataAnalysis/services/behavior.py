from typing import List, Dict, Any
from datetime import date
import pandas as pd
from sqlalchemy import text
from common.database import Database
from common.parser import LogDate
from common.utils import DataFrameUtils, ChartUtils
from models.data_models import UserEvent


class BehaviorAnalysisService:
    def __init__(self):
        self.db = Database()
        self.session = self.db.get_session()

    def get_event_analysis(self, start_date: date, end_date: date) -> LogDate:
        """获取事件分析数据"""
        query = f"SELECT * FROM sys_log WHERE create_time >= '{str(start_date)}' AND create_time <= '{str(end_date)}' ORDER BY create_time DESC"
        results = self.session.execute(text(query) ).mappings()
        return LogDate(data=[i for i in results])

    def get_funnel_analysis(self, start_date: date, end_date: date, stages: List[str]) -> Dict[str, List]:
        """获取漏斗分析数据"""
        stage_data = []
        for stage in stages:
            query = text("""
            SELECT COUNT(DISTINCT user_id) as user_count
            FROM user_events
            WHERE event_type = :stage
            AND event_date BETWEEN :start_date AND :end_date
            """)
            result = self.session.execute(query, {
                "stage": stage,
                "start_date": start_date,
                "end_date": end_date
            }).scalar()
            stage_data.append({'name': stage, 'value': result})

        return ChartUtils.prepare_funnel_data(stage_data)

    def get_retention_analysis(self, start_date: date, end_date: date) -> pd.DataFrame:
        """获取留存分析数据"""
        query = text("""
        SELECT user_id, event_date
        FROM user_events
        WHERE event_date BETWEEN :start_date AND :end_date
        """)
        df = pd.read_sql(query, self.session.bind, params={"start_date": start_date, "end_date": end_date})
        return DataFrameUtils.calculate_retention_rate(df, 'user_id', 'event_date')

    def get_user_path_analysis(self, start_date: date, end_date: date) -> List[Dict[str, Any]]:
        """获取用户行为路径分析"""
        query = text("""
        SELECT user_id, event_type, event_date, duration
        FROM user_events
        WHERE event_date BETWEEN :start_date AND :end_date
        ORDER BY user_id, event_date
        """)
        results = self.session.execute(query, {
            "start_date": start_date,
            "end_date": end_date
        }).mappings().all()

        paths = {}
        for row in results:
            user_id = row['user_id']
            if user_id not in paths:
                paths[user_id] = []
            paths[user_id].append({
                'event': row['event_type'],
                'date': row['event_date'],
                'duration': float(row['duration'])
            })

        return [{'user_id': k, 'path': v} for k, v in paths.items()]

    def get_user_tags(self, start_date: date, end_date: date) -> Dict[str, int]:
        """获取用户标签分析"""
        query = text("""
        SELECT ut.tag_name, COUNT(DISTINCT ue.user_id) as user_count
        FROM user_events ue
        JOIN user_tags ut ON ue.user_id = ut.user_id
        WHERE ue.event_date BETWEEN :start_date AND :end_date
        GROUP BY ut.tag_name
        """)
        results = self.session.execute(query, {
            "start_date": start_date,
            "end_date": end_date
        }).mappings().all()

        return {r['tag_name']: r['user_count'] for r in results}

    def __del__(self):
        self.session.close()
