from django.shortcuts import render
import json
import numpy as np
import pickle
from . forms import predictForm,convertForm,iConvertForm,tohForm
from predictor.myScript import *



__model = None
__location = None
__data_columns = None
# our home page view



def index(request):
    return render(request,'index.html')     


def project(request):
    return render(request,'myform/projects.html')     

def base(request):
    if request.method == 'POST':
        form = convertForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            base = form.cleaned_data['base']
            result1 = baseConverter(value,base)
            return render(request, 'myform/result.html', {'result1':result1})       

    form = convertForm()
    return render(request,'myform/convertForm.html',{'form':form})  




def predictor(request):  
    if request.method == 'POST':
        form = predictForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            sqft = form.cleaned_data['sqft']
            bhk = form.cleaned_data['bhk']
            bath = form.cleaned_data['bath']

            result1 = predict_price(location,float(sqft),int(bath),int(bhk))
            result1 = 'Price Predicted for the given requirement is ' + str(result1) + ' Lakhs'
            return render(request, 'myform/result.html', {'result1':result1})       

    form = predictForm()
    return render(request,'myform/predictor.html',{'form':form})       


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








#Infix to Postfix converryer


def iConverter(request):
    if request.method == 'POST':
        form = iConvertForm(request.POST)
        if form.is_valid():
            exp = form.cleaned_data['expression']
            text = 'Converted Postfix Expression is :'
            result1 = infixToPostFix(exp)
            return render(request, 'myform/result.html', {'result1':result1,'text':text})       

    form = iConvertForm()
    return render(request,'myform/infix.html',{'form':form})  


def palindrome(request):
    if request.method == 'POST':
        form = iConvertForm(request.POST)
        if form.is_valid():
            exp = form.cleaned_data['expression']
            result1 = isPalindrome(exp)
            if result1 == True:
                text = 'The expression '+exp+' is palindrome'
            else:
                text = 'The expression '+exp+' is not palindrome'

            return render(request, 'myform/result.html', {'text':text})       

    form = iConvertForm()
    return render(request,'myform/palCheck.html',{'form':form})  




def tower(request):
    if request.method == 'POST':
        form = tohForm(request.POST)
        if form.is_valid():
            no_of_disk = form.cleaned_data['no_of_disk']
            from_disk = form.cleaned_data['from_disk']
            to_disk = form.cleaned_data['to_disk']
            with_disk = form.cleaned_data['with_disk'] 
            text1 = 'Steps to solve tower of Hanoi'
            result1 = simulator(int(no_of_disk),from_disk, to_disk, with_disk)
            return render(request, 'myform/result2.html', {'result1':result1,'text1':text1})       

    form = tohForm()
    return render(request,'myform/towerOfHanoi.html',{'form':form})  

