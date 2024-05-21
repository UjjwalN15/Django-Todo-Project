from django.shortcuts import render, redirect
from starttodo.models import Todo_Table
# Create your views here.
def home (request):
    all_data = Todo_Table.objects.all()
    data = {"datas" : all_data} 
    return render(request,'index.html', context = data )

def Create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo_Table.objects.create(Name = name, Description = description, Status = status)
        return redirect('home')
    return render(request,'create.html')