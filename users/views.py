from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Useregister as u  , UserUpdateForm as uu, ProfileUpdateForm as pu
from django.contrib.auth.decorators import login_required
def reg (request) :
	if request.method == 'POST':
		form =u(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Acccount cereated for {username}! kindly login')
			return redirect('login')
	else :
		form = u()
	return render( request,'users/register.html', {'form':form} )

@login_required
def profile (request) :
	if request.method == 'POST':
		u_form =uu(request.POST,instance= request.user)
		p_form= pu(request.POST,request.FILES,instance= request.user.profile)
	
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been updated !')
			return redirect('profile')
	else :
		u_form =uu(instance= request.user)
		p_form= pu(instance= request.user.profile)
		

		context ={
		'u_form': u_form,
		'p_form': p_form
			 }

	return render(request,'users/profile.html',context)