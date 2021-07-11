from django.urls import path
from .views import (
    # my_inbox,
    DiscussionCreateView,
    CommentCreateView,

)


urlpatterns = [
    path('discussion-add/', DiscussionCreateView.as_view(), name= 'discussion_add'),

    path('comment-add/',CommentCreateView.as_view(), name = 'comment_add'),

    #   path('',.as_view(), name = '')

]