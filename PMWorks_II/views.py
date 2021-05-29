from rest_framework import generics

from .models import AssetCategory, AssetClass, AssetClassSubdivision, FailureMode, FailureCause, SpecificData, \
    JobCategory, Department, Personnel, AssetPriority, Location, Asset, AssetSubdivision, SparePartDimension, \
    SparePartCategory, Document, AssetSpecificData, SparePart, TaskType, AssetClassTask, Supplier, SupplierSpecific, \
    SupplierSpecificData, WorkRequest, TypeWr, WorkPriority, WorkOrder, WOSupplier, WOPersonnel, Delay, WODelay, \
    WOSparePart, WOTask, Frequency, WOTemplate, WOTemplateSchualing, AssetClassSpecificData, AssetClassDocument, \
    AssetSubdivisionSparePart, PersonnelJobCategory, WorkRequestFailureCause

from .serializers import AssetCategorySerializer, AssetClassSerializer, AssetClassSubdivisionSerializer, \
    AssetClassSpecificDataSerializer, SpecificDataSerializer, FailureModeSerializer, LocationSerializer, \
    AssetPrioritySerializer, DocumentSerializer, AssetClassDocumentSerializer, AssetSerializer, AssetSpecificDataSerializer, \
    AssetSubdivisionSerializer, SparePartDimensionSerializer, SparePartCategorySerializer, SparePartSerializer, \
    AssetSubdivisionSparePartSerializer, TaskTypeSerializer, JobCategorySerializer, DepartmentSerializer, PersonnelSerializer, \
    PersonnelJobCategorySerializer, TypeWrSerializer, WorkPrioritySerializer, SupplierSerializer, SupplierSpecificSerializer, \
    SupplierSpecificDataSerializer, AssetClassTaskSerializer, WorkRequestSerializer, WorkOrderSerializer, \
    WOSupplierSerializer, WOPersonnelSerializer, DelaySerializer, WODelaySerializer, WOSparePartSerializer, \
    WOTaskSerializer, UserSerializer, AssetSubdivisionAssetSerializer, FailureCauseSerializer, WorkRequestFailureCauseSerializer

from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
import django_filters
from django.contrib.auth.models import User

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class AssetCatFath(filters.FilterSet):
    AssetClassFather = NumberInFilter(field_name='AssetClassFather', lookup_expr='in')
    AssetClassFather__isnull = filters.BooleanFilter(field_name='AssetClassFather', lookup_expr='isnull')


class AssetCategoryView(generics.ListCreateAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AssetCategoryName', 'id', 'AssetClassFather',]
    filter_class = AssetCatFath


class AssetCategoryCreate(generics.ListCreateAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AssetCategoryName', 'id', 'AssetClassFather',]
    filter_class = AssetCatFath


class AssetCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetCategorySerializer
    queryset = AssetCategory.objects.all()


class AssetClassView(generics.ListCreateAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AssetClassName', 'id', ]


class AssetClassCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AssetClassName', 'id', ]


class AssetClassRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSerializer
    queryset = AssetClass.objects.all()


class AssetClassSubdivisionView(generics.ListCreateAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AssetClassFatherID', 'id', ]


class AssetClassSubdivisionCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AssetClassFatherID', 'id', ]


class AssetClassSubdivisionRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSubdivisionSerializer
    queryset = AssetClassSubdivision.objects.all()


class AssetClassSpecificDataView(generics.ListCreateAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AssetClassID', 'id', 'SpecificDataID', ]


class AssetClassSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AssetClassID', 'id', 'SpecificDataID', ]


class AssetClassSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassSpecificDataSerializer
    queryset = AssetClassSpecificData.objects.all()


class SpecificDataView(generics.ListCreateAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['SpecificDataCode', 'id', 'SpecificDataName', ]


class SpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['SpecificDataCode', 'id', 'SpecificDataName', ]


class SpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpecificDataSerializer
    queryset = SpecificData.objects.all()


class FailureModeView(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'FailureModeCode', 'FailureModeName', 'FailureModeDescription', 'AssetClassID', ]


class FailureModeCreate(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'FailureModeCode', 'FailureModeName', 'FailureModeDescription', 'AssetClassID', ]


class FailureModeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureModeSerializer
    queryset = FailureMode.objects.all()

class FailureCauseView(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'FailureCauseCode', 'FailureCauseName', 'FailureCauseDescription', 'FailureModeID', ]


class FailureCauseCreate(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'FailureCauseCode', 'FailureCauseName', 'FailureCauseDescription', 'FailureModeID', ]


class FailureCauseRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureCauseSerializer
    queryset = FailureCause.objects.all()

class LocationFath(filters.FilterSet):
    LocationFatherID = NumberInFilter(field_name='LocationFatherID', lookup_expr='in')
    LocationFatherID__isnull = filters.BooleanFilter(field_name='LocationFatherID', lookup_expr='isnull')


class LocationView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'LocationCode', 'LocationName', 'LocationFatherID', ]
    filter_class = LocationFath


class LocationCreate(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'LocationCode', 'LocationName', 'LocationFatherID', ]
    filter_class = LocationFath


class LocationRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class DocumentView(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'DocumentCode', 'DocumentName', 'DocumentDescription', ]


class DocumentCreate(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'DocumentCode', 'DocumentName', 'DocumentDescription', ]


class DocumentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class AssetPriorityView(generics.ListCreateAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetPriorityCode', 'AssetPriorityName', 'AssetPriorityValue', ]


class AssetPriorityCreate(generics.ListCreateAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetPriorityCode', 'AssetPriorityName', 'AssetPriorityValue', ]


class AssetPriorityRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetPrioritySerializer
    queryset = AssetPriority.objects.all()


class AssetClassDocumentView(generics.ListCreateAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetClassID', 'DocumentID', ]


class AssetClassDocumentCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetClassID', 'DocumentID', ]


class AssetClassDocumentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassDocumentSerializer
    queryset = AssetClassDocument.objects.all()


class AssetView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetCode', 'AssetName', 'InstallationDate', 'AssetPriorityID', 'LocationID',
                        'AssetClassID', ]


class AssetCreate(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetCode', 'AssetName', 'InstallationDate', 'AssetPriorityID', 'LocationID',
                        'AssetClassID', ]


class AssetRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()


class AssetSpecificDataView(generics.ListCreateAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetSubdivisionID', 'SpecificDataID', 'SpecificAmount', ]


class AssetSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetSubdivisionID', 'SpecificDataID', 'SpecificAmount', ]


class AssetSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSpecificDataSerializer
    queryset = AssetSpecificData.objects.all()


class AssetSubdivisionView(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSerializer
    queryset = AssetSubdivision.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetID', 'AssetChildID', 'AssetSubdivisionFatherID','tree', 'fakelocation', 'AssetClassCodeChain', 'AssetClassNameChain', 'idChain', 'AssetCode', 'AssetName'] 


class AssetSubdivisionCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSerializer
    queryset = AssetSubdivision.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetID', 'AssetChildID', 'AssetSubdivisionFatherID','tree', 'fakelocation', 'AssetClassCodeChain', 'AssetClassNameChain', 'idChain', 'AssetCode', 'AssetName']


class AssetSubdivisionRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionSerializer
    queryset = AssetSubdivision.objects.all()


class SparePartDimensionView(generics.ListCreateAPIView):
    serializer_class = SparePartDimensionSerializer
    queryset = SparePartDimension.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SparePartDimensionCode', 'SparePartDimensionName', ]


class SparePartDimensionCreate(generics.ListCreateAPIView):
    serializer_class = SparePartDimensionSerializer
    queryset = SparePartDimension.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SparePartDimensionCode', 'SparePartDimensionName', ]


class SparePartDimensionRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartDimensionSerializer
    queryset = SparePartDimension.objects.all()


class SparePartCatFath(filters.FilterSet):
    SparePartCategoryFather = NumberInFilter(field_name='SparePartCategoryFather', lookup_expr='in')
    SparePartCategoryFather__isnull = filters.BooleanFilter(field_name='SparePartCategoryFather', lookup_expr='isnull')


class SparePartCategoryView(generics.ListCreateAPIView):
    serializer_class = SparePartCategorySerializer
    queryset = SparePartCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SparePartCategoryCode', 'SparePartCategoryName', 'SparePartCategoryFather',]
    filter_class = SparePartCatFath


class SparePartCategoryCreate(generics.ListCreateAPIView):
    serializer_class = SparePartCategorySerializer
    queryset = SparePartCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SparePartCategoryCode', 'SparePartCategoryName', 'SparePartCategoryFather',]
    filter_class = SparePartCatFath


class SparePartCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartCategorySerializer
    queryset = SparePartCategory.objects.all()


class SparePartView(generics.ListCreateAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SparePartCode', 'SparePartName', 'SparePartCategoryID', 'SparePartDimensionID', ]


class SparePartCreate(generics.ListCreateAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SparePartCode', 'SparePartName', 'SparePartCategoryID', 'SparePartDimensionID', ]


class SparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SparePartSerializer
    queryset = SparePart.objects.all()


class AssetSubdivisionSparePartView(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetSubdivisionID', 'SparePartID', ]


class AssetSubdivisionSparePartCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'AssetSubdivisionID', 'SparePartID', ]


class AssetSubdivisionSparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionSparePartSerializer
    queryset = AssetSubdivisionSparePart.objects.all()

class TaskTypeView(generics.ListCreateAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'TaskTypeCode', 'TaskTypeName', 'TaskTypeDescription', ]


class TaskTypeCreate(generics.ListCreateAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'TaskTypeCode', 'TaskTypeName', 'TaskTypeDescription', ]


class TaskTypeRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()


class JobCategoryView(generics.ListCreateAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'JobCategoryCode', 'JobCategoryName', ]


class JobCategoryCreate(generics.ListCreateAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'JobCategoryCode', 'JobCategoryName', ]


class JobCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'DepartmentCode', 'DepartmentName', ]


class DepartmentCreate(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'DepartmentCode', 'DepartmentName', ]


class DepartmentRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class PersonnelView(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'PersonnelCode', 'PersonnelNetCode', 'PersonnelName', 'PersonnelFamily', 'PersonnelMobile',
                  'DepartmentID', ]


class PersonnelCreate(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'PersonnelCode', 'PersonnelNetCode', 'PersonnelName', 'PersonnelFamily', 'PersonnelMobile',
                  'DepartmentID', ]


class PersonnelRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()


class PersonnelJobCategoryView(generics.ListCreateAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'PersonnelID', 'JobCategoryID', ]


class PersonnelJobCategoryCreate(generics.ListCreateAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'PersonnelID', 'JobCategoryID', ]


class PersonnelJobCategoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonnelJobCategorySerializer
    queryset = PersonnelJobCategory.objects.all()


class TypeWrView(generics.ListCreateAPIView):
    serializer_class = TypeWrSerializer
    queryset = TypeWr.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'TypeWrCode', 'TypeWrName', ]


class TypeWrCreate(generics.ListCreateAPIView):
    serializer_class = TypeWrSerializer
    queryset = TypeWr.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'TypeWrCode', 'TypeWrName', ]


class TypeWrRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =TypeWrSerializer
    queryset = TypeWr.objects.all()


class WorkPriorityView(generics.ListCreateAPIView):
    serializer_class = WorkPrioritySerializer
    queryset = WorkPriority.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkPriorityCode', 'WorkPriorityName', 'WorkPriorityValue', ]


class WorkPriorityCreate(generics.ListCreateAPIView):
    serializer_class = WorkPrioritySerializer
    queryset = WorkPriority.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkPriorityCode', 'WorkPriorityName', 'WorkPriorityValue', ]


class WorkPriorityRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =WorkPrioritySerializer
    queryset = WorkPriority.objects.all()


class SupplierView(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SupplierCode', 'SupplierName', ]


class SupplierCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SupplierCode', 'SupplierName', ]


class SupplierRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierSpecificView(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SupplierSpecificCode', 'SupplierSpecificName', ]


class SupplierSpecificCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SupplierSpecificCode', 'SupplierSpecificName', ]


class SupplierSpecificRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSpecificSerializer
    queryset = SupplierSpecific.objects.all()


class SupplierSpecificDataView(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SupplierID', 'SupplierSpecificID', 'SpecificAmount', ]


class SupplierSpecificDataCreate(generics.ListCreateAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SupplierID', 'SupplierSpecificID', 'SpecificAmount', ]


class SupplierSpecificDataRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSpecificDataSerializer
    queryset = SupplierSpecificData.objects.all()


class AssetClassTaskView(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'TaskCode', 'TaskName', 'TaskDescription', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo',
                  'Functor', 'TaskTypeID', 'JobCategoryID', 'AssetClassID', ]


class AssetClassTaskCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'TaskCode', 'TaskName', 'TaskDescription', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo',
                  'Functor', 'TaskTypeID', 'JobCategoryID', 'AssetClassID', ]


class AssetClassTaskRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassTaskSerializer
    queryset = AssetClassTask.objects.all()


class WorkRequestView(generics.ListCreateAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WRDate', 'WRDateOfRegistration', 'AssetSubdivisionID', 'FailureModeID',
                        'WorkPriorityID', 'TypeWrID', ]


class WorkRequestCreate(generics.ListCreateAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WRDate', 'WRDateOfRegistration', 'AssetSubdivisionID', 'FailureModeID',
                        'WorkPriorityID', 'TypeWrID', ]


class WorkRequestRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkRequestSerializer
    queryset = WorkRequest.objects.all()


class WorkOrderView(generics.ListCreateAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WODateOfRegistration', 'WODescription', 'DateOfPlanStart', 'DateOfPlanFinish', 'WorkRequestID', ]


class WorkOrderCreate(generics.ListCreateAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WODateOfRegistration', 'WODescription', 'DateOfPlanStart', 'DateOfPlanFinish', 'WorkRequestID', ]


class WorkOrderRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()


class WOSupplierView(generics.ListCreateAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkStartDate', 'WorkFinishDate', 'WorkOrderID', 'SupplierID', ]


class WOSupplierCreate(generics.ListCreateAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkStartDate', 'WorkFinishDate', 'WorkOrderID', 'SupplierID', ]


class WOSupplierRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOSupplierSerializer
    queryset = WOSupplier.objects.all()


class WOPersonnelView(generics.ListCreateAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkDate', 'WorkTime', 'WorkOrderID', 'PersonnelID', ]


class WOPersonnelCreate(generics.ListCreateAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkDate', 'WorkTime', 'WorkOrderID', 'PersonnelID', ]


class WOPersonnelRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOPersonnelSerializer
    queryset = WOPersonnel.objects.all()


class DelayView(generics.ListCreateAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'DelayCode', 'DelayName', ]


class DelayCreate(generics.ListCreateAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'DelayCode', 'DelayName', ]


class DelayRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DelaySerializer
    queryset = Delay.objects.all()


class WODelayView(generics.ListCreateAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'DayAmount', 'HourAmount', 'WODelayDescription', 'WorkOrderID', 'DelayID', ]


class WODelayCreate(generics.ListCreateAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'DayAmount', 'HourAmount', 'WODelayDescription', 'WorkOrderID', 'DelayID', ]


class WODelayRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WODelaySerializer
    queryset = WODelay.objects.all()


class WOSparePartView(generics.ListCreateAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkOrderID', 'SparePartID', 'SparePartAmount', ]


class WOSparePartCreate(generics.ListCreateAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkOrderID', 'SparePartID', 'SparePartAmount', ]


class WOSparePartRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOSparePartSerializer
    queryset = WOSparePart.objects.all()


class WOTaskView(generics.ListCreateAPIView):
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkOrderID', 'TaskID', 'WOTaskSituationOfDo', ]


class WOTaskCreate(generics.ListCreateAPIView):
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'WorkOrderID', 'TaskID', 'WOTaskSituationOfDo', ]


class WOTaskRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WOTaskSerializer
    queryset = WOTask.objects.all()

class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username', 'first_name', 'last_name', 'password',
                  'email', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', ]


class UserCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username', 'first_name', 'last_name', 'password',
                  'email', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', ]


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


class FailureAssetModeCreate(generics.ListCreateAPIView):
    serializer_class = FailureModeSerializer

    def get_queryset(self):
        queryset = FailureMode.objects.all()
        asset=self.request.query_params.get('AssetClassID', '')
        if asset:
            assetclass=AssetSubdivision.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assetclass[0].AssetChildID.id)
        return queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'FailureModeCode', 'FailureModeName', 'FailureModeDescription', 'AssetClassID', ]


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation', ]


class AssetSubdivisionAssetCreate(generics.ListCreateAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation', ]


class AssetSubdivisionAssetRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSubdivisionAssetSerializer
    queryset = AssetSubdivision.objects.all().values('id','AssetID__AssetName','AssetID__AssetCode','AssetSubdivisionFatherID','AssetID','AssetChildID','tree','fakelocation')


class WorkRequestFailureCauseView(generics.ListCreateAPIView):
    serializer_class = WorkRequestFailureCauseSerializer
    queryset = WorkRequestFailureCause.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['WorkRequestID', 'id', 'FailureCauseID', ]


class WorkRequestFailureCauseCreate(generics.ListCreateAPIView):
    serializer_class = WorkRequestFailureCauseSerializer
    queryset = WorkRequestFailureCause.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['WorkRequestID', 'id', 'FailureCauseID', ]


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


class WRCauseCreate(generics.ListCreateAPIView):
    serializer_class = FailureCauseSerializer

    def get_queryset(self):
        queryset = FailureCause.objects.all()
        mode=self.request.query_params.get('FailureModeID', '')
        if mode:
            fmode=WorkRequest.objects.filter(id = mode)
            return queryset.filter(FailureModeID = fmode[0].FailureModeID)
        return queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'FailureCauseCode', 'FailureCauseName', 'FailureModeID', ]


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'SparePartCode', 'SparePartName', 'SparePartCategoryID', 'SparePartDimensionID', ]


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


class WRTaskView(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].WorkRequestID.AssetSubdivisionID.AssetChildID)
        return queryset


class WRTaskCreate(generics.ListCreateAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].WorkRequestID.AssetSubdivisionID.AssetChildID)
        return queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'TaskCode', 'TaskName', 'TaskDescription', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo',
                  'Functor', 'TaskTypeID', 'JobCategoryID', 'AssetClassID', ]

class WRTaskRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetClassTaskSerializer

    def get_queryset(self):
        queryset = AssetClassTask.objects.all()
        asset=self.request.query_params.get('WorkOrderID', '')
        if asset:
            assets=WorkOrder.objects.filter(id = asset)
            return queryset.filter(AssetClassID = assets[0].WorkRequestID.AssetSubdivisionID.AssetChildID)
        return queryset
