from api.fabricante.fabricanteSLR import FabricanteSerializado
from api.models import Fabricante
from rest_framework.response import Response
from rest_framework.views import APIView

class FabricanteAPI(APIView):
    def get(self, request):
        try:
            fabricantes = Fabricante.objects.all()
            serializador = FabricanteSerializado(fabricantes, many=True)

            return Response(serializador.data, status=200)
        except:
            return Response(status=400)

    def post(self, request):
        serializador = FabricanteSerializado(data=request.data)

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=200)
        else:
            return Response(serializador.errors, status=400)

    def put(self, request, id):
        fabricante = Fabricante.objects.get(id = id)

        serializador = FabricanteSerializado(fabricante, data=request.data)

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=200)
        else:
            return Response(serializador.errors, status=400)

    def delete(self, request, id):
        fabricante = Fabricante.objects.get(id = id)
        fabricante.delete()
        
        return Response(status=200)
