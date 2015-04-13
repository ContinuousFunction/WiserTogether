from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from medicaldata.models import MedicalData
from medicaldata.serializers import MedicalDataSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
    @csrf_exempt
    def medicaldata_list(request):
        """
        List all code medicaldata, or create a new medicaldata.
        """
        if request.method == 'GET':
            medicaldatas = MedicalData.objects.all()
            serializer = MedicalDataSerializer(medicaldatas, many=True)
            return JSONResponse(serializer.data)
    
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = MedicalData(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)
    @csrf_exempt
    def medicaldata_detail(request, pk):
        """
        Retrieve, update or delete a code medicaldata.
        """
        try:
            medicaldata = MedicalData.objects.get(pk=pk)
        except MedicalData.DoesNotExist:
            return HttpResponse(status=404)
    
        if request.method == 'GET':
            serializer = MedicalDataSerializer(snippet)
            return JSONResponse(serializer.data)
    
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = MedicalDataSerializer(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)
    
        elif request.method == 'DELETE':
            medicaldata.delete()
            return HttpResponse(status=204)