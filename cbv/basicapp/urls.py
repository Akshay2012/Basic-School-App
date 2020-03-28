from django.urls import path
from . import views

app_name="basicapp"

urlpatterns=[
    path('',views.Tempview.as_view(),name='home'),
    
    # path('schooldetails/',views.school_details_view.as_view()),
    
    path('base/',views.school_list_view.as_view(),name="list"),
    
    path('base/<int:pk>/',views.school_details_view.as_view(),name='detail'),

    path('base/create/',views.school_create_view.as_view(),name='create'),
    
    path('base/update/<int:pk>',views.school_update_view.as_view(),name='update'),

    path('base/delete/<int:pk>',views.school_delete_view.as_view(),name="delete"),


    #---------STUDENT URLS-----------------

    path('base/create_student/',views.student_create_view.as_view(),name="create_student"),

    path('base/update_student/<int:pk>',views.student_update_view.as_view(),name="update_student"),

    path('base/delete_student/<int:pk>',views.student_delete_view.as_view(),name="delete_student"),



    
    

]

