"""
URL configuration for Elite project.

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
from django.urls import path
from .views import home,HomeView
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from hotel.views import PostListView

urlpatterns = [
   path('admin/', admin.site.urls),
   path('mychatapp/', include('mychatapp.urls')),
   #path('home/', home, name='home'),  
   # path('',include('hotel.urls')),
   #path('homeview/', HomeView.as_view(), name='homeview'),
    path('', home, name='homeview'),
   #  path('', TemplateView.as_view(template_name='home.html'), name='HomeView'),
    path('hotel/',include('hotel.urls')),
    path('feed/', include('feed.urls')),
   # path('inbox/notifications/', include('notifications.urls', namespace='notifications')),

    path('seassion/',include('seassion.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


