#!/bin/evn python
#coding: UTF-8
from proto_render import ProtoRender
# 请保持一个proto文件内有一个message与文件名相同
# 这样才会导出，如果有其它需求，请更改下面的代码
from protos.FateConfig_pb2 import FateConfig as Desc
class FateConfigRender(ProtoRender):
	def __init__(self):
		ProtoRender.__init__(self)

	def render(self, data):
		# 如有特殊处理请复写
		ProtoRender.render(self, data)

