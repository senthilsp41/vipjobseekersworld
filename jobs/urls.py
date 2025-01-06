from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import LoginForm

app_name = 'jobs'

urlpatterns = [
    path('',views.index,name='index'),
    path('all/', views.indexs, name='indexs'),
    path('blog/', views.blog, name='blog'),
    path('reset-password/', views.reset_password, name='reset_password'),  # This handles reset password page
    path('verify-otp/', views.verify_otp, name='verify_otp'),  # This handles OTP verification page
    path('request-email/', views.request_email, name='request_email'),  # This handles email input for OTP request

    # Accept email as URL parameter
    path('new-password/<str:email>/', views.new_password, name='new_password'),  # This handles the new password page
    path('contact/', views.contact, name='contact'),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='jobs/login.html',authentication_form=LoginForm),name='login'),
    # path('logout/', LogoutView.as_view(next_page='jobs:index'), name='logout'),
    

    # path('password_reset/', views.password_reset_request, name='password_reset'),
    # path('password_reset/', views.password_reset_request, name='password_reset'),
    # path('password_reset/done/', views.password_reset_done, name='password_reset_done'),

    # # Password reset confirmation (enter new password)
    # path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', views.password_reset_complete, name='password_reset_complete'),

    
    
    
]
