from django.shortcuts import render
import json
import numpy as np
import pickle
from . forms import predictForm


__model = None
__location = None
__data_columns = None
# our home page view

def home(request):  
    if request.method == 'POST':
        form = predictForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            sqft = form.cleaned_data['sqft']
            bhk = form.cleaned_data['bhk']
            bath = form.cleaned_data['bath']

            result1 = predict_price(location,float(sqft),int(bath),int(bhk))
            return render(request, 'result.html', {'result1':result1})       

    form = predictForm()
    return render(request,'myform/home.html',{'form':form})       


def get_locations():

    global __locations
    global __data_columns

    with open("predictor/model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk


def predict_price(location,sqft,bath,bhk): 
    get_locations()
    loadModel() 
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)



# custom method for generating predictions
def loadModel():
    global __model
    if __model is None:
        with open('predictor/model/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)


