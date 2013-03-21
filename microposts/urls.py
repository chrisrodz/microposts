from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'microposts.views.home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^allposts/$', 'posts.views.allposts'),
    url(r'^accounts/profile/$', 'posts.views.profile'),
    url(r'^addpost/$', 'posts.views.add'),
    url(r'^follow/$', 'posts.views.follow'),
    url(r'^register/$', 'posts.views.register'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
