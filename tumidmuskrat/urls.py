from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import blog.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tumidmuskrat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),

    url('^blog/', blog.views.index, name='blog_index'),
# TODO: remove following line in production.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
