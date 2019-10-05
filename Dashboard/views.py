from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import *
from .forms import *

# Create your views here.

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

#####################################################

def is_customer(user):
    return user.groups.filter(name='customer').exists() or user.is_superuser

def is_company(user):
    return user.groups.filter(name='company').exists() or user.is_superuser 

#####################################################

class customer_register(generic.View):
    form_class = CustomerForm
    template_name = r'Dashboard/Customer_signup.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            customer = Customer()
            customer.user = user
            customer.save()

            group = Group(name = 'customer')
            group.save()
            user.groups.add(group)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Dashboard:a')

        return render(request, self.template_name, {'form' : form})

class company_register(generic.View):
    form_class = CompanyForm
    template_name = r'Dashboard/Company_signup.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            company = Company()
            company.user = user
            company.save()

            group = Group(name = 'company')
            group.save()
            user.groups.add(group)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Dashboard:a')

        return render(request, self.template_name, {'form' : form})

######################################################

decorators = [
    login_required,
    user_passes_test(is_company),
]

@method_decorator(decorators, name='dispatch')  
class ProductCreate(CreateView):
    model = Product
    fields = ['name','image','desc','price']

    def form_valid(self, form):
        self.object.company = self.request.user.company
        return super(ProductCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
@user_passes_test(is_company)   
class ProductUpdate(UpdateView):
    model = Product
    fields = ['name','image','desc','price']

@method_decorator(login_required, name='dispatch')
@user_passes_test(is_company)    
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('Dashboard:a')

######################################################
def a(request):
    if is_customer(request.user):
        return render(request, r'Dashboard/a.html', {'type' : 'customer'})
    elif is_company(request.user):
        return render(request, r'Dashboard/a.html', {'type' : 'company'})
    else:
        return render(request, r'Dashboard/a.html', {'type' : 'None'})