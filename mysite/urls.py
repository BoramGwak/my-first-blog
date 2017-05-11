from django.conf.urls import include, url
from django.contrib import admin

# urlresolver(어떤 웹사이트로 가야할지 판단해주는)가 사용하는 패턴 목록을 목함
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
