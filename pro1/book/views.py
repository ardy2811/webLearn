from django.shortcuts import render

# Create your views here.
from django.views import View


class BookInfoView(View):

    def get(self, request):
        """ 客户端发送get请求时调用的函数 """

        pass

    def post(self, request):
        """ 客户端发送get请求时调用的函数 """
        pass
