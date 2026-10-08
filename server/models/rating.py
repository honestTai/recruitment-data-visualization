# 在 models 目录下新增 Rating 模型
from sqlalchemy import Column, Integer, Float, ForeignKey
from db import db

class Rating(db.Model):
    __tablename__ = 'tb_rate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, nullable=False)  # 用户 ID
    iid = Column(Integer, nullable=False)  # 职位 ID
    rate = Column(Float, nullable=False)  # 评分