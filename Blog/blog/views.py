from django.shortcuts import render

#request 'es un diccionario que continuamente se va pasando entre el navegador y el servidor'

def Home(request):

	return render(request, 'base.html')


def Nosotros(request):

	return render(request, 't_nosotros.html')