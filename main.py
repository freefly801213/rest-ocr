# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-02 22:14

from flask import Flask
from flask_restful import Api

from api.ProcessIDCardAPI import ProcessIDCardAPI
from api.ProcessBusinessLicenseAPI import ProcessBusinessLicenseAPI
from api.InvoiceAPI import InvoiceAPI
from api.GeneralAPI import GeneralApi


app = Flask(__name__)
api = Api(app)

# 构建路由
api.add_resource(GeneralApi, '/general') # 通用OCR接口
api.add_resource(ProcessIDCardAPI, '/idcard') # 身份证OCR接口
api.add_resource(ProcessBusinessLicenseAPI, '/businesslicense') # 营业执照OCR接口
api.add_resource(InvoiceAPI, '/invoice') # 发票OCR接口

# 执行app
if __name__ == "__main__":
    app.run(debug=True)
