from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .forms import BlogerProfileCreationForm, MyUserCreationForm


# Create your views here.


def homepage_view(request):
    return render(request, 'homepage.html')


class Register(View):
    def get(self, request):
        form = MyUserCreationForm()
        # print('form', form)

        context = {
            "form": form,
        }
        # print('context', context)
        return render(request, 'registration/register.html', context)

    def post(self, request):

        form = MyUserCreationForm(request.POST)
        print(form.errors)

        print('form 2:', form)
        print('request', request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            usertype = form.cleaned_data['usertype']

            setattr(user, usertype, True)

            user.save()
            user = authenticate(username=username, password=password, usertype=usertype)
            print('user', user)
            login(request, user)
            # send_welcome_signup(user)

            # reverse('create_profile'), form.cleaned_data['usertype']
            return redirect('homepage')

        return render(request, 'registration/register.html', {"form": form})


#
#
# class MyLoginView(LoginView):
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('homepage')
#         return super().get(self, request, *args, **kwargs)