from django.urls import path
from .views import SignUpView, profile


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='profile')
]
