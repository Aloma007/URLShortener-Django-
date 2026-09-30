from django.urls import path
from .views import ShortURLCreate, ShortURLDetail, ShortURLStats

urlpatterns = [
    # Maps to POST /shorten
    path('shorten', ShortURLCreate.as_view(), name='shorten-create'),
    
    # Maps to GET, PUT, and DELETE /shorten/<shortCode>
    path('shorten/<str:shortCode>', ShortURLDetail.as_view(), name='shorten-detail'),
    
    # Maps to GET /shorten/<shortCode>/stats
    path('shorten/<str:shortCode>/stats', ShortURLStats.as_view(), name='shorten-stats'),
]