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
    url(r'^teacher/add/(?P<teacher_id>\d+)$', 'teacher_edit'),
<<<<<<< HEAD
    url(r'^project/add$', 'project_add'),
    url(r'^project$', 'project_view'),
=======
    url(r'^project$', 'project_view'),
    url(r'^project/add$', 'project_add'),
>>>>>>> e7ee6506225887abbc08f325c8ba7235a5ba6eef
    url(r'^expense$', 'expense_add'),
    url(r'^record$', 'expense_view'),
)

urlpatterns += staticfiles_urlpatterns()
