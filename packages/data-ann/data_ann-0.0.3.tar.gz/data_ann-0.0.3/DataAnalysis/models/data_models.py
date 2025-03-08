from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserEvent(Base):
    __tablename__ = 'user_events'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    module = Column(String(50))
    event_type = Column(String(50))
    request_url = Column(String(255))
    request_body = Column(Text)
    response_body = Column(Text)
    event_date = Column(DateTime)
    duration = Column(Integer)

class RowData(BaseModel):
    id: int
    user_id: Optional[str]
    module: str
    event_type: str
    request_url: str
    request_body: str
    response_body: str
    event_date: str
    duration: int

    def extract_user_id(self) -> Optional[str]:
        """提取用户ID"""
        return self.user_id

    def extract_search_data(self) -> Optional[str]:
        """提取检索数据"""
        if self.request_url and 'GET' in self.request_url:
            return self.request_url
        elif self.request_body:
            return self.request_body
        return None

    def extract_success_status(self) -> bool:
        """提取成功状态"""
        try:
            response = eval(self.response_body)
            return response.get('code') == 200
        except:
            return False

class LodData(BaseModel):
    data: List[RowData]

    def get_user_data(self) -> 'LodData':
        """获取所有用户数据"""
        filtered_data = [row for row in self.data if row.user_id]
        return LodData(data=filtered_data)

    def get_search_data(self) -> 'LodData':
        """获取所有检索数据"""
        filtered_data = [row for row in self.data if row.module == '资源数据']
        return LodData(data=filtered_data)

    def get_sales_data(self) -> 'LodData':
        """获取销售数据"""
        filtered_data = [row for row in self.data if row.module == '订单管理']
        return LodData(data=filtered_data)