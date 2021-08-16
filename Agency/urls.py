from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from django.views.static import serve as mediaserve

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


from django.contrib.sitemaps.views import sitemap
from About.sitemaps import StaticViewSitemap,BlogpostSitemap,ProjectSitemap,ServiceSitemap

sitemaps = {
    'static':StaticViewSitemap,
    'blogpost':BlogpostSitemap,
    'Projects':ProjectSitemap,
    'services':ServiceSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls', namespace='Home')),
    path('Blog/', include('Blog.urls', namespace='Blog')),
    path('About/', include('About.urls', namespace='About')),
    path('Services/', include('Services.urls', namespace='Services')),
    path('Projects/', include('Projects.urls', namespace='Projects')),
    path('Contact/', include('Contact.urls', namespace='Contact')),
    path("sitemap.xml", sitemap, {'sitemaps':sitemaps}, 
    name='django.contrib.sitemaps.views import sitemap'),
    path("robots.txt", TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('summernote/', include('django_summernote.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                       mediaserve, {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
