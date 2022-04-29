
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('contact/',views.contact,name='contactpage'),
    path('dashboard/',views.dashboard,name='dashboardpage'),
    path('signup/',views.user_signup,name='signuppage'),
    path('login/',views.user_login,name='loginpage'),
    path('logout/',views.user_logout,name='logoutpage'),
    path('updatepost/<int:id>/',views.updatepost,name='updatepost'),
    path('addpost/',views.addpost,name='addpost'),
    path('deletepost/<int:id>/',views.deletepost,name='deletepost'),




]
