from django.urls import path, include
from .views import register_user,get_all_users, login_user,logout_user,change_password

urlpatterns = [
    path('users/', get_all_users, name='users'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('reset_password/', include('django_rest_passwordreset.urls', namespace='password_reset')), #namespace is optional 

]