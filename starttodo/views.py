from django.shortcuts import render, redirect
from starttodo.models import Todo_Table
# Create your views here.
def home (request):
    all_data = Todo_Table.objects.all()
    data = {"datas" : all_data} 
    return render(request,'index.html', context = data )
def Admin(request):
    return render(request, 'admin', context={"current_url": "admin"})

def Create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo_Table.objects.create(Name = name, Description = description, Status = status)
        return redirect('home')
    else:
        return render(request,'create.html', context={"current_url": "create"})
    
def Edit(request,pk):
    todo = Todo_Table.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        #Line number 20 ko todo object of Todo_Table
        todo.Name = name
        todo.Description = description
        todo.Status = status
        todo.save()
        return redirect('home')
    edit_todo = {'todo' : todo}
    return render(request,'edit.html', context=edit_todo)

def Delete(request,pk):
    todo = Todo_Table.objects.get(id=pk)
    todo.delete()
    return redirect('home')

def Delete_all(request):
    todo = Todo_Table.objects.all()
    todo.delete()
    return redirect('home')
    