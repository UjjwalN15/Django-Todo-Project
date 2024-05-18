from django.shortcuts import render
from starttodo.models import Todo_Table
# Create your views here.
def home (request):
    all_data = Todo_Table.objects.all()
    data = {"datas" : all_data} 
    return render(request,'index.html', context = data )