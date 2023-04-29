from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from Auth.models import Test

from .forms import userForm


@login_required(login_url='login')
class Home:
    def home(request):
        return render(request, 'Home/home.html')

    def user(request):
        test = Test.objects.all()
        messages.success(request, '')
        messages.error(request, '')
        return render(request, 'Home/user.html', {'test': test})

    def add_form(request):
        form = userForm()
        form.fields['pid'].label = ''
        return render(request, 'Home/__user.html', {'form': form})

    # Start Add user
    def add_user(request):
        form = userForm(request.POST)
        if request.method == "POST":
            try:
                if form.is_valid():
                    name = form.cleaned_data['name']
                    email = form.cleaned_data['email']
                    password = make_password(form.cleaned_data['password'])
                    ins = Test.objects.create(
                        name=name, email=email, password=password)
                    if ins:
                        messages.success(
                            request, 'Record has been saved successfull')
                    else:
                        messages.error(
                            request, 'Something went wrong, Please try again later')
                    return redirect('user')
                else:
                    form = userForm()
            except IntegrityError:
                messages.error(request, 'Email already exists')
                form = userForm()

            class AddForm(userForm):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
        old_values = {'name': request.POST.get('name'), 'email': request.POST.get(
            'email'), 'password': request.POST.get('password')}
        form = AddForm(initial=old_values)
        form.fields['pid'].label = ''
        return render(request, 'Home/__user.html', {'form': form})
    # End Add user

    def edit_form(request, id):
        if id is not None:
            test = Test.objects.get(id=id)
            initial_values = {
                'name': test.name, 'email': test.email, 'password': test.password,  'pid': id}

            class EditForm(userForm):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.fields['password'].widget.input_type = 'hidden'
            form = EditForm(initial=initial_values)
            form.fields['pid'].label = ''
            form.fields['password'].label = ''
            return render(request, 'Home/__user.html', {'form': form, 'edit': True})

    def edit_user(request):
        if request.method == "POST":
            try:
                test = Test.objects.filter(id=request.POST.get('pid')).update(
                    name=request.POST.get('name'), email=request.POST.get('email'))
                if test:
                    messages.success(
                        request, 'Record has been updated successfully')
                    return redirect('user')
                else:
                    messages.error(request, 'Sorry, Something went wrong')
                    return HttpResponseRedirect('/edit-form/{}', format(request.POST.get('pid')))
            except IntegrityError:
                messages.error(request, 'Email already exists')
                return HttpResponseRedirect('/edit-form/'+request.POST.get('pid'))

    def delete_user(request, id):
        test = Test.objects.filter(id=id).delete()
        if test:
            messages.success(request, 'Record has been deleted successfully')
        else:
            messages.error(
                request, 'Something went wrong, Please try again later')
        return redirect('user')
