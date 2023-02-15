import logging
from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def testlog(request):
    # 进行日志配置的测试
    logger = logging.getLogger('django')
    logger.info('loading url')
    logger.error('error')
    logger.debug('debug')
    return HttpResponse("Hello world ! ")
