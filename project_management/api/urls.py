from django.urls import path
from .views import (
    RegisterUserView,
    LoginUserView,
    UserDetailView,
    UpdateUserView,
    DeleteUserView,
    ProjectListCreateView,
    ProjectRetrieveUpdateDeleteView,
    ProjectMemberListCreateView, 
    ProjectMemberRetrieveUpdateDeleteView,
    TaskListCreateView,
    TaskRetrieveUpdateDeleteView,
    CommentListCreateView,
    CommentRetrieveUpdateDeleteView,
)

urlpatterns = [
    # Users
    path('users/register/', RegisterUserView.as_view(), name='register_user'),
    path('users/login/', LoginUserView.as_view(), name='login_user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/update/', UpdateUserView.as_view(), name='update_user'),
    path('users/<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),
    
    # Projects
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDeleteView.as_view(), name='project-detail'),

    # Project Members
    path('projects/<int:project_id>/members/', ProjectMemberListCreateView.as_view(), name='project-member-list-create'),
    path('members/<int:pk>/', ProjectMemberRetrieveUpdateDeleteView.as_view(), name='project-member-detail'),
    
    # Tasks
    path('projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),

    # Comments
    path('tasks/<int:task_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(), name='comment-detail'),
]
