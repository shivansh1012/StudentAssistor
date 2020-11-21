from django.shortcuts import render,HttpResponse,redirect
from .forms import MyfileUploadForm
from .models import file_upload
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
	if request.method=='POST':
		form= MyfileUploadForm(request.POST, request.FILES)	
		if request.POST and form.is_valid():
			file_name=form.cleaned_data['file_name']
			my_file=form.cleaned_data['files_data']	
			file_upload.objects.get_or_create(
	            username=request.user.username,
				file_name= file_name,
				my_file= my_file,
	        )

			return redirect('fileuploadapp:upload')
		else:
			return HttpResponse('ERROR')
	else:

		context={
			'form':MyfileUploadForm()
		}
		return render(request,'fileuploadapp/index.html',context)
@login_required(login_url='login')
def show_file(request):
	all_data=file_upload.objects.filter(username=request.user.username)

	context={
		'data':all_data
	}

	return render(request,'fileuploadapp/views.html',context)
@login_required(login_url='login')
def delete_book(request,pk):
	if request.method=='POST':
		book=file_upload.objects.get(pk=pk)
		book.delete()
	return redirect('fileuploadapp:upload')