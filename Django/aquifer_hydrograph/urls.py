from django.urls import path

from .views import aquifer_hydrograph_view
from aquifer_hydrograph.dashApp import app

app_name = "aquifer_hydrograph"
urlpatterns = [
    path(route='', view=aquifer_hydrograph_view, name='aquifer_hydrograph')
]
