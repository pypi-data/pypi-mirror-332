from typing import Dict, List
from datetime import date
import pandas as pd
from common.database import Database
from common.utils import ChartUtils

class SearchAnalysisService:
    def __init__(self):
        self.db = Database.get_connection()

    def get_daily_search_stats(self) -> Dict[str, List]:
        """获取每日搜索统计数据"""
        query = """
        SELECT DATE(search_time) as search_date,
               COUNT(*) as search_count
        FROM search_logs
        GROUP BY DATE(search_time)
        ORDER BY search_date
        """
        df = pd.read_sql(query, self.db)
        return ChartUtils.prepare_time_series_data(df, 'search_date', 'search_count')

    def get_monthly_search_stats(self) -> Dict[str, List]:
        """获取每月搜索统计数据"""
        query = """
        SELECT DATE_FORMAT(search_time, '%Y-%m') as search_month,
               COUNT(*) as search_count
        FROM search_logs
        GROUP BY search_month
        ORDER BY search_month
        """
        df = pd.read_sql(query, self.db)
        return ChartUtils.prepare_time_series_data(df, 'search_month', 'search_count')

    def get_popular_keywords(self, limit: int = 10) -> Dict[str, int]:
        """获取热门搜索关键词"""
        query = """
        SELECT keyword, COUNT(*) as search_count
        FROM search_logs
        GROUP BY keyword
        ORDER BY search_count DESC
        LIMIT %s
        """
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query, (limit,))
        results = cursor.fetchall()
        cursor.close()

        return {r['keyword']: r['search_count'] for r in results}

    def get_search_trends(self, keyword: str) -> Dict[str, List]:
        """获取特定关键词的搜索趋势"""
        query = """
        SELECT DATE(search_time) as search_date,
               COUNT(*) as search_count
        FROM search_logs
        WHERE keyword = %s
        GROUP BY search_date
        ORDER BY search_date
        """
        df = pd.read_sql(query, self.db, params=(keyword,))
        return ChartUtils.prepare_time_series_data(df, 'search_date', 'search_count')