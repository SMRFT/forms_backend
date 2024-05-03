# forms.py
from django import forms
from .models import SICU,OTData

class MonthlyDataForm(forms.ModelForm):
    class Meta:
        model = SICU
        fields = '__all__'



from django import forms

class OTDataForm(forms.ModelForm):
    class Meta:
        model = OTData
        fields = '__all__'

from django import forms
from .models import RecoveryWard

class RecoveryWardForm(forms.ModelForm):
    class Meta:
        model = RecoveryWard
        fields = '__all__'


from .models import NICU

class NICUForm(forms.ModelForm):
    class Meta:
        model = NICU
        fields = '__all__'

from .models import ChemoWard,Lab,CT,MRI,Xray

class ChemoWardForm(forms.ModelForm):
    class Meta:
        model = ChemoWard
        fields = '__all__'


class Labwardform(forms.ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'

class CTwardform(forms.ModelForm):
    class Meta:
        model = CT
        fields = '__all__'

class MRIwardform(forms.ModelForm):
    class Meta:
        model = MRI
        fields = '__all__'

class Xraywardform(forms.ModelForm):
    class Meta:
        model = Xray
        fields = '__all__'
from .models import PhysiotherapyDialysis

class PhysiotherapyDialysisForm(forms.ModelForm):
    class Meta:
        model = PhysiotherapyDialysis
        fields = '__all__'

from .models import DiagnosticCenter

class DiagnosticCenterForm(forms.ModelForm):
    class Meta:
        model = DiagnosticCenter
        fields = '__all__'


from .models import EmergencyRoom,firstsuit,Secondsuit,Firstfloor,Secondfloor,Thirdfloor,MICU

class EmergencyRoomForm(forms.ModelForm):
    class Meta:
        model = EmergencyRoom
        fields = '__all__'

class firstsuitForm(forms.ModelForm):
    class Meta:
        model = firstsuit
        fields = '__all__'
class secondsuitForm(forms.ModelForm):
    class Meta:
        model = Secondsuit
        fields = '__all__'
class firstfloorForm(forms.ModelForm):
    class Meta:
        model = Firstfloor
        fields = '__all__'

class secondfloorForm(forms.ModelForm):
    class Meta:
        model = Secondfloor
        fields = '__all__'

class thirdfloorForm(forms.ModelForm):
    class Meta:
        model = Thirdfloor
        fields = '__all__'
class MICUForm(forms.ModelForm):
    class Meta:
        model = MICU
        fields = '__all__'

from .models import SICU,Frontoffice,MRD
from django import forms

class SicuDataForm(forms.ModelForm):
    class Meta:
        model = SICU
        fields = '__all__'

class FrontofficeDataForm(forms.ModelForm):
    class Meta:
        model = Frontoffice
        fields = '__all__'


class MRDDataForm(forms.ModelForm):
    class Meta:
        model = MRD
        fields = '__all__'

# class MRDDataForm(forms.ModelForm):
#     class Meta:
#         model = MRD
#         fields = '__all__'