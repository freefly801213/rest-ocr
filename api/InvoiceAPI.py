# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-03 00:02

from flask_restful import Resource, reqparse, marshal_with
from service.InvoiceService import InvoiceService
from common import Commons, HttpCommons


class InvoiceAPI(Resource):
    """
    用于处理发票的图片的OCR处理类
    """

    def __init__(self):
        """
        类初始化方法
        定义了接口处理类中的参数校验规则
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('file', type=str, required=True, location='json', trim=True)
        self.reqparse.add_argument('filetype', type=str, choices=['img', 'pdf'], required=True, location='json', trim=True)
        self.invoiceService = InvoiceService()
        super(InvoiceAPI, self).__init__()

    @marshal_with(HttpCommons.HTTP_RESPONSE_STR_LIST_FIELDS)
    def post(self):
        """
        POST请求处理方法
        该类只接收并处理POST方式的请求
        """
        # 首先验证并得到所有的请求参数
        args = self.reqparse.parse_args()
        if not Commons.verify_filedata(args['file'], args['filetype']):
            return "base64文件数据错误"
        results = ""
        # 调用业务方法得到识别结果
        if args['filetype'] == 'img':
            results = self.invoiceService.processImg(args['file'])
        if args['filetype'] == 'pdf':
            results = self.invoiceService.processPdf(args['file'])
        # 返回结果
        return HttpCommons.success(data=results)
