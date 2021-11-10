from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import AssetCategory, AssetClass, AssetClassSubdivision, FailureMode, FailureCause, SpecificData, \
    JobCategory, Department, Personnel, AssetPriority, Location, Asset, AssetSubdivision, SparePartDimension, \
    SparePartCategory, Document, AssetSpecificData, SparePart, TaskType, AssetClassTask, Supplier, SupplierSpecific, \
    SupplierSpecificData, WorkRequest, TypeWr, WorkPriority, WorkOrder, WOSupplier, WOPersonnel, Delay, WODelay, \
    WOSparePart, WOTask, Frequency, WOTemplate, WOTemplateSchualing, AssetClassSpecificData


@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_filter = ('AssetCategoryCode', 'AssetCategoryName', 'Create')
    list_display = ('AssetCategoryCode', 'AssetCategoryName', 'Create')
    search_fields = ('AssetCategoryCode', 'AssetCategoryName')
    ordering = ['Create', 'AssetCategoryCode']
    prepopulated_fields = {'slug': ('AssetCategoryName',)}


@admin.register(AssetClass)
class AssetClassAdmin(admin.ModelAdmin):
    list_display = ('AssetClassCode', 'AssetClassName', 'AssetCategory_Name', 'Create')

    def AssetCategory_Name(self, obj):
        return obj.AssetCategoryID.AssetCategoryName

    list_filter = ('AssetClassCode', 'AssetClassName', 'Create')
    search_fields = ('AssetClassCode', 'AssetClassName')
    ordering = ['Create', 'AssetClassCode']


@admin.register(AssetClassSubdivision)
class AssetClassSubdivisionAdmin(admin.ModelAdmin):
    list_display = ('AssetClassFatherID_Name', 'AssetClassChildID_Name', 'AssetClassChildNumber', 'Create')

    def AssetClassFatherID_Name(self, obj):
        return obj.AssetClassFatherID.AssetClassName

    def AssetClassChildID_Name(self, obj):
        return obj.AssetClassChildID.AssetClassName

    list_filter = ('AssetClassFatherID', 'AssetClassChildID', 'Create')
    search_fields = ('AssetClassFatherID', 'AssetClassChildID')
    ordering = ['Create']


@admin.register(AssetClassSpecificData)
class AssetClassSpecificDataAdmin(admin.ModelAdmin):
    list_display = ('AssetClassID_Name', 'SpecificDataID_Name', 'Create')

    def AssetClassID_Name(self, obj):
        return obj.AssetClassID.AssetClassName

    def SpecificDataID_Name(self, obj):
        return obj.SpecificDataID.SpecificDataName

    list_filter = ('AssetClassID', 'SpecificDataID', 'Create')
    search_fields = ('AssetClassID', 'SpecificDataID')
    ordering = ['Create']


@admin.register(FailureMode)
class FailureModeAdmin(admin.ModelAdmin):
    list_display = ('FailureModeCode', 'FailureModeName', 'AssetClassID_Name', 'Create')

    def AssetClassID_Name(self, obj):
        return obj.AssetClassID.AssetClassName

    list_filter = ('FailureModeCode', 'FailureModeName', 'AssetClassID', 'Create')
    search_fields = ('FailureModeCode', 'FailureModeName')
    ordering = ['Create', 'FailureModeCode']


@admin.register(FailureCause)
class FailureCauseAdmin(admin.ModelAdmin):
    list_display = ('FailureCauseCode', 'FailureCauseName', 'FailureModeID_Name', 'Create')

    def FailureModeID_Name(self, obj):
        return obj.FailureModeID.FailureModeName

    list_filter = ('FailureCauseCode', 'FailureCauseName', 'FailureModeID', 'Create')
    search_fields = ('FailureCauseCode', 'FailureCauseName')
    ordering = ['Create', 'FailureCauseCode']


@admin.register(SpecificData)
class SpecificDataAdmin(admin.ModelAdmin):
    list_display = ('SpecificDataCode', 'SpecificDataName', 'Create')
    list_filter = ('SpecificDataCode', 'SpecificDataName', 'Create')
    search_fields = ('SpecificDataCode', 'SpecificDataName')
    ordering = ['Create', 'SpecificDataCode']


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('JobCategoryCode', 'JobCategoryName', 'Create')
    list_filter = ('JobCategoryCode', 'JobCategoryName', 'Create')
    search_fields = ('JobCategoryCode', 'JobCategoryName')
    ordering = ['Create', 'JobCategoryCode']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DepartmentCode', 'DepartmentName', 'Create')
    list_filter = ('DepartmentCode', 'DepartmentName', 'Create')
    search_fields = ('DepartmentCode', 'DepartmentName')
    ordering = ['Create', 'DepartmentCode']


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = (
        'PersonnelCode', 'PersonnelNetCode', 'PersonnelName', 'PersonnelFamily', 'PersonnelMobile',
        'DepartmentID_Name', 'Create')

    def DepartmentID_Name(self, obj):
        return obj.DepartmentID.DepartmentName

    list_filter = ('PersonnelCode', 'PersonnelNetCode', 'DepartmentID', 'Create')
    search_fields = ('PersonnelCode', 'PersonnelNetCode')
    ordering = ['Create', 'PersonnelCode']


@admin.register(AssetPriority)
class AssetPriorityAdmin(admin.ModelAdmin):
    list_display = ('AssetPriorityCode', 'AssetPriorityName', 'AssetPriorityValue', 'Create')
    list_filter = ('AssetPriorityCode', 'AssetPriorityName', 'Create')
    search_fields = ('AssetPriorityCode', 'AssetPriorityName')
    ordering = ['Create', 'AssetPriorityCode']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('LocationCode', 'LocationName', 'LocationFatherID_Name', 'Create')

    def LocationFatherID_Name(self, obj):
        return obj.LocationFatherID.LocationName

    list_filter = ('LocationCode', 'LocationName', 'LocationFatherID', 'Create')
    search_fields = ('LocationCode', 'LocationName')
    ordering = ['Create', 'LocationCode']


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        'AssetCode', 'AssetName', 'InstallationDate', 'AssetClassID_Name', 'AssetPriorityID_Name', 'LocationID_Name'
        , 'Create')

    def AssetPriorityID_Name(self, obj):
        return obj.AssetPriorityID.AssetPriorityName

    def LocationID_Name(self, obj):
        return obj.LocationID.LocationName

    def AssetClassID_Name(self, obj):
        return obj.AssetClassID.AssetClassName

    list_filter = ('AssetCode', 'AssetName', 'InstallationDate', 'AssetClassID', 'AssetPriorityID', 'LocationID',
                   'Create')
    search_fields = ('AssetCode', 'AssetName')
    ordering = ['Create', 'AssetCode']


@admin.register(AssetSubdivision)
class AssetSubdivisionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'AssetID_Name', 'AssetChildID_Name', 'AssetSubdivisionFatherID_Name', 'tree', 'Create')

    def AssetID_Name(self, obj):
        return obj.AssetID.AssetName

    def AssetChildID_Name(self, obj):
        return obj.AssetChildID.AssetClassName

    def AssetSubdivisionFatherID_Name(self, obj):
        return obj.AssetSubdivisionFatherID

    list_filter = ('AssetID', 'AssetChildID', 'Create')
    search_fields = ('AssetID', 'AssetChildID')
    ordering = ['Create']


@admin.register(SparePartDimension)
class SparePartDimensionAdmin(admin.ModelAdmin):
    list_display = ('SparePartDimensionCode', 'SparePartDimensionName', 'Create')
    list_filter = ('SparePartDimensionCode', 'SparePartDimensionName', 'Create')
    search_fields = ('SparePartDimensionCode', 'SparePartDimensionName')
    ordering = ['Create', 'SparePartDimensionCode']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('DocumentCode', 'DocumentName', 'FileAddress', 'Create')
    list_filter = ('DocumentCode', 'DocumentName', 'Create')
    search_fields = ('DocumentCode', 'DocumentName')
    ordering = ['Create', 'DocumentCode']


@admin.register(AssetSpecificData)
class AssetSpecificDataAdmin(admin.ModelAdmin):
    list_display = ('AssetSubdivisionID_Name', 'SpecificDataID_Name', 'SpecificAmount', 'Create')

    def SpecificDataID_Name(self, obj):
        return obj.SpecificDataID.SpecificDataName

    def AssetSubdivisionID_Name(self, obj):
        return obj.AssetSubdivisionID.id

    list_filter = ('SpecificDataID', 'Create')
    search_fields = ('AssetSubdivisionID', 'SpecificDataID')
    ordering = ['Create']


@admin.register(SparePartCategory)
class SparePartCategoryAdmin(admin.ModelAdmin):
    list_display = ('SparePartCategoryCode', 'SparePartCategoryName', 'SparePartCategoryFather_Name', 'Create')

    def SparePartCategoryFather_Name(self, obj):
        return obj.SparePartCategoryFather.SparePartCategoryName

    list_filter = ('SparePartCategoryCode', 'SparePartCategoryName', 'SparePartCategoryFather', 'Create')
    search_fields = ('SparePartCategoryCode', 'SparePartCategoryName')
    ordering = ['Create', 'SparePartCategoryCode']


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ('SparePartCode', 'SparePartName', 'SparePartCategoryID_Name', 'SparePartDimensionID_Name', 'Create')

    def SparePartCategoryID_Name(self, obj):
        return obj.SparePartCategoryID.SparePartCategoryName

    def SparePartDimensionID_Name(self, obj):
        return obj.SparePartDimensionID.SparePartDimensionName

    list_filter = ('SparePartCode', 'SparePartName', 'SparePartCategoryID', 'SparePartDimensionID', 'Create')
    search_fields = ('SparePartCode', 'SparePartName')
    ordering = ['Create', 'SparePartCode']


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('TaskTypeCode', 'TaskTypeName', 'Create')
    list_filter = ('TaskTypeCode', 'TaskTypeName', 'Create')
    search_fields = ('TaskTypeCode', 'TaskTypeName')
    ordering = ['Create', 'TaskTypeCode']


@admin.register(AssetClassTask)
class AssetClassTaskAdmin(admin.ModelAdmin):
    list_display = (
        'TaskCode', 'TaskName', 'FrequencyName', 'FrequencyAmount', 'DurationOfDo', 'Functor', 'TaskTypeID_Name',
        'JobCategoryID_Name', 'AssetSubdivisionID_Name', 'Create')

    def TaskTypeID_Name(self, obj):
        return obj.TaskTypeID.TaskTypeName

    def JobCategoryID_Name(self, obj):
        return obj.JobCategoryID.JobCategoryName

    def AssetSubdivisionID_Name(self, obj):
        return obj.AssetSubdivisionID.AssetChildID

    list_filter = ('TaskCode', 'TaskName', 'FrequencyName', 'Functor', 'TaskTypeID', 'JobCategoryID', 'Create')
    search_fields = ('TaskCode', 'TaskName')
    ordering = ['Create', 'TaskCode']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('SupplierCode', 'SupplierName', 'Create')
    list_filter = ('SupplierCode', 'SupplierName', 'Create')
    search_fields = ('SupplierCode', 'SupplierName')
    ordering = ['Create', 'SupplierCode']


@admin.register(SupplierSpecific)
class SupplierSpecificAdmin(admin.ModelAdmin):
    list_display = ('SupplierSpecificCode', 'SupplierSpecificName', 'Create')
    list_filter = ('SupplierSpecificCode', 'SupplierSpecificName', 'Create')
    search_fields = ('SupplierSpecificCode', 'SupplierSpecificName')
    ordering = ['Create', 'SupplierSpecificCode']


@admin.register(SupplierSpecificData)
class SupplierSpecificDataAdmin(admin.ModelAdmin):
    list_display = ('SupplierID_Name', 'SupplierSpecificID_Name', 'SpecificAmount', 'Create')

    def SupplierID_Name(self, obj):
        return obj.SupplierID.SupplierName

    def SupplierSpecificID_Name(self, obj):
        return obj.SupplierSpecificID.SupplierSpecificName

    list_filter = ('SupplierID', 'SupplierSpecificID', 'SpecificAmount', 'Create')
    search_fields = ('SupplierID', 'SupplierSpecificID')
    ordering = ['Create']


@admin.register(WorkRequest)
class WorkRequestAdmin(admin.ModelAdmin):
    list_display = (
        'WRDate', 'AssetSubdivisionID_Name', 'FailureModeID_Name', 'WorkPriorityID_Name',
        'TypeWrID_Name', 'Create')

    def AssetSubdivisionID_Name(self, obj):
        return obj.AssetSubdivisionID.AssetChildID

    def FailureModeID_Name(self, obj):
        return obj.FailureModeID.FailureModeName

    def WorkPriorityID_Name(self, obj):
        return obj.WorkPriorityID.WorkPriorityName

    def TypeWrID_Name(self, obj):
        return obj.TypeWrID.TypeWrName

    list_filter = (
        'WRDate', 'AssetSubdivisionID', 'FailureModeID', 'WorkPriorityID', 'TypeWrID', 'Create')
    ordering = ['Create', 'WRDate']


@admin.register(TypeWr)
class TypeWrAdmin(admin.ModelAdmin):
    list_display = ('TypeWrCode', 'TypeWrName', 'Create')
    list_filter = ('TypeWrCode', 'TypeWrName', 'Create')
    search_fields = ('TypeWrCode', 'TypeWrName')
    ordering = ['Create', 'TypeWrCode']


@admin.register(WorkPriority)
class WorkPriorityAdmin(admin.ModelAdmin):
    list_display = ('WorkPriorityCode', 'WorkPriorityName', 'WorkPriorityValue', 'Create')
    list_filter = ('WorkPriorityCode', 'WorkPriorityName', 'WorkPriorityValue', 'Create')
    search_fields = ('WorkPriorityCode', 'WorkPriorityName')
    ordering = ['Create', 'WorkPriorityCode']


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('WODateOfRegistration', 'DateOfPlanStart', 'DateOfPlanFinish', 'WorkRequestID_Name', 'Create')

    def WorkRequestID_Name(self, obj):
        return obj.WorkRequestID

    list_filter = ('WODateOfRegistration', 'DateOfPlanStart', 'DateOfPlanFinish', 'WorkRequestID', 'Create')
    ordering = ['Create', 'WODateOfRegistration']


@admin.register(WOSupplier)
class WOSupplierAdmin(admin.ModelAdmin):
    list_display = ('WorkStartDate', 'WorkFinishDate', 'WorkOrderID_Name', 'SupplierID_Name', 'Create')

    def WorkOrderID_Name(self, obj):
        return obj.WorkOrderID.id

    def SupplierID_Name(self, obj):
        return obj.SupplierID.SupplierName

    list_filter = ('WorkStartDate', 'WorkFinishDate', 'WorkOrderID', 'SupplierID', 'Create')
    ordering = ['Create']


@admin.register(Delay)
class DelayAdmin(admin.ModelAdmin):
    list_display = ('DelayCode', 'DelayName', 'Create')
    list_filter = ('DelayCode', 'DelayName', 'Create')
    search_fields = ('DelayCode', 'DelayName')
    ordering = ['Create', 'DelayCode']


@admin.register(WODelay)
class WODelayAdmin(admin.ModelAdmin):
    list_display = ('DayAmount', 'HourAmount', 'WODelayDescription', 'WorkOrderID_Name', 'DelayID_Name', 'Create')

    def WorkOrderID_Name(self, obj):
        return obj.WorkOrderID.id

    def DelayID_Name(self, obj):
        return obj.DelayID.DelayName

    list_filter = ('DayAmount', 'HourAmount', 'WorkOrderID', 'DelayID', 'Create')
    ordering = ['Create']


@admin.register(WOSparePart)
class WOSparePartAdmin(admin.ModelAdmin):
    list_display = ('WOTaskID', 'SparePartID', 'SparePartAmount', 'Create')

    def SparePartID_Name(self, obj):
        return obj.SparePartID.SparePartName

    list_filter = ('WOTaskID', 'SparePartID', 'Create')
    ordering = ['Create']


@admin.register(WOTask)
class WOTaskAdmin(admin.ModelAdmin):
    list_display = ('WorkOrderID_Name', 'TaskID_Name', 'WOTaskSituationOfDo', 'Create')

    def WorkOrderID_Name(self, obj):
        return obj.WorkOrderID.id

    def TaskID_Name(self, obj):
        return obj.TaskID.TaskName

    list_filter = ('WorkOrderID', 'TaskID', 'Create')
    ordering = ['Create']


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('FrequencyCode', 'FrequencyName', 'Create')
    list_filter = ('FrequencyCode', 'FrequencyName', 'Create')
    search_fields = ('FrequencyCode', 'FrequencyName')
    ordering = ['Create', 'FrequencyCode']


@admin.register(WOTemplate)
class WOTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'WOTemplateCode', 'WOTemplateName', 'WOTemplateDurationDay', 'WOTemplateAlarmDay', 'DepartmentID_Name', 'Create')

    def DepartmentID_Name(self, obj):
        return obj.DepartmentID.DepartmentName

    list_filter = ('WOTemplateCode', 'DepartmentID', 'Create')
    search_fields = ('WOTemplateCode', 'WOTemplateName')
    ordering = ['Create', 'WOTemplateCode']


@admin.register(WOTemplateSchualing)
class WOTemplateSchualingAdmin(admin.ModelAdmin):
    list_display = ('WOTemplateSchualingStartDate', 'WOTemplateSchualingFinishDate', 'AmountFrequency', 'Status',
                    'WOTemplateID_Name', 'FrequencyID_Name', 'Create')

    def WOTemplateID_Name(self, obj):
        return obj.WOTemplateID.WOTemplateName

    def FrequencyID_Name(self, obj):
        return obj.FrequencyID.FrequencyName

    list_filter = (
        'WOTemplateSchualingStartDate', 'WOTemplateSchualingFinishDate', 'WOTemplateID', 'FrequencyID', 'Create')
    ordering = ['Create']
