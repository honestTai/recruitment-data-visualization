from datetime import time

import requests
import pymysql
import re

from config import HOST, USERNAME, PASSWORD, DATABASE

# 请求参数
headers = {
    "User-Agent": "Mozilla/5.0"
}

# 城市编码映射表
city_ids = [
    "530", "538", "765", "763", "635",
    "639", "636", "638", "646", "653",
    "654", "664", "531", "736", "854",
    "801", "600", "613", "719"
]

# 数据库连接配置
db =  pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD, port=3306, database=DATABASE,
                      charset='utf8')
cursor = db.cursor()

def parse_salary(salary_str):
    match = re.findall(r'(\d+)', salary_str)
    if len(match) == 2:
        return float(match[0]), float(match[1])
    return None, None

def parse_size(size_str):
    match = re.findall(r'(\d+)', size_str)
    if len(match) == 2:
        return float(match[0]), float(match[1])
    return None, None

def parse_workexp(exp_str):
    match = re.findall(r'(\d+)', exp_str)
    if len(match) == 2:
        return float(match[0]), float(match[1])
    return None, None

def insert_job(item):
    sql = """
        INSERT IGNORE INTO tb_job2 (
            number, company_name, position_name, city, salary0, salary1,
            degree, company_logo, url, company_url, education, coattr,
            cosize0, cosize1, worktime0, worktime1, welfare, publish_time, province
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    salary0, salary1 = parse_salary(item.get("salary", ""))
    cosize0, cosize1 = parse_size(item.get("companySize", ""))
    worktime0, worktime1 = parse_workexp(item.get("workingExp", ""))
    welfare = ",".join(item.get("welfareLabel", [])) if item.get("welfareLabel") else None

    cursor.execute(sql, (
        item["number"],
        item["company"],
        item["name"],
        item["workCity"],
        salary0,
        salary1,
        item["education"],
        item["companyLogo"],
        item["positionUrl"],
        item["companyUrl"],
        item["education"],
        item["property"],
        cosize0,
        cosize1,
        worktime0,
        worktime1,
        welfare,
        item["publishTime"],
        item["workCity"].split("-")[0] if "-" in item["workCity"] else item["workCity"]
    ))
    db.commit()

def crawl_city(city_id, max_page=10):
    for page_no in range(1, max_page + 1):
        url = f"https://fe-api.zhaopin.com/c/i/jobs/searched-jobs?pageNo={page_no}&pageSize=90&cityId={city_id}"
        print(f"正在抓取城市ID {city_id} 第 {page_no} 页...")
        try:
            response = requests.get(url, headers=headers, timeout=10)
            data = response.json()
            job_list = data.get('data').get('list')
            for job in job_list:
                insert_job(job)
                print(f"插入：{job.get('name')} @ {job.get('company')}")
        except Exception as e:
            print(f"抓取失败: {e}")
        time.sleep(1)

def main():
    for city_id in city_ids:
        crawl_city(city_id)
    print("所有城市职位抓取完成！")
    cursor.close()
    db.close()
if __name__ == "__main__":
    main()