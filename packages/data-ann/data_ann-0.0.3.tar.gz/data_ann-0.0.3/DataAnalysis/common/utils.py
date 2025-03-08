from datetime import date, datetime
from typing import Union, List, Dict, Any
import pandas as pd
from pandas import DataFrame


class DateUtils:
    @staticmethod
    def validate_date_range(start_date: date, end_date: date) -> bool:
        """验证日期范围的有效性"""
        return start_date <= end_date and start_date <= date.today()

    @staticmethod
    def format_date(d: date) -> str:
        """格式化日期为字符串"""
        return d.strftime('%Y-%m-%d')

    @staticmethod
    def parse_date(date_str: str) -> date:
        """将字符串解析为日期对象"""
        return datetime.strptime(date_str, '%Y-%m-%d').date()

class DataFrameUtils:
    @staticmethod
    def calculate_retention_rate(df: pd.DataFrame, user_col: str, date_col: str) -> pd.DataFrame:
        """计算用户留存率"""
        total_users = len(df[user_col].unique())
        retention_data = df.groupby(date_col)[user_col].nunique() / total_users * 100
        return retention_data.reset_index()

    @staticmethod
    def calculate_conversion_rate(total: int, converted: int) -> float:
        """计算转化率"""
        return (converted / total * 100) if total > 0 else 0.0

    @staticmethod
    def format_percentage(value: float) -> str:
        """格式化百分比"""
        return f"{value:.2f}%"

    @staticmethod
    def format_currency(value: float) -> str:
        """格式化货币金额"""
        return f"¥{value:.2f}"

class ChartUtils:
    @staticmethod
    def prepare_funnel_data(stages: List[Dict[str, Any]]) -> Dict[str, List]:
        """准备漏斗图数据"""
        return {
            'stages': [stage['name'] for stage in stages],
            'values': [stage['value'] for stage in stages]
        }

    @staticmethod
    def prepare_time_series_data(df: pd.DataFrame, date_col: str, value_col: str) -> Dict[str, List]:
        """准备时间序列数据"""
        return {
            'dates': df[date_col].tolist(),
            'values': df[value_col].tolist()
        }


def calculate_duration(df) -> DataFrame:
    """计算用户停留时间

    将用户数据按用户ID分组并按时间排序，计算相邻记录之间的时间差作为停留时间

    Args:
        df (pd.DataFrame): 包含用户行为数据的DataFrame
    """
    print(df['时间'])


    # 按用户ID和时间排序
    df = df.sort_values(['用户ID', '时间'])

    # 计算时间差（与下一条记录的时间差）
    df['停留时间'] = df.groupby('用户ID')['时间'].diff().shift(-1)

    # 将时间差转换为秒数
    df['停留时间'] = df['停留时间'].dt.total_seconds()

    # 处理每个用户的最后一条记录
    df.loc[df.groupby('用户ID')['时间'].idxmax(), '停留时间'] = 0

    # 处理异常值（如果时间差大于1小时，认为是会话结束）
    df.loc[df['停留时间'] > 3600, '停留时间'] = 0

    return df