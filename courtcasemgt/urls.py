from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',TemplateView.as_view(template_name='home.html'),name="home"),
    path('', include('base.urls')),
    path('task/', include('task.urls')),
    path('matter/', include('matter.urls')),
    path('event/', include('event.urls')),
    path('contact/', include('contact.urls')),
    path('system-settings/', include('systemsettings.urls')),
    path('inbox/notifications/', include('notice.urls')),
    path('notifications/', include('notice.urls')),
    path('matter-update/', include('matterupdate.urls')),
    path('api/', include('api.urls')),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  