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
    url(r'^home$', 'index'),
    url(r'^teacher$', 'teacher_view'),
    url(r'^teacher/add$', 'teacher_add'),
    url(r'^teacher/edit/(?P<teacher_id>\d+)$', 'teacher_edit'),
    url(r'^teacher/delete/(?P<teacher_id>\d+)$', 'teacher_delete'),
    url(r'^teacher/search/(?P<key>.+)$', 'teacher_search'),
    url(r'^project$', 'project_index'),
    url(r'^project/(?P<project_id>\d+)$', 'project_view'),
    url(r'^project/edit/(?P<project_id>\d+)$', 'project_edit'),
    url(r'^project/add$', 'project_add'),
    url(r'^project/delete/(?P<project_id>\d+)$', 'project_edit'),
    url(r'^project/add/device/(?P<project_id>\d+)$', 'project_add_device'),
    url(r'^/device/edit/(?P<device_id>\d+)$', 'device_edit'),
    url(r'^/device/delete/(?P<device_id>\d+)$', 'device_delete'),
    url(r'^/business/edit/(?P<business_id>\d+)$', 'business_edit'),
    url(r'^/business/delete/(?P<business_id>\d+)$', 'business_delete'),
    url(r'^expense$', 'expense_add'),
    url(r'^record$', 'expense_view'),
)

urlpatterns += staticfiles_urlpatterns()
