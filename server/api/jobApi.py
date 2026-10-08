# -*- codeing = utf-8 -*-

# @File :jobApi.py
import operator

from flask import Blueprint, request
from sqlalchemy import func, distinct
from sqlalchemy.sql import label

from algorithm import ItemCF, UserCF
from app import app
from base.code import ResponseCode, ResponseMessage

from base.response import ResMsg
from db import db
from models.model import chart_data
from models.job import getWords, Job, job_schema
from models.rating import Rating
from utils.mytool import formatDegree

jobBp = Blueprint("job", __name__)

# 词云使用--分词接口
@jobBp.route('/getWordCut', methods=["GET"])
def getWordCut():
    res = ResMsg()
    result = getWords()
    res.update(code=ResponseCode.SUCCESS, data=result)
    return res.data

# Library搜索
@jobBp.route('/get', methods=["GET"])
def get():
    res = ResMsg()
    keyword = request.args.get('keyword', '')
    page = request.args.get('page', 1, type=int)  # 获取当前页码，默认为1
    per_page = request.args.get('per_page', 10, type=int)  # 每页显示数量，默认为10

    # 分页查询
    pagination = db.session.query(Job).filter(Job.position_name.like('%' + keyword + '%')) \
        .order_by(Job.publish_time.desc()) \
        .paginate(page=page, per_page=per_page, error_out=False)

    # 获取当前页的数据
    items = pagination.items
    data = job_schema.dump(items)

    # 返回分页信息
    res.update(code=ResponseCode.SUCCESS, data={
        'items': data,
        'total': pagination.total,  # 总记录数
        'pages': pagination.pages,  # 总页数
        'current_page': pagination.page,  # 当前页码
        'per_page': pagination.per_page  # 每页记录数
    })
    return res.data

# 热门 / 最新
@jobBp.route('/getHot', methods=["GET"])
def getHot():
    res = ResMsg()
    # result = db.session.query(Job).order_by(Job.publish_time.desc()).all()[:4]
    result = db.session.query(Job).order_by(Job.publish_time.desc()).limit(4).all()
    data = job_schema.dump(result)
    res.update(code=ResponseCode.SUCCESS, data=data)
    return res.data

# 推荐 --停用
@jobBp.route('/getRec', methods=["GET"])
def getRec():
    res = ResMsg()
    # result = db.session.query(Job).filter(Job.type.like('%科幻%')).order_by(Job.rate.desc()).all()[:4]
    # data = job_schema.dump(result)
    # res.update(code=ResponseCode.SUCCESS, data=data)
    return res.data


@jobBp.route('/getChart1', methods=["GET"])
def getChart1():
    res = ResMsg()
    all = []
    dz = []
    kh = []
    aq = []
    xj = []
    ranges = [('1900', '1950'), ('1950', '1960'), ('1960', '1970'), ('1970', '1980'), ('1980', '1990'),
              ('1990', '2000'), ('2000', '2010'), ('2010', '2020'), ('2020', '2030')]
    for r in ranges:
        cnt = db.session.query(Job).filter(Job.myear >= r[0], Job.myear < r[1]).count()
        dzcnt = db.session.query(Job).filter(Job.type.like('%动作%'), Job.myear >= r[0], Job.myear < r[1]).count()
        khcnt = db.session.query(Job).filter(Job.type.like('%科幻%'), Job.myear >= r[0], Job.myear < r[1]).count()
        aqcnt = db.session.query(Job).filter(Job.type.like('%爱情%'), Job.myear >= r[0], Job.myear < r[1]).count()
        xjcnt = db.session.query(Job).filter(Job.type.like('%喜剧%'), Job.myear >= r[0], Job.myear < r[1]).count()

        chart = dict(name=r[0] + '-' + r[1], value=cnt)
        all.append(chart)
        chart2 = dict(name=r[0] + '-' + r[1], value=dzcnt)
        dz.append(chart2)
        chart3 = dict(name=r[0] + '-' + r[1], value=khcnt)
        kh.append(chart3)
        chart4 = dict(name=r[0] + '-' + r[1], value=aqcnt)
        aq.append(chart4)
        chart5 = dict(name=r[0] + '-' + r[1], value=xjcnt)
        xj.append(chart5)
    # data = chart_data.dump(result)
    res.update(code=ResponseCode.SUCCESS, data=dict(all=all, kh=kh, dz=dz, aq=aq, xj=xj))
    return res.data


@jobBp.route('/getAreaChart', methods=["GET"])
def getAreaChart():
    res = ResMsg()
    kh = []
    ranges = [('1900', '1970'), ('1970', '1990'), ('1990', '2000'), ('2000', '2010'), ('2010', '2020')]
    for r in ranges:
        khcnt = db.session.query(Job).filter(Job.myear >= r[0], Job.myear < r[1]).count()
        chart3 = dict(name=r[0] + '-' + r[1], value=khcnt)
        kh.append(chart3)
    # data = chart_data.dump(result)
    res.update(code=ResponseCode.SUCCESS, data=dict(kh=kh))
    return res.data

@jobBp.route('/getChart2', methods=["GET"])
def getChart2():
    res = ResMsg()
    datas = []
    for i in range(2001, 2021):
        cnt = db.session.query(Job).filter(Job.myear == i).count()
        chart = dict(name=i, value=cnt)
        datas.append(chart)
    res.update(code=ResponseCode.SUCCESS, data=datas)
    return res.data

@jobBp.route('/getChart3', methods=["GET"])
def getChart3():
    res = ResMsg()
    result = db.session.query(Job.myear.label('name'), func.count('*').label('value')).group_by(Job.myear).order_by(
        Job.myear.asc()).all()
    datas = chart_data.dump(result)
    res.update(code=ResponseCode.SUCCESS, data=datas)
    return res.data

@jobBp.route('/getNationRank', methods=["GET"])
def getNationRank():
    res = ResMsg()
    nations = ['摩纳哥', '西班牙', '印度', '比利时', '塞浦路斯', '英国', '冒险', '韩国', '希腊', '奥地利', '意大利', '动画', '德国', '泰国', '喜剧', '澳大利亚',
               '中国台湾', '巴西', '中国香港', '墨西哥', '加拿大', '匈牙利', '中国大陆', '瑞典', '新西兰', '卡塔尔', '捷克', '瑞士', '南非', '法国', '伊朗',
               '黎巴嫩', '阿联酋', '日本', '悬疑', '约旦', '爱尔兰', '波兰', '丹麦', '美国', '阿根廷', '荷兰']
    datas = []
    for t in nations:
        cnt = db.session.query(Job).filter(Job.nation.like('%' + t + '%')).count()
        chart = dict(name=t, value=cnt)
        datas.append(chart)
    datas = sorted(datas, key=operator.itemgetter('value'), reverse=True)

    res.update(code=ResponseCode.SUCCESS, data=dict(datas=datas))
    return res.data


# @JobBp.before_request
# def init_session():
#     db.session = db.session.session_factory()

# 不同城市，不同学历的收入情况
@jobBp.route('/getTypeRate', methods=["GET"])
def getTypeRate():
    res = ResMsg()
    types = ['上海','北京','深圳','广州','苏州']

    datas = []
    for t in types:
        data = []
        jobs = db.session.query(Job).filter(Job.city.like('%' + t + '%'), Job.salary1!=0).all()
        for m in jobs:
            rateData = []
            rateData.append(formatDegree(m.degree))
            rateData.append(m.salary1)
            rateData.append(m.degree)
            rateData.append(m.salary0)
            rateData.append(m.position_name)
            rateData.append(m.company_name)
            data.append(rateData)
        datas.append(data)
    res.update(code=ResponseCode.SUCCESS, data=dict(datas=datas, labels=types))
    return res.data

@jobBp.route('/getTimeLine', methods=["GET"])
def getTimeLine():
    res = ResMsg()
    types = ['美国', '英国', '日本', '中国香港', '中国大陆', '法国', '德国', '韩国', '意大利', '加拿大','中国台湾','澳大利亚','西班牙','印度','瑞士','新西兰']
    datas = []
    for y in range(2000, 2021):
        yearData = []
        for t in types:
            cnt = db.session.query(Job).filter(Job.myear==y, Job.nation.like('%' + t + '%')).count()
            yearData.append(cnt)
        datas.append(yearData)

    res.update(code=ResponseCode.SUCCESS, data=dict(datas=datas))
    return res.data

# Flask 推荐算法接口（基于itemCF）
# 只推荐A领域的东西给目标用户，因为目标用户的主要兴趣点在A领域，
# 这样他有限的推荐列表中就会包含该领域一定数量不热门的物品，所以推荐长尾能力较强，但多样性不足
@jobBp.route('/getRecomendation', methods=["GET"])
def getRecomendation():
    userId = request.args.get('userId')
    userId = int(userId)
    res = ResMsg()
    rates = []
    dd = []
    datas = ItemCF.recommend(userId)
    for id, rate in datas:
        print(id)
        item = db.session.query(Job).filter(Job.id == id).first()
        dd.append(item)
        rates.append(rate)
    data = job_schema.dump(dd)
    res.update(code=ResponseCode.SUCCESS, data=dict(datas=data, rates=rates))
    return res.data

# Flask 推荐算法接口（基于userCF）
# 系统会找到与目标用户兴趣相似的其他用户然后将其他用户关注的东西推荐给目标用户，所以是某个群体内的热门物品；
# 同时也反应出如果某些物品没有被该群体关注，则不会推荐给该群体，即推荐长尾能力的不足
@jobBp.route('/getRecomendation2', methods=["GET"])
def getRecomendation2():
    userId = request.args.get('userId')
    userId = int(userId)
    res = ResMsg()
    datas = UserCF.recommend(userId)
    dd = []
    rates = []
    for id, rate in datas:
        # print(id)
        item = db.session.query(Job).filter(Job.id==id).first()
        dd.append(item)
        rates.append(rate)
    data = job_schema.dump(dd)
    res.update(code=ResponseCode.SUCCESS, data=dict(datas=data, rates=rates))
    return res.data

# 获取几个统计数字
@jobBp.route('/getPanel', methods=["GET"])
def getPanel():
    res = ResMsg()
    cnt1 = db.session.query(Job).count()
    cnt2 = db.session.query(func.count(distinct(Job.city))).scalar()
    cnt3 = db.session.query(func.count(distinct(Job.company_name))).scalar()
    cnt4 = db.session.query(func.count(distinct(Job.coattr))).scalar()

    res.update(code=ResponseCode.SUCCESS, data=dict(data1=cnt1, data2=cnt2, data3=cnt3, data4=cnt4))
    return res.data

# 职位按照省份来分组统计
@jobBp.route('/getCityJob', methods=["GET"])
def getCityJob():
    res = ResMsg()
    result = db.session.query(Job.province.label('name'), func.count('*').label('value')).group_by(Job.province).order_by(
        func.count('*').desc()).all()
    datas = chart_data.dump(result)
    res.update(code=ResponseCode.SUCCESS, data=datas)
    return res.data

# 职位按照城市来分组统计
@jobBp.route('/getCityJob2', methods=["GET"])
def getCityJob2():
    res = ResMsg()
    result = db.session.query(Job.city.label('name'), func.count('*').label('value')).group_by(Job.city).order_by(
        Job.city.asc()).all()
    datas = chart_data.dump(result)
    res.update(code=ResponseCode.SUCCESS, data=datas)
    return res.data

# 按照公司类型分组统计
@jobBp.route('/getTypeRank', methods=["GET"])
def getTypeRank():
    res = ResMsg()
    result = db.session.query(Job.coattr.label('name'), func.count('*').label('value')).group_by(Job.coattr).order_by(
        func.count('*').desc()).all()
    datas = chart_data.dump(result)
    res.update(code=ResponseCode.SUCCESS, data=datas)
    return res.data

# 按照需求的学历分组统计
@jobBp.route('/getDegreeRank', methods=["GET"])
def getDegreeRank():
    res = ResMsg()
    result = db.session.query(Job.degree.label('name'), func.count('*').label('value')).group_by(Job.degree).order_by(
        func.count('*').desc()).all()
    datas = chart_data.dump(result)
    res.update(code=ResponseCode.SUCCESS, data=datas)
    return res.data

@jobBp.after_request
def close_session(response):
    db.session.close()
    return response
# 在 `api/jobApi.py` 中新增评分接口
@jobBp.route('/rate', methods=["GET"])
def rate():
    res = ResMsg()
    try:
        # 获取请求数据
        user_id = request.args.get('userId')
        job_id = request.args.get('jobId')
        score = request.args.get('rating')


        # 校验参数
        if not all([user_id, job_id, score]):
            res.update(code=ResponseCode.FAIL, msg="参数缺失")
            return res.data

        # 查询是否已有评分记录
        rating = db.session.query(Rating).filter_by(uid=user_id, iid=job_id).first()

        if rating:
            # 更新评分
            rating.rate = score
            msg = "评分更新成功"
        else:
            # 新增评分记录
            rating = Rating(uid=user_id, iid=job_id, rate=score)
            db.session.add(rating)
            msg = "评分新增成功"

        db.session.commit()
        res.update(code=ResponseCode.SUCCESS, msg=msg)
    except Exception as e:
        db.session.rollback()
        res.update(code=ResponseCode.FAIL, msg=f"评分操作失败: {str(e)}")
    return res.data

@jobBp.route('/getRating', methods=["GET"])
def get_rating():
    res = ResMsg()
    try:
        # 获取请求参数
        user_id = request.args.get('userId')
        job_id = request.args.get('jobId')

        # 校验参数
        if not all([user_id, job_id]):
            res.update(code=ResponseCode.FAIL, msg="参数缺失")
            return res.data

        # 查询评分
        rating = db.session.query(Rating).filter_by(uid=user_id, iid=job_id).first()

        if rating:
            res.update(code=ResponseCode.SUCCESS, data={"score": rating.rate})
        else:
            res.update(code=ResponseCode.SUCCESS, data={"score": 0})  # 未找到评分记录，返回评分为0
    except Exception as e:
        res.update(code=ResponseCode.FAIL, msg=f"查询失败: {str(e)}")
    return res.data


from ZhilianspiderSpider import main
import threading
#数据爬取
@jobBp.route('/crawl', methods=['GET'])
def start_crawl():
    res = ResMsg()

    def async_task():
        try:
            main()  # 调用爬取主方法
        except Exception as e:
            app.logger.error(f"爬取任务失败: {e}")

    # 创建线程执行异步任务
    thread = threading.Thread(target=async_task)
    thread.start()

    res.update(code=0, msg="爬取任务已启动，正在后台执行")
    return res.data
