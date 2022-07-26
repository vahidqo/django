from.models import TemplateSchualingDate, WorkOrder, WOTemplateAsset, WOAssetSubdivision, WOTemplateActivity, WOTask
from datetime import timedelta
from django.utils import timezone


def transfer_daily_data():
    wo = TemplateSchualingDate.objects.all()
    for i in wo:
        if i.SchedualingAlarmDate <= timezone.now() and i.StatusOfDo == False:
            
            instance=WorkOrder.objects.create(WODateOfRegistration=i.SchedualingAlarmDate, WODescription=i.WOTemplateSchualingID.WOTemplateID.WOTemplateName,
                                     DateOfPlanStart=i.SchualingDate,
                                     DateOfPlanFinish=i.SchualingDate+timedelta(days=i.WOTemplateSchualingID.WOTemplateID.WOTemplateDurationDay, hours=i.WOTemplateSchualingID.WOTemplateID.WOTemplateDurationHour),
                                     DepartmentID=i.WOTemplateSchualingID.WOTemplateID.DepartmentID, WorkOrderType='1',
                                              WOTemplateCode=i.WOTemplateSchualingID.WOTemplateID.WOTemplateCode)

            TemplateSchualingDate.objects.filter(id=i.id).update(WorkOrderID=instance.id, StatusOfDo = True)
            
            ida = WOTemplateAsset.objects.filter(WOTemplateID=i.WOTemplateSchualingID.WOTemplateID.id)
            for m in ida:
                ins = WOAssetSubdivision.objects.create(WorkOrderID=instance.id, AssetSubdivisionID=m.AssetSubdivisionID)
                task = WOTemplateActivity.objects.filter(WOTemplateAssetID=m.id)
                for j in task:
                    WOTask.objects.create(WOAssetSubdivisionID=ins, TaskID=j.TaskID, WOTaskSituationOfDo="ND")
