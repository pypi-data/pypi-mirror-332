from typing import Dict, Any
from datetime import date
import pandas as pd
from common.database import Database
from common.utils import DataFrameUtils, ChartUtils

class SalesAnalysisService:
    def __init__(self):
        self.db = Database.get_connection()

    def get_sales_metrics(self, start_date: date, end_date: date) -> Dict[str, Any]:
        """获取销售转化指标"""
        # 订单基础数据查询
        query = """
        SELECT 
            COUNT(*) as total_orders,
            SUM(order_amount) as total_amount,
            COUNT(DISTINCT user_id) as total_users,
            SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) as paid_orders,
            SUM(CASE WHEN status = 'paid' THEN order_amount ELSE 0 END) as paid_amount,
            COUNT(DISTINCT CASE WHEN status = 'paid' THEN user_id END) as paid_users,
            SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) as cancelled_orders
        FROM orders
        WHERE order_date BETWEEN %s AND %s
        """
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query, (start_date, end_date))
        result = cursor.fetchone()
        cursor.close()

        # 计算复购用户数
        repurchase_query = """
        SELECT COUNT(DISTINCT user_id) as repurchase_users
        FROM (
            SELECT user_id
            FROM orders
            WHERE status = 'paid'
            AND order_date BETWEEN %s AND %s
            GROUP BY user_id
            HAVING COUNT(*) > 1
        ) t
        """
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(repurchase_query, (start_date, end_date))
        repurchase_result = cursor.fetchone()
        cursor.close()

        # 计算各项指标
        total_orders = result['total_orders']
        total_amount = float(result['total_amount'])
        total_users = result['total_users']
        paid_orders = result['paid_orders']
        paid_amount = float(result['paid_amount'])
        paid_users = result['paid_users']
        cancelled_orders = result['cancelled_orders']
        repurchase_users = repurchase_result['repurchase_users']

        # 计算复购率和客单价
        repurchase_rate = DataFrameUtils.calculate_conversion_rate(paid_users, repurchase_users)
        average_order_value = paid_amount / paid_orders if paid_orders > 0 else 0

        return {
            'order_metrics': {
                'total_orders': total_orders,
                'total_amount': DataFrameUtils.format_currency(total_amount),
                'total_users': total_users
            },
            'payment_metrics': {
                'paid_orders': paid_orders,
                'paid_amount': DataFrameUtils.format_currency(paid_amount),
                'paid_users': paid_users
            },
            'performance_metrics': {
                'cancelled_orders': cancelled_orders,
                'repurchase_rate': DataFrameUtils.format_percentage(repurchase_rate),
                'average_order_value': DataFrameUtils.format_currency(average_order_value)
            }
        }

    def get_daily_sales_trend(self, start_date: date, end_date: date) -> Dict[str, List]:
        """获取每日销售趋势"""
        query = """
        SELECT 
            DATE(order_date) as sale_date,
            COUNT(*) as order_count,
            SUM(order_amount) as total_amount
        FROM orders
        WHERE order_date BETWEEN %s AND %s
        AND status = 'paid'
        GROUP BY DATE(order_date)
        ORDER BY sale_date
        """
        df = pd.read_sql(query, self.db, params=(start_date, end_date))
        return {
            'dates': df['sale_date'].tolist(),
            'orders': df['order_count'].tolist(),
            'amounts': df['total_amount'].tolist()
        }