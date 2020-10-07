
from django.urls import path,include
from predictor import views
from rest_framework import routers


'''
router = routers.DefaultRouter()
router.register('predictor',views.predictView)
'''

urlpatterns = [
    path('form/', views.cxcontact,name='cxform'),
    path('api/',include(router.urls)),
    path('predict/',views.price_predict),
    

]
