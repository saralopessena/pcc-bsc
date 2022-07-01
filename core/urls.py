from codecs import namereplace_errors
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import index
from posts.views import get_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls','users'), namespace='users')),
    path('posts/', include(('posts.urls','posts'), namespace='posts')),
    
    path('quiz/', include(('quiz.urls','quiz'), namespace='quiz')),
    path('p/<str:name_page>/', get_page, name="posts-s"),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name="homepage")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)