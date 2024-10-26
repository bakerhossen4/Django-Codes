
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('contact/', views.Contact),
    path('gallery/', views.Gallery),
    path('app1/', include('App1.urls'))
]
