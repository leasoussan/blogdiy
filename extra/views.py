from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy


from .models import Comment, Discussion
from extra.forms import AddDiscussionForm, AddCommentForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView, RedirectView
)

# Create your views here.


class GenericCustomRedirectView(RedirectView):

    pattern_name = 'comment_add'
    form_class = None

    def save_form(self, form):
        return form.save()

    def can_save(self,form):
        return True


    def get_redirect_url(self, *args, **kwargs):
        form = self.form_class(self.request.POST, self.request.FILES or None)
        fail = True
        if form.is_valid():
            if self.can_save(form):
                self.object = self.save_form(form)
                fail=False
                messages.success(self.request,  f'Your {self.object._meta.model.__name__} was added succesfuly')

        if fail:
            messages.warning(self.request, f'Your {self.object._meta.model.__name__} wasn\'t saved')

        return self.request.GET.get('next')








class DiscussionCreateView(GenericCustomRedirectView):

    pattern_name = 'discussion_add'
    form_class = AddDiscussionForm


# ________________________________________________________________________________________Comment CreateView>>>>>>>>>>


class CommentCreateView(GenericCustomRedirectView):

    pattern_name = 'comment_add'
    form_class= AddCommentForm