from django.urls import path
from django.urls.conf import include
from .views import EvaluasiModelDataBaru, EvaluasiModelListData

app_name = 'evaluasimodel'
urlpatterns = [
    path('', EvaluasiModelListData.as_view(), name='index'),
    path('databaru/', EvaluasiModelDataBaru.as_view(), name='evaldatabaru'),
]
