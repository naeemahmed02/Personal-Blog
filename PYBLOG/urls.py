from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('go_in/', admin.site.urls),
    path('', include('core.urls')),
    path('category/', include('category.urls')),
    path('blog/', include('blog.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    path('projects/', include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    path('resume/', include('resume.urls')),
    path('tinymce/', include('tinymce.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)