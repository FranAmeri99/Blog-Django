from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^',include('myblog.urls', namespace = 'index')),
    url(r'^admin/', admin.site.urls),
]
