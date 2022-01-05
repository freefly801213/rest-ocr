# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-03 00:02

from .ProcessBaseService import ProcessBaseService


class GeneralService(ProcessBaseService):
    """
    通用OCR处理业务类
    """

    def __init__(self):
        super().__init__()

    def processImg(self, fileData):
        """
        处理图片的入口方法

        :param fileData str: 图片的base64数据
        """
        # 调用基类方法得到识别结果
        txts = super().processImgData(fileData)
        # 返回结果
        return txts

    def processPdf(self, pdfData):
        """
        处理PDF的入口方法

        :param pdfData str: PDF文件的base64数据
        """
        # 调用基类方法得到识别结果
        txts = super().processPdfData(pdfData)
        # 返回结果
        return txts
