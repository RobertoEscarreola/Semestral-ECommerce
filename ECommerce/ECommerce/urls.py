from django.contrib import admin
from django.urls import path,include

""" urls de admin """
urlpatterns = [
    path('jet/', include('jet.urls','jet')),
    path('jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')),
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
