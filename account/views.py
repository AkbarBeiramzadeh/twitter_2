from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'account/register.html', context=context)

    def post(self, request):
        pass
