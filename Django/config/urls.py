from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from aquifer_hydrograph.views import aquifer_hydrograph_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='', view=include('home.urls')),
    path(route='', view=include('accounts.urls')),
    path(route='aquifer_hydrograph/', view=include('aquifer_hydrograph.urls')),
    path(route='django_plotly_dash/', view=include('django_plotly_dash.urls'))    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
