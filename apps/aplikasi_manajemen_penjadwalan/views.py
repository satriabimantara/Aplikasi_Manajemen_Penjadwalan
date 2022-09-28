from django.views import View
from django.shortcuts import render


class IndexView(View):
    template_name = 'index.html'
    context = {
        'title_page': "Home",
        'subtitle_page': 'Halaman Home'
    }

    def get(self, request, **params):
        return render(request, self.template_name, self.context)


def error_404_view(request, exception):
    return render(request, '404.html')
