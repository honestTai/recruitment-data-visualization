# -*- codeing = utf-8 -*-

# @File: fileApi.py
# @Desc:
import os

from flask import Flask, send_from_directory

APP_ID = '24936196'
API_KEY = 'CHANGE_ME_BEFORE_RUNNING'
SECRET_KEY = 'CHANGE_ME_BEFORE_RUNNING'

# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

idCardSide = "back"

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def idocr(filename):
    image = get_file_content('upload/' + filename)
    # result = client.idcard(image, idCardSide)
    # print("姓名:", result['words_result']['姓名']['words'])
    # print("性别:", result['words_result']['性别']['words'])
    # print("民族:", result['words_result']['民族']['words'])
    # print("出生:", result['words_result']['出生']['words'])
    # print("公民身份号码:", result['words_result']['公民身份号码']['words'])
    # print("住址:", result['words_result']['住址']['words'])
    # return  result['words_result']['公民身份号码']['words'], result['words_result']['姓名']['words']
    return "xx"

