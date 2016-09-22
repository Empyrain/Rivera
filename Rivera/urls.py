from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls import handler404, handler500

handler404 = 'messenger.views.page_not_found'
handler500 = 'messenger.views.page_not_found'

urlpatterns = [
    url(r'^messenger/', include('messenger.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('login.urls'))
]
