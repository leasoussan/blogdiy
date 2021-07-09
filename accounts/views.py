from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .forms import BlogerProfileCreateForm, MyUserCreationForm, BusinessProfileCreateForm, UserForm
from accounts.models import Bloger, Business

# Create your views here.


def homepage_view(request):
    return render(request, 'homepage.html')


class Register(View):
    def get(self, request):
        form = MyUserCreationForm()
        context = {
            "form": form,
        }
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            usertype = form.cleaned_data['usertype']

            setattr(user, usertype, True)

            user.save()
            user = authenticate(username=username, password=password, usertype=usertype)
            login(request, user)
            # send_welcome_signup(user)

            reverse('create_profile'), form.cleaned_data['usertype']
            # return redirect('homepage')

        return render(request, 'registration/register.html', {"form": form})


# --------------------------------------------------

def get_user_profile_form(request, edit=False):
    """ This function allows is to check which profile is requested,
    and to know what page/authorization to direct it to"""
    user = request.user

    if edit:
        instance = user.profile()
    else:
        instance = None

    data = request.POST or None

    if user.is_bloger:

        profile_form = BlogerProfileCreateForm(data, instance=instance)


    elif user.is_business:
        profile_form = BusinessProfileCreateForm(data, instance=instance)

    return profile_form


# ----------------------

class CreateProfile(View):
    """ Any one who creats an accounts will be directed to create a Profile,
    and wont be able to do any actions unless this is done"""

    def get(self, request):

        user_form = UserForm(instance=request.user)
        profile_form = get_user_profile_form(request)
        user = request.user

        return render(request, 'accounts/profile/edit_profile.html', {'profile_form': profile_form,
                                                                      'user_form': user_form, }
                      )

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = get_user_profile_form(request)
        user = request.user

        if profile_form.is_valid() and user_form.is_valid():

            user_form.save()
            object = profile_form.save(commit=False)

            if request.user.is_bloger:
                object.user = Bloger.objects.get_or_create(user=request.user)
                object.save()

            profile.save()
            return redirect('board_view')

            elif request.user.is_business:
                object.user = Business.objects.get_or_create(user=request.user)
                object.save()
            return redirect('dashboard')

        # messages.add_message(request, messages.ERROR, 'You have an error in your form')

        return render(request, 'accounts/profile/edit_profile.html',
                      {'user_form': user_form, 'form': profile_form, 'institution_form': institution_form})
