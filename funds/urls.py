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
#<<<<<<< HEAD
#<<<<<<< HEAD
    #url(r'^teacher/edit/(?P<teacher_id>\d+)$', 'teacher_edit'),
    #url(r'^teacher/delete/(?P<teacher_id>\d+)$', 'teacher_delete'),
    #url(r'^project$', 'project_view'),
    #url(r'^project/add$', 'project_add'),
#=======
    #url(r'^teacher/add/(?P<teacher_id>\d+)$', 'teacher_edit'),
    #url(r'^teacher/search/(?P<key>.+)$', 'teacher_search'),
    #url(r'^project/add$', 'project_add'),
    #url(r'^project$', 'project_view'),
#>>>>>>> 330c5a0d2cb1911d6966f56d77de18a446388b77
#=======
    url(r'^teacher/edit/(?P<teacher_id>\d+)$', 'teacher_edit'),
    url(r'^teacher/search/(?P<key>.+)$', 'teacher_search'),
    url(r'^project$', 'project_index'),
    url(r'^project/(?P<project_id>\d+)$', 'project_view'),
    url(r'^project/add$', 'project_add'),
    url(r'^project/add/device/(?P<project_id>\d+)$', 'project_add_device'),
#>>>>>>> dbb09a6f48a3c66585860cb8f7cf8a9bd11544bc
    url(r'^expense$', 'expense_add'),
    url(r'^record$', 'expense_view'),
)

urlpatterns += staticfiles_urlpatterns()
