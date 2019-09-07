from django.conf.urls import url
from . import views
app_name = 'campusresale'

urlpatterns=[
    url('', views.index, name='index'),
    url('^about/', views.about, name='about'),
    url('^services/', views.services, name='services'),
    url('^login/', views.login, name='login'),
    url('^product_list/', views.product_list, name='product_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list'),
    url('^product_detail/', views.product_detail, name='product_detail'),

]
