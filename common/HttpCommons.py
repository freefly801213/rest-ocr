# -*- coding: utf-8 -*-
# @Author: freefly801213
# @Date: 2022-01-03 00:02

from flask_restful import fields

# 定义返回结构中的CODE值
RESPONSE_SUCCESS_CODE = 200
RESPONSE_ERROR_CODE = 500

# 定义全局的返回参数结构和字段 - 返回数据为字符串List
HTTP_RESPONSE_STR_LIST_FIELDS = {
    # 返回的状态值
    'code': fields.Integer,
    # 接口执行是否成功 True - 成功  False - 失败
    'success': fields.Boolean,
    # 返回的调用结果提示消息内容
    'message': fields.String,
    # 接口返回的实际数据
    # TODO 这里目前是直接返回了识别结果的字符串列表
    'data': fields.List(fields.String, default=[])
}

# 定义全局的返回参数结构和字段 - 返回数据为Dict List
# HTTP_RESPONSE_DIC_LIST_FIELDS = {
#     # 返回的状态值
#     'code': fields.Integer,
#     # 接口执行是否成功 True - 成功  False - 失败
#     'success': fields.Boolean,
#     # 返回的调用结果提示消息内容
#     'message': fields.String,
#     # 接口返回的实际数据
#     # TODO 这里目前是直接返回了识别结果的字典列表
#     'data': fields.List(fields..Nested, default=[])
# }

# 接口成功返回数据构建方法
def success(code=RESPONSE_SUCCESS_CODE, success=True, message='success', data=[]):
    """
    成功返回
    """
    response_data = {
        'code': code,
        'success': success,
        'message': message,
        'data': data
    }
    return response_data

# 接口失败返回数据构建方法
def error(code=RESPONSE_ERROR_CODE, success=False, message='error', data=[]):
    """
    失败返回
    """
    response_data = {
        'code': code,
        'success': success,
        'message': message,
        'data': data
    }
    return response_data
