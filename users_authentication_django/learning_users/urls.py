"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
""" from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^admin/', admin.site.urls),
    url(r'^basic_app/',include('basic_app.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
 """
from django.conf.urls import url, include
from django.contrib import admin
from basic_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^admin/', admin.site.urls),
    url(r'^basic_app/', include('basic_app.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)