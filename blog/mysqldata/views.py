from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
#from django.http import Http404
from django.template import loader
from .models import userdata
from django.views.generic import View
from .forms import userform

# Create your views here.
def display_usr(request):
	all_users = userdata.objects.all()
	# template = loader.get_template('mysqldata/usr_list.html')
	# return HttpResponse(template.render({'all_users':all_users}, request))
	return render(request, 'mysqldata/usr_list.html', {'all_users':all_users})


def detail_usr(request, user_id):
	# try:
	# 	user = userdata.objects.get(pk = user_id)
	# except userdata.DoesNotExist:
	# 	raise Http404("No Such Blog Exist")
	user = get_object_or_404(userdata, pk = user_id)
	return render(request, 'mysqldata/description.html', {'user':user})

def newuser(request):

	if request.method == 'POST':
		form = userform(request.POST)

		if form.is_valid():
			name = request.POST.get('name', '')
			blog_title = request.POST.get('blog_title', '')
			blog_description = request.POST.get('blog_description', '')

		user_obj_temp_save = userdata(name=name, blog_title=blog_title, blog_description=blog_description)
		user_obj_temp_save.save()
		return render(request, 'mysqldata/input.html', {'user_obj_temp_save':user_obj_temp_save, 'is_registered':True})

	else:
		form = userform()
		return render(request, 'mysqldata/input.html', {'form':form})






