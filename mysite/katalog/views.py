from django.shortcuts import render,redirect
from .forms import BukuForm
from django.contrib import messages
from .models import Buku
# Create your views here.

def index(request):
    buku=Buku.objects.all()
    context={
        'title':'katalog', 
        'buku':buku   
    }
    return render(request,'katalog/index.html',context)

def create(request):
    if request.method == 'POST':
        buku_form = BukuForm(request.POST, request.FILES)  
        if buku_form.is_valid():
            buku_form.save()  
            messages.success(request,'Data Berhasil Ditambahkan')
            return redirect('katalog:create')  
    else:
        buku_form = BukuForm() 

    context = {
        'title': 'add buku',
        'f_buku': buku_form,
    }
    return render(request, 'katalog/create.html', context)

def delete(request,id):
    Buku.objects.filter(id=id).delete()
    messages.error(request, "Data berhasil dihapus.")
    return redirect ('katalog:index')

def update(request,id):
     obj_buku=Buku.objects.get(id=id)

     if request.method == 'POST':
      buku_form=BukuForm(request.POST or None, request.FILES or None,instance=obj_buku)
      if buku_form.is_valid():
         buku_form.save()
         messages.success(request,'Data Berhasil Di Update')
         return redirect('katalog:index')
      
     else:
        buku_form= BukuForm(instance=obj_buku)

     context = {
        'title': 'Edit Buku',
        'f_buku': buku_form,
    }
     
     return render(request,'katalog/update.html',context)

def detail(request,id):
    detail_buku=Buku.objects.get(id=id)
    context = {
        'title': 'detail Buku',
        'detail_buku': detail_buku,
    }
    return render(request,'katalog/detail.html',context)