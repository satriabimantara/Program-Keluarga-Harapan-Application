from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = 'index.html'
    context = {
        'page_title': 'PKH | Home'
    }

    def get(self, request):
        return render(request, self.template_name, self.context)
