from django.urls import path
from . import views
from . views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    #path('', views.getRoutes),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path("users/", UsersList.as_view(), name="users"),
]
