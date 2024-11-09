from django.shortcuts import render
from django.views.generic import TemplateView

class class_view(TemplateView):
<<<<<<< HEAD
    template_name = 'second_task/class_template.html'


def func_view(request):
    return render(request, 'second_task/func_template.html')
=======
    template_name = 'class_template.html'


def func_view(request):
    return render(request, 'func_template.html')
>>>>>>> origin/main

