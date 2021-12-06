from django.urls import path
from .views import home,student_list_view,student_add_view,student_detail_view,student_update_view,student_delete_view

urlpatterns = [
    path('', home, name="home"),
    path('list/', student_list_view, name="list"),
    path('add/', student_add_view, name="add"),
    path('<int:id>/detail', student_detail_view, name="detail"),
    path('<int:id>/update', student_update_view, name="update"),
    path('<int:id>/delete', student_delete_view, name="delete"),
    
] 