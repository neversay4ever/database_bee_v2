from django.urls import path
from .views import StrainHomeView

urlpatterns = [
    path('', StrainHomeView.as_view(), name='strain_home'),

]
