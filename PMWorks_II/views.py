from rest_framework import generics

from .models import AssetCategory, AssetClass, AssetClassSubdivision, FailureMode, FailureCause, SpecificData, \
    JobCategory, Department, Personnel, AssetPriority, Location, Asset, AssetSubdivision, SparePartDimension, \
    SparePartCategory, Document, AssetSpecificData, SparePart, TaskType, AssetClassTask, Supplier, SupplierSpecific, \
    SupplierSpecificData, WorkRequest, TypeWr, WorkPriority, WorkOrder, WOSupplier, WOPersonnel, Delay, WODelay, \
    WOSparePart, WOTask, Frequency, WOTemplate, WOTemplateSchualing, AssetClassSpecificData, AssetClassDocument, \
    AssetSubdivisionSparePart, PersonnelJobCategory, WorkRequestFailureCause, WOTemplateType, WOTemplate, \
    WOActivityTemplateTbl, TemplateSchualingDate

from .serializers import AssetCategorySerializer, AssetClassSerializer, AssetClassSubdivisionSerializer, \
    AssetClassSpecificDataSerializer, SpecificDataSerializer, FailureModeSerializer, LocationSerializer, \
    AssetPrioritySerializer, DocumentSerializer, AssetClassDocumentSerializer, AssetSerializer, AssetSpecificDataSerializer, \
    AssetSubdivisionSerializer, SparePartDimensionSerializer, SparePartCategorySerializer, SparePartSerializer, \
    AssetSubdivisionSparePartSerializer, TaskTypeSerializer, JobCategorySerializer, DepartmentSerializer, PersonnelSerializer, \
    PersonnelJobCategorySerializer, TypeWrSerializer, WorkPrioritySerializer, SupplierSerializer, SupplierSpecificSerializer, \
    SupplierSpecificDataSerializer, AssetClassTaskSerializer, WorkRequestSerializer, WorkOrderSerializer, \
    WOSupplierSerializer, WOPersonnelSerializer, DelaySerializer, WODelaySerializer, WOSparePartSerializer, \
    WOTaskSerializer, UserSerializer, AssetSubdivisionAssetSerializer, FailureCauseSerializer, WorkRequestFailureCauseSerializer, \
    WOTemplateTypeSerializer, WOTemplateSerializer, WOActivityTemplateSerializer, WOTemplateSchualingSerializer, FrequencySerializer, \
    TemplateSchualingDateSerializer

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import rest_framework as filters
import django_filters
from django.contrib.auth.models import User

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class AssetCatFath(filters.FilterSet):
    AssetClassFather = NumberInFilter(field_name='AssetClassFather', lookup_expr='in')
    AssetClassFather__isnull = filters.BooleanFilter(field_name='AssetClassFather', lookup_expr='isnull')
    AssetCategoryCode = filters.CharFilter(field_name='AssetCategoryCode')
    AssetCategoryName = filters.CharFilter(field_name='AssetCategoryName')


class AssetCategoryView(generics.ListCreateAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['AssetCategoryName', 'id', 'AssetClassFather__AssetCategoryName', 'AssetCategoryCode',]
    filter_class = AssetCatFath
    ordering_fields = ['AssetCategoryName', 'id', 'AssetClassFather__AssetCategoryName', 'AssetCategoryCode',]


class AssetCategoryCreate(generics.ListCreateAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['AssetCategoryName', 'id', 'AssetClassFather__AssetCategoryName', 'AssetCategoryCode',]
    filter_class = AssetCatFath
    ordering_fields = ['AssetCategoryName', 'id', 'AssetClassFather__AssetCategoryName', 'AssetCategoryCode',]


class AssetCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()


class AssetClassView(generics.ListCreateAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['AssetClassName', 'id', 'AssetClassCode', 'AssetCategoryID__AssetCategoryName', ]
    ordering_fields = ['AssetClassName', 'id', 'AssetClassCode', 'AssetCategoryID__AssetCategoryName', ]


class AssetClassCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['AssetClassName', 'id', 'AssetClassCode', 'AssetCategoryID__AssetCategoryName', ]
    ordering_fields = ['AssetClassName', 'id', 'AssetClassCode', 'AssetCategoryID__AssetCategoryName', ]
    

class AssetClassRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()


class AssetClassSubdivisionView(generics.ListCreateAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['AssetClassFatherID', 'id', 'AssetClassChildID', 'AssetClassFatherID__AssetClassName', 'AssetClassFatherID__AssetClassCode', 'AssetClassChildID__AssetClassName', 'AssetClassChildID__AssetClassCode', ]
    ordering_fields = ['AssetClassFatherID', 'id', 'AssetClassChildID', 'AssetClassFatherID__AssetClassName', 'AssetClassFatherID__AssetClassCode', 'AssetClassChildID__AssetClassName', 'AssetClassChildID__AssetClassCode', ]


class AssetClassSubdivisionCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['AssetClassFatherID', 'id', 'AssetClassChildID', 'AssetClassFatherID__AssetClassName', 'AssetClassFatherID__AssetClassCode', 'AssetClassChildID__AssetClassName', 'AssetClassChildID__AssetClassCode', ]
    ordering_fields = ['AssetClassFatherID', 'id', 'AssetClassChildID', 'AssetClassFatherID__AssetClassName', 'AssetClassFatherID__AssetClassCode', 'AssetClassChildID__AssetClassName', 'AssetClassChildID__AssetClassCode', ]


class AssetClassSubdivisionRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()


class AssetClassSpecificDataView(generics.ListCreateAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['AssetClassID', 'id', 'SpecificDataID', ]
    ordering_fields = '__all__'


class AssetClassSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['AssetClassID', 'id', 'SpecificDataID', ]
    ordering_fields = '__all__'


class AssetClassSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()


class SpecificDataView(generics.ListCreateAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['SpecificDataCode', 'id', 'SpecificDataName', 'Measurment', ]
    ordering_fields = '__all__'


class SpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['SpecificDataCode', 'id', 'SpecificDataName', 'Measurment', ]
    ordering_fields = '__all__'


class SpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()


class FailureModeView(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'FailureModeCode', 'FailureModeName', 'FailureModeDescription', 'AssetClassID', ]
    ordering_fields = '__all__'


class FailureModeCreate(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'FailureModeCode', 'FailureModeName', 'FailureModeDescription', 'AssetClassID', ]
    ordering_fields = '__all__'


class FailureModeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()

class FailureCauseView(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'FailureCauseCode', 'FailureCauseName', 'FailureCauseDescription', 'FailureModeID', ]
    ordering_fields = '__all__'


class FailureCauseCreate(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'FailureCauseCode', 'FailureCauseName', 'FailureCauseDescription', 'FailureModeID', ]
    ordering_fields = '__all__'


class FailureCauseRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()

class LocationFath(filters.FilterSet):
    LocationFatherID = NumberInFilter(field_name='LocationFatherID', lookup_expr='in')
    LocationFatherID__isnull = filters.BooleanFilter(field_name='LocationFatherID', lookup_expr='isnull')


class LocationView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'LocationCode', 'LocationName', 'LocationFatherID', ]
    filter_class = LocationFath
    ordering_fields = '__all__'


class LocationCreate(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'LocationCode', 'LocationName', 'LocationFatherID', ]
    filter_class = LocationFath
    ordering_fields = '__all__'


class LocationRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class DocumentView(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'DocumentCode', 'DocumentName', 'DocumentDescription', ]
    ordering_fields = '__all__'


class DocumentCreate(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'DocumentCode', 'DocumentName', 'DocumentDescription', ]
    ordering_fields = '__all__'


class DocumentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class AssetPriorityView(generics.ListCreateAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetPriorityCode', 'AssetPriorityName', 'AssetPriorityValue', ]
    ordering_fields = '__all__'


class AssetPriorityCreate(generics.ListCreateAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetPriorityCode', 'AssetPriorityName', 'AssetPriorityValue', ]
    ordering_fields = '__all__'


class AssetPriorityRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()


class AssetClassDocumentView(generics.ListCreateAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetClassID', 'DocumentID', ]
    ordering_fields = '__all__'


class AssetClassDocumentCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetClassID', 'DocumentID', ]
    ordering_fields = '__all__'


class AssetClassDocumentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()


class AssetView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetCode', 'AssetName', 'InstallationDate', 'AssetPriorityID', 'LocationID',
                        'AssetClassID', ]
    ordering_fields = '__all__'


class AssetCreate(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetCode', 'AssetName', 'InstallationDate', 'AssetPriorityID', 'LocationID',
                        'AssetClassID', ]
    ordering_fields = '__all__'


class AssetRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()


class AssetSpecificDataView(generics.ListCreateAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetSubdivisionID', 'SpecificDataID', 'SpecificAmount', ]
    ordering_fields = '__all__'


class AssetSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetSubdivisionID', 'SpecificDataID', 'SpecificAmount', ]
    ordering_fields = '__all__'


class AssetSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()


class AssetSubdivisionView(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSerializer
    queryset = AssetSubdivision.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetID', 'AssetChildID', 'AssetSubdivisionFatherID','tree', 'fakelocation', 'AssetClassCodeChain', 'AssetClassNameChain', 'idChain', 'AssetCode', 'AssetName'] 
    ordering_fields = '__all__'


class AssetSubdivisionCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSerializer
    queryset = AssetSubdivision.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetID', 'AssetChildID', 'AssetSubdivisionFatherID','tree', 'fakelocation', 'AssetClassCodeChain', 'AssetClassNameChain', 'idChain', 'AssetCode', 'AssetName']
    ordering_fields = '__all__'


class AssetSubdivisionRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionSerializer
    queryset = AssetSubdivision.objects.all()


class SparePartDimensionView(generics.ListCreateAPIView):
    serializer_class = SparePartDimensionSerializer
    queryset = SparePartDimension.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SparePartDimensionCode', 'SparePartDimensionName', ]
    ordering_fields = '__all__'


class SparePartDimensionCreate(generics.ListCreateAPIView):
    serializer_class = SparePartDimensionSerializer
    queryset = SparePartDimension.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SparePartDimensionCode', 'SparePartDimensionName', ]
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
    filterset_fields = ['id', 'SparePartCategoryCode', 'SparePartCategoryName', 'SparePartCategoryFather',]
    filter_class = SparePartCatFath
    ordering_fields = '__all__'


class SparePartCategoryCreate(generics.ListCreateAPIView):
    serializer_class = SparePartCategorySerializer
    queryset = SparePartCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SparePartCategoryCode', 'SparePartCategoryName', 'SparePartCategoryFather',]
    filter_class = SparePartCatFath
    ordering_fields = '__all__'


class SparePartCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartCategorySerializer
    queryset = SparePartCategory.objects.all()


class SparePartView(generics.ListCreateAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SparePartCode', 'SparePartName', 'SparePartCategoryID', 'SparePartDimensionID', ]
    ordering_fields = '__all__'


class SparePartCreate(generics.ListCreateAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SparePartCode', 'SparePartName', 'SparePartCategoryID', 'SparePartDimensionID', ]
    ordering_fields = '__all__'


class SparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()


class AssetSubdivisionSparePartView(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetSubdivisionID', 'SparePartID', ]
    ordering_fields = '__all__'


class AssetSubdivisionSparePartCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'AssetSubdivisionID', 'SparePartID', ]
    ordering_fields = '__all__'


class AssetSubdivisionSparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()

class TaskTypeView(generics.ListCreateAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TaskTypeCode', 'TaskTypeName', 'TaskTypeDescription', ]
    ordering_fields = '__all__'


class TaskTypeCreate(generics.ListCreateAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TaskTypeCode', 'TaskTypeName', 'TaskTypeDescription', ]
    ordering_fields = '__all__'


class TaskTypeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()


class JobCategoryView(generics.ListCreateAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'JobCategoryCode', 'JobCategoryName', ]
    ordering_fields = '__all__'


class JobCategoryCreate(generics.ListCreateAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'JobCategoryCode', 'JobCategoryName', ]
    ordering_fields = '__all__'


class JobCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'DepartmentCode', 'DepartmentName', ]
    ordering_fields = '__all__'


class DepartmentCreate(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'DepartmentCode', 'DepartmentName', ]
    ordering_fields = '__all__'


class DepartmentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class PersonnelView(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'PersonnelCode', 'PersonnelNetCode', 'PersonnelName', 'PersonnelFamily', 'PersonnelMobile',
                  'DepartmentID', ]
    ordering_fields = '__all__'


class PersonnelCreate(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'PersonnelCode', 'PersonnelNetCode', 'PersonnelName', 'PersonnelFamily', 'PersonnelMobile',
                  'DepartmentID', ]
    ordering_fields = '__all__'


class PersonnelRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()


class PersonnelJobCategoryView(generics.ListCreateAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'PersonnelID', 'JobCategoryID', ]
    ordering_fields = '__all__'


class PersonnelJobCategoryCreate(generics.ListCreateAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'PersonnelID', 'JobCategoryID', ]
    ordering_fields = '__all__'


class PersonnelJobCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()


class TypeWrView(generics.ListCreateAPIView):
    serializer_class = TypeWrSerializer
    queryset = TypeWr.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TypeWrCode', 'TypeWrName', ]
    ordering_fields = '__all__'


class TypeWrCreate(generics.ListCreateAPIView):
    serializer_class = TypeWrSerializer
    queryset = TypeWr.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TypeWrCode', 'TypeWrName', ]
    ordering_fields = '__all__'


class TypeWrRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =TypeWrSerializer
    queryset = TypeWr.objects.all()


class WorkPriorityView(generics.ListCreateAPIView):
    serializer_class = WorkPrioritySerializer
    queryset = WorkPriority.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkPriorityCode', 'WorkPriorityName', 'WorkPriorityValue', ]
    ordering_fields = '__all__'


class WorkPriorityCreate(generics.ListCreateAPIView):
    serializer_class = WorkPrioritySerializer
    queryset = WorkPriority.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkPriorityCode', 'WorkPriorityName', 'WorkPriorityValue', ]
    ordering_fields = '__all__'


class WorkPriorityRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =WorkPrioritySerializer
    queryset = WorkPriority.objects.all()


class SupplierView(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SupplierCode', 'SupplierName', ]
    ordering_fields = '__all__'


class SupplierCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SupplierCode', 'SupplierName', ]
    ordering_fields = '__all__'


class SupplierRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierSpecificView(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SupplierSpecificCode', 'SupplierSpecificName', ]
    ordering_fields = '__all__'


class SupplierSpecificCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SupplierSpecificCode', 'SupplierSpecificName', ]
    ordering_fields = '__all__'


class SupplierSpecificRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()


class SupplierSpecificDataView(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SupplierID', 'SupplierSpecificID', 'SpecificAmount', ]
    ordering_fields = '__all__'


class SupplierSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'SupplierID', 'SupplierSpecificID', 'SpecificAmount', ]
    ordering_fields = '__all__'


class SupplierSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()


class AssetClassTaskView(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TaskCode', 'TaskName', 'TaskDescription', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo',
                  'Functor', 'TaskTypeID', 'JobCategoryID', 'AssetClassID', ]
    ordering_fields = '__all__'


class AssetClassTaskCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TaskCode', 'TaskName', 'TaskDescription', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo',
                  'Functor', 'TaskTypeID', 'JobCategoryID', 'AssetClassID', ]
    ordering_fields = '__all__'


class AssetClassTaskRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()


class WorkRequestView(generics.ListCreateAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WRDate', 'WRDateOfRegistration', 'AssetSubdivisionID', 'FailureModeID',
                        'WorkPriorityID', 'TypeWrID', ]
    ordering_fields = '__all__'


class WorkRequestCreate(generics.ListCreateAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WRDate', 'WRDateOfRegistration', 'AssetSubdivisionID', 'FailureModeID',
                        'WorkPriorityID', 'TypeWrID', ]
    ordering_fields = '__all__'


class WorkRequestRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()


class WorkOrderView(generics.ListCreateAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WODateOfRegistration', 'WODescription', 'DateOfPlanStart', 'DateOfPlanFinish', 'WorkRequestID', ]
    ordering_fields = '__all__'


class WorkOrderCreate(generics.ListCreateAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WODateOfRegistration', 'WODescription', 'DateOfPlanStart', 'DateOfPlanFinish', 'WorkRequestID', ]
    ordering_fields = '__all__'


class WorkOrderRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()


class WOSupplierView(generics.ListCreateAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkStartDate', 'WorkFinishDate', 'WorkOrderID', 'SupplierID', ]
    ordering_fields = '__all__'


class WOSupplierCreate(generics.ListCreateAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkStartDate', 'WorkFinishDate', 'WorkOrderID', 'SupplierID', ]
    ordering_fields = '__all__'


class WOSupplierRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()


class WOPersonnelView(generics.ListCreateAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkDate', 'WorkTime', 'WorkOrderID', 'PersonnelID', ]
    ordering_fields = '__all__'


class WOPersonnelCreate(generics.ListCreateAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkDate', 'WorkTime', 'WorkOrderID', 'PersonnelID', ]
    ordering_fields = '__all__'


class WOPersonnelRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()


class DelayView(generics.ListCreateAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'DelayCode', 'DelayName', ]
    ordering_fields = '__all__'


class DelayCreate(generics.ListCreateAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'DelayCode', 'DelayName', ]
    ordering_fields = '__all__'


class DelayRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()


class WODelayView(generics.ListCreateAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'DayAmount', 'HourAmount', 'WODelayDescription', 'WorkOrderID', 'DelayID', ]
    ordering_fields = '__all__'


class WODelayCreate(generics.ListCreateAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'DayAmount', 'HourAmount', 'WODelayDescription', 'WorkOrderID', 'DelayID', ]
    ordering_fields = '__all__'


class WODelayRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()


class WOSparePartView(generics.ListCreateAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkOrderID', 'SparePartID', 'SparePartAmount', ]
    ordering_fields = '__all__'


class WOSparePartCreate(generics.ListCreateAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkOrderID', 'SparePartID', 'SparePartAmount', ]
    ordering_fields = '__all__'


class WOSparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()


class WOTaskView(generics.ListCreateAPIView):
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkOrderID', 'TaskID', 'WOTaskSituationOfDo', ]
    ordering_fields = '__all__'


class WOTaskCreate(generics.ListCreateAPIView):
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WorkOrderID', 'TaskID', 'WOTaskSituationOfDo', ]
    ordering_fields = '__all__'


class WOTaskRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()

class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'username', 'first_name', 'last_name', 'password',
                  'email', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', ]
    ordering_fields = '__all__'


class UserCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'username', 'first_name', 'last_name', 'password',
                  'email', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', ]
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
            return queryset.filter(AssetClassID = assetclass[0].AssetChildID)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'


class FailureAssetModeCreate(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer

    def get_queryset(self):
        queryset = FailureMode.objects.all()
        asset=self.request.query_params.get('AssetClassID', '')
        if asset:
            assetclass=AssetSubdivision.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assetclass[0].AssetChildID.id)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'FailureModeCode', 'FailureModeName', 'FailureModeDescription', 'AssetClassID', ]
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
    filterset_fields = ['id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation', ]
    ordering_fields = '__all__'


class AssetSubdivisionAssetCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation')
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation', ]
    ordering_fields = '__all__'


class AssetSubdivisionAssetRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation')


class WorkRequestFailureCauseView(generics.ListCreateAPIView):
    serializer_class = WorkRequestFailureCauseSerializer
    queryset = WorkRequestFailureCause.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['WorkRequestID', 'id', 'FailureCauseID', ]
    ordering_fields = '__all__'


class WorkRequestFailureCauseCreate(generics.ListCreateAPIView):
    serializer_class = WorkRequestFailureCauseSerializer
    queryset = WorkRequestFailureCause.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['WorkRequestID', 'id', 'FailureCauseID', ]
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
    filterset_fields = ['id', 'FailureCauseCode', 'FailureCauseName', 'FailureModeID', ]
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
    filterset_fields = ['id', 'SparePartCode', 'SparePartName', 'SparePartCategoryID', 'SparePartDimensionID', ]
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
    filterset_fields = ['id', 'WOTemplateTypeCode', 'WOTemplateTypeName', 'WOTemplateTypeDescription', ]
    ordering_fields = '__all__'


class WOTemplateTypeCreate(generics.ListCreateAPIView):
    serializer_class = WOTemplateTypeSerializer
    queryset = WOTemplateType.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WOTemplateTypeCode', 'WOTemplateTypeName', 'WOTemplateTypeDescription', ]
    ordering_fields = '__all__'


class WOTemplateTypeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTemplateTypeSerializer
    queryset = WOTemplateType.objects.all()


class WOTemplateView(generics.ListCreateAPIView):
    serializer_class = WOTemplateSerializer
    queryset = WOTemplate.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WOTemplateCode', 'WOTemplateName', 'WOTemplateDurationDay', 'WOTemplateDurationHour',
                          'WOTemplateAlarmDay', 'WOTemplateAlarmHour', 'DepartmentID', 'WOTemplateTypeID', ]
    ordering_fields = '__all__'


class WOTemplateCreate(generics.ListCreateAPIView):
    serializer_class = WOTemplateSerializer
    queryset = WOTemplate.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WOTemplateCode', 'WOTemplateName', 'WOTemplateDurationDay', 'WOTemplateDurationHour',
                          'WOTemplateAlarmDay', 'WOTemplateAlarmHour', 'DepartmentID', 'WOTemplateTypeID', ]
    ordering_fields = '__all__'


class WOTemplateRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTemplateSerializer
    queryset = WOTemplate.objects.all()

    
class WOActivityTemplateView(generics.ListCreateAPIView):
    serializer_class = WOActivityTemplateSerializer
    queryset = WOActivityTemplateTbl.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WOTemplateID', 'AssetClassTaskID', 'AssetSubdivisionID', ]
    ordering_fields = '__all__'


class WOActivityTemplateCreate(generics.ListCreateAPIView):
    serializer_class = WOActivityTemplateSerializer
    queryset = WOActivityTemplateTbl.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WOTemplateID', 'AssetClassTaskID', 'AssetSubdivisionID', ]
    ordering_fields = '__all__'


class WOActivityTemplateRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOActivityTemplateSerializer
    queryset = WOActivityTemplateTbl.objects.all()


class WOTemplateSchualingView(generics.ListCreateAPIView):
    serializer_class = WOTemplateSchualingSerializer
    queryset = WOTemplateSchualing.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WOTemplateSchualingStartDate', 'WOTemplateSchualingFinishDate', 'AmountFrequency', 'Status',
                          'WOTemplateID', 'FrequencyID', ]
    ordering_fields = '__all__'


class WOTemplateSchualingCreate(generics.ListCreateAPIView):
    serializer_class = WOTemplateSchualingSerializer
    queryset = WOTemplateSchualing.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'WOTemplateSchualingStartDate', 'WOTemplateSchualingFinishDate', 'AmountFrequency', 'Status',
                          'WOTemplateID', 'FrequencyID', ]
    ordering_fields = '__all__'

class WOTemplateSchualingRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTemplateSchualingSerializer
    queryset = WOTemplateSchualing.objects.all()


class FrequencyView(generics.ListCreateAPIView):
    serializer_class = FrequencySerializer
    queryset = Frequency.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'FrequencyCode', 'FrequencyName', ]
    ordering_fields = '__all__'


class FrequencyCreate(generics.ListCreateAPIView):
    serializer_class = FrequencySerializer
    queryset = Frequency.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'FrequencyCode', 'FrequencyName', ]
    ordering_fields = '__all__'


class FrequencyRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FrequencySerializer
    queryset = Frequency.objects.all()

class TemplateSchualingDateView(generics.ListCreateAPIView):
    serializer_class = TemplateSchualingDateSerializer
    queryset = TemplateSchualingDate.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TemplateSchualingDate', 'WOTemplateSchualingID', 'StatusOfDo', ]
    ordering_fields = '__all__'


class TemplateSchualingDateCreate(generics.ListCreateAPIView):
    serializer_class = TemplateSchualingDateSerializer
    queryset = TemplateSchualingDate.objects.all()
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TemplateSchualingDate', 'WOTemplateSchualingID', 'StatusOfDo', ]
    ordering_fields = '__all__'


class TemplateSchualingDateRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TemplateSchualingDateSerializer
    queryset = TemplateSchualingDate.objects.all()


class WRTaskView(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].WorkRequestID.AssetSubdivisionID.AssetChildID)
        return queryset
    ordering_fields = '__all__'
    filter_backends =  (DjangoFilterBackend, OrderingFilter)


class WRTaskCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].WorkRequestID.AssetSubdivisionID.AssetChildID)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TaskCode', 'TaskName', 'TaskDescription', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo',
                  'Functor', 'TaskTypeID', 'JobCategoryID', 'AssetClassID', ]
    ordering_fields = '__all__'

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
        if asset:
            assets=AssetSubdivision.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].AssetChildID)
        return queryset
    filter_backends =  (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['id', 'TaskCode', 'TaskName', 'TaskDescription', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo',
                  'Functor', 'TaskTypeID', 'JobCategoryID', 'AssetClassID', ]
    ordering_fields = '__all__'

class TaskTempRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('AssetSubdivisionID', '')
        if asset:
            assets=AssetSubdivision.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].AssetChildID)
        return queryset
