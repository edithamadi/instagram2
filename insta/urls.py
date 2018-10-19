from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/image/$', views.new_img, name = 'new_img'),
    url(r'^search/', views.search_profile, name='search_profile'),
    url(r'^profile/$' , views.profile , name= 'profile'),
    url(r'^edit/$' , views.profile , name= 'edit_profile'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),  
    url(r'^comment/(?P<post_id>\d+)', views.add_comment, name='comment'),
  
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)