from django.db import models
from django.db.models.signals import post_save
from django_jalali.db import models as jmodels


class AssetCategory(models.Model):
    AssetCategoryCode = models.CharField(max_length=100, verbose_name='کد خانواده تجهیز')
    AssetCategoryName = models.CharField(max_length=100, verbose_name='نام خانواده تجهیز')
    slug = models.SlugField(max_length=100)
    AssetClassFather = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, verbose_name='خانواده تجهیز پدر')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'خانواده تجهیز'
        verbose_name_plural = 'خانواده های تجهیز'

    def __str__(self):
        return "{}-{}".format(self.AssetCategoryCode, self.AssetCategoryName)


class AssetClass(models.Model):
    AssetClassCode = models.CharField(max_length=100, verbose_name='کد کلاس تجهیز')
    AssetClassName = models.CharField(max_length=200, verbose_name='نام کلاس تجیز')
    AssetCategoryID = models.ForeignKey('AssetCategory', on_delete=models.CASCADE, blank=False,
                                        verbose_name='خانواده تجیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'کلاس تجهیز'
        verbose_name_plural = 'کلاس های تجهیز'

    def __str__(self):
        return "{}-{}".format(self.AssetClassCode, self.AssetClassName)


class AssetClassSubdivision(models.Model):
    AssetClassFatherID = models.ForeignKey('AssetClass', on_delete=models.CASCADE, related_name='ClassFather',
                                           blank=False,
                                           verbose_name='کلاس تجهیز پدر')
    AssetClassChildID = models.ForeignKey('AssetClass', on_delete=models.CASCADE, related_name='ClassChild',
                                          blank=False,
                                          verbose_name='کلاس تجیز فرزند')
    AssetClassChildNumber = models.IntegerField(verbose_name='تعداد فرزند')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'زیر کلاس تجهیز'
        verbose_name_plural = 'زیر کلاس تجهیزات'

    def __str__(self):
        return "{}-{}".format(self.AssetClassFatherID, self.AssetClassChildID)


class FailureMode(models.Model):
    FailureModeCode = models.CharField(max_length=100, verbose_name='کد نوع خرابی')
    FailureModeName = models.CharField(max_length=200, verbose_name='نام نوع حرابی')
    FailureModeDescription = models.TextField(verbose_name='توضیحات')
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.CASCADE, blank=False,
                                     verbose_name='کلاس تجهیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'نوع خرابی'
        verbose_name_plural = 'انواع خرابی'

    def __str__(self):
        return "{}-{}".format(self.FailureModeCode, self.FailureModeName)


class FailureCause(models.Model):
    FailureCauseCode = models.CharField(max_length=100, verbose_name='کد علت خرابی')
    FailureCauseName = models.CharField(max_length=200, verbose_name='نام علت حرابی')
    FailureCauseDescription = models.TextField(verbose_name='توضیحات')
    FailureModeID = models.ForeignKey('FailureMode', on_delete=models.CASCADE, blank=False,
                                      verbose_name='نوع خرابی')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'علت خرابی'
        verbose_name_plural = 'علل خرابی'

    def __str__(self):
        return "{}-{}".format(self.FailureCauseCode, self.FailureCauseName)


class SpecificData(models.Model):
    SpecificDataCode = models.CharField(max_length=100, verbose_name='کد ویژگی')
    SpecificDataName = models.CharField(max_length=200, verbose_name='نام ویژگی')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'

    def __str__(self):
        return "{}-{}".format(self.SpecificDataCode, self.SpecificDataName)


class AssetClassSpecificData(models.Model):
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.CASCADE, blank=True, verbose_name='کلاس تجهیز')
    SpecificDataID = models.ForeignKey('SpecificData', on_delete=models.CASCADE, blank=False, verbose_name='ویژگی')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'مشخصات کلاس'
        verbose_name_plural = 'مشخصات کلاس ها'

    def __str__(self):
        return "{}-{}".format(self.AssetClassID, self.SpecificDataID)


class AssetPriority(models.Model):
    AssetPriorityCode = models.CharField(max_length=100, verbose_name='کد اولویت')
    AssetPriorityName = models.CharField(max_length=200, verbose_name='نام اولویت')
    AssetPriorityValue = models.IntegerField(verbose_name='ارزش اولویت')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'اولویت'
        verbose_name_plural = 'اولویت ها'

    def __str__(self):
        return "{}-{}".format(self.AssetPriorityCode, self.AssetPriorityName)


class Location(models.Model):
    LocationCode = models.CharField(max_length=100, verbose_name='کد مکان')
    LocationName = models.CharField(max_length=200, verbose_name='نام مکان')
    LocationFatherID = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, verbose_name='مکان پدر')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان ها'

    def __str__(self):
        return "{}-{}".format(self.LocationCode, self.LocationName)


class Asset(models.Model):
    AssetCode = models.CharField(max_length=100, verbose_name='کد تجهیز')
    AssetName = models.CharField(max_length=200, verbose_name='نام تجهیز')
    InstallationDate = models.DateField(verbose_name='تاریخ نصب')
    AssetPriorityID = models.ForeignKey('AssetPriority', on_delete=models.CASCADE, blank=False, verbose_name='اولویت')
    LocationID = models.ForeignKey('Location', on_delete=models.CASCADE, blank=False, verbose_name='مکان')
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.CASCADE, blank=False, verbose_name='کلاس تجهیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تجهیز'
        verbose_name_plural = 'تجهیزات'

    def __str__(self):
        return "{}-{}".format(self.AssetCode, self.AssetName)


class AssetSubdivision(models.Model):
    AssetID = models.ForeignKey('Asset', on_delete=models.CASCADE, blank=True,
                                verbose_name='تجهیز')
    AssetChildID = models.ForeignKey('AssetClass', on_delete=models.CASCADE, blank=False,
                                     verbose_name='زیر تجهیز')
    AssetSubdivisionFatherID = models.ForeignKey('self', on_delete=models.CASCADE,
                                                 blank=True, verbose_name='کلاس پدر')
    tree = models.IntegerField(blank=True, verbose_name='وضعیت درخت')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'زیر مجموعه'
        verbose_name_plural = 'زیر مجموعه'


def save_Asset(sender, instance, created, **kwargs):
    if created:
        AssetSubdivision.objects.create(AssetID=instance, AssetChildID=instance.AssetClassID, tree=1)
        cn = AssetClassSubdivision.objects.filter(AssetClassFatherID=instance.AssetClassID)
        ma = AssetSubdivision.objects.last()
        for i in cn:
            chn = range(i.AssetClassChildNumber)
            for j in chn:
                AssetSubdivision.objects.create(AssetChildID=i.AssetClassChildID, AssetSubdivisionFatherID=ma, tree=0)
                cnn = AssetClassSubdivision.objects.filter(AssetClassFatherID=i.AssetClassChildID)
                maa = AssetSubdivision.objects.filter(AssetChildID=i.AssetClassChildID, AssetSubdivisionFatherID=ma)
                for z in cnn:
                    chnn = range(z.AssetClassChildNumber)
                    for x in chnn:
                        AssetSubdivision.objects.create(AssetChildID=z.AssetClassChildID,
                                                        AssetSubdivisionFatherID=maa[0], tree=0)
                        ccnn = AssetClassSubdivision.objects.filter(AssetClassFatherID=z.AssetClassChildID)
                        mmaa = AssetSubdivision.objects.filter(AssetChildID=z.AssetClassChildID,
                                                               AssetSubdivisionFatherID=maa[0])
                        for y in ccnn:
                            chhnn = range(y.AssetClassChildNumber)
                            for m in chhnn:
                                AssetSubdivision.objects.create(AssetChildID=y.AssetClassChildID,
                                                                AssetSubdivisionFatherID=mmaa[0], tree=0)


post_save.connect(save_Asset, sender=Asset)

class AssetSubdivisionSparePart(models.Model):
    AssetSubdivisionID = models.ForeignKey('AssetSubdivision', on_delete=models.CASCADE, blank=False,
                                           verbose_name='تجهیز')
    SparePartID = models.ForeignKey('SparePart', on_delete=models.CASCADE, blank=True, verbose_name='قطعات یدکی')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی زیر مجموعه'
        verbose_name_plural = 'ویژگی های زیر مجموعه'


class AssetSpecificData(models.Model):
    AssetSubdivisionID = models.ForeignKey('AssetSubdivision', on_delete=models.CASCADE, blank=False,
                                           verbose_name='تجهیز')
    SpecificDataID = models.ForeignKey('SpecificData', on_delete=models.CASCADE, blank=False, verbose_name='ویژگی')
    SpecificAmount = models.IntegerField(verbose_name='مقدار ویژگی', blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی تجهیز'
        verbose_name_plural = 'ویژگی تجهیزات'

    def __str__(self):
        return "{}-{}".format(self.AssetSubdivisionID, self.SpecificDataID)


def save_AssetSpe(sender, instance, created, **kwargs):
    if created:
        As = AssetClass.objects.filter(id=instance.AssetChildID.id)
        sp = AssetClassSpecificData.objects.filter(AssetClassID=As[0])
        for n in sp:
            AssetSpecificData.objects.create(AssetSubdivisionID=instance, SpecificDataID=n.SpecificDataID)


post_save.connect(save_AssetSpe, sender=AssetSubdivision)


class SparePartDimension(models.Model):
    SparePartDimensionCode = models.CharField(max_length=100, verbose_name='کد بعد')
    SparePartDimensionName = models.CharField(max_length=200, verbose_name='نام بعد')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'بعد قطعه'
        verbose_name_plural = 'بعد قطعات'

    def __str__(self):
        return "{}-{}".format(self.SparePartDimensionCode, self.SparePartDimensionName)


class SparePartCategory(models.Model):
    SparePartCategoryCode = models.CharField(max_length=100, verbose_name='کد خانواده قطعه')
    SparePartCategoryName = models.CharField(max_length=200, verbose_name='نام خانواده قطعه')
    SparePartCategoryFather = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                                                verbose_name='خانواده قطعه  پدر')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'خانواده قطعه'
        verbose_name_plural = 'خانواده های قطعه'

    def __str__(self):
        return "{}-{}".format(self.SparePartCategoryCode, self.SparePartCategoryName)


class SparePart(models.Model):
    SparePartCode = models.CharField(max_length=100, verbose_name='کد قطعه')
    SparePartName = models.CharField(max_length=200, verbose_name='نام قطعه')
    SparePartCategoryID = models.ForeignKey('SparePartCategory', on_delete=models.CASCADE, blank=False,
                                            verbose_name='خانواده قطعه')
    SparePartDimensionID = models.ForeignKey('SparePartDimension', on_delete=models.CASCADE, blank=False,
                                             verbose_name='بعد قطعه')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'قطعه'
        verbose_name_plural = 'قطعات'

    def __str__(self):
        return "{}-{}".format(self.SparePartCode, self.SparePartName)


# class AssetSparePart(models.Model):
#   AssetSubdivisionID = models.ForeignKey('AssetSubdivision', on_delete=models.CASCADE, blank=False,
#                                         verbose_name='زیر تجهیز')
# SparePartID = models.ForeignKey('SparePart', on_delete=models.CASCADE, blank=False, verbose_name='قطعه')
# Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
# Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

# class Meta:
#   ordering = ['-Create']
#  verbose_name = 'قطعه تجهیز'
# verbose_name_plural = 'قطعات تجهیز'

# def __str__(self):
#   return "{}-{}".format(self.AssetSubdivisionID, self.SparePartID)


def upload_path(instance, filename):
    return '/'.join(['Files', str(instance.DocumentCode), filename])


class Document(models.Model):
    DocumentCode = models.CharField(max_length=100, verbose_name='کد فایل')
    DocumentName = models.CharField(max_length=200, verbose_name='نام فایل')
    DocumentDescription = models.TextField(verbose_name='توضیحات')
    FileAddress = models.FileField(upload_to=upload_path, verbose_name='فایل')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'قایل'
        verbose_name_plural = 'فایل ها'

    def __str__(self):
        return "{}-{}".format(self.DocumentCode, self.DocumentName)


class AssetClassDocument(models.Model):
    DocumentID = models.ForeignKey('Document', on_delete=models.Model, blank=False, verbose_name='فایل')
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.Model, blank=False, verbose_name='تجهیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'قایل تجهیز'
        verbose_name_plural = 'فایل های تجهیز'

    def __str__(self):
        return "{}-{}".format(self.DocumentID, self.AssetClassID)


class TaskType(models.Model):
    TaskTypeCode = models.CharField(max_length=100, verbose_name='کد نوع وظیفه')
    TaskTypeName = models.CharField(max_length=200, verbose_name='نام نوع وظیفه')
    TaskTypeDescription = models.TextField(verbose_name='توضیحات', blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'نوع وظیفه'
        verbose_name_plural = 'انواع وظیفه'

    def __str__(self):
        return "{}-{}".format(self.TaskTypeCode, self.TaskTypeName)


class JobCategory(models.Model):
    JobCategoryCode = models.CharField(max_length=100, verbose_name='کد نوع شغل')
    JobCategoryName = models.CharField(max_length=200, verbose_name='نام نوع شغل')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'نوع شغل'
        verbose_name_plural = 'انواع شغل'

    def __str__(self):
        return "{}-{}".format(self.JobCategoryCode, self.JobCategoryName)


class AssetClassTask(models.Model):
    Frequency = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
        ('F', 'Functionally')
    )
    fun = (
        ('O', 'Operator'),
        ('T', 'Technician'),
    )
    TaskCode = models.CharField(max_length=100, verbose_name='کد وظیفه')
    TaskName = models.CharField(max_length=200, verbose_name='نام وظیفه')
    TaskDescription = models.TextField(verbose_name='توضیحات')
    FrequencyName = models.CharField(max_length=1, choices=Frequency, verbose_name='نام تناوب')
    FrequencyAmount = models.IntegerField(verbose_name='مقدار تناوب')
    DurationOfDo = models.IntegerField(verbose_name='مدت زمان انجام')
    Functor = models.CharField(max_length=1, choices=fun, verbose_name='مسئول')
    TaskTypeID = models.ForeignKey('TaskType', on_delete=models.CASCADE, blank=False, verbose_name='نوع وظیفه')
    JobCategoryID = models.ForeignKey('JobCategory', on_delete=models.CASCADE, blank=False, verbose_name='نوع شغل')
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.CASCADE, blank=False,
                                           verbose_name='کلاس تجهیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظایف'

    def __str__(self):
        return "{}-{}".format(self.TaskCode, self.TaskName)


class Department(models.Model):
    DepartmentCode = models.CharField(max_length=100, verbose_name='کد دپارتمان')
    DepartmentName = models.CharField(max_length=200, verbose_name='نام دپارتمان')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'دپارتمان'
        verbose_name_plural = 'دپارتمان ها'

    def __str__(self):
        return "{}-{}".format(self.DepartmentCode, self.DepartmentName)


class Personnel(models.Model):
    PersonnelCode = models.CharField(max_length=100, verbose_name='کد پرسنل')
    PersonnelNetCode = models.CharField(max_length=100, verbose_name='کد نت پرسنل')
    PersonnelName = models.CharField(max_length=200, verbose_name='نام پرسنل')
    PersonnelFamily = models.CharField(max_length=200, verbose_name='فامیل پرسنل')
    PersonnelMobile = models.CharField(max_length=100, verbose_name='شماره پرسنل')
    DepartmentID = models.ForeignKey('Department', on_delete=models.CASCADE, blank=False, verbose_name='دپارتمان')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'پرسنل'
        verbose_name_plural = 'پرسنل'

    def __str__(self):
        return "{}-{}".format(self.PersonnelCode, self.PersonnelName)


class PersonnelJobCategory(models.Model):
   JobCategoryID = models.ForeignKey('JobCategory', on_delete=models.CASCADE, blank=False, verbose_name='نوع شغل')
   PersonnelID = models.ForeignKey('Personnel', on_delete=models.CASCADE, blank=False, verbose_name='پرسنل')
   Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
   Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

   class Meta:
      ordering = ['-Create']
      verbose_name = 'شغل پرسنل'
      verbose_name_plural = 'شغل های پرسنل'
 
   def __str__(self):
      return "{}-{}".format(self.JobCategoryID, self.PersonnelID)


class TypeWr(models.Model):
    TypeWrCode = models.CharField(max_length=100, verbose_name='کد نوع درخواست کار')
    TypeWrName = models.CharField(max_length=200, verbose_name='نام نوع درخواست کار')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'نوع درخواست کار'
        verbose_name_plural = 'انواع درخواست کار'

    def __str__(self):
        return "{}-{}".format(self.TypeWrCode, self.TypeWrName)


class WorkPriority(models.Model):
    WorkPriorityCode = models.CharField(max_length=100, verbose_name='کد اولویت')
    WorkPriorityName = models.CharField(max_length=200, verbose_name='نام اولویت')
    WorkPriorityValue = models.IntegerField(verbose_name='مقدار اولویت')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'اولویت درخواست کار'
        verbose_name_plural = 'اولویت های درخواست کار'

    def __str__(self):
        return "{}-{}".format(self.WorkPriorityCode, self.WorkPriorityName)


class Supplier(models.Model):
    SupplierCode = models.CharField(max_length=100, verbose_name='کد تامین کننده')
    SupplierName = models.CharField(max_length=200, verbose_name='نام تامین کننده')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تامین کننده'
        verbose_name_plural = 'تامین کنندگان'

    def __str__(self):
        return "{}-{}".format(self.SupplierCode, self.SupplierName)


class SupplierSpecific(models.Model):
    SupplierSpecificCode = models.CharField(max_length=100, verbose_name='کد ویژگی تامین کننده')
    SupplierSpecificName = models.CharField(max_length=200, verbose_name='نام ویژگی تامین کننده')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی تامین کننده'
        verbose_name_plural = 'ویژگی های تامین کننده'

    def __str__(self):
        return "{}-{}".format(self.SupplierSpecificCode, self.SupplierSpecificName)


class SupplierSpecificData(models.Model):
    SupplierID = models.ForeignKey('Supplier', on_delete=models.CASCADE, blank=False, verbose_name='تامین کننده')
    SupplierSpecificID = models.ForeignKey('SupplierSpecific', on_delete=models.CASCADE, blank=False,
                                           verbose_name='ویژگی')
    SpecificAmount = models.CharField(max_length=50, verbose_name='مقدار ویژگی')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی های تامین کننده'
        verbose_name_plural = 'ویژگی های تامین کنندگان'

    # def __str__(self):
    #   return "{}-{}".format(self.SupplierSpecificCode, self.SupplierSpecificName)


class WorkRequest(models.Model):
    WRDate = models.DateField(verbose_name='تاریخ')
    WRDateOfRegistration = models.DateField(verbose_name='تاریخ ثبت')
    AssetSubdivisionID = models.ForeignKey('AssetSubdivision', on_delete=models.CASCADE, blank=False,
                                           verbose_name='تجهیز')
    FailureModeID = models.ForeignKey('FailureMode', on_delete=models.CASCADE, blank=False, verbose_name='نوع خرابی')
    FailureCauseID = models.ManyToManyField('FailureCause', blank=False, verbose_name='علل خرابی')
    WorkPriorityID = models.ForeignKey('WorkPriority', on_delete=models.CASCADE, blank=False, verbose_name='اولویت')
    TypeWrID = models.ForeignKey('TypeWr', on_delete=models.CASCADE, blank=False, verbose_name='نوع')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'درخواست کار'
        verbose_name_plural = 'درخواست کار ها'

    def __str__(self):
        return "WR%06d" % self.id


class WorkOrder(models.Model):
    WODateOfRegistration = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    WODescription = models.TextField(verbose_name='توضیحات')
    DateOfPlanStart = models.DateField(verbose_name='تاریخ شروع')
    DateOfPlanFinish = models.DateField(verbose_name='تاریخ پایان')
    WorkRequestID = models.ForeignKey('WorkRequest', on_delete=models.CASCADE, blank=False, verbose_name='درخواست کار')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'دستور کار'
        verbose_name_plural = 'دستور کار ها'

    def __str__(self):
        return "WR%06d-WO%06d".format(self.WorkRequestID, self.id)


class WOSupplier(models.Model):
    WorkStartDate = models.DateField(verbose_name='تاریخ شروع')
    WorkFinishDate = models.DateField(verbose_name='تاریخ پایان')
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.CASCADE, blank=False, verbose_name='دستور کار')
    SupplierID = models.ForeignKey('Supplier', on_delete=models.CASCADE, blank=False, verbose_name='تامین کنده')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تامین کننده دستور کار'
        verbose_name_plural = 'تامین کننده های دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.SupplierID)


class WOPersonnel(models.Model):
    WorkDate = models.DateField(verbose_name='تاریخ انجام')
    WorkTime = models.IntegerField(verbose_name='مدت زمان انجام')
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.CASCADE, blank=False, verbose_name='دستور کار')
    PersonnelID = models.ForeignKey('Personnel', on_delete=models.CASCADE, blank=False, verbose_name='پرسنل')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'پرسنل دستور کار'
        verbose_name_plural = 'پرسنل های دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.PersonnelID)


class Delay(models.Model):
    DelayCode = models.CharField(max_length=100, verbose_name='کد تاخیر')
    DelayName = models.CharField(max_length=200, verbose_name='نام تاخیر')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تاخیر'
        verbose_name_plural = 'تاخیر ها'

    def __str__(self):
        return "{}-{}".format(self.DelayCode, self.DelayName)


class WODelay(models.Model):
    DayAmount = models.IntegerField(verbose_name='روز')
    HourAmount = models.IntegerField(verbose_name='ساعت')
    WODelayDescription = models.TextField(verbose_name='توضیحات')
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.CASCADE, blank=False, verbose_name='دستور کار')
    DelayID = models.ForeignKey('Delay', on_delete=models.CASCADE, blank=False, verbose_name='تاخیر')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تاخیر دستور کار'
        verbose_name_plural = 'تاخیر های دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.DelayID)


class WOSparePart(models.Model):
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.CASCADE, blank=False, verbose_name='دستور کار')
    SparePartID = models.ForeignKey('SparePart', on_delete=models.CASCADE, blank=False, verbose_name='قطعه')
    SparePartAmount = models.IntegerField(verbose_name='تعداد قطعه')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'قطعه دستور کار'
        verbose_name_plural = 'قطعات دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.SparePartID)


class WOTask(models.Model):
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.CASCADE, blank=False, verbose_name='دستور کار')
    TaskID = models.ForeignKey('AssetClassTask', on_delete=models.CASCADE, blank=False, verbose_name='وظیفه')
    WOTaskSituationOfDo = models.CharField(max_length=50, verbose_name='وضعیت انجام')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'وظیفه دستور کار'
        verbose_name_plural = 'وظایف دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.TaskID)


class Frequency(models.Model):
    FrequencyCode = models.CharField(max_length=100, verbose_name='کد تناوب')
    FrequencyName = models.CharField(max_length=200, verbose_name='نام تناوب')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تناوب'
        verbose_name_plural = 'تناوب ها'

    def __str__(self):
        return "{}-{}".format(self.FrequencyCode, self.FrequencyName)


class WOTemplateType(models.Model):
    WOTemplateTypeCode = models.CharField(max_length=100, verbose_name='کد نوع برنامه')
    WOTemplateTypeName = models.CharField(max_length=200, verbose_name='نام نوع برنامه')
    WOTemplateTypeDescription = models.TextField(verbose_name='توضیحات', blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'نوع برنامه'
        verbose_name_plural = 'انواع برنامه'

    def __str__(self):
        return "{}-{}".format(self.WOTemplateTypeCode, self.WOTemplateTypeName)


class WOTemplate(models.Model):
    WOTemplateCode = models.CharField(max_length=100, verbose_name='کد تناوب دستور کار')
    WOTemplateName = models.CharField(max_length=200, verbose_name='نام تناوب دستور کار')
    WOTemplateDurationDay = models.IntegerField(verbose_name='روز تناوب')
    WOTemplateDurationHour = models.IntegerField(verbose_name='ساعت تناوب')
    WOTemplateAlarmDay = models.IntegerField(verbose_name='روز اعلام تناوب')
    WOTemplateAlarmHour = models.IntegerField(verbose_name='ساعت اعلام تناوب')
    DepartmentID = models.ForeignKey('Department', on_delete=models.CASCADE, blank=False, verbose_name='دپارتمان')
    WOTemplateTypeID = models.ForeignKey('WOTemplateType', on_delete=models.CASCADE, blank=False, verbose_name='نوع')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تناوب دستور کار'
        verbose_name_plural = 'تناوب های دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WOTemplateCode, self.WOTemplateName)


class WOActivityTemplateTbl(models.Model):
    WOTemplateID = models.ForeignKey('WOTemplate', on_delete=models.CASCADE, blank=False, verbose_name='برنامه')
    AssetClassTaskID = models.ForeignKey('AssetClassTask', on_delete=models.CASCADE, blank=False,
                                           verbose_name='فعالیت')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'فعالیت های برنامه'
        verbose_name_plural = 'فعالیت های برنامه ها'
    
    def __str__(self):
        return "{}-{}".format(self.WOTemplateID, self.AssetClassTaskID)


class WOTemplateSchualing(models.Model):
    WOTemplateSchualingStartDate = models.DateField(verbose_name='روز شروع برنامه')
    WOTemplateSchualingFinishDate = models.DateField(verbose_name='روز پایان برنامه')
    AmountFrequency = models.IntegerField(verbose_name='مقدار')
    Status = models.BooleanField(verbose_name='وضعیت')
    WOTemplateID = models.ForeignKey('WOTemplate', on_delete=models.CASCADE, blank=False, verbose_name='دستور کار')
    FrequencyID = models.ForeignKey('Frequency', on_delete=models.CASCADE, blank=False, verbose_name='تناوب')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'برنامه ریزی شده'
        verbose_name_plural = 'برنامه ریزی شده ها'

    def __str__(self):
        return "{}-{}".format(self.WOTemplateID, self.FrequencyID)


class TemplateSchualingDate(models.Model):
    TemplateSchualingDate = models.DateField(verbose_name='روز برنامه')
    StatusOfDo = models.CharField(max_length=100, verbose_name='وضعیت انجام')
    WOTemplateSchualingID = models.ForeignKey('WOTemplateSchualing', on_delete=models.CASCADE, blank=False, verbose_name='برنامه')
    Create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'برنامه ریزی '
        verbose_name_plural = 'برنامه ریزی ها'

    def __str__(self):
        return "{}-{}".format(self.TemplateSchualingDate, self.WOTemplateSchualingID)



