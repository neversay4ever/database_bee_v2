from django.urls import path
from .views import SampleHomeView, SampleDetailView
urlpatterns = [
    path('', SampleHomeView.as_view(), name='sample_home'),
    path('detail/', SampleDetailView.as_view(), name='sample_detail'),
]
