from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This forwards API traffic to your shortener app's routing file
    path('', include('shortener.urls')), 
]