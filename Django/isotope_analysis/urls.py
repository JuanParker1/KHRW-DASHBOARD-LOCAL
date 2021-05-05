from django.urls import path

from .views import isotope_analysis_view
from isotope_analysis.dashApp import app

app_name = "isotope_analysis"
urlpatterns = [
    path(route='', view=isotope_analysis_view, name='isotope_analysis')
]
