import json
from datetime import date
from typing import List, Dict

import jwt
from pydantic import BaseModel, Field, field_validator


class BaseData(BaseModel):
    module: str  # 所属模块
    description: str | None  # 日志描述
    create_time: date  # 事件
    city: str | None = None  # 城市
    province: str | None = None  # 省份
    country: str | None = None  # 国家
    # address: str             # 用户地址
    operators: str  # 用户运营商
    os: str  # 事件


class SalesData(BaseData):
    pass


class SearchData(BaseData):
    pass


class UserData(BaseData):
    # 用户数据
    user_id: str  # 用户ID


class LogDate(BaseModel):
    data: List[Dict] = None
    user_data: List[UserData] = []
    sales_data: List[SalesData] = []
    search_data: List[SearchData] = []

    def _extract_login_id(self, headers_json: str) -> str:
        """从请求头中提取并解析JWT token获取login_id
        Args:
            headers_json: JSON格式的请求头数据

        Returns:
            解析出的login_id，如果解析失败则返回空字符串
        """
        # 从JSON中提取headers
        headers = json.loads(headers_json)
        # 从headers中获取user_id，如果没有则从token中获取loginId
        user_id = headers.get('user_id') or headers.get('userId')
        if not user_id:
            token = headers.get('token', '')
            if not token:
                # 从Authorization头部获取token
                auth_header = headers.get('Authorization', '')
                token = auth_header.split(" ", 1)[1] if " " in auth_header else ''
            # 解析JWT token，不验证签名
            if not token:
                return ''
            payload = jwt.decode(token, options={"verify_signature": False})
            user_id = payload.get('loginId', '')

        return str(user_id)

    @field_validator('data', mode='before')
    def parse_interval(cls, value):
        data_list = []
        if value:
            for row in value:
                row = dict(row)
                row["create_time"] = row["create_time"].date()
                row["operators"], row["country"], row["province"], row["city"] = cls._parse_operators(row['address'])
                data_list.append(row)
        return data_list

    @classmethod
    def _parse_operators(cls, address: str):
        """
        解析用户地址信息
        :param address: 中国北京北京市 鹏博士
        :param address: 中国四川省阿坝 移动
        :return:
            city: str | None = None  # 城市
            province: str | None = None  # 省份
            country: str | None = None  # 国家
        """
        operators, country, province, city = '', '', '', ''
        # 中国贵州省贵阳市 移动
        if not address:
            return operators, country, province, city
        operators = address.split(' ')[-1]
        country = address[:2]
        province = address[2:].split('省')[0]
        if province.endswith('省'):
            province = province + '省'
            city = address[2:].split('省')[1].split('市')[1]
        else:
            province = None
        # if not city:
        #     city = address[2:].split('省')[1].split('市')[0]
        return operators, country, province, city

    def get_user_all(self) -> List[UserData]:
        """获取所有用户相关数据
        Returns:
            List[UserData]: 用户数据列表
        """
        if not self.data:
            return []
        if self.user_data:
            return self.user_data
        for item in self.data:
            user_id = self._extract_login_id(item['request_headers'])

            if user_id:
                item['user_id'] = user_id
                self.user_data.append(UserData(**item))
        return self.user_data

    def get_sales_all(self) -> List[SalesData]:
        """获取所有销售数据

        Returns:
            List[SalesData]: 销售数据列表
        """
        if not self.data:
            return []
        if self.sales_data:
            return self.sales_data

        for item in self.data:
            if 'order_id' in item:
                self.sales_data.append(SalesData(
                    order_id=item['order_id'],
                    user_id=item['user_id'],
                    create_time=item['create_time'],
                    amount=item['amount'],
                    status=item['status'],
                    product_info=item.get('product_info')
                ))
        return self.sales_data

    def get_search_all(self) -> List[SearchData]:
        """获取所有搜索数据

        Returns:
            List[SearchData]: 搜索数据列表
        """
        if not self.data:
            return []
        if self.search_data:
            return self.search_data
        for item in self.data:
            if 'search_id' in item:
                self.search_data.append(SearchData(
                    search_id=item['search_id'],
                    user_id=item.get('user_id'),
                    create_time=item['create_time'],
                    keyword=item['keyword'],
                    search_type=item['search_type'],
                    result_count=item['result_count']
                ))
        return self.search_data
