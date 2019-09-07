from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    url('^$', views.index, name='index'),
    url('^about/', views.about, name='about'),
    url('^services/', views.services, name='services'),
    url('^login/', views.login, name='login'),
    url('^product_list/', views.product_list, name='product_list'),
    url('^(?P<category_slug>[-\w]+)/', views.product_list, name='product_list'),
    url('^(?P<id>\d+)(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
    # path('campusresale/',include( 'campusresale.urls')),
]
