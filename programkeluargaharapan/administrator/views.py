import pickle
from django.conf import settings
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView
)
from .forms import DataKecamatanForms, DataKelurahanForms
from evaluasimodel.models import Kecamatan, Kelurahan
import os
# Create your views here.


class AdministratorIndexView(SuccessMessageMixin, View):
    template_name = 'administrator/index.html'
    context = {
        'page_title': 'Administrator Page'
    }

    def get(self, request):
        return render(request, self.template_name, self.context)


class InputOtomatisDataAtribut(SuccessMessageMixin, View):
    template_name = 'administrator/index.html'
    context = {
        'page_title': 'Administrator Page',
        'messages': []
    }
    DATASET_DIR = os.path.join(settings.DATASET_DIR, 'dataset.pkl')
    dataset = pickle.load(open(DATASET_DIR, 'rb'))

    def __init__(self, *args, **kwargs):
        super(InputOtomatisDataAtribut, self).__init__(*args, **kwargs)
        self.set_context('messages', [])

    def set_context(self, key, value):
        self.context[key] = value

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        unique_values_attributes = self.dataset['attributes']['unique_values']
        if request.POST.get('btnSubmit') == "data_kecamatan":
            post_form = DataKecamatanForms(request.POST or None)
            if post_form.is_valid():
                unique_values_kecamatan = unique_values_attributes['NMKECA']
                for idx, kecamatan in enumerate(unique_values_kecamatan):
                    Kecamatan.objects.create(
                        kode_kecamatan='KCM-'+str(idx+1),
                        nama_kecamatan=kecamatan
                    )
                # add message success
                self.context['messages'].append(
                    {
                        'type': 'success',
                        'heading': 'Success',
                        'msg': 'Data atribut kecamatan berhasil diinput secara otomatis berdasarkan dataset'
                    }
                )
            else:
                # form invalid
                self.context['messages'].append(
                    {
                        'type': 'danger',
                        'heading': 'Error',
                        'msg': 'Invalid Input!'
                    }
                )

        elif request.POST.get('btnSubmit') == "data_kelurahan":
            post_form = DataKelurahanForms(request.POST or None)
            if post_form.is_valid():
                unique_values_kelurahan = unique_values_attributes['NMKELR']
                for idx, kelurahan in enumerate(unique_values_kelurahan):
                    Kelurahan.objects.create(
                        kode_kelurahan='KLR-'+str(idx+1),
                        nama_kelurahan=kelurahan
                    )
                # add message success
                self.context['messages'].append(
                    {
                        'type': 'success',
                        'heading': 'Success',
                        'msg': 'Data atribut kelurahan berhasil diinput secara otomatis berdasarkan dataset'
                    }
                )
            else:
                # form invalid
                self.context['messages'].append(
                    {
                        'type': 'danger',
                        'heading': 'Error',
                        'msg': 'Invalid Input!'
                    }
                )
        else:
            # button form submit tidak terdaftar
            self.context['messages'].append(
                {
                    'type': 'warning',
                    'heading': 'Warning',
                    'msg': 'Tidak ditemukan button submit ini!'
                }
            )

        return render(request, self.template_name, self.context)


# class InputOtomatisDataAtribut(SuccessMessageMixin, CreateView):
#     template_name = 'administrator/index.html'
#     extra_context = {
#         'page_title': "Administrator Page"
#     }
#     form_class = DataKecamatanForms
#     success_url = reverse_lazy("administrator:index")
#     success_message = ''

#     def form_valid(self, form):
#         print(form)
#         print('form_valid')
#         # form.save()
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         print('form_invalid')
#         return super().form_invalid(form)

#     def get_context_data(self, **kwargs):
#         self.kwargs.update(self.extra_context)
#         kwargs = self.kwargs
#         return super().get_context_data(**kwargs)
