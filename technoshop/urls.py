"""
URL configuration for technoshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import sys
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from technoshop.settings import local, base

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path("", include("django.contrib.auth.urls")),
    path("", include("products.urls"))
]

if sys.argv[2] == "--settings=technoshop.settings.local": 
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
