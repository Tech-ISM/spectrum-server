"""spectrum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from event.views import get_events_list, change_event_participated_status, get_user_events_list, get_events_details
from otp.views import send_otp, verify_otp
from splash_screen.views import splash_screen

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create_user/$', send_otp),
    url(r'^verify_otp/$', verify_otp),
    url(r'^is_update_available/$', splash_screen),
    url(r'^get_events_list/$', get_events_list),
    url(r'^get_events_details/$', get_events_details),
    url(r'^user_event_list/$', get_user_events_list),
    url(r'^change_event_participated_status/$', change_event_participated_status),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
