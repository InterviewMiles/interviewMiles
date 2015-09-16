from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^question/$', views.question_list),
    url(r'^question/(?P<pk>[0-9]+)/$', views.question_detail),
]