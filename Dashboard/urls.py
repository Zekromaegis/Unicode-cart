from django.conf.urls import url
from . import views

app_name = 'Dashboard'


urlpatterns = [
    # /
    url(r'^$', views.a, name='a'),

    # /product/add/
    url(r'product/add/$',views.ProductCreate.as_view(), name='ProductCreate'),

    # /product/update/<pk>/
    url(r'product/update/(?P<pk>[0-9]+)/$',views.ProductUpdate.as_view(), name='ProductUpdate'),

    # /register/customer/
    url(r'^register/customer/$', views.customer_register.as_view(), name='customer_register'),

    # /register/company/
    url(r'^register/company/$', views.company_register.as_view(), name='company_register'),

    # /login/
    url(r'^login/$', views.user_login.as_view(), name='login'),

    # /logout/
    url(r'^logout/$', views.user_logout, name='logout'),
]
