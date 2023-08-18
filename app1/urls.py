from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from app1 import views
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('addSchool',views.addSchool.as_view(),name='create__school_data'),
    path('addTeacher', views.addTeacher.as_view(), name='create_teacher_data'),
    path('addStudent', views.addStudent.as_view(), name='create_student_data'),
    path('addStaff', views.addStaff.as_view(), name='create_staff_data'),
    path('viewSchool', views.viewSchool.as_view(), name='view_school'),
    path('viewTeacher', views.viewTecaher.as_view(), name='view_teacher'),
    path('viewStudent', views.viewStudent.as_view(), name='view_student'),
    path('viewStaff', views.viewStaff.as_view(), name='view_staff'),
    path('deleteSchool', views.deleteSchool.as_view(), name='del_school'),
    path('deleteStudent', views.deleteStudent.as_view(), name='del_student'),
    path('deleteTeacher', views.deleteTeacher.as_view(), name='del_teacher'),
    path('deleteStaff', views.deleteStaff.as_view(), name='del_staff'),
    path('updateSchool', views.updateSchool.as_view(), name='update_school'),
    path('updateTeacher', views.updateTeacher.as_view(), name='update_teacher')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)