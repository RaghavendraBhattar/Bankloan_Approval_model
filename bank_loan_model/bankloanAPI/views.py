from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import approvals
from .forms import ApprovalForm
from .serializers import approvalSerializer
import pickle
import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd


class ApprovalView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalSerializer

# def myform(request):
#     if request.method == "post":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             myform = form.save(commit=False)
#     else:
#         form = MyForm()

# @api_view(["POST"])
# def approvereject(request):
#     try:
#         mdl=
#         mydata=request.data
#         unit=np.array(list(mydata.values()))
#         unit = unit.reshape(-1,1)
#         scalers = 
#         X=scalers.transform(unit)
#         y_pred=mdl.predict(X)
#         y_pred=(y_pred>0.58)
#         newdf=pd.DataFrame(y_pred, columns=['Status'])
#         newdf=newdf.replace({True:'Approved', False:'Rejected'})
#         return JsonResponse('Your Status is {}'.format(newdf), safe=False)

#     except ValueError as e:
#         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def cxcontact(request):
    if request.method == 'POST':
        form = ApprovalForm() 
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname=form.cleaned_data['firstname']
            dependants=form.cleaned_data['firstname']
            applicantincome=form.cleaned_data['firstname']
            coapplicatincome=form.cleaned_data['firstname']
            loanamt=form.cleaned_data['firstname']
            loanterm=form.cleaned_data['firstname']
            credithistory=form.cleaned_data['firstname']
            gender=form.cleaned_data['firstname']
            married=form.cleaned_data['firstname']
            graduatededucation=form.cleaned_data['firstname']
            selfemployed=form.cleaned_data['firstname']
            area=form.cleaned_data['firstname']
    form = ApprovalForm()
    vpath = '/home/raghubhattar/Desktop/Bankloan_Approval_model/bank_loan_model/bankloanAPI/templates/confirm.html'
    return render(request, vpath, {'form':form})