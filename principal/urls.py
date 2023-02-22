from django.urls import path
from . import views

app_name = 'principal'

urlpatterns = [

  path('view_teacher',views.view_teacher_page,name='view_tr'),
  path('view_student',views.view_student_page,name='view_student'),
  path('principal_home',views.principal_home_page,name='princi_home'),
  
  path('assign_class_teacher',views.class_teacher_page,name='assign_cls_tr'),
  path('addexams',views.add_exams,name='addexams'),
]