from django import偏forms
from .models import Juego, Reseña

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        return precio

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        # Excluimos usuario_username porque lo llenaremos en la vista automáticamente
        exclude = ['usuario_username']

    def clean_puntuacion(self):
        puntuacion = self.cleaned_data.get('puntuacion')
        if puntuacion < 1 or puntuacion > 10:
            raise forms.ValidationError("La puntuación debe estar entre 1 y 10.")
        return puntuacion