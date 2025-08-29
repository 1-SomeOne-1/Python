from django.urls import path
from .views import home, login_view, dashboard, latest_blogs, blog_detail

urlpatterns = [
    path('', home , name='home'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard' ),
    path('latest-blogs/', latest_blogs, name='latest_blogs'),
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),

]
