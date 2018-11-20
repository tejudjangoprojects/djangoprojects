from django.shortcuts import render
from testapp.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')
def hydjobs1(request):
    jobs_list=hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    paginator=Paginator(jobs_list,3)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/hydjobs.html',context=my_dict)
