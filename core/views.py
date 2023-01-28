from django.shortcuts import render, redirect

from core.models import Contact


# Create your views here.
# def index(request):
#     contacts = Contact.objects.all()
#     context = {'contact': contacts}
#     return render(request, 'home.html', context)
#
#
# def addcontact(request):
#     if request.method == 'POST':
#         new_contact = Contact(
#             full_name=request.POST['fullname'],
#             relationship=request.POST['relationship'],
#             email=request.POST['email'],
#             phone_number=request.POST['phonenumber'],
#             address=request.POST['address']
#         )
#         new_contact.save()
#         return redirect('index')
#     return render(request, 'new.html')

def index(request):
    contacts = Contact.objects.all()
    search_in = request.GET.get('search-area')
    if search_in:
        contacts = Contact.objects.filter(full_name__icontains = search_in)
    else:
        contacts = Contact.objects.all()
        search_in = ''
    context = {'contacts':contacts,'search_in':search_in}
    return render(request, 'home.html',context)

def addcontact(request):
    if request.method == 'POST':

        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phonenumber'],
            address=request.POST['address'],
            )
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')
def contactprofile(request,pk):
    profile = Contact.objects.get(id=pk)
    context = {'contact':profile}
    return render(request,'contact-profile.html',context)

def edit_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phonenumber']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/contactprofile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def delete_contact(request,pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    context ={'contact':contact}
    return render(request,'delete.html',context)