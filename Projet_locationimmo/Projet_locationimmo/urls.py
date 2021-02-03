"""Projet_locationimmo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from compte import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('compte/inscription/', views.inscriptionPage, name='inscription'),
    path('compte/acces/', views.accesPage, name='acces'),
    path('compte/quitter/', views.logoutUser, name='quitter'),
    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account_settings'),
    path('', include('produit.urls')),
    path('client', include('client.urls')),
    path('commande', include('commande.urls')),
   # path('compte/', include('compte.urls')),
    path('posts/', include('posts.urls')),
   # path('create-post/', views.create_post_view, name='create-post'),
   # path('<int:id>/', views.detail_view, name='detail'),
    url('^soumission/', include('soumission.urls')),
    url('^soumission/validation/', include('soumission.urls')),
    # url('^soumission/request-meeting/<int:id>/', include('soumission.urls')),
    url('^soumission/client/', include('soumission.urls')),
 #   path('reset_password/', auth_views.PasswordResetView.as_view(),name="reset_password"),
  #  path('reset_password_sent/', auth_views.PasswordResetDone.as_view(),name="password_reset_done"),
  #  path('reset/<uidb64>/<token>/', auth_views.PasswordConfirmView.as_view(),name="password_reset_confirm"),
  #  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""Password Reset

    1. Submit  email form  // passwordResetView.as_view()
    2. Email sent success message // passwordResetDoneView.as_view()
    3. Link to password Reset form in email // passwordResetConfirmView.as_view()
    4. Password successful changed message // passwordResetCompleteView.as_view()
"""