from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from jobs.views import index, contact, blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('inbox/',include('conversation.urls')),
    path('', include('jobs.urls')),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

