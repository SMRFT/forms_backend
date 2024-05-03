from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .forms import MonthlyDataForm
from .models import SICU
from django.views.decorators.csrf import csrf_exempt

class MonthlyView(APIView):
    def post(self, request):
        serializer = MonthlyDataForm(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            employee.save()
            return Response({'message': 'Submitted'})
        else:
            return Response(serializer.errors, status=400)

from django.core import serializers

@csrf_exempt
def get_monthly_data(request):
    monthly_data = SICU.objects.all()
    # Serialize queryset to JSON
    data = serializers.serialize('json', monthly_data)
    # Return JSON response
    return JsonResponse(data, safe=False)






    



    


from django.shortcuts import render
from django.http import JsonResponse
from .forms import OTDataForm
from .models import OTData
@csrf_exempt
def post_ot_data(request):
    if request.method == 'POST':
        form = OTDataForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'ICU data saved successfully'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def get_ot_data(request):
    if request.method == 'GET':
        icu_data = OTData.objects.all().values()
        return JsonResponse(list(icu_data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    


from .forms import RecoveryWardForm
from .models import RecoveryWard

def get_recovery_ward_data(request):
    if request.method == 'GET':
        recovery_ward_data = RecoveryWard.objects.all().values()
        return JsonResponse(list(recovery_ward_data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)




from .forms import NICUForm
from .models import NICU



def get_nicu_data(request):
    if request.method == 'GET':
        nicu_data = NICU.objects.all().values()
        return JsonResponse(list(nicu_data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)



from .forms import ChemoWardForm
from .models import ChemoWard


from rest_framework.decorators import api_view

from rest_framework import status

@api_view(['POST'])
@csrf_exempt
def post_chemo_ward_data(request):
    if request.method == 'POST':
        serializer = ChemoWardForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def get_chemo_ward_data(request):
    if request.method == 'GET':
        chemo_ward_data = ChemoWard.objects.all().values()
        return JsonResponse(list(chemo_ward_data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    


from .forms import PhysiotherapyDialysisForm
from .models import PhysiotherapyDialysis


# @csrf_exempt
def get_physiotherapy_dialysis_data(request):
    if request.method == 'GET':
        data = PhysiotherapyDialysis.objects.all().values()
        return JsonResponse(list(data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    


from .forms import DiagnosticCenterForm,SicuDataForm
from .models import DiagnosticCenter


from rest_framework.decorators import api_view

from rest_framework import status

@api_view(['POST'])
@csrf_exempt
def post_diagnostic_center_data(request):
    if request.method == 'POST':
        serializer = DiagnosticCenterForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def get_diagnostic_center_data(request):
    if request.method == 'GET':
        data = DiagnosticCenter.objects.all().values()
        return JsonResponse(list(data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    


from .forms import EmergencyRoomForm,Labwardform,CTwardform,MRIwardform,Xraywardform,FrontofficeDataForm,MRDDataForm,firstsuitForm,secondsuitForm,firstfloorForm,secondfloorForm,thirdfloorForm,MICUForm,OTDataForm
from .models import EmergencyRoom,Lab,Frontoffice,MRD,firstsuit,Secondsuit,Firstfloor,Secondfloor,Thirdfloor,MICU



def get_emergency_room_data(request):
    if request.method == 'GET':
        data = EmergencyRoom.objects.all().values()
        return JsonResponse(list(data), safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    
from rest_framework.decorators import api_view

from rest_framework import status

@api_view(['POST'])
@csrf_exempt
def submit_sicu_data(request):
    if request.method == 'POST':
        serializer = SicuDataForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@csrf_exempt
def submit_lab_data(request):
    if request.method == 'POST':
        serializer = Labwardform(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@csrf_exempt
def submit_CT_data(request):
    if request.method == 'POST':
        serializer = CTwardform(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@csrf_exempt
def submit_MRI_data(request):
    if request.method == 'POST':
        serializer = MRIwardform(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@csrf_exempt
def submit_Xray_data(request):
    if request.method == 'POST':
        serializer = Xraywardform(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@csrf_exempt
def post_nicu_data(request):
    if request.method == 'POST':
        serializer = NICUForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
@csrf_exempt
def post_physiotherapy_dialysis_data(request):
    if request.method == 'POST':
        serializer = PhysiotherapyDialysisForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@csrf_exempt
def post_recovery_ward_data(request):
    if request.method == 'POST':
        serializer = RecoveryWardForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
@csrf_exempt
def post_frontoffice_data(request):
    if request.method == 'POST':
        serializer = FrontofficeDataForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def post_MRD_data(request):
    if request.method == 'POST':
        serializer =MRDDataForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def post_firstsuit_data(request):
    if request.method == 'POST':
        serializer =firstsuitForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@csrf_exempt
def post_secondsuit_data(request):
    if request.method == 'POST':
        serializer =secondsuitForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@csrf_exempt
def post_emergency_room_data(request):
    if request.method == 'POST':
        serializer =EmergencyRoomForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def post_firstfloor_data(request):
    if request.method == 'POST':
        serializer =firstfloorForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@csrf_exempt
def post_secondfloor_data(request):
    if request.method == 'POST':
        serializer =secondfloorForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@csrf_exempt
def post_thirdfloor_data(request):
    if request.method == 'POST':
        serializer =thirdfloorForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@csrf_exempt
def post_MICU_data(request):
    if request.method == 'POST':
        serializer =MICUForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@csrf_exempt
def post_OT_data(request):
    if request.method == 'POST':
        serializer =OTDataForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)