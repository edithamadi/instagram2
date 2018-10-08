from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/image$', views.new_img, name = 'new_img'),
    # url(r'^search/', views.search_image, name='search_image')
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)