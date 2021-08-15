from django.conf.urls import url
from mywebApp2 import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  url(r'^api/customer$', views.sddetails_list),
  url(r'^api/customer/(?P<pk>[0-9]+)$', csrf_exempt(views.sddetails_detail)),
  url(r'^api/customer/(?P<pk>[0-9]+)$', csrf_exempt(views.sddetails_delete)),
  url(r'^api/product$', views.sddetails_list1),
  url(r'^api/product/(?P<pk>[0-9]+)$', csrf_exempt(views.sddetails_detail1)),
  url(r'^api/product/(?P<pk>[0-9]+)$', csrf_exempt(views.sddetails_delete1)),
  ]