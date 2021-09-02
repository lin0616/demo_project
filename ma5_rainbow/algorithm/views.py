from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Md5Rainbow
from django.http import HttpResponse
import json
import re
import time
import hashlib


class QueryMd5View(View):
    def get(self, request):

        # 获取传过来的密文
        ciphertext = request.GET.get('md5', '')

        # 如果没有获取到,就返回没有密文
        if not ciphertext:
            return HttpResponse('no md5')

        # 从数据库里面查找密文
        rainbow = Md5Rainbow.objects.filter(ciphertext=str(ciphertext)).first()

        # 如果没有找到,就返回没有密文
        if not rainbow:
            return HttpResponse('not exists')

        # 如果数据库找到密文,就返回密文对应的明文
        if rainbow:
            return HttpResponse(rainbow.plaintext)


class IncreaseMd5View(View):
    def post(self, request):

        # 获取当前时间
        str_time = time.time()
        print(request.body)
        data = json.loads(request.body.decode())
        print(data)

        # 明文
        plaintext = str(data.get('plaintext', ''))
        if not plaintext or not re.match(r'\d{1,5}', plaintext):
            return HttpResponse(request, {'code': 9999, 'msg': '明文传参错误'})

        # 加密密文
        m1 = hashlib.md5()
        m1.update(str(plaintext).encode(encoding='utf-8'))
        ciphertext = m1.hexdigest()

        rainbow = Md5Rainbow.objects.filter(plaintext=plaintext).values('ciphertext').first()
        if rainbow:
            if rainbow['ciphertext'] != ciphertext:
                Md5Rainbow.objects.filter(plaintext=plaintext).update(ciphertext=ciphertext)
            end_time = time.time()
            spend_time = end_time - str_time
            return HttpResponse('数据库里已经构建成功，使用了%s秒' % spend_time)

        Md5Rainbow.objects.create(plaintext=plaintext, ciphertext=ciphertext)
        end_time = time.time()
        spend_time = end_time - str_time
        return HttpResponse('构建成功，使用了%s秒' % spend_time)
