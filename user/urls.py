from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, SignUpView, ProfileView, PasswordChangeView, ProfileUpdateView

app_name = 'user'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('profile/', ProfileView.as_view(), name='profile_view'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('profile/<int:pk>', ProfileUpdateView.as_view(), name='profile_update_view'),
]