from django.contrib import admin
from django.urls import path
from apicrud.views import *
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('apipage/',api_page,name='api_page'),
    path('apisingle/<int:id>/',api_single,name='api_single'),

    path('createdata/',create_data,name='createdata'),
    path('delete/<int:id>/',deletee,name='deletee'),

    # path('updatesingle/<int:id>/',update_single,name='updatesingle'),
    path('updateall/<int:id>/',update_all,name='updateall'),

    path('studentapi/<id>',studentapi.as_view(),name='studentapi'),


    #token authentication
    path('api-token-auth/', views.obtain_auth_token),  #through post method
    path('registertoken/',Registeruser.as_view()),       #manually generate the token


    path('verifytoken/',studentapitokenchecking.as_view()),       #manually check token to verify user


    #always use jwt token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #JWT TOKEN
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #JWT TOKEN



    path('api/excel/',excelimportexport.as_view(), name='excel'), #excel file



]