# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-03 00:02

import os
from paddleocr import PaddleOCR
from common.FileUtil import FileUtil


class ProcessBaseService():
    """
    文件处理的基础类，给定了一些基础的处理
    """

    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        self.fileUtil = FileUtil()

    def processImgData(self, fileData):
        """
        处理身份证图片的公用方法

        :param fileData str: 身份证图片的base64数据
        """
        # 处理base64临时图片文件
        image_path = self.fileUtil.createImgFile(fileData)
        # 根据得到的图片数据进行识别
        result = self.ocr.ocr(image_path)
        # 得到识别的文字结果
        txts = []
        if result:
            txts = [line[1][0] for line in result]
        # 处理结束删除文件
        os.remove(image_path)
        # 返回识别结果
        return txts

    def processPdfData(self, pdfData):
        """
        处理身份证PDF的公用方法

        :param pdfData str: 身份证的PDF文件的base64数据
        """
        # 处理base64临时图片文件
        image_path = self.fileUtil.createPdfImgFile(pdfData)
        # 根据得到的图片数据进行识别
        result = self.ocr.ocr(image_path)
        # 得到识别的文字结果
        txts = []
        if result:
            txts = [line[1][0] for line in result]
        # 处理结束删除文件
        os.remove(image_path)
        # 返回识别结果
        return txts
