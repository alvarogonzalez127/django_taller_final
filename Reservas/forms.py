from django import forms
from Reservas.models import Reserva

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        
    fechainscrito = forms.DateField(label="Fecha de inscripción", widget=forms.SelectDateWidget)
    horainscrito = forms.TimeField(label="Hora de inscripción",widget=forms.TimeInput(attrs={'type':'time'}))