# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-03 00:02

import base64
import time
import paddleocr
from . import Commons
import os
import fitz


class FileUtil():
    """
    文件处理相关工具类
    """

    def __init__(self):
        pass

    def createImgFile(self, imgData):
        """
        用于创建OCR目标图片文件

        :param imgData Object: 从base64解码得到的图片对象
        """
        # 判断文件夹是否存在
        tmp_path = Commons.PROJECT_PATH.rstrip('/')
        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)
        # 临时文件路径和文件名
        image_file = f"{Commons.PROJECT_PATH}{time.time()}.{self._getFileSuffix(imgData)}"
        # 将base64数据转为图片
        image_data = base64.b64decode(imgData.split(',')[1])
        # 进行文件写入
        with open(image_file, 'wb') as imgFile:
            imgFile.write(image_data)
        return image_file

    def createPdfImgFile(self, pdfData):
        """
        用于创建PDF文件对应的图片文件并返回图片文件的路径

        :param pdfData str: base64的pdf文件
        """
        # 处理并生成临时PDF文件
        pdf_path = self._createPdfFile(pdfData)
        # 临时文件路径和文件名
        image_file = f"{Commons.PROJECT_PATH}{time.time()}.png"
        # pdf文件转图片
        pdf_doc = fitz.open(pdf_path)
        for pg in range(pdf_doc.pageCount):
            page = pdf_doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
            # 此处若是不做设置，默认图片大小为：792X612, dpi=96
            zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
            zoom_y = 1.33333333
            mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pix = page.getPixmap(matrix=mat, alpha=False)
            pix.writePNG(image_file)
        # 删除PDF临时文件
        os.remove(pdf_path)

        return image_file

    def _getFileSuffix(self, imgData):
        """
        根据base64的图片内容获取图片文件的后缀

        :param imgData str: 图片文件的base64数据
        """
        return imgData.split(',')[0].split(';')[0].split('/')[1]

    def _createPdfFile(self, fileData):
        """
        统一创建PDF文件

        :param fileData str: base的pdf文件原始数据
        """
        # 判断文件夹是否存在
        tmp_path = Commons.PROJECT_PATH.rstrip('/')
        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)
        # 临时文件路径和文件名
        pdf_file = f"{Commons.PROJECT_PATH}{time.time()}.{self._getFileSuffix(fileData)}"
        # 将base64数据转为图片
        pdf_data = base64.b64decode(fileData.split(',')[1])
        # 进行文件写入
        with open(pdf_file, 'wb') as imgFile:
            imgFile.write(pdf_data)
        return pdf_file
