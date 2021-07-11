from django.urls import path
# from django.contrib.auth import views as auth_views
# /from django.contrib.auth.views import LoginView, LogoutView

#
from blogdiy.views import (
    my_board_view,
    CreateProject,
    DiyProjectDetailView,
    DiyProjectListView
)

urlpatterns = [
    #
    path('board/', my_board_view, name='board_view'),
    path('create-project/', CreateProject.as_view(), name='create_project'),
    path('diy-detail/<int:pk>', DiyProjectDetailView.as_view(), name='diy_detail'),
    path('diy-list/', DiyProjectListView.as_view(), name='diy_list'),

]

