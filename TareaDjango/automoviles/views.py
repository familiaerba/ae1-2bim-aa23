from django.shortcuts import render

# Create your views here.
from automoviles.models import Automovil

def listarInformacion(request):

   mis_listado = Automovil.objects.all()
   informacion_template ={"listado_automoviles":mis_listado}
   return render(request, "listarInformacion.html", informacion_template)
