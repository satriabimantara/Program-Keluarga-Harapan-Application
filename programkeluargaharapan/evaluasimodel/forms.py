from django import forms
from .models import DataPenduduk, Kecamatan, Kelurahan
import pickle
import os
from django.conf import settings


class DataPendudukForms(forms.ModelForm):
    # method untuk memberikan class Bootstrap untuk form field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # get numerical attributes from pickle
        dataset_dir = os.path.join(
            settings.DATASET_DIR,
            'dataset.pkl'
        )
        dataset = pickle.load(
            open(dataset_dir, 'rb')
        )
        numerical_attributes = dataset['attributes']['types']['numerical']
        self.fields['prediksi_bantuan'].widget.attrs['readonly'] = True
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })
        for num_field in numerical_attributes:
            self.fields[num_field].widget.attrs['max'] = 5
            self.fields[num_field].widget.attrs['min'] = 0
            self.fields[num_field].help_text = 'Minimal 0 | Maksimal 5'

    def save(self, commit=True):
        instance = super(DataPendudukForms, self).save(commit=False)
        if commit:
            instance.save()
        return instance

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        return cleaned_data

    # mengganti value pada option form dengan nama_kecamatan
    kecamatan = forms.ModelChoiceField(
        queryset=Kecamatan.objects.all(),
        empty_label='- Pilih Kecamatan -',
        label='Nama Kecamatan',
        to_field_name="nama_kecamatan"  # value pada option list
    )
    # mengganti value pada option form dengan nama_kelurahan
    kelurahan = forms.ModelChoiceField(
        queryset=Kelurahan.objects.all(),
        empty_label='- Pilih Kelurahan -',
        label='Nama Kelurahan',
        to_field_name="nama_kelurahan"  # value pada option list
    )

    class Meta:
        model = DataPenduduk
        fields = "__all__"
