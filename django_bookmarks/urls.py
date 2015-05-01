from django.conf.urls import patterns, include, url
from bookmarks.views import *
import os.path
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

site_media = os.path.join(
    os.path.abspath(os.path.dirname(__name__)), 'site_media'
)

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$','django.contrib.auth.views.login'),
    (r'^logout/$',logout_page),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':site_media}),
    (r'^register/$', register_page),
    (r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html')),
    (r'^save/$', bookmark_save_page),
    (r'^vote/$', bookmark_vote_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloud_page),
    (r'^search/$', search_page),

)


# Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),