import os
import pickle
from pandas import DataFrame as DF
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from .forms import DataPendudukForms
from .models import DataPenduduk
# Create your views here.


class EvaluasiModelListData(ListView):
    template_name = 'evaluasimodel/index.html'
    context = {
        'page_title': 'Evaluasi Model',
    }
    # load dataset
    dataset_dir = os.path.join(
        settings.DATASET_DIR,
        'dataset.pkl'
    )
    dataset = pickle.load(
        open(dataset_dir, 'rb')
    )
    numerical_attributes = dataset['attributes']['types']['numerical']

    def get(self, request):
        all_data_penduduk = DataPenduduk.objects.all()
        self.context.update(
            {
                'all_data_penduduk': all_data_penduduk,
                'numerical_attributes': self.numerical_attributes,
            }
        )
        return render(request, self.template_name, self.context)


class EvaluasiModelDataBaru(SuccessMessageMixin, CreateView):
    template_name = 'evaluasimodel/evaldatabaru.html'
    extra_context = {
        'page_title': "Evaluasi Model Data Baru"
    }
    form_class = DataPendudukForms
    success_url = reverse_lazy("evaluasimodel:index")
    success_message = '%(nik)s | %(nama_lengkap)s | berhasil disimpan'

    # load dataset
    dataset_dir = os.path.join(
        settings.DATASET_DIR,
        'dataset.pkl'
    )
    dataset = pickle.load(
        open(dataset_dir, 'rb')
    )

    # load predictors
    predictors_dir = os.path.join(
        settings.PREDICTORS_DIR,
        'predictors.pkl'
    )
    predictors = pickle.load(
        open(predictors_dir, 'rb')
    )
    standardscaler = predictors['StandardScaler']
    categorical_encoder = predictors['CategoricalEncoder']
    label_encoder = categorical_encoder['LabelEncoder']
    one_hot_encoder = categorical_encoder['OneHotEncoder']['encoder']
    encoded_columns = categorical_encoder['OneHotEncoder']['encoded_columns']
    pca_scaler = predictors['PCA']['merged']['scaler']
    # load trained-ANN Models
    models_dir = os.path.join(
        settings.MODELS_DIR,
        'multilayerperceptron_prep_merged.pkl'
    )
    multilayerperceptron = pickle.load(
        open(models_dir, 'rb')
    )

    def form_valid(self, form):
        # get cleaned data from form
        cleaned_data = form.cleaned_data
        instance = form.save(commit=False)

        # define features_name from dataset
        numerical_attributes = self.dataset['attributes']['types']['numerical']
        categorical_attributes = self.dataset['attributes']['types']['categorical']

        # tangkap inputan user
        X_inputs = dict()
        for num_col in numerical_attributes:
            X_inputs[num_col] = int(cleaned_data[num_col])
        X_inputs['kecamatan'] = str(
            cleaned_data['kecamatan'].nama_kecamatan)

        # preparing user input using predictors
        input_df = DF(
            data=X_inputs,
            index=[0]
        )

        # standardization numerical attributes using Z-score
        input_df[numerical_attributes] = self.standardscaler.transform(
            input_df[numerical_attributes]
        )

        # label encoding for categorical attributes
        input_df[categorical_attributes] = DF(
            data=self.label_encoder.transform(
                input_df[categorical_attributes].values.ravel()),
            columns=categorical_attributes
        )

        # one-hot-encoding
        input_df[self.encoded_columns] = DF(
            data=self.one_hot_encoder.transform(
                input_df[categorical_attributes]),
            columns=self.encoded_columns
        )

        # drop categorical attributes after one hot encoding process
        input_df.drop(categorical_attributes, axis=1, inplace=True)

        # dimensionality reduction using PCA
        X_inputs = self.pca_scaler.transform(input_df)

        # predict inputs using Trained MultiLayerPerceptron
        prediksi_bantuan = self.multilayerperceptron.predict(X_inputs)

        # save predicted prediksi_bantuan into instance object
        print(prediksi_bantuan)
        print(instance)
        print(cleaned_data)
        instance.prediksi_bantuan = round(prediksi_bantuan[0], 4)
        instance.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)
