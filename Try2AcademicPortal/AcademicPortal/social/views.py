from django.shortcuts import render,HttpResponse,redirect
from .forms import DocumentUploadForm
from .models import document_upload
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.method=='POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            branch = form.cleaned_data['branch']
            semester = form.cleaned_data['semester']
            course = form.cleaned_data['course']
            file_name = form.cleaned_data['file_name']
            my_file = form.cleaned_data['my_file']
            document_upload(branch=branch,semester=semester,course=course,file_name=file_name,my_file=my_file).save()
            return redirect('social:upload')
        else:
            return HttpResponse('ERROR')

    context={'form': DocumentUploadForm()}
    return render(request,'social/index.html',context)


def show_file(request):
	all_data=document_upload.objects.all()

	context={
		'data':all_data
	}

	return render(request,'social/views.html',context)

def delete_book(request,pk):
	if request.method=='POST':
		book=document_upload.objects.get(pk=pk)
		book.delete()
	return redirect('social:upload')