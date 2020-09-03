from django.views.generic import TemplateView
#from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from ibprojecten.api.models import (Product,
                                    ProductType,
                                    Requirement,
                                    Scope,
                                    ScopeType,
                                    Criteria,
                                    CriteriaType,
                                    Dimension,
                                    SubDimension,
                                    SubDimensionType,
                                    DataElement)
from ibprojecten.api.serializers import (ProductSerializer,
                                    ProductTypeSerializer,
                                    RequirementSerializer,
                                    ScopeSerializer,
                                    ScopeTypeSerializer,
                                    CriteriaSerializer,
                                    CriteriaTypeSerializer,
                                    DimensionSerializer,
                                    SubDimensionSerializer,
                                    SubDimensionType,
                                    SubDimensionTypeSerializer,
                                    DataElementSerializer)

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


#def projectenGeojson(request):
#    projectenList = serialize('geojson',Project.objects.all())
#    return HttpResponse(projectenList, content_type='json')


class ProductViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class RequirementViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class ScopeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Scope.objects.all()
    serializer_class = ScopeSerializer


class ScopeTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = ScopeType.objects.all()
    serializer_class = ScopeTypeSerializer


class CriteriaViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer


class CriteriaTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = CriteriaType.objects.all()
    serializer_class = CriteriaTypeSerializer


class DimensionViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer


class SubDimensionViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = SubDimension.objects.all()
    serializer_class = SubDimensionSerializer


class SubDimensionTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = SubDimensionType.objects.all()
    serializer_class = SubDimensionTypeSerializer


class DataElementViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = DataElement.objects.all()
    serializer_class = DataElementSerializer


def requirementList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        requirements = Requirement.objects.all()
        serializer = RequirementSerializer(requirements, many=True)
        return JsonResponse(serializer.data, safe=False)


def requirementDetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        requirement = Requirement.objects.get(pk=pk)
    except Requirement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RequirementSerializer(requirement)
        return JsonResponse(serializer.data)
