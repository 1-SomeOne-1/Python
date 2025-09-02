from django.urls import path
from .views import home, login_view, dashboard, latest_blogs, blog_detail, create_blog
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('', home , name='home'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard' ),
    path('latest-blogs/', latest_blogs, name='latest_blogs'),
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),
    path('create_blog/', create_blog, name='create_blog'),

]
 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)