from django.urls import include, path
from .views import login_view, logout_view

app_name = 'custom_auth'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]