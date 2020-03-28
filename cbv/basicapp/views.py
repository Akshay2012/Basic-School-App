from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)

from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from . import models

#FUNCTION BASED VIEW
# def index(request):
#     return render(request,"index.html")


#CLASS BASED VIEW
# class CBview(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS KARKE KYA MAZA AYA")



#CLASS BASED TEMPLATE VIEW
# class Tempview(TemplateView):
#     template_name='index.html'

#     def get_context_data(self, **kwargs):

#         context=super().get_context_data(**kwargs)

#         context["cricketername"]="STEVE SMITH!"
#         return context




class Tempview(TemplateView):
    template_name="index.html"

class school_list_view(ListView):

    # LOWERS model name ie : school and creates school_list .This is returned by ListView default
    #you can change it by using below approach
    
    model=models.School
    context_object_name='schools'
    
    #Now you can reference using schools in templates
    #If you do not do this you can refer it using *school_list*



#---------STUDENT--------------------

class student_create_view(CreateView):
    model=models.Student
    fields=('name','age','school')


class student_update_view(UpdateView):
    model=models.Student
    fields=('name','age','school')

class student_delete_view(DeleteView):
    model=models.Student
    success_url=reverse_lazy("basicapp:list")


#------------SCHOOL-----------------------    

class school_details_view(DetailView):

    #This just return lowered modelname ie returns school
    context_object_name="school_detail"
    model=models.School
    template_name='basicapp/school_detail.html'


class school_create_view(CreateView):
    model=models.School
    fields=('name','principal','location')



class school_update_view(UpdateView):
    model=models.School
    fields=('name','principal')



class school_delete_view(DeleteView):
    model=models.School
    #This all are already defined class variables
    success_url=reverse_lazy("basicapp:list")
    
