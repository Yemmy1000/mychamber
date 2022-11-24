from django.urls import path
from . import views
from django.http import HttpResponse
# from .views import UserListJson



urlpatterns = [
    path('', views.home, name="home" ),
   
    path('login/', views.loginView, name="login" ),
    path('user-profile/<str:pk>', views.UserProfile, name="user-profile" ),
    # path('register/', views.registerView, name="register" ),
    path('user/', views.User, name="user-staff" ),

    path('logout/', views.logoutUser, name="logout" ),    
    
    path('update-profile/<str:pk>', views.UpdateProfile, name="update-profile" ),
    path('update-user/', views.UpdateUser, name="update-user" ),
    path('update-user-info/<str:pk>', views.UpdateUserInfo, name="update-user-info" ),

    # path('create-profile/', views.CreateUserProfile, name="create-profile" ),
    path('change-password/', views.ChangePassword, name="change-password" ),
    # path('password-reset/', views.PasswordReset, name="password-reset" ),

    path('add-new-user/', views.AddNewUser, name="add-new-user" ), 
    # path('user-list/', UserListJson.as_view(), name="user_list_json"),

]
