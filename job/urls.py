"""job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from account.views import activate
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobapp.urls')),
    path('', include('account.urls')),
    path('', include('letter.urls')),
    path('', include('posts.urls')),
    path('cv/', include("cvbuilder.urls")),
    path("quiz/", include("quiz.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('tinymce/', include('tinymce.urls')),
    
    
    
    path('activate/<uidb64>/<token>',
        activate, name='activate'),

    path('oauth/', include('social_django.urls', namespace='social')),


   path('password_reset_form/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password/password_reset_form.html'
         ),
         name='password_reset'),
         
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

