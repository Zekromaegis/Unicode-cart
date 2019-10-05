from django.conf.urls import url
from . import views

app_name = 'Dashboard'


urlpatterns = [
    # /
    url(r'^$', views.a, name='a'),

    # /music/album/add/
    url(r'product/add/$',views.ProductCreate.as_view(), name='ProductCreate'),

    # /register/customer/
    url(r'^register/customer/$', views.customer_register.as_view(), name='customer_register'),

    # /register/company/
    url(r'^register/company/$', views.company_register.as_view(), name='company_register'),
]
