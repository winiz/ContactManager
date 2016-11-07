from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect 


from .forms import ContactForm
from .models import Contact 


def index(request):
	contact_list = Contact.objects.all()
	context = {
		'contact_list':contact_list,
	}
	return render(request, 'mainapp/index.html', context)

def detail(request, contact_id):
	try:
		contact = Contact.objects.get(pk = contact_id)
	except Contact.DoesNotExist:
		raise Http404("uh on... thie contact DNE")
	return render(request, 'mainapp/detail.html', {'contact': contact})

def post_contact(request):
	form = ContactForm(request.POST)

	if form.is_valid():
		form.save(commit = True)

	return HttpResponseRedirect('/mainapp')

def new(request):
	form = ContactForm()
	context = {
		'form':form,
	}
	return render(request, 'mainapp/new.html',context)

def edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == "POST": 
        form = ContactForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mainapp')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'mainapp/edit.html', {'form': form})









