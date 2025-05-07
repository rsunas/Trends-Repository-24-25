from django.contrib import admin
from django.urls import path
from app.views import index  # importing the index view from app

urlpatterns = [
    path('admin/', admin.site.urls),  # route to Django admin panel
    path('', index, name="index"),    # root URL (home page) goes to the index view
]