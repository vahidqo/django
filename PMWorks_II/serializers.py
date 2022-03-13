from rest_framework import serializers
from .models import AssetCategory, AssetClass, AssetClassSubdivision, FailureMode, FailureCause, SpecificData, \
    JobCategory, Department, Personnel, AssetPriority, Location, Asset, AssetSubdivision, SparePartDimension, \
    SparePartCategory, Document, AssetSpecificData, SparePart, TaskType, AssetClassTask, Supplier, SupplierSpecific, \
    SupplierSpecificData, WorkRequest, TypeWr, WorkPriority, WorkOrder, WOSupplier, WOPersonnel, Delay, WODelay, \
    WOSparePart, WOTask, Frequency, WOTemplate, WOTemplateSchualing, AssetClassSpecificData, AssetClassDocument, AssetSubdivisionSparePart, \
    PersonnelJobCategory, WorkRequestFailureCause, WOTemplateType, WOActivityTemplateTbl, TemplateSchualingDate, WOStatus, WRStatus, \
    WRWORelationStatus, Status, WorkflowLevel, WorkflowLevelStatus, WorkflowLevelStatusShow
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64FileField

class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ['pdf']

    def get_file_extension(self, filename, decoded_file):
        try:
            PyPDF2.PdfFileReader(io.BytesIO(decoded_file))
        except PyPDF2.utils.PdfReadError as e:
            logger.warning(e)
        else:
            return 'pdf'


class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = ['id', 'AssetCategoryCode', 'AssetCategoryName', 'AssetClassFather']
        extra_kwargs = {
            'AssetClassFather': {'required': False,
                                 'allow_null': True
                                 },
        }


class AssetClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClass
        fields = ['id', 'AssetClassCode', 'AssetClassName', 'AssetCategoryID']


class AssetClassSpecificDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClassSpecificData
        fields = ['id', 'AssetClassID', 'SpecificDataID']
        extra_kwargs = {
            'AssetClassID': {'required': False,
                             'allow_null': True
                             },
        }


class AssetClassSubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClassSubdivision
        fields = ['id', 'AssetClassFatherID', 'AssetClassChildID', 'AssetClassChildNumber']


class FailureModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureMode
        fields = ['id', 'FailureModeCode', 'FailureModeName', 'FailureModeDescription', 'AssetClassID']


class FailureCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureCause
        fields = ['id', 'FailureCauseCode', 'FailureCauseName', 'FailureCauseDescription', 'FailureModeID']


class SpecificDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificData
        fields = ['id', 'SpecificDataCode', 'SpecificDataName', 'Measurment']


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'JobCategoryCode', 'JobCategoryName']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'DepartmentCode', 'DepartmentName']


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['id', 'user', 'PersonnelCode', 'PersonnelNetCode', 'PersonnelName', 'PersonnelFamily', 'PersonnelMobile',
                  'DepartmentID']


class PersonnelJobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonnelJobCategory
        fields = ['id', 'PersonnelID', 'JobCategoryID']


class AssetPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetPriority
        fields = ['id', 'AssetPriorityCode', 'AssetPriorityName', 'AssetPriorityValue']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'LocationCode', 'LocationName', 'LocationFatherID', 'LocationCodeChain', 'LocationNameChain']
        extra_kwargs = {
            'LocationFatherID': {'required': False,
                                 'allow_null': True
                                 },
        }


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'AssetCode', 'AssetName', 'InstallationDate', 'AssetPriorityID', 'LocationID', 'AssetClassID', 'status', 'fakesub']


class AssetClassDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClassDocument
        fields = ['id', 'AssetClassID', 'DocumentID']
        extra_kwargs = {
            'AssetClassID': {'required': False,
                        'allow_null': True
                        },
        }


class AssetSubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetSubdivision
        fields = ['id', 'AssetID', 'AssetChildID', 'AssetSubdivisionFatherID', 'tree', 'fakelocation', 'AssetClassCodeChain', 'AssetClassNameChain', 'idChain', 'AssetCode', 'AssetName']


class SparePartDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePartDimension
        fields = ['id', 'SparePartDimensionCode', 'SparePartDimensionName']


class SparePartCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePartCategory
        fields = ['id', 'SparePartCategoryCode', 'SparePartCategoryName', 'SparePartCategoryFather']
        extra_kwargs = {
            'SparePartCategoryFather': {'required': False,
                                        'allow_null': True
                                        },
        }


class DocumentSerializer(serializers.ModelSerializer):
  
    FileAddress= PDFBase64File(required=False)

    class Meta:
        model = Document
        fields = ['id', 'DocumentCode', 'DocumentName', 'DocumentDescription', 'FileAddress']


class AssetSubdivisionSparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetSubdivisionSparePart
        fields = ['id', 'AssetSubdivisionID', 'SparePartID']


class AssetSpecificDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetSpecificData
        fields = ['id', 'AssetSubdivisionID', 'SpecificDataID', 'SpecificAmount']


class SparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePart
        fields = ['id', 'SparePartCode', 'SparePartName', 'SparePartCategoryID', 'SparePartDimensionID']


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = ['id', 'TaskTypeCode', 'TaskTypeName', 'TaskTypeDescription']


class AssetClassTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClassTask
        fields = ['id', 'TaskCode', 'TaskName', 'TaskDescription', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo',
                  'Functor', 'TaskTypeID', 'JobCategoryID', 'AssetClassID']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'SupplierCode', 'SupplierName']


class SupplierSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierSpecific
        fields = ['id', 'SupplierSpecificCode', 'SupplierSpecificName']


class SupplierSpecificDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierSpecificData
        fields = ['id', 'SupplierID', 'SupplierSpecificID', 'SpecificAmount']


class WorkRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkRequest
        fields = ['id', 'WRDate', 'WRTime', 'WRDateOfRegistration', 'WRDescription', 'WRTimeOfRegistration', 'AssetSubdivisionID', 'FailureModeID',
                  'WorkPriorityID', 'TypeWrID', 'StatusID']


class TypeWrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeWr
        fields = ['id', 'TypeWrCode', 'TypeWrName']


class WorkPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPriority
        fields = ['id', 'WorkPriorityCode', 'WorkPriorityName', 'WorkPriorityValue']


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ['id', 'WODateOfRegistration', 'WODescription', 'DateOfPlanStart', 'DateOfPlanFinish', 'WorkRequestID', 'StatusID', 'DepartmentID', 'DateOfStart', 'DateOfFinish']


class WOSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOSupplier
        fields = ['id', 'WorkStartDate', 'WorkFinishDate', 'WorkOrderID', 'SupplierID']


class WOPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOPersonnel
        fields = ['id', 'WorkDate', 'WorkTime', 'WOTaskID', 'PersonnelID']


class DelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delay
        fields = ['id', 'DelayCode', 'DelayName']


class WODelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WODelay
        fields = ['id', 'DayAmount', 'HourAmount', 'WODelayDescription', 'WorkOrderID', 'DelayID']


class WOSparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOSparePart
        fields = ['id', 'WOTaskID', 'SparePartID', 'SparePartAmount']


class WOTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOTask
        fields = ['id', 'WorkOrderID', 'TaskID', 'WOTaskSituationOfDo']


class FrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequency
        fields = ['id', 'FrequencyCode', 'FrequencyName']


class WOTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOTemplate
        fields = ['id', 'WOTemplateCode', 'WOTemplateName', 'WOTemplateDurationDay', 'WOTemplateDurationHour',
                  'WOTemplateAlarmDay', 'WOTemplateAlarmHour', 'DepartmentID', 'WOTemplateTypeID']


class WOTemplateSchualingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOTemplateSchualing
        fields = ['id', 'WOTemplateSchualingStartDate', 'WOTemplateSchualingFinishDate', 'AmountFrequency', 'Status',
                  'WOTemplateID', 'FrequencyID']


class WOTemplateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOTemplateType
        fields = ['id', 'WOTemplateTypeCode', 'WOTemplateTypeName', 'WOTemplateTypeDescription']


class WOActivityTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOActivityTemplateTbl
        fields = ['id', 'WOTemplateID', 'AssetClassTaskID', 'AssetSubdivisionID']



class UserSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password',
                  'email', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.last_name = self.data['password']
        instance.save()
        return instance
        
class TemplateSchualingDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateSchualingDate
        fields = ['id', 'TemplateSchualingDate', 'WOTemplateSchualingID', 'StatusOfDo']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'StatusCode', 'StatusName', 'StatusCondition','OpCl']

class WRWORelationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WRWORelationStatus
        fields = ['id', 'StatusWOID', 'StstusWRID']

class WRStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WRStatus
        fields = ['id', 'StatusID', 'WorkRequestID', 'StatusDate', 'StatusTime', 'StatusDescription']

class WOStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOStatus
        fields = ['id', 'StatusID', 'WorkOrderID', 'StatusDate', 'StatusTime', 'StatusDescription']

class WorkflowLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowLevel
        fields = ['id', 'WorkflowLevelName']

class WorkflowLevelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowLevelStatus
        fields = ['id', 'StatusID', 'WorkflowLevelID', 'WorkflowLevelStatusPeriority']


class AssetSubdivisionAssetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    AssetID__AssetName = serializers.CharField()
    AssetID__AssetCode = serializers.CharField()
    AssetSubdivisionFatherID=serializers.IntegerField()
    AssetID = serializers.IntegerField()
    AssetChildID = serializers.IntegerField()
    tree = serializers.IntegerField()
    fakelocation = serializers.IntegerField()
    AssetClassCodeChain = serializers.CharField()
    AssetClassNameChain = serializers.CharField()
    idChain = serializers.CharField()
    AssetCode = serializers.CharField()
    AssetName = serializers.CharField()
    AssetID__LocationID__LocationName = serializers.CharField()
    AssetID__LocationID__LocationCode = serializers.CharField()
    AssetID__LocationID__LocationCodeChain = serializers.CharField()
    AssetID__LocationID__LocationNameChain = serializers.CharField()


class WorkRequestFailureCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkRequestFailureCause
        fields = ['id', 'WorkRequestID', 'FailureCauseID']


class WorkOrderNewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    WODateOfRegistration = serializers.DateField()
    DateOfPlanStart = serializers.DateField()
    DateOfPlanFinish = serializers.DateField()
    WODescription = serializers.CharField()
    WorkRequestID = serializers.IntegerField()
    StatusID = serializers.IntegerField()
    DepartmentID = serializers.IntegerField()
    DateOfStart = serializers.DateField()
    DateOfFinish = serializers.DateField()
    WorkRequestID__AssetSubdivisionID =serializers.IntegerField()
    WorkRequestID__FailureModeID = serializers.IntegerField()


class WOTaskorderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    WorkOrderID = serializers.CharField()
    TaskID = serializers.CharField()
    WOTaskSituationOfDo = serializers.CharField()
    TaskID__TaskName = serializers.CharField()
    TaskID__TaskCode = serializers.CharField()
    
    class Meta:
        model = WOTask
        fields = ['id', 'WorkOrderID', 'TaskID', 'WOTaskSituationOfDo', 'TaskID__TaskName', 'TaskID__TaskCode']
    
    
class WorkflowLevelStatusShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowLevelStatusShow
        fields = ['id', 'StatusID', 'WorkflowLevelStatusID']
