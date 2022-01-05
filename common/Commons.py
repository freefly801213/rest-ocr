# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-03 00:02

import os


p_name = 'rest-ocr'
project_path = os.path.abspath(os.path.dirname(__file__))
separator = '/'
# Windows
if project_path.find('\\') != -1: separator = '\\'
# Mac、Linux、Unix
if project_path.find('/') != -1: separator = '/'

root_path = project_path[:project_path.find(f'{p_name}{separator}') + len(f'{p_name}{separator}')]

PROJECT_PATH = f"{root_path}temp/"

# 图片文件类型
IMAGE_TYPES = ['png', 'jpeg', 'jpg', 'gif', 'bmp']
# 非文件类型
FILE_TYPES = ['pdf']

def verify_filedata(fileData, fileType):
    """
    用于校验传入的文件base64数据是否正确

    :param fileData str: 文件base64数据
    :param fileType str: 文件类型
    """
    tmpDataPrefix = fileData.split(',')[0]
    verifed = False
    if fileType == 'img':
        for imgType in IMAGE_TYPES:
            if imgType in tmpDataPrefix:
                verifed = True
                break
    elif fileType == 'pdf':
        for fileType in FILE_TYPES:
            if fileType in tmpDataPrefix:
                verifed = True
                break
    # 返回验证结果
    return verifed
