from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length = 40)
    tutor = forms.CharField(max_length = 40)
    cupo = forms.IntegerField()
    fecha = forms.DateField()
    imagen = forms.ImageField(upload_to = "cursos",null = True)
    descripcion = forms.CharField(max_length = 400, null = True)

    def _str__(self):
        return self.nombre

