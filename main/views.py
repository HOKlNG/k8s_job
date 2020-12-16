from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import FormView, View
# Create your views here.

import ast


def index(request):
    return render(request, 'index.html')


class MyPage(View):
    """

    """
    params = dict()
    template_name = None

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        keyword_list = request.POST.get('keyword')
        try:
            keyword_list = ast.literal_eval(keyword_list)
        except:
            pass
        return JsonResponse({})