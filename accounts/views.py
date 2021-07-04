from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .forms import BlogerProfileCreationForm, MyUserCreationForm


# Create your views here.





def homepage_view(request):
    return render(request, 'homepage.html' )





class Register(View):
    def get(self, request):
        form = MyUserCreationForm()
        #
        # if 'key' in  request.GET:
        #     form = MySpeakerCreationForm(initial={'usertype': 'is_speaker'})

        context = {
         "form": form
        }
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            usertype=form.cleaned_data['usertype']


            setattr(user, usertype, True)

            # if user.is_speaker:
            #     key = request.GET.get('key')
            #     if SpeakerInvite.objects.filter(key=key, used=False).exists():
            #         invite = SpeakerInvite.objects.get(key=key)
            #         invite.used = True
            #         user.save()
            #         invite.joined_user = user
            #         invite.save()

            user.save()
            user = authenticate(username= username, password = password, usertype =usertype)
            login(request, user)
            # send_welcome_signup(user)

            # reverse('create_profile'), form.cleaned_data['usertype']
            return redirect('globaletemplates/homepage')

        return render(request, 'registration/register.html', {"form":form})


