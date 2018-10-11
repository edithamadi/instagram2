from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^new/image/$', views.new_img, name = 'new_img'),
    url(r'^search/', views.search_profile, name='search_profile'),
    url(r'^(?P<user_username>\w+)/$' , views.profile , name= 'profile'),
    url(r'^(?P<user_username>\w+)/edit$' , views.profile , name= 'edit_profile'),
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)