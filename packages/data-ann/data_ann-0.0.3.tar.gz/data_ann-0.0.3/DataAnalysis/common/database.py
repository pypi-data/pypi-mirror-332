from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import Engine
from dotenv import load_dotenv
import os

class Database:


    def __init__(self):
        # 加载环境变量
        load_dotenv()
        self._engine: Optional[Engine] = None
        self._SessionLocal: Optional[sessionmaker] = None
        # 从环境变量中读取配置参数
        self.connection_params = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', 3306)),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', ''),
            'database': os.getenv('DB_DATABASE', 'chongmu')
        }

    def get_engine(self) -> Engine:
        """获取数据库引擎单例"""
        if self._engine is None:
            load_dotenv()

        connection_str = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?connect_timeout=10".format(
            **self.connection_params)
        self._engine = create_engine(connection_str)
        self._engine = create_engine(connection_str)
        return self._engine

    def get_session(self) -> Session:
        """获取数据库会话"""
        if self._SessionLocal is None:
            self._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.get_engine())
        return self._SessionLocal()

    def close(self) -> None:
        """关闭数据库连接"""
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None
            self._SessionLocal = None