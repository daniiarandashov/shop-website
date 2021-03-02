from django.shortcuts import render, redirect
from django.views.generic import  View ,ListView
from.forms import RegistrationForm, UserUpdateForm
from .models import Product


class MainView(View):
    '''Данный класс выводит главную html'''
    def get(self, request):
        return render(
            request=request,
            template_name='registration/index.html'
        )

class LaptopsView(ListView):
    '''Вывод товаров по категории'''
    model = Product
    template_name = 'registration/cards.html'
    
    def get_context_data(self, **kwargs):
        kwargs["data"]= Product.objects.filter(categorie='Laptops')
        return super().get_context_data(**kwargs)

class SmarphonesView(ListView):
    '''Вывод товаров по категории'''
    model = Product
    template_name = 'registration/cards.html'
    
    def get_context_data(self, **kwargs):
        kwargs["data"]= Product.objects.filter(categorie='Smarphones')
        return super().get_context_data(**kwargs)


def registration(request):
    '''Функция регистрации пользователя'''
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            form = registration_form.save(commit=False)
            form.first_name = registration_form.cleaned_data["first_name"]
            form.last_name = registration_form.cleaned_data["last_name"]
            form.email = registration_form.cleaned_data["email"]
            form.save()
            return redirect('main:main')

    else:
        registration_form = RegistrationForm()

    return render(
        request=request,
        template_name='registration/registration.html',
        context={"sign_in_form": registration_form}
    )


def update(request,pk):
    '''Функция изменения профиля'''
    reservation_form = UserUpdateForm()

    if request.method == 'POST':
        reservation_form = UserUpdateForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return render(
                reguest=request,
                template_name='registration/update_profile.html',
            )
        else:
            reservation_form = UserUpdateForm()
            return render(
                request=request,
                template_name='registration/update_profile.html',
                context={"form": reservation_form}
            )
    reservation_form = UserUpdateForm()
    return render(
        request=request,
        template_name='registration/update_profile.html',
        context={"form": reservation_form}
    )

    