# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-03 00:02


from .ProcessBaseService import ProcessBaseService


class BusinessLicenseService(ProcessBaseService):
    """
    银业执照的的OCR业务处理类
    """

    def __init__(self):
        super().__init__()

    def processImg(self, fileData):
        """
        处理营业执照图片的入口方法

        :param fileData str: 营业执照图片的base64数据
        """
        # 调用基类方法得到识别结果
        txts = super().processImgData(fileData)
        # 返回结果
        return txts

    def processPdf(self, pdfData):
        """
        处理营业执照PDF的入口方法

        :param pdfData str: 营业执照的PDF文件的base64数据
        """
        # 调用基类方法得到识别结果
        txts = super().processPdfData(pdfData)
        # 返回结果
        return txts
