from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import DiyProject
from blogdiy.forms import AddDiyProject

def my_board_view(request, pk):

    context={

    }


    return render(request, 'board.html', context)




class CreateProject(CreateView):
    model = DiyProject
    template_name = 'crud/create.html'
    form_class = AddDiyProject


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user.profile()
        self.completed=False
        self.object.save()

        return super().form_valid(form)




class DiyProjectListView(ListView):
    model=DiyProject
    template_name = 'diy_list.html'
    context_object_name = 'diy_list'

    def get_queryset(self):
        if self.request.user.is_bloger:
            return self.request.user.profile().diyproject_set


class DiyProjectDetailView(DetailView):
    model = DiyProject
    template_name = 'detail_diy.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(DiyProject, pk=pk)