from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', views.create_user, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name ='users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='users/logout.html'), name = 'logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name ='users/password_reset.html'), name = 'password_reset'),
    path('account/profile/', views.profile, name='profile'),
    path('account/profile/update', views.update_profile, name='profile_update'),
    path('account/profile/password/', auth_views.PasswordChangeView.as_view(template_name ='users/password_change.html'), name = 'password_change'),  
    path('account/profile/password/done', auth_views.PasswordChangeDoneView.as_view(template_name ='users/password_change_done.html'), name = 'password_change_done'),  
]