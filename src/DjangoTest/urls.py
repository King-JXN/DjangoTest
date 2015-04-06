from django.conf.urls import patterns, include, url
from django.contrib import admin
from Blog.views import archive

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', archive),
    url(r'^static/(?P<path>.*)', 'django.views.static.serve',{'document_root': settings.STATIC_PATH}),
)
