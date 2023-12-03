from django.urls import path
from .views import APICALLS

urlpatterns = [
    path('', APICALLS.as_view())
]
