from django.contrib import admin
from django.urls import path, include
from .views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('data/', include('dataset.urls', namespace='dataset')),
    path('evaluasimodel/', include('evaluasimodel.urls', namespace='evaluasimodel')),
    path('administrator/', include('administrator.urls', namespace='administrator')),
]
