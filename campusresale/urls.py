from django.urls import path,re_path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('login/', views.login, name='login'),
    path('products/<slug:category_slug>/', views.product_list, name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('<int:id>/<slug>/', views.product_detail, name='product_detail'),

    # If you want to use regular expression use something like this
    #    re_path('^(?P<id>\d+)(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
]
