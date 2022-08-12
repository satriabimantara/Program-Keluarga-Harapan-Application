from django.urls import path
from .views import AdministratorIndexView, InputOtomatisDataAtribut

app_name = 'administrator'
urlpatterns = [
    path('', AdministratorIndexView.as_view(), name='index'),
    path('input_data_atribut/',
         InputOtomatisDataAtribut.as_view(), name='input_otomatis')
]
