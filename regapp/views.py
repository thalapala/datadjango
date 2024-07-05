import os
from django.shortcuts import render, redirect # type: ignore
#from django.http import HttpResponse # type: ignore
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import PricePredictionForm
import joblib
import numpy as np
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'regapp/home.html')

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'regapp/register.html', {'form': form})




def page(request):
    #print("I am in predict page")
    if request.method == 'POST':
        form = PricePredictionForm(request.POST)
        if form.is_valid():
            # Load the trained linear regression model
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'linear_regression_model.pkl')
            model = joblib.load(model_path)

            # Extract input data from the form
            new_data = np.array(list(form.cleaned_data.values())).reshape(1, -1)

            # Perform prediction
            predicted_price = model.predict(new_data)[0]
            print('Predict price',predicted_price) 
            # Prepare the response
            context = {
                'form': form,
                'predicted_price': round(predicted_price, 2),
            }
            return render(request, 'regapp/page.html', context)
    else:
        form = PricePredictionForm()

    context = {'form': form}
    return render(request, 'regapp/page.html', context)

@login_required()
def profile(request):
    return render(request, 'regapp/profile.html')

def logout(request):
    logout(request)
    return render(request, 'regapp/logout.html')
