from django.urls import path, reverse_lazy
from . import views
from .views import send_json

app_name='courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='all'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/create',
        views.CourseCreateView.as_view(success_url=reverse_lazy('courses:all')), name='course_create'),
    path('course/<int:pk>/update',
        views.CourseUpdateView.as_view(success_url=reverse_lazy('courses:all')), name='course_update'),
    path('course/<int:pk>/delete',
        views.CourseDeleteView.as_view(success_url=reverse_lazy('courses:all')), name='course_delete'),

    path('sendjson/', send_json, name='send_json'),
]
# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined