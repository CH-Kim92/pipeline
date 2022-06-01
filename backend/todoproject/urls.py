
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('housedata/', include('checkboxpost.urls')),
    path('request/', include('sendrequest.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('token/', include('login.urls')),
    path('login/', include('logininfo.urls')),
    path('contactUs/', include('contactUs.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
