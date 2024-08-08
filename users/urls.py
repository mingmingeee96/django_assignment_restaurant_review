from rest_framework.urls import path
from users import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('signup/', views.UserSignupView.as_view(), name='user-signup'),
    path('logout/', LoginView.as_view(), name='user-logout'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
