from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from chandahotel_and_lodging.views import *
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index),
                  path('index/', index),
                  path('home/', index),
                  path('feedback/', index),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
