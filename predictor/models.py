from django.db import models
import json, os

# Create your models here.
class price_predictor(models.Model):
    with open('predictor/model/columns.json') as f:
        countries_json = json.load(f)
        #print(countries_json)
        choice = []
        for i in countries_json['data_columns'][3:]:
            choice.append([i,i])
    location_choice = choice
    Bath_choice = (
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10')   
    )

    BHK_choice = (
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10')
    )

    location = models.CharField(max_length=50,choices=choice)
    square_fit = models.IntegerField()
    bath = models.CharField(max_length =15,choices=Bath_choice)
    bhk = models.CharField(max_length =15,choices=BHK_choice)


    def __str__(self):
        return self.price
