from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from users.views import RegisterView

urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls),
    
    # Menu URLs
    path('', RedirectView.as_view(url='/menu/', permanent=False)),
    path('menu/', include('menu.urls')),
    
    # Order URLs
    path('api/', include('orders.urls')),
    
    # Authentication URLs
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add login redirect URL to settings
LOGIN_REDIRECT_URL = '/menu/'