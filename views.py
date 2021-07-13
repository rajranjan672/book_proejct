from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import BookForm

# Create your views here.
def home(request):
    form =BookForm
    if request.method =="POST":
        bkForm = BookForm(request.POST)
        if bkForm.is_valid():
            bkForm.save()
            messages.success(request,'Data has been added')
            return redirect('/')
    return render(request, 'book.html',{'form':form})