from django.urls import path
from django.urls.conf import include
from .views import DataIndexView, TrainingSetView, TestingSetView, LihatDataView

app_name = 'dataset'
urlpatterns = [
    path('', DataIndexView.as_view(), name='index'),
    path('lihat/', LihatDataView.as_view(), name='lihat'),
    path('latih/', TrainingSetView.as_view(), name='training'),
    path('uji/', TestingSetView.as_view(), name='testing'),
]
