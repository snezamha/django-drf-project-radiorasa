from django.urls import path, include
from .views import AudioList

app_name = 'api'

urlpatterns = [
    path('v1/', AudioList.as_view(), name='audio')
]
