from django.conf.urls import patterns, include, url
from django.contrib import admin
from Blog.views import archive
from SetAddress.views import loadDisplayInfor

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', archive),
    url(r'^setAddress/$', loadDisplayInfor),
)
