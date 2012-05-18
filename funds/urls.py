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
    url(r'^project/delete/(?P<project_id>\d+)$', 'project_delete'),
    url(r'^project/add$', 'project_add'),
    url(r'^project/add/device/(?P<project_id>.+)$', 'project_add_device'),
    url(r'^project/add/business/(?P<project_id>.+)$','project_add_business'),
    url(r'^device/edit/(?P<device_id>.+)$','device_edit'),
    url(r'^device/delete/(?P<device_id>.+)$','device_delete'),
    url(r'^business/edit/(?P<business_id>.+)$','business_edit'),
    url(r'^business/delete/(?P<business_id>.+)$','business_delete'),
    url(r'^project$', 'project_view'),
    url(r'^expense$', 'teacher_select'),
    url(r'^project/select/(?P<teacher_id>\d+)$', 'project_select'),
    url(r'^funds/select/(?P<teacher_id>\d+)/(?P<project_id>\d+)$', 'funds_select'),
    url(r'^deviceExpense/add/(?P<device_id>\d+)/(?P<teacher_id>\d+)$', 'device_expense_add'),
    url(r'^businessExpense/add/(?P<business_id>\d+)/(?P<teacher_id>\d+)$', 'business_expense_add'),
    url(r'^record$', 'expense_view'),

)

urlpatterns += staticfiles_urlpatterns()
