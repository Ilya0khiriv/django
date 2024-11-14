from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

users = ["Cole", "Max", "Peter"]
info = {}


def get_info(object, print=False):
    data = ["username", "password", "password_2", "age"]
    return_list = []

    for i in data:
        try:
            return_list.append(object(i))
        except:
            return_list.append(object[i])

    return return_list

def carry_on(data=None, request=None, form=None):
    username = False
    password = False
    age = False

    if data[0] not in users:
        username = True

    if data[1] == data[2]:
        password = True

    try:
        age_ = int(data[3])
    except:
        age_ = 0

    if age_ >= 18:
        age = True

    if username == password == age:
        return render(request, './fifth_task/registration_page.html', {'success': data[0]})

    error = []

    if not age:
        error.append('Вы должны быть старше 18')
    if not username:
        error.append('Пользователь уже существует')
    if not password:
        error.append('Пароли не совпадают')

    return render(request, './fifth_task/registration_page.html', {'form': form, "error": error})


def sign_up_by_html(request):
    if request.method == 'POST':
        info_ = get_info(request.POST.get, print=True)
        print(info_)

        return carry_on(data=info_, request=request)

    return render(request, './fifth_task/registration_page.html')


def sign_up_by_django(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            info_ = get_info(request.POST.get, print=True)
            print(info_)

            return carry_on(data=info_, request=request, form=form)
        else:
            print("nooooo")

    return render(request, './fifth_task/registration_page.html', {'form': form})
