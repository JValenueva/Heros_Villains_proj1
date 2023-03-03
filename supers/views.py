from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        
        super_type_name= request.query_params.get('super_type')
        print(super_type_name)
        queryset = Super.objects.all()


        if super_type_name:
            queryset = queryset.filter(super_type__name=super_type_name)      

        serializer = SuperSerializer(queryset, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def supers_detail(request, pk):
    try:
        
        super = Super.objects.get(pk=pk)
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    
    except Super.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    