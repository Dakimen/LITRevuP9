"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from authentification.views import CustomLoginView, sign_up, logout_user
from flux import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(
        template_name='authentification/landing.html',
        redirect_authenticated_user=True
    ), name='landing'),
    path('sign-up/', sign_up, name='sign-up'),
    path('flux/', views.flux, name='flux'),
    path('logout/', logout_user, name='logout'),
    path('create-ticket/', views.add_ticket, name='create-ticket'),
    path('create-review/', views.add_review, name='create-review'),
    path('create-review/<int:id>/',
         views.add_review_to_ticket,
         name='create-review-response'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('own-posts/', views.my_posts, name='own-posts'),
    path('subscriptions/<int:id>/',
         views.manage_subscriptions,
         name='manage-subscriptions'),
    path('modify-ticket/<int:id>/', views.modify_ticket, name="modify-ticket"),
    path('modify-review/<int:id>/', views.modify_review, name='modify-review'),
    path('delete-ticket/<int:id>/', views.delete_ticket, name='delete-ticket'),
    path('delete-review/<int:id>/', views.delete_review, name='delete-review'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
