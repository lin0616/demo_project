from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'query', views.QueryMd5View.as_view()),  # 查询
    url(r'init', views.IncreaseMd5View.as_view()),  # 增加
]
