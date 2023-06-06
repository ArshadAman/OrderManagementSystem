
from django.contrib import admin
from django.urls import path, include
from .views import create_super_user
from django.conf.urls.static import static
from django.conf import settings
from .views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-admin/', name="create-admin", view=create_super_user),
    path('masters/', include('masters.urls')),
    path('quality/', include('qao.urls')),
    path('', view=homepage, name="home")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
