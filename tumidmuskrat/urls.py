from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import blog.views
import pages.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tumidmuskrat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^$', pages.views.home, name='home'),
    url(r'^blog/$', blog.views.list_posts, name='blog_index'),
    url(r'^blog/(?P<page>[0-9]+)/$', blog.views.list_posts, name='blog_post_list'),
# TODO: remove following line in production.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
