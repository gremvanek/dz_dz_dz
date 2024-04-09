from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserProfileForm, UserRegisterForm
from users.utils import send_email_for_verify

User = get_user_model()


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:confirm_email')

    def get(self, request, *args, **kwargs):
        context = {
            'form': UserRegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()  # Сохраняем объект пользователя
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)  # Передаем запрос и пользователя в функцию
            return redirect('users:email_register')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/user_form.html'

    def get_object(self, queryset=None):
        return self.request.user


class EmailVerifyView(View):
    success_url = reverse_lazy('users:login')

    @staticmethod
    def get(request, uidb64, token):
        try:
            # Декодируем uid и получаем пользователя
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        # Проверяем токен и пользователя
        if user is not None and token_generator.check_token(user, token):
            # Устанавливаем email_verified в True
            user.email_verified = True
            user.save()
            messages.success(request, "Ваш email успешно подтвержден")
            return redirect('users:email_success')

            # Если токен недействителен, выводим сообщение об ошибке
        messages.error(request, "Ссылка для подтверждения недействительна или истекла")
        return redirect('users:email_fail')
