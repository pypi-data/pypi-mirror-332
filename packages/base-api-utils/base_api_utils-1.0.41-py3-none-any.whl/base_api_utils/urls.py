from django.urls import path

from .views import TasksResultAPIView

private_tasks_admin_patterns = ([
    path('', TasksResultAPIView.as_view({'get': 'list', 'post': 'retry'}), name='tasks_result'),
], 'private-tasks-admin-endpoints')