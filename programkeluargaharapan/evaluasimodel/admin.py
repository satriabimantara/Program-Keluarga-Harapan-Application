from django.contrib import admin
from .models import DataPenduduk, Kelurahan, Kecamatan
# Register your models here.


admin.site.register([
    DataPenduduk,
    Kelurahan,
    Kecamatan,
])
