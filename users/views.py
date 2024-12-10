from django.shortcuts import render, get_object_or_404, redirect
from .models import User

# Create (and Read All)
def user_list(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        User.objects.create(name=name, email=email, age=age)
        return redirect('user_list')

    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# Update
def user_update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.age = request.POST['age']
        user.save()
        return redirect('user_list')
    return render(request, 'users/user_update.html', {'user': user})

# Delete
def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('user_list')
