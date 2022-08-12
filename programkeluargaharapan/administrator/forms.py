from django import forms
from evaluasimodel.models import Kecamatan, Kelurahan


class DataKecamatanForms(forms.Form):
    # method untuk memberikan class Bootstrap untuk form field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Kecamatan
        fields = "__all__"
        labels = {
            'kode_kecamatan': 'Kode Kecamatan',
            'nama_kecamatan': 'Nama Kecamatan'
        }


class DataKelurahanForms(forms.Form):
    # method untuk memberikan class Bootstrap untuk form field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Kelurahan
        fields = "__all__"
        labels = {
            'kode_kelurahan': 'Kode Kelurahan',
            'nama_kelurahan': 'Nama Kelurahan'
        }
