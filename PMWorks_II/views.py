from rest_framework import generics

from .models import AssetCategory, AssetClass, AssetClassSubdivision, FailureMode, FailureCause, SpecificData, \
    JobCategory, Department, Personnel, AssetPriority, Location, Asset, AssetSubdivision, SparePartDimension, \
    SparePartCategory, Document, AssetSpecificData, SparePart, TaskType, AssetClassTask, Supplier, SupplierSpecific, \
    SupplierSpecificData, WorkRequest, TypeWr, WorkPriority, WorkOrder, WOSupplier, WOPersonnel, Delay, WODelay, \
    WOSparePart, WOTask, WOTemplate, WOTemplateSchualing, AssetClassSpecificData, AssetClassDocument, \
    AssetSubdivisionSparePart, PersonnelJobCategory, WorkRequestFailureCause, WOTemplateType, WOTemplate, \
    TemplateSchualingDate, Status, WRWORelationStatus, WRStatus, WOStatus, WorkflowLevel, \
    WorkflowLevelStatus, WorkflowLevelStatusShow, WOTemplateAsset, WOTemplateActivity

from .serializers import AssetCategorySerializer, AssetClassSerializer, AssetClassSubdivisionSerializer, \
    AssetClassSpecificDataSerializer, SpecificDataSerializer, FailureModeSerializer, LocationSerializer, \
    AssetPrioritySerializer, DocumentSerializer, AssetClassDocumentSerializer, AssetSerializer, AssetSpecificDataSerializer, \
    AssetSubdivisionSerializer, SparePartDimensionSerializer, SparePartCategorySerializer, SparePartSerializer, \
    AssetSubdivisionSparePartSerializer, TaskTypeSerializer, JobCategorySerializer, DepartmentSerializer, PersonnelSerializer, \
    PersonnelJobCategorySerializer, TypeWrSerializer, WorkPrioritySerializer, SupplierSerializer, SupplierSpecificSerializer, \
    SupplierSpecificDataSerializer, AssetClassTaskSerializer, WorkRequestSerializer, WorkOrderSerializer, \
    WOSupplierSerializer, WOPersonnelSerializer, DelaySerializer, WODelaySerializer, WOSparePartSerializer, \
    WOTaskSerializer, UserSerializer, AssetSubdivisionAssetSerializer, FailureCauseSerializer, WorkRequestFailureCauseSerializer, \
    WOTemplateTypeSerializer, WOTemplateSerializer, WOTemplateSchualingSerializer, \
    TemplateSchualingDateSerializer, StatusSerializer, WRWORelationStatusSerializer, WRStatusSerializer, WOStatusSerializer, \
    WorkflowLevelSerializer, WorkflowLevelStatusSerializer, WorkOrderNewSerializer, WOTaskorderSerializer, \
    WorkflowLevelStatusShowSerializer, WOTemplateAssetSerializer, WOTemplateActivitySerializer, WOTemplateAssetNewSerializer

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import rest_framework as filters
import django_filters
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class AssetCatFath(filters.FilterSet):
    AssetClassFather = NumberInFilter(field_name='AssetClassFather', lookup_expr='in')
    AssetClassFather__isnull = filters.BooleanFilter(field_name='AssetClassFather', lookup_expr='isnull')
    AssetCategoryCode = filters.CharFilter(field_name='AssetCategoryCode', lookup_expr='icontains')
    AssetCategoryName = filters.CharFilter(field_name='AssetCategoryName', lookup_expr='icontains')
    AssetClassFatherName = filters.CharFilter(field_name='AssetClassFather__AssetCategoryName', lookup_expr='icontains')


class AssetCategoryView(generics.ListCreateAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'AssetCategoryName': ['icontains'], 'id': ['exact'], 'AssetClassFather__AssetCategoryName': ['icontains'], 'AssetCategoryCode': ['icontains']}
    filter_class = AssetCatFath
    ordering_fields = ['AssetCategoryName', 'id', 'AssetClassFather__AssetCategoryName', 'AssetCategoryCode',]

class AssetCategoryCreate(generics.ListCreateAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'AssetCategoryName': ['icontains'], 'id': ['exact'], 'AssetClassFather__AssetCategoryName': ['icontains'], 'AssetCategoryCode': ['icontains']}
    filter_class = AssetCatFath
    ordering_fields = ['AssetCategoryName', 'id', 'AssetClassFather__AssetCategoryName', 'AssetCategoryCode',]


class AssetCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()


class AssetClassView(generics.ListCreateAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'AssetClassName': ['icontains'], 'id': ['exact'], 'AssetClassCode': ['icontains'], 'AssetCategoryID__AssetCategoryName': ['icontains'], 'AssetCategoryID': ['exact']}
    ordering_fields = ['AssetClassName', 'id', 'AssetClassCode', 'AssetCategoryID__AssetCategoryName', ]


class AssetClassCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'AssetClassName': ['icontains'], 'id': ['exact'], 'AssetClassCode': ['icontains'], 'AssetCategoryID__AssetCategoryName': ['icontains'], 'AssetCategoryID': ['exact']}
    ordering_fields = ['AssetClassName', 'id', 'AssetClassCode', 'AssetCategoryID__AssetCategoryName', ]

class AssetClassRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()


class AssetClassSubdivisionView(generics.ListCreateAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'AssetClassFatherID': ['exact'], 'id': ['exact'], 'AssetClassChildID': ['exact'], 'AssetClassFatherID__AssetClassName': ['icontains'], 'AssetClassFatherID__AssetClassCode': ['icontains'], 'AssetClassChildID__AssetClassName': ['icontains'], 'AssetClassChildID__AssetClassCode': ['icontains']}
    ordering_fields = ['AssetClassFatherID', 'id', 'AssetClassChildID', 'AssetClassFatherID__AssetClassName', 'AssetClassFatherID__AssetClassCode', 'AssetClassChildID__AssetClassName', 'AssetClassChildID__AssetClassCode', ]


class AssetClassSubdivisionCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'AssetClassFatherID': ['exact'], 'id': ['exact'], 'AssetClassChildID': ['exact'], 'AssetClassFatherID__AssetClassName': ['icontains'], 'AssetClassFatherID__AssetClassCode': ['icontains'], 'AssetClassChildID__AssetClassName': ['icontains'], 'AssetClassChildID__AssetClassCode': ['icontains']}
    ordering_fields = ['AssetClassFatherID', 'id', 'AssetClassChildID', 'AssetClassFatherID__AssetClassName', 'AssetClassFatherID__AssetClassCode', 'AssetClassChildID__AssetClassName', 'AssetClassChildID__AssetClassCode', ]


class AssetClassSubdivisionRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()


class AssetClassSpecificDataView(generics.ListCreateAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'AssetClassID': ['exact'], 'id': ['exact'], 'SpecificDataID': ['exact'], 'SpecificDataID__SpecificDataName': ['icontains'], 'SpecificDataID__SpecificDataCode': ['icontains'], 'SpecificDataID__Measurment': ['icontains']}
    ordering_fields = '__all__'


class AssetClassSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'AssetClassID': ['exact'], 'id': ['exact'], 'SpecificDataID': ['exact'], 'SpecificDataID__SpecificDataName': ['icontains'], 'SpecificDataID__SpecificDataCode': ['icontains'], 'SpecificDataID__Measurment': ['icontains']}
    ordering_fields = '__all__'


class AssetClassSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()


class SpecificDataView(generics.ListCreateAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'SpecificDataCode': ['icontains'], 'id': ['exact'], 'SpecificDataName': ['icontains'], 'Measurment': ['icontains']}
    ordering_fields = '__all__'


class SpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'SpecificDataCode': ['icontains'], 'id': ['exact'], 'SpecificDataName': ['icontains'], 'Measurment': ['icontains']}
    ordering_fields = '__all__'


class SpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()


class FailureModeView(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'FailureModeCode': ['icontains'], 'FailureModeName': ['icontains'], 'FailureModeDescription': ['icontains'], 'AssetClassID': ['exact']}
    ordering_fields = '__all__'


class FailureModeCreate(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'FailureModeCode': ['icontains'], 'FailureModeName': ['icontains'], 'FailureModeDescription': ['icontains'], 'AssetClassID': ['exact']}
    ordering_fields = '__all__'


class FailureModeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()

class FailureCauseView(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'FailureCauseCode': ['icontains'], 'FailureCauseName': ['icontains'], 'FailureCauseDescription': ['icontains'], 'FailureModeID': ['exact']}
    ordering_fields = '__all__'


class FailureCauseCreate(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'FailureCauseCode': ['icontains'], 'FailureCauseName': ['icontains'], 'FailureCauseDescription': ['icontains'], 'FailureModeID': ['exact']}
    ordering_fields = '__all__'


class FailureCauseRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()

class LocationFath(filters.FilterSet):
    LocationFatherID = NumberInFilter(field_name='LocationFatherID', lookup_expr='in')
    LocationFatherID__isnull = filters.BooleanFilter(field_name='LocationFatherID', lookup_expr='isnull')
    LocationCode = filters.CharFilter(field_name='LocationCode', lookup_expr='icontains')
    LocationName = filters.CharFilter(field_name='LocationName', lookup_expr='icontains')
    LocationFatherName = filters.CharFilter(field_name='LocationFatherID__LocationName', lookup_expr='icontains')


class LocationView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'LocationCode': ['icontains'], 'LocationName': ['icontains'], 'LocationFatherID': ['exact']}
    filter_class = LocationFath
    ordering_fields = '__all__'


class LocationCreate(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'LocationCode': ['icontains'], 'LocationName': ['icontains'], 'LocationFatherID': ['exact']}
    filter_class = LocationFath
    ordering_fields = '__all__'


class LocationRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class DocumentView(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'DocumentCode': ['icontains'], 'DocumentName': ['icontains'], 'DocumentDescription': ['icontains']}
    ordering_fields = '__all__'


class DocumentCreate(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'DocumentCode': ['icontains'], 'DocumentName': ['icontains'], 'DocumentDescription': ['icontains']}
    ordering_fields = '__all__'


class DocumentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class AssetPriorityView(generics.ListCreateAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetPriorityCode': ['icontains'], 'AssetPriorityName': ['icontains'], 'AssetPriorityValue': ['icontains']}
    ordering_fields = '__all__'


class AssetPriorityCreate(generics.ListCreateAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetPriorityCode': ['icontains'], 'AssetPriorityName': ['icontains'], 'AssetPriorityValue': ['icontains']}
    ordering_fields = '__all__'


class AssetPriorityRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()


class AssetClassDocumentView(generics.ListCreateAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetClassID': ['exact'], 'DocumentID': ['exact'], 'DocumentID__DocumentName': ['icontains'], 'DocumentID__DocumentCode': ['icontains']}
    ordering_fields = '__all__'


class AssetClassDocumentCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetClassID': ['exact'], 'DocumentID': ['exact'], 'DocumentID__DocumentName': ['icontains'], 'DocumentID__DocumentCode': ['icontains']}
    ordering_fields = '__all__'


class AssetClassDocumentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()


class AssetView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetCode': ['icontains'], 'AssetName': ['icontains'], 'InstallationDate': ['icontains'], 'AssetPriorityID': ['exact'], 'LocationID': ['exact'],
                        'AssetClassID': ['exact']}
    ordering_fields = '__all__'


class AssetCreate(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetCode': ['icontains'], 'AssetName': ['icontains'], 'InstallationDate': ['icontains'], 'AssetPriorityID': ['exact'], 'LocationID': ['exact'],
                        'AssetClassID': ['exact']}
    ordering_fields = '__all__'


class AssetRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()


class AssetSpecificDataView(generics.ListCreateAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetSubdivisionID': ['exact'], 'SpecificDataID': ['exact'], 'SpecificAmount': ['icontains']}
    ordering_fields = '__all__'


class AssetSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetSubdivisionID': ['exact'], 'SpecificDataID': ['exact'], 'SpecificAmount': ['icontains']}
    ordering_fields = '__all__'


class AssetSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()


class AssetSubdivisionView(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation', 'AssetClassCodeChain', 'AssetClassNameChain', 'idChain', 'AssetCode', 'AssetName', 'AssetID__AssetName', 'AssetID__AssetCode', 'AssetID__LocationID__LocationName', 'AssetID__LocationID__LocationCode', 'AssetID__LocationID__LocationCodeChain', 'AssetID__LocationID__LocationNameChain')
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetID': ['exact'], 'AssetChildID': ['exact'], 'AssetSubdivisionFatherID': ['exact'],'tree': ['exact'], 'fakelocation': ['exact'], 'AssetClassCodeChain': ['icontains'], 'AssetClassNameChain': ['icontains'], 'idChain': ['exact'], 'AssetCode': ['icontains'], 'AssetName': ['icontains'], 'AssetID__LocationID__LocationCodeChain': ['icontains'], 'AssetID__LocationID__LocationNameChain': ['icontains']} 
    ordering_fields = '__all__'


class AssetSubdivisionCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation', 'AssetClassCodeChain', 'AssetClassNameChain', 'idChain', 'AssetCode', 'AssetName', 'AssetID__AssetName', 'AssetID__AssetCode', 'AssetID__LocationID__LocationName', 'AssetID__LocationID__LocationCode', 'AssetID__LocationID__LocationCodeChain', 'AssetID__LocationID__LocationNameChain')
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetID': ['exact'], 'AssetChildID': ['exact'], 'AssetSubdivisionFatherID': ['exact'],'tree': ['exact'], 'fakelocation': ['exact'], 'AssetClassCodeChain': ['icontains'], 'AssetClassNameChain': ['icontains'], 'idChain': ['exact'], 'AssetCode': ['icontains'], 'AssetName': ['icontains'], 'AssetID__LocationID__LocationCodeChain': ['icontains'], 'AssetID__LocationID__LocationNameChain': ['icontains']} 
    ordering_fields = '__all__'


class AssetSubdivisionRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation', 'AssetClassCodeChain', 'AssetClassNameChain', 'idChain', 'AssetCode', 'AssetName', 'AssetID__AssetName', 'AssetID__AssetCode', 'AssetID__LocationID__LocationName', 'AssetID__LocationID__LocationCode', 'AssetID__LocationID__LocationCodeChain', 'AssetID__LocationID__LocationNameChain')


class SparePartDimensionView(generics.ListCreateAPIView):
    serializer_class = SparePartDimensionSerializer
    queryset = SparePartDimension.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SparePartDimensionCode': ['icontains'], 'SparePartDimensionName': ['icontains']}
    ordering_fields = '__all__'


class SparePartDimensionCreate(generics.ListCreateAPIView):
    serializer_class = SparePartDimensionSerializer
    queryset = SparePartDimension.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SparePartDimensionCode': ['icontains'], 'SparePartDimensionName': ['icontains']}
    ordering_fields = '__all__'


class SparePartDimensionRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartDimensionSerializer
    queryset = SparePartDimension.objects.all()


class SparePartCatFath(filters.FilterSet):
    SparePartCategoryFather = NumberInFilter(field_name='SparePartCategoryFather', lookup_expr='in')
    SparePartCategoryFather__isnull = filters.BooleanFilter(field_name='SparePartCategoryFather', lookup_expr='isnull')


class SparePartCategoryView(generics.ListCreateAPIView):
    serializer_class = SparePartCategorySerializer
    queryset = SparePartCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SparePartCategoryCode': ['icontains'], 'SparePartCategoryName': ['icontains'], 'SparePartCategoryFather': ['exact']}
    filter_class = SparePartCatFath
    ordering_fields = '__all__'


class SparePartCategoryCreate(generics.ListCreateAPIView):
    serializer_class = SparePartCategorySerializer
    queryset = SparePartCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SparePartCategoryCode': ['icontains'], 'SparePartCategoryName': ['icontains'], 'SparePartCategoryFather': ['exact']}
    filter_class = SparePartCatFath
    ordering_fields = '__all__'


class SparePartCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartCategorySerializer
    queryset = SparePartCategory.objects.all()


class SparePartView(generics.ListCreateAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SparePartCode': ['icontains'], 'SparePartName': ['icontains'], 'SparePartCategoryID': ['exact'], 'SparePartDimensionID': ['exact']}
    ordering_fields = '__all__'


class SparePartCreate(generics.ListCreateAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SparePartCode': ['icontains'], 'SparePartName': ['icontains'], 'SparePartCategoryID': ['exact'], 'SparePartDimensionID': ['exact']}
    ordering_fields = '__all__'


class SparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()


class AssetSubdivisionSparePartView(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetSubdivisionID': ['exact'], 'SparePartID': ['exact']}
    ordering_fields = '__all__'


class AssetSubdivisionSparePartCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'AssetSubdivisionID': ['exact'], 'SparePartID': ['exact']}
    ordering_fields = '__all__'


class AssetSubdivisionSparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()

class TaskTypeView(generics.ListCreateAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TaskTypeCode': ['icontains'], 'TaskTypeName': ['icontains'], 'TaskTypeDescription': ['icontains']}
    ordering_fields = '__all__'


class TaskTypeCreate(generics.ListCreateAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TaskTypeCode': ['icontains'], 'TaskTypeName': ['icontains'], 'TaskTypeDescription': ['icontains']}
    ordering_fields = '__all__'


class TaskTypeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()


class JobCategoryView(generics.ListCreateAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'JobCategoryCode': ['icontains'], 'JobCategoryName': ['icontains']}
    ordering_fields = '__all__'


class JobCategoryCreate(generics.ListCreateAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'JobCategoryCode': ['icontains'], 'JobCategoryName': ['icontains']}
    ordering_fields = '__all__'


class JobCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'DepartmentCode': ['icontains'], 'DepartmentName': ['icontains']}
    ordering_fields = '__all__'


class DepartmentCreate(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'DepartmentCode': ['icontains'], 'DepartmentName': ['icontains']}
    ordering_fields = '__all__'


class DepartmentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class PersonnelView(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'PersonnelCode': ['icontains'], 'PersonnelNetCode': ['icontains'], 'PersonnelName': ['icontains'], 'PersonnelFamily': ['icontains'], 'PersonnelMobile': ['icontains'],
                  'DepartmentID': ['exact']}
    ordering_fields = '__all__'


class PersonnelCreate(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'PersonnelCode': ['icontains'], 'PersonnelNetCode': ['icontains'], 'PersonnelName': ['icontains'], 'PersonnelFamily': ['icontains'], 'PersonnelMobile': ['icontains'],
                  'DepartmentID': ['exact']}
    ordering_fields = '__all__'


class PersonnelRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()


class PersonnelJobCategoryView(generics.ListCreateAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'PersonnelID': ['exact'], 'JobCategoryID': ['exact']}
    ordering_fields = '__all__'


class PersonnelJobCategoryCreate(generics.ListCreateAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'PersonnelID': ['exact'], 'JobCategoryID': ['exact']}
    ordering_fields = '__all__'


class PersonnelJobCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()


class TypeWrView(generics.ListCreateAPIView):
    serializer_class = TypeWrSerializer
    queryset = TypeWr.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TypeWrCode': ['icontains'], 'TypeWrName': ['icontains']}
    ordering_fields = '__all__'


class TypeWrCreate(generics.ListCreateAPIView):
    serializer_class = TypeWrSerializer
    queryset = TypeWr.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TypeWrCode': ['icontains'], 'TypeWrName': ['icontains']}
    ordering_fields = '__all__'


class TypeWrRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =TypeWrSerializer
    queryset = TypeWr.objects.all()


class WorkPriorityView(generics.ListCreateAPIView):
    serializer_class = WorkPrioritySerializer
    queryset = WorkPriority.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkPriorityCode': ['icontains'], 'WorkPriorityName': ['icontains'], 'WorkPriorityValue': ['icontains']}
    ordering_fields = '__all__'


class WorkPriorityCreate(generics.ListCreateAPIView):
    serializer_class = WorkPrioritySerializer
    queryset = WorkPriority.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkPriorityCode': ['icontains'], 'WorkPriorityName': ['icontains'], 'WorkPriorityValue': ['icontains']}
    ordering_fields = '__all__'


class WorkPriorityRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =WorkPrioritySerializer
    queryset = WorkPriority.objects.all()


class SupplierView(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SupplierCode': ['icontains'], 'SupplierName': ['icontains']}
    ordering_fields = '__all__'


class SupplierCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SupplierCode': ['icontains'], 'SupplierName': ['icontains']}
    ordering_fields = '__all__'


class SupplierRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierSpecificView(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SupplierSpecificCode': ['icontains'], 'SupplierSpecificName': ['icontains']}
    ordering_fields = '__all__'


class SupplierSpecificCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SupplierSpecificCode': ['icontains'], 'SupplierSpecificName': ['icontains']}
    ordering_fields = '__all__'


class SupplierSpecificRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()


class SupplierSpecificDataView(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SupplierID': ['exact'], 'SupplierSpecificID': ['exact'], 'SpecificAmount': ['icontains']}
    ordering_fields = '__all__'


class SupplierSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SupplierID': ['exact'], 'SupplierSpecificID': ['exact'], 'SpecificAmount': ['icontains']}
    ordering_fields = '__all__'


class SupplierSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()


@csrf_exempt
def AssetClassTask_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        AssetClassTasks = AssetClassTask.objects.all()
        serializer = AssetClassTaskSerializer(AssetClassTasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print('dddd', data)
        if 'DurationOfDo' in data:
            if isinstance(data['DurationOfDo'], int) == False:
                data['DurationOfDo'] = None
        if 'FrequencyAmount' in data:
            if isinstance(data['FrequencyAmount'], int) == False:
                data['FrequencyAmount'] = None
        print('d2', data)
        serializer = AssetClassTaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class AssetClassTaskView(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TaskCode': ['icontains'], 'TaskName': ['icontains'], 'TaskDescription': ['icontains'], 'FrequencyName': ['exact'], 'FrequencyAmount': ['exact'], 'DurationOfDo': ['icontains'],
                  'Functor': ['icontains'], 'TaskTypeID': ['exact'], 'JobCategoryID': ['exact'], 'AssetClassID': ['exact'], 'TaskTypeID__TaskTypeName': ['icontains'], 'JobCategoryID__JobCategoryName': ['icontains']}
    ordering_fields = ['id', 'TaskCode', 'TaskName', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo', 'Functor', 'TaskTypeID__TaskTypeName', 'JobCategoryID__JobCategoryName',]


class AssetClassTaskCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TaskCode': ['icontains'], 'TaskName': ['icontains'], 'TaskDescription': ['icontains'], 'FrequencyName': ['exact'], 'FrequencyAmount': ['exact'], 'DurationOfDo': ['icontains'],
                  'Functor': ['icontains'], 'TaskTypeID': ['exact'], 'JobCategoryID': ['exact'], 'AssetClassID': ['exact'], 'TaskTypeID__TaskTypeName': ['icontains'], 'JobCategoryID__JobCategoryName': ['icontains']}
    ordering_fields = ['id', 'TaskCode', 'TaskName', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo', 'Functor', 'TaskTypeID__TaskTypeName', 'JobCategoryID__JobCategoryName',]


class AssetClassTaskRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()


class WorkRequestView(generics.ListCreateAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WRDate': ['icontains'], 'WRDateOfRegistration': ['icontains'], 'AssetSubdivisionID': ['exact'], 'FailureModeID': ['exact'],
                        'WorkPriorityID': ['exact'], 'TypeWrID': ['exact'], 'StatusID': ['exact'], 'StatusID__OpCl': ['exact']}
    ordering_fields = '__all__'


class WorkRequestCreate(generics.ListCreateAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WRDate': ['icontains'], 'WRDateOfRegistration': ['icontains'], 'AssetSubdivisionID': ['exact'], 'FailureModeID': ['exact'],
                        'WorkPriorityID': ['exact'], 'TypeWrID': ['exact'], 'StatusID': ['exact'], 'StatusID__OpCl': ['exact']}
    ordering_fields = '__all__'


class WorkRequestRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()


class WorkOrderView(generics.ListCreateAPIView):
    serializer_class = WorkOrderNewSerializer
    queryset = WorkOrder.objects.all().values('id', 'WOTemplateCode', 'WorkOrderType', 'DateOfStart','DateOfFinish','WODateOfRegistration','WODescription','DateOfPlanStart','DateOfPlanFinish','WorkRequestID','StatusID','WorkRequestID__AssetSubdivisionID','WorkRequestID__FailureModeID','DepartmentID')
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WODateOfRegistration': ['icontains'], 'WODescription': ['icontains'], 'DateOfStart': ['icontains'], 'DateOfFinish': ['icontains'], 'DateOfPlanStart': ['icontains'], 'DateOfPlanFinish': ['icontains'], 'WorkRequestID': ['exact'], 'StatusID': ['exact'], 'DepartmentID': ['exact'], 'StatusID__OpCl': ['exact']}
    ordering_fields = '__all__'


class WorkOrderCreate(generics.ListCreateAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkOrderType': ['exact'],'WODateOfRegistration': ['icontains'], 'WODescription': ['icontains'], 'DateOfStart': ['icontains'], 'DateOfFinish': ['icontains'], 'DateOfPlanStart': ['icontains'], 'DateOfPlanFinish': ['icontains'], 'WorkRequestID': ['exact'], 'StatusID': ['exact'], 'StatusID__OpCl': ['exact'], 'DepartmentID': ['exact']}
    ordering_fields = '__all__'


class WorkOrderRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOrderNewSerializer
    queryset = WorkOrder.objects.all().values('id', 'WOTemplateCode', 'WorkOrderType','DateOfStart','DateOfFinish','WODateOfRegistration','WODescription','DateOfPlanStart','DateOfPlanFinish','WorkRequestID','StatusID','WorkRequestID__AssetSubdivisionID','WorkRequestID__FailureModeID','DepartmentID')


class WOSupplierView(generics.ListCreateAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkStartDate': ['icontains'], 'WorkFinishDate': ['icontains'], 'WorkOrderID': ['exact'], 'SupplierID': ['exact']}
    ordering_fields = '__all__'


class WOSupplierCreate(generics.ListCreateAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkStartDate': ['icontains'], 'WorkFinishDate': ['icontains'], 'WorkOrderID': ['exact'], 'SupplierID': ['exact']}
    ordering_fields = '__all__'


class WOSupplierRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()


class WOPersonnelView(generics.ListCreateAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkDate': ['icontains'], 'WorkTime': ['icontains'], 'WOTaskID': ['exact'], 'PersonnelID': ['exact'], 'WOTaskID__WorkOrderID': ['exact']}
    ordering_fields = '__all__'


class WOPersonnelCreate(generics.ListCreateAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkDate': ['icontains'], 'WorkTime': ['icontains'], 'WOTaskID': ['exact'], 'PersonnelID': ['exact'], 'WOTaskID__WorkOrderID': ['exact']}
    ordering_fields = '__all__'


class WOPersonnelRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()


class DelayView(generics.ListCreateAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'DelayCode': ['icontains'], 'DelayName': ['icontains']}
    ordering_fields = '__all__'


class DelayCreate(generics.ListCreateAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'DelayCode': ['icontains'], 'DelayName': ['icontains']}
    ordering_fields = '__all__'


class DelayRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()


class WODelayView(generics.ListCreateAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'DayAmount': ['icontains'], 'HourAmount': ['icontains'], 'WODelayDescription': ['icontains'], 'WorkOrderID': ['exact'], 'DelayID': ['exact']}
    ordering_fields = '__all__'


class WODelayCreate(generics.ListCreateAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'DayAmount': ['icontains'], 'HourAmount': ['icontains'], 'WODelayDescription': ['icontains'], 'WorkOrderID': ['exact'], 'DelayID': ['exact']}
    ordering_fields = '__all__'


class WODelayRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()


class WOSparePartView(generics.ListCreateAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTaskID': ['exact'], 'SparePartID': ['exact'], 'SparePartAmount': ['icontains'], 'WOTaskID__WorkOrderID': ['exact']}
    ordering_fields = '__all__'


class WOSparePartCreate(generics.ListCreateAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTaskID': ['exact'], 'SparePartID': ['exact'], 'SparePartAmount': ['icontains'], 'WOTaskID__WorkOrderID': ['exact']}
    ordering_fields = '__all__'


class WOSparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()


class WOTaskView(generics.ListCreateAPIView):
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkOrderID': ['exact'], 'TaskID': ['exact'], 'WOTaskSituationOfDo': ['icontains']}
    ordering_fields = '__all__'


class WOTaskCreate(generics.ListCreateAPIView):
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkOrderID': ['exact'], 'TaskID': ['exact'], 'WOTaskSituationOfDo': ['icontains']}
    ordering_fields = '__all__'


class WOTaskRetrive(generics.RetrieveUpdateDestroyAPIView):
    #serializer_class = WOTaskorderSerializer
    #queryset = WOTask.objects.all().values('id', 'WorkOrderID', 'TaskID', 'WOTaskSituationOfDo', 'TaskID__TaskName', 'TaskID__TaskCode')
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()
    
class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'username': ['icontains'], 'first_name': ['icontains'], 'last_name': ['icontains'], 'password': ['exact'],
                  'email': ['icontains'], 'groups': ['icontains'], 'user_permissions': ['icontains'], 'is_staff': ['icontains'], 'is_active': ['icontains'], 'is_superuser': ['icontains'], 'last_login': ['icontains'], 'date_joined': ['icontains']}
    ordering_fields = '__all__'


class UserCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'username': ['icontains'], 'first_name': ['icontains'], 'last_name': ['icontains'], 'password': ['exact'],
                  'email': ['icontains'], 'groups': ['icontains'], 'user_permissions': ['icontains'], 'is_staff': ['icontains'], 'is_active': ['icontains'], 'is_superuser': ['icontains'], 'last_login': ['icontains'], 'date_joined': ['icontains']}
    ordering_fields = '__all__'


class UserRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FailureAssetModeView(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer

    def get_queryset(self):
        queryset = FailureMode.objects.all()
        asset=self.request.query_params.get('AssetClassID', '')
        if asset:
            assetclass=AssetSubdivision.objects.filter(id = asset)
            print('as', queryset.filter(AssetClassID = assetclass[0].AssetChildID.id))
            return queryset.filter(AssetClassID = assetclass[0].AssetChildID)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'FailureModeCode': ['icontains'], 'FailureModeName': ['icontains']}
    ordering_fields = '__all__'


class FailureAssetModeCreate(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer

    def get_queryset(self):
        queryset = FailureMode.objects.all()
        asset=self.request.query_params.get('AssetClassID', '')
        if asset:
            assetclass=AssetSubdivision.objects.filter(id = asset)
            print('as', queryset.filter(AssetClassID = assetclass[0].AssetChildID.id))
            return queryset.filter(AssetClassID = assetclass[0].AssetChildID.id)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'FailureModeCode': ['icontains'], 'FailureModeName': ['icontains']}
    ordering_fields = '__all__'


class FailureAssetModeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureModeSerializer

    def get_queryset(self):
        queryset = FailureMode.objects.all()
        asset=self.request.query_params.get('AssetClassID', '')
        if asset:
            assetclass=AssetSubdivision.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assetclass[0].AssetChildID.id)
        return queryset
    

class AssetSubdivisionAssetView(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation')
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'],'AssetID__AssetName': ['icontains'],'AssetID__AssetCode': ['icontains'],'AssetSubdivisionFatherID': ['exact'],'AssetID': ['exact'],'AssetChildID': ['exact'],'tree': ['exact'],'fakelocation': ['exact']}
    ordering_fields = '__all__'


class AssetSubdivisionAssetCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation')
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'],'AssetID__AssetName': ['icontains'],'AssetID__AssetCode': ['icontains'],'AssetSubdivisionFatherID': ['exact'],'AssetID': ['exact'],'AssetChildID': ['exact'],'tree': ['exact'],'fakelocation': ['exact']}
    ordering_fields = '__all__'


class AssetSubdivisionAssetRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation')


class WorkRequestFailureCauseView(generics.ListCreateAPIView):
    serializer_class = WorkRequestFailureCauseSerializer
    queryset = WorkRequestFailureCause.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'WorkRequestID': ['exact'], 'id': ['exact'], 'FailureCauseID': ['exact']}
    ordering_fields = '__all__'


class WorkRequestFailureCauseCreate(generics.ListCreateAPIView):
    serializer_class = WorkRequestFailureCauseSerializer
    queryset = WorkRequestFailureCause.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'WorkRequestID': ['exact'], 'id': ['exact'], 'FailureCauseID': ['exact']}
    ordering_fields = '__all__'


class WorkRequestFailureCauseRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkRequestFailureCauseSerializer
    queryset = WorkRequestFailureCause.objects.all()

    
class WRCauseView(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer

    def get_queryset(self):
        queryset = FailureCause.objects.all()
        mode=self.request.query_params.get('FailureModeID', '')
        if mode:
            fmode=WorkRequest.objects.filter(id = mode)
            return queryset.filter(FailureModeID = fmode[0].FailureModeID)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'


class WRCauseCreate(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer

    def get_queryset(self):
        queryset = FailureCause.objects.all()
        mode=self.request.query_params.get('FailureModeID', '')
        if mode:
            fmode=WorkRequest.objects.filter(id = mode)
            return queryset.filter(FailureModeID = fmode[0].FailureModeID)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'FailureCauseCode': ['icontains'], 'FailureCauseName': ['icontains'], 'FailureModeID': ['exact']}
    ordering_fields = '__all__'


class WRCauseRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureCauseSerializer

    def get_queryset(self):
        queryset = FailureCause.objects.all()
        mode=self.request.query_params.get('FailureModeID', '')
        if mode:
            fmode=WorkRequest.objects.filter(id = mode)
            return queryset.filter(FailureModeID = fmode[0].FailureModeID)
        return queryset


class WRSpareView(generics.ListCreateAPIView):
    serializer_class = SparePartSerializer

    def get_queryset(self):
        queryset = SparePart.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            spare = AssetSubdivisionSparePart.objects.filter(AssetSubdivisionID = assets[0].WorkRequestID.AssetSubdivisionID)
            return queryset.filter(id__in = spare.values('SparePartID'))
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'


class WRSpareCreate(generics.ListCreateAPIView):
    serializer_class = SparePartSerializer

    def get_queryset(self):
        queryset = SparePart.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            spare = AssetSubdivisionSparePart.objects.filter(AssetSubdivisionID = assets[0].WorkRequestID.AssetSubdivisionID)
            return queryset.filter(id__in = spare.values('SparePartID'))
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SparePartCode': ['icontains'], 'SparePartName': ['icontains'], 'SparePartCategoryID': ['exact'], 'SparePartDimensionID': ['exact']}
    ordering_fields = '__all__'


class WRSpareRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartSerializer

    def get_queryset(self):
        queryset = SparePart.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            spare = AssetSubdivisionSparePart.objects.filter(AssetSubdivisionID = assets[0].WorkRequestID.AssetSubdivisionID)
            return queryset.filter(id__in = spare.values('SparePartID'))
        return queryset

class WOTemplateTypeView(generics.ListCreateAPIView):
    serializer_class = WOTemplateTypeSerializer
    queryset = WOTemplateType.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateTypeCode': ['icontains'], 'WOTemplateTypeName': ['icontains'], 'WOTemplateTypeDescription': ['icontains']}
    ordering_fields = '__all__'


class WOTemplateTypeCreate(generics.ListCreateAPIView):
    serializer_class = WOTemplateTypeSerializer
    queryset = WOTemplateType.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateTypeCode': ['icontains'], 'WOTemplateTypeName': ['icontains'], 'WOTemplateTypeDescription': ['icontains']}
    ordering_fields = '__all__'


class WOTemplateTypeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTemplateTypeSerializer
    queryset = WOTemplateType.objects.all()


class WOTemplateView(generics.ListCreateAPIView):
    serializer_class = WOTemplateSerializer
    queryset = WOTemplate.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateCode': ['icontains'], 'WOTemplateName': ['icontains'], 'WOTemplateDurationDay': ['icontains'], 'WOTemplateDurationHour': ['icontains'],
                          'WOTemplateAlarmDay': ['icontains'], 'WOTemplateAlarmHour': ['icontains'], 'DepartmentID': ['exact'], 'DepartmentID__DepartmentName': ['icontains'],
                          'DepartmentID__DepartmentCode': ['icontains'], 'WOTemplateTypeID': ['exact'], 'WOTemplateTypeID__WOTemplateTypeName': ['icontains'], 'WOTemplateTypeID__WOTemplateTypeCode': ['icontains']}
    ordering_fields = '__all__'


class WOTemplateCreate(generics.ListCreateAPIView):
    serializer_class = WOTemplateSerializer
    queryset = WOTemplate.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateCode': ['icontains'], 'WOTemplateName': ['icontains'], 'WOTemplateDurationDay': ['icontains'], 'WOTemplateDurationHour': ['icontains'],
                          'WOTemplateAlarmDay': ['icontains'], 'WOTemplateAlarmHour': ['icontains'], 'DepartmentID': ['exact'], 'DepartmentID__DepartmentName': ['icontains'],
                          'DepartmentID__DepartmentCode': ['icontains'], 'WOTemplateTypeID': ['exact'], 'WOTemplateTypeID__WOTemplateTypeName': ['icontains'], 'WOTemplateTypeID__WOTemplateTypeCode': ['icontains']}
    ordering_fields = '__all__'


class WOTemplateRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTemplateSerializer
    queryset = WOTemplate.objects.all()

    
class WOTemplateAssetView(generics.ListCreateAPIView):
    serializer_class = WOTemplateAssetSerializer
    queryset = WOTemplateAsset.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateID': ['exact'], 'AssetSubdivisionID': ['exact']}
    ordering_fields = '__all__'


class WOTemplateAssetCreate(generics.ListCreateAPIView):
    serializer_class = WOTemplateAssetSerializer
    queryset = WOTemplateAsset.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateID': ['exact'], 'AssetSubdivisionID': ['exact']}
    ordering_fields = '__all__'


class WOTemplateAssetRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTemplateAssetNewSerializer
    queryset = WOTemplateAsset.objects.all().values('id', 'WOTemplateID__WOTemplateCode', 'WOTemplateID__WOTemplateName', 'WOTemplateID', 'AssetSubdivisionID__AssetCode', 'AssetSubdivisionID__AssetName', 'AssetSubdivisionID' )


class WOTemplateActivityView(generics.ListCreateAPIView):
    serializer_class = WOTemplateActivitySerializer
    queryset = WOTemplateActivity.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateAssetID': ['exact'], 'TaskID': ['exact']}
    ordering_fields = '__all__'


class WOTemplateActivityCreate(generics.ListCreateAPIView):
    serializer_class = WOTemplateActivitySerializer
    queryset = WOTemplateActivity.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateAssetID': ['exact'], 'TaskID': ['exact']}
    ordering_fields = '__all__'


class WOTemplateActivityRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTemplateActivitySerializer
    queryset = WOTemplateActivity.objects.all()


class WOTemplateSchualingView(generics.ListCreateAPIView):
    serializer_class = WOTemplateSchualingSerializer
    queryset = WOTemplateSchualing.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateSchualingStartDate': ['icontains'], 'WOTemplateSchualingFinishDate': ['icontains'], 'AmountFrequency': ['icontains'], 'Status': ['icontains'],
                          'WOTemplateID': ['exact'], 'FrequencyName': ['exact']}
    ordering_fields = '__all__'


class WOTemplateSchualingCreate(generics.ListCreateAPIView):
    serializer_class = WOTemplateSchualingSerializer
    queryset = WOTemplateSchualing.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WOTemplateSchualingStartDate': ['icontains'], 'WOTemplateSchualingFinishDate': ['icontains'], 'AmountFrequency': ['icontains'], 'Status': ['icontains'],
                          'WOTemplateID': ['exact'], 'FrequencyName': ['exact']}
    ordering_fields = '__all__'

class WOTemplateSchualingRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTemplateSchualingSerializer
    queryset = WOTemplateSchualing.objects.all()


class TemplateSchualingDateView(generics.ListCreateAPIView):
    serializer_class = TemplateSchualingDateSerializer
    queryset = TemplateSchualingDate.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SchualingDate': ['icontains'], 'WorkOrderID': ['exact'], 'SchedualingAlarmDate': ['icontains'], 'WOTemplateSchualingID': ['exact'], 'StatusOfDo': ['icontains']}
    ordering_fields = '__all__'


class TemplateSchualingDateCreate(generics.ListCreateAPIView):
    serializer_class = TemplateSchualingDateSerializer
    queryset = TemplateSchualingDate.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'SchualingDate': ['icontains'], 'WorkOrderID': ['exact'], 'SchedualingAlarmDate': ['icontains'], 'WOTemplateSchualingID': ['exact'], 'StatusOfDo': ['icontains']}
    ordering_fields = '__all__'


class TemplateSchualingDateRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TemplateSchualingDateSerializer
    queryset = TemplateSchualingDate.objects.all()

class StatusView(generics.ListCreateAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusCode': ['icontains'], 'StatusCondition': ['exact'], 'StatusName': ['icontains'], 'OpCl': ['exact']}
    ordering_fields = '__all__'

class StatusCreate(generics.ListCreateAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusCode': ['icontains'], 'StatusCondition': ['exact'], 'StatusName': ['icontains'], 'OpCl': ['exact']}
    ordering_fields = '__all__'

class StatusRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class WRWORelationStatusView(generics.ListCreateAPIView):
    serializer_class = WRWORelationStatusSerializer
    queryset = WRWORelationStatus.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusWOID': ['exact'], 'StstusWRID': ['exact']}
    ordering_fields = '__all__'

class WRWORelationStatusCreate(generics.ListCreateAPIView):
    serializer_class = WRWORelationStatusSerializer
    queryset = WRWORelationStatus.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusWOID': ['exact'], 'StstusWRID': ['exact']}
    ordering_fields = '__all__'

class WRWORelationStatusRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WRWORelationStatusSerializer
    queryset = WRWORelationStatus.objects.all()


class WRStatusView(generics.ListCreateAPIView):
    serializer_class = WRStatusSerializer
    queryset = WRStatus.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusID': ['exact'], 'WorkRequestID': ['exact'], 'StatusDate': ['exact'], 'StatusTime': ['exact'], 'StatusID__StatusCode': ['icontains'], 'StatusID__StatusName': ['icontains']}
    ordering_fields = '__all__'

class WRStatusCreate(generics.ListCreateAPIView):
    serializer_class = WRStatusSerializer
    queryset = WRStatus.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusID': ['exact'], 'WorkRequestID': ['exact'], 'StatusDate': ['exact'], 'StatusTime': ['exact'], 'StatusID__StatusCode': ['icontains'], 'StatusID__StatusName': ['icontains']}
    ordering_fields = '__all__'

class WRStatusRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WRStatusSerializer
    queryset = WRStatus.objects.all()


class WOStatusView(generics.ListCreateAPIView):
    serializer_class = WOStatusSerializer
    queryset = WOStatus.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusID': ['exact'], 'WorkOrderID': ['exact'], 'StatusDate': ['exact'], 'StatusTime': ['exact'], 'StatusID__StatusCode': ['icontains'], 'StatusID__StatusName': ['icontains']}
    ordering_fields = '__all__'

class WOStatusCreate(generics.ListCreateAPIView):
    serializer_class = WOStatusSerializer
    queryset = WOStatus.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusID': ['exact'], 'WorkOrderID': ['exact'], 'StatusDate': ['exact'], 'StatusTime': ['exact'], 'StatusID__StatusCode': ['icontains'], 'StatusID__StatusName': ['icontains']}
    ordering_fields = '__all__'

class WOStatusRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOStatusSerializer
    queryset = WOStatus.objects.all()


class WorkflowLevelView(generics.ListCreateAPIView):
    serializer_class = WorkflowLevelSerializer
    queryset = WorkflowLevel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkflowLevelName': ['exact'], 'WorkflowLevelType': ['exact']}
    ordering_fields = '__all__'

class WorkflowLevelCreate(generics.ListCreateAPIView):
    serializer_class = WorkflowLevelSerializer
    queryset = WorkflowLevel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'WorkflowLevelName': ['exact'], 'WorkflowLevelType': ['exact']}
    ordering_fields = '__all__'

class WorkflowLevelRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkflowLevelSerializer
    queryset = WorkflowLevel.objects.all()

class WorkflowLevelStatusView(generics.ListCreateAPIView):
    serializer_class = WorkflowLevelStatusSerializer
    queryset = WorkflowLevelStatus.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusID': ['exact'], 'WorkflowLevelID': ['exact'], 'WorkflowLevelStatusPeriority': ['exact'], 'WorkflowLevelID__WorkflowLevelType': ['exact']}
    ordering_fields = '__all__'

class WorkflowLevelStatusCreate(generics.ListCreateAPIView):
    serializer_class = WorkflowLevelStatusSerializer
    queryset = WorkflowLevelStatus.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusID': ['exact'], 'WorkflowLevelID': ['exact'], 'WorkflowLevelStatusPeriority': ['exact'], 'WorkflowLevelID__WorkflowLevelType': ['exact']}
    ordering_fields = '__all__'

class WorkflowLevelStatusRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkflowLevelStatusSerializer
    queryset = WorkflowLevelStatus.objects.all()

class WorkflowLevelStatusShowView(generics.ListCreateAPIView):
    serializer_class = WorkflowLevelStatusShowSerializer
    queryset = WorkflowLevelStatusShow.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusID': ['exact'], 'WorkflowLevelStatusID': ['exact']}
    ordering_fields = '__all__'

class WorkflowLevelStatusShowCreate(generics.ListCreateAPIView):
    serializer_class = WorkflowLevelStatusShowSerializer
    queryset = WorkflowLevelStatusShow.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'StatusID': ['exact'], 'WorkflowLevelStatusID': ['exact']}
    ordering_fields = '__all__'

class WorkflowLevelStatusShowRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkflowLevelStatusShowSerializer
    queryset = WorkflowLevelStatusShow.objects.all()
    
class WRTaskView(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            if assets[0].WorkRequestID:
                return queryset.filter(AssetClassID = assets[0].WorkRequestID.AssetSubdivisionID.AssetChildID)
            else:
                pm = TemplateSchualingDate.objects.filter(WorkOrderID = asset)
                pm2 = WOTemplateSchualing.objects.filter(id = pm[0].WOTemplateSchualingID.id)
                pm3 = WOTemplateAsset.objects.filter(WOTemplateID = pm2[0].WOTemplateID)
                pm4 = AssetSubdivision.objects.filter(id__in = pm3.values('AssetSubdivisionID'))
                return queryset.filter(AssetClassID__in = pm4.values('AssetChildID'))        
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TaskCode': ['icontains'], 'TaskName': ['icontains'], 'TaskDescription': ['icontains'], 'FrequencyName': ['exact'], 'FrequencyAmount': ['exact'], 'DurationOfDo': ['icontains'],
                  'Functor': ['icontains'], 'TaskTypeID': ['exact'], 'JobCategoryID': ['exact'], 'AssetClassID': ['exact'], 'TaskTypeID__TaskTypeName': ['icontains'], 'JobCategoryID__JobCategoryName': ['icontains']}
    ordering_fields = ['id', 'TaskCode', 'TaskName', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo', 'Functor', 'TaskTypeID__TaskTypeName', 'JobCategoryID__JobCategoryName',]
    
class WRTaskCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            if assets[0].WorkRequestID:
                return queryset.filter(AssetClassID = assets[0].WorkRequestID.AssetSubdivisionID.AssetChildID)
            else:
                pm = TemplateSchualingDate.objects.filter(WorkOrderID = asset)
                pm2 = WOTemplateSchualing.objects.filter(id = pm[0].WOTemplateSchualingID.id)
                pm3 = WOTemplateAsset.objects.filter(WOTemplateID = pm2[0].WOTemplateID)
                pm4 = AssetSubdivision.objects.filter(id__in = pm3.values('AssetSubdivisionID'))
                return queryset.filter(AssetClassID__in = pm4.values('AssetChildID'))        
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TaskCode': ['icontains'], 'TaskName': ['icontains'], 'TaskDescription': ['icontains'], 'FrequencyName': ['exact'], 'FrequencyAmount': ['exact'], 'DurationOfDo': ['icontains'],
                  'Functor': ['icontains'], 'TaskTypeID': ['exact'], 'JobCategoryID': ['exact'], 'AssetClassID': ['exact'], 'TaskTypeID__TaskTypeName': ['icontains'], 'JobCategoryID__JobCategoryName': ['icontains']}
    ordering_fields = ['id', 'TaskCode', 'TaskName', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo', 'Functor', 'TaskTypeID__TaskTypeName', 'JobCategoryID__JobCategoryName',]
    
class WRTaskRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].WorkRequestID.AssetSubdivisionID.AssetChildID)
        return queryset

class TaskTempView(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('AssetSubdivisionID', '')
        wo = self.request.query_params.get('WOTemplateAssetID', '')
        if asset:
            asset = asset
        elif wo:
            woi = WOTemplateAsset.objects.filter(id = wo)
            asset = woi[0].AssetSubdivisionID.id
        if asset:
            assets=AssetSubdivision.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].AssetChildID)
        return queryset
    ordering_fields = '__all__'
    filter_backends =  (DjangoFilterBackend, OrderingFilter)


class TaskTempCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('AssetSubdivisionID', '')
        wo = self.request.query_params.get('WOTemplateAssetID', '')
        if asset:
            asset = asset
        elif wo:
            woi = WOTemplateAsset.objects.filter(id = wo)
            asset = woi[0].AssetSubdivisionID.id
        if asset:
            assets=AssetSubdivision.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].AssetChildID)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filter_fields = {'id': ['exact'], 'TaskCode': ['icontains'], 'TaskName': ['icontains'], 'TaskDescription': ['icontains'], 'FrequencyName': ['icontains'], 'FrequencyAmount': ['icontains'], 'DurationOfDo': ['icontains'],
                  'Functor': ['icontains'], 'TaskTypeID': ['exact'], 'JobCategoryID': ['exact'], 'AssetClassID': ['exact']}
    ordering_fields = '__all__'

class TaskTempRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('AssetSubdivisionID', '')
        wo = self.request.query_params.get('WOTemplateAssetID', '')
        if asset:
            asset = asset
        elif wo:
            woi = WOTemplateAsset.objects.filter(id = wo)
            asset = woi[0].AssetSubdivisionID.id
        if asset:
            assets=AssetSubdivision.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].AssetChildID)
        return queryset

class StatusWRView(generics.ListCreateAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        wr=self.request.query_params.get('WorkRequestID', '')
        if wr:
            wrs=WorkRequest.objects.filter(id = wr)
            wf=WorkflowLevelStatus.objects.filter(StatusID = wrs[0].StatusID)
            st=WorkflowLevelStatusShow.objects.filter(WorkflowLevelStatusID = wf[0].id)
            stt=WorkflowLevelStatus.objects.filter(StatusID__in = st.values('StatusID'), WorkflowLevelID__WorkflowLevelType='WR')
            
            return queryset.filter(id__in = stt.values('StatusID'))
        return queryset
    ordering_fields = '__all__'
    filter_backends =  (DjangoFilterBackend, OrderingFilter)


class StatusWRCreate(generics.ListCreateAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        wr=self.request.query_params.get('WorkRequestID', '')
        if wr:
            wrs=WorkRequest.objects.filter(id = wr)
            wf=WorkflowLevelStatus.objects.filter(StatusID = wrs[0].StatusID)
            st=WorkflowLevelStatusShow.objects.filter(WorkflowLevelStatusID = wf[0].id)
            stt=WorkflowLevelStatus.objects.filter(StatusID__in = st.values('StatusID'), WorkflowLevelID__WorkflowLevelType='WR')
            
            return queryset.filter(id__in = stt.values('StatusID'))
        return queryset
    ordering_fields = '__all__'
    filter_backends =  (DjangoFilterBackend, OrderingFilter)

class StatusWRRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        wr=self.request.query_params.get('WorkRequestID', '')
        if wr:
            wrs=WorkRequest.objects.filter(id = wr)
            wf=WorkflowLevelStatus.objects.filter(StatusID = wrs[0].StatusID)
            st=WorkflowLevelStatusShow.objects.filter(WorkflowLevelStatusID = wf[0].id)
            stt=WorkflowLevelStatus.objects.filter(StatusID__in = st.values('StatusID'), WorkflowLevelID__WorkflowLevelType='WR')
            
            return queryset.filter(id__in = stt.values('StatusID'))            
        return queryset

class StatusWOView(generics.ListCreateAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        wr=self.request.query_params.get('WorkOrderID', '')
        if wr:
            wrs=WorkOrder.objects.filter(id = wr)
            wf=WorkflowLevelStatus.objects.filter(StatusID = wrs[0].StatusID)
            st=WorkflowLevelStatusShow.objects.filter(WorkflowLevelStatusID = wf[0].id)
            stt=WorkflowLevelStatus.objects.filter(StatusID__in = st.values('StatusID'), WorkflowLevelID__WorkflowLevelType='WO')
            
            return queryset.filter(id__in = stt.values('StatusID'))
        return queryset
    ordering_fields = '__all__'
    filter_backends =  (DjangoFilterBackend, OrderingFilter)


class StatusWOCreate(generics.ListCreateAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        wr=self.request.query_params.get('WorkOrderID', '')
        if wr:
            wrs=WorkOrder.objects.filter(id = wr)
            wf=WorkflowLevelStatus.objects.filter(StatusID = wrs[0].StatusID)
            st=WorkflowLevelStatusShow.objects.filter(WorkflowLevelStatusID = wf[0].id)
            stt=WorkflowLevelStatus.objects.filter(StatusID__in = st.values('StatusID'), WorkflowLevelID__WorkflowLevelType='WO')
            
            return queryset.filter(id__in = stt.values('StatusID'))
        return queryset
    ordering_fields = '__all__'
    filter_backends =  (DjangoFilterBackend, OrderingFilter)

class StatusWORetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        wr=self.request.query_params.get('WorkOrderID', '')
        if wr:
            wrs=WorkOrder.objects.filter(id = wr)
            wf=WorkflowLevelStatus.objects.filter(StatusID = wrs[0].StatusID)
            st=WorkflowLevelStatusShow.objects.filter(WorkflowLevelStatusID = wf[0].id)
            stt=WorkflowLevelStatus.objects.filter(StatusID__in = st.values('StatusID'), WorkflowLevelID__WorkflowLevelType='WO')
            
            return queryset.filter(id__in = stt.values('StatusID'))
        return queryset
