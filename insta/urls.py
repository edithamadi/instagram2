from django.conf.urls import url
from . import views

from django.conf import settings
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # url(r'^search/', views.search_image, name='search_image')
]