from django.shortcuts import render , redirect
from django.views.generic import  DetailView,CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import FormularioComentario
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

################################################################ 

def inicio(request):
    #pagina de inicio
    return render(request, 'CursosApp/index.html')

def cursos(request): 
    #pagina de curso
    return render(request, 'CursosApp/cursos.html')

def estudiantes(request):
    #pagina de estudiantes
    return render(request, 'CursosApp/estudiantes.html')

def nosotros(request):
    #pagina sobre nosotros
    return render ( request , "CursosApp/nosotros.html" )

###################################################################

def imprimir_cursos(request):
    #pagina para imprimir los cursos
    cursos = Curso.objects.all()

    context = {
        'cursos': cursos
    }
    return render(request, r"CursosApp\cursos.html",context)

class CursoDetalle(DetailView):
    #pagina para los detalles de los cursos
    model = Curso
    template_name = 'CursosApp/curso_detalle.html'

class CursoCreateView(CreateView):
      model = Curso
      template_name = "CursosApp/cursoFormulario.html"
      success_url = reverse_lazy("Nuevo")
      fields= ["nombre","tutor","cupo","fecha","descripcion"]

class CursoUpdateView(UpdateView):
      model = Curso
      template_name = "CursosApp/cursoEdit.html"
      success_url = reverse_lazy("Editar")
      fields= ["nombre","tutor"]


############################################
class Comentarios(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'CursosApp/comentario.html'
    success_url = 'CursosApp/base.html'

    def form_valid(self, form):
        form.instance.comentario = Curso.objects.get(pk=self.kwargs['curso_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mi_formulario'] = context['form']  # Renombrar el formulario para que coincida con tu plantilla
        return context


