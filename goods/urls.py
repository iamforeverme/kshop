from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from goods import views

urlpatterns = [
    url(r'^producer/$', views.ProducerList.as_view()),
    url(r'^producer/(?P<pk>[0-9]+)/$', views.ProducerDetail.as_view()),
    url(r'^brand/$', views.BrandList.as_view()),
    url(r'^brand/(?P<pk>[0-9]+)/$', views.BrandDetail.as_view()),
    url(r'^product/$', views.ProductList.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)