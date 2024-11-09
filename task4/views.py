from django.shortcuts import render
from task4.lang_platform import all_langs as localization
print(localization)

chosen_lang = "Русский"
context = dict(localization[chosen_lang].__dict__)

def platform(request):
    return render(request, 'fourth_task/platform.html', context)

def games(request):
    return render(request, 'fourth_task/store.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html', context)

def lang(request):
    global chosen_lang
    global context
    list_lang = list(localization.keys())

    if request.method == 'GET':
        lang = request.GET.get('lang', '')
        if lang in list_lang:

            chosen_lang = lang
            context = dict(localization[chosen_lang].__dict__)

    context.update({"universal_langs": list_lang})

    return render(request, 'fourth_task/lang.html', context)
