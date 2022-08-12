from django.shortcuts import render
from django.views import View
from django.conf import settings
import sys
import os
import pickle
sys.path.append(settings.DATASET_DIR)

# Create your views here.


class DataIndexView(View):
    template_name = 'dataset/index.html'
    context = {
        'page_title': 'Data Penelitian'
    }

    def get(self, request):
        return render(request, self.template_name, self.context)


class LihatDataView(View):
    template_name = 'dataset/lihat.html'
    context = {
        'page_title': 'Data Penelitian'
    }
    dataset_dir = os.path.join(
        settings.DATASET_DIR, 'dataset.pkl')
    dataset = pickle.load(open(dataset_dir, 'rb'))

    def get(self, request):
        self.context['pkh'] = {
            'features': self.dataset['features_name'],
            'data': self.dataset['all'],
        }
        return render(request, self.template_name, self.context)


class TrainingSetView(LihatDataView):
    template_name = 'dataset/training.html'
    context = {
        'page_title': 'Data Latih'
    }

    def get(self, request):
        training_set = self.dataset['training']
        self.context['training'] = {
            'features': self.dataset['features_name'],
            'data': training_set['data'],
        }
        return render(request, self.template_name, self.context)


class TestingSetView(LihatDataView):
    template_name = 'dataset/testing.html'
    context = {
        'page_title': 'Data Uji'
    }

    def get(self, request):
        testing_set = self.dataset['testing']
        self.context['testing'] = {
            'features': self.dataset['features_name'],
            'data': testing_set['data'],
        }
        return render(request, self.template_name, self.context)
