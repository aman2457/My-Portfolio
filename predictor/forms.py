from django import forms
import json, os
from . models import price_predictor

class predictForm(forms.Form):
    Bath_choice = (
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10')   
    )

    BHK_choice = (
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10')
    )

    with open('predictor/model/columns.json') as f:
        countries_json = json.load(f)
        #print(countries_json)
        choice = []
        for i in countries_json['data_columns'][3:]:
            choice.append([i,i])
    
    
    location = forms.ChoiceField(choices=choice)
    
    sqft = forms.IntegerField()
    
    bath = forms.ChoiceField(choices=BHK_choice)
    
    bhk = forms.ChoiceField(choices=Bath_choice)
