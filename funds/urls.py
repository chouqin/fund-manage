from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('funds.views',
    # Examples:
     #url(r'^$', 'fundManage.views.home', name='home'),
    # url(r'^fundManage/', include('fundManage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index'),
)

urlpatterns += staticfiles_urlpatterns()
