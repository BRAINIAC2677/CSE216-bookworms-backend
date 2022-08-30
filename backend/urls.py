"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path

from django.views.static import serve
from django.conf import settings

from reader.views import obtain_auth_token


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Bookworms API",
      default_version='v1',
      description="A Private API for Bookworms Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="asifazad0178@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-token-auth/', obtain_auth_token, name='api-token-auth'),
    
    path('api/reader/', include('reader.urls')),
    path('api/genre/', include('genre.urls')),
    path('api/book/', include('book.urls')),
    path('api/read/', include('read.urls')),
    path('api/bookreview/', include('bookreview.urls')),
    path('api/library/', include('library.urls')),
    path('api/librarystock/', include('librarystock.urls')),
    path('api/bookborrow/', include('bookborrow.urls')),
    path('api/friend/', include('friend.urls')),
    path('api/comment/', include('comment.urls')),
    path('api/notification/', include('notification.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}), 
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
