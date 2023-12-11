from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "post":
            form = UserCreationForm()
            return render(request, 'users/register.html', {'form':form})
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data.get('username')
        #     messages.success(request, f'Account created for {username}!')
        #     return redirect('visitors-home')

    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

def login(request):
    return render(request, 'users/login.html') 


# def (request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("main:homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="main/register.html", context={"register_form":form})
