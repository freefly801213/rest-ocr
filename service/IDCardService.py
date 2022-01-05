# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-03 00:02

from .ProcessBaseService import ProcessBaseService


class IDCardService(ProcessBaseService):
    """
    身份证的OCR业务处理类
    """

    def __init__(self):
        super().__init__()

    def processImg(self, fileData):
        """
        处理身份证图片的入口方法

        :param fileData str: 身份证图片的base64数据
        """
        # 调用基类方法得到识别结果
        txts = super().processImgData(fileData)
        # 返回结果
        return txts

    def processPdf(self, pdfData):
        """
        处理身份证PDF的入口方法

        :param pdfData str: 身份证的PDF文件的base64数据
        """
        # 调用基类方法得到识别结果
        txts = super().processPdfData(pdfData)
        # 返回结果
        return txts
