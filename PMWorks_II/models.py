from django.db import models
from django.db.models.signals import post_save, pre_save
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.core.validators import RegexValidator
from datetime import datetime

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

post_save.connect(create_auth_token, sender=settings.AUTH_USER_MODEL)


class AssetCategory(models.Model):
    AssetCategoryCode = models.CharField(max_length=100, unique=True, validators=[alphanumeric], verbose_name='کد خانواده تجهیز')
    AssetCategoryName = models.CharField(max_length=100, verbose_name='نام خانواده تجهیز')
    slug = models.SlugField(max_length=100)
    AssetClassFather = models.ForeignKey('self', on_delete=models.RESTRICT, blank=True, null=True, verbose_name='خانواده تجهیز پدر')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'خانواده تجهیز'
        verbose_name_plural = 'خانواده های تجهیز'

    def __str__(self):
        return "{}-{}".format(self.AssetCategoryCode, self.AssetCategoryName)


class AssetClass(models.Model):
    AssetClassCode = models.CharField(max_length=100, unique=True, validators=[alphanumeric], verbose_name='کد کلاس تجهیز')
    AssetClassName = models.CharField(max_length=200, verbose_name='نام کلاس تجیز')
    AssetCategoryID = models.ForeignKey('AssetCategory', on_delete=models.RESTRICT, null=True, blank=False,
                                        verbose_name='خانواده تجیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'کلاس تجهیز'
        verbose_name_plural = 'کلاس های تجهیز'

    def __str__(self):
        return "{}-{}".format(self.AssetClassCode, self.AssetClassName)


class AssetClassSubdivision(models.Model):
    AssetClassFatherID = models.ForeignKey('AssetClass', on_delete=models.RESTRICT, null=True, related_name='ClassFather',
                                           blank=False,
                                           verbose_name='کلاس تجهیز پدر')
    AssetClassChildID = models.ForeignKey('AssetClass', on_delete=models.RESTRICT, null=True, related_name='ClassChild',
                                          blank=False,
                                          verbose_name='کلاس تجیز فرزند')
    AssetClassChildNumber = models.IntegerField(verbose_name='تعداد فرزند')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'زیر کلاس تجهیز'
        verbose_name_plural = 'زیر کلاس تجهیزات'

    def __str__(self):
        return "{}-{}".format(self.AssetClassFatherID, self.AssetClassChildID)


class FailureMode(models.Model):
    FailureModeCode = models.CharField(max_length=100, unique=True, validators=[alphanumeric], verbose_name='کد نوع خرابی')
    FailureModeName = models.CharField(max_length=200, verbose_name='نام نوع حرابی')
    FailureModeDescription = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.RESTRICT, null=True, blank=False,
                                     verbose_name='کلاس تجهیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'نوع خرابی'
        verbose_name_plural = 'انواع خرابی'

    def __str__(self):
        return "{}-{}".format(self.FailureModeCode, self.FailureModeName)


class FailureCause(models.Model):
    FailureCauseCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد علت خرابی')
    FailureCauseName = models.CharField(max_length=200, verbose_name='نام علت حرابی')
    FailureCauseDescription = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    FailureModeID = models.ForeignKey('FailureMode', on_delete=models.RESTRICT, null=True, blank=False,
                                      verbose_name='نوع خرابی')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'علت خرابی'
        verbose_name_plural = 'علل خرابی'

    def __str__(self):
        return "{}-{}".format(self.FailureCauseCode, self.FailureCauseName)


class SpecificData(models.Model):
    SpecificDataCode = models.CharField(max_length=100, unique=True, validators=[alphanumeric], verbose_name='کد ویژگی')
    SpecificDataName = models.CharField(max_length=200, verbose_name='نام ویژگی')
    Measurment = models.CharField(max_length=200, verbose_name='اندازه گيري')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'

    def __str__(self):
        return "{}-{}".format(self.SpecificDataCode, self.SpecificDataName)


class AssetClassSpecificData(models.Model):
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.RESTRICT, null=True, blank=True, verbose_name='کلاس تجهیز')
    SpecificDataID = models.ForeignKey('SpecificData', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='ویژگی')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'مشخصات کلاس'
        verbose_name_plural = 'مشخصات کلاس ها'

    def __str__(self):
        return "{}-{}".format(self.AssetClassID, self.SpecificDataID)


class AssetPriority(models.Model):
    AssetPriorityCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد اولویت')
    AssetPriorityName = models.CharField(max_length=200, verbose_name='نام اولویت')
    AssetPriorityValue = models.IntegerField(verbose_name='ارزش اولویت')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'اولویت'
        verbose_name_plural = 'اولویت ها'

    def __str__(self):
        return "{}-{}".format(self.AssetPriorityCode, self.AssetPriorityName)


class Location(models.Model):
    LocationCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد مکان')
    LocationName = models.CharField(max_length=200, verbose_name='نام مکان')
    LocationFatherID = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True, verbose_name='مکان پدر')
    LocationCodeChain = models.CharField(max_length=1000, null=True, blank=True, verbose_name='کد مکانزنجيزه')
    LocationNameChain = models.CharField(max_length=1000, null=True, blank=True, verbose_name='زنجيزه نام مکان')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان ها'

    def __str__(self):
        return "{}-{}".format(self.LocationCode, self.LocationName)

def save_Loc(sender, instance, **kwargs):
    if instance.LocationFatherID:
        instance.LocationCodeChain="_".join([instance.LocationFatherID.LocationCodeChain, instance.LocationCode])
        instance.LocationNameChain="_".join([instance.LocationFatherID.LocationNameChain, instance.LocationName])
    else:
        instance.LocationCodeChain=instance.LocationCode
        instance.LocationNameChain=instance.LocationName
        
pre_save.connect(save_Loc, sender=Location)

class Asset(models.Model):
    AssetCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد تجهیز')
    AssetName = models.CharField(max_length=200, verbose_name='نام تجهیز')
    InstallationDate = models.DateField(verbose_name='تاریخ نصب', null=True, blank=True)
    AssetPriorityID = models.ForeignKey('AssetPriority', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='اولویت')
    LocationID = models.ForeignKey('Location', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='مکان')
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='کلاس تجهیز')
    status = models.IntegerField(verbose_name='وضعيت توليد', blank=True)
    fakesub = models.IntegerField(verbose_name='زيرمجموعه فيک', blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تجهیز'
        verbose_name_plural = 'تجهیزات'

    def __str__(self):
        return "{}-{}".format(self.AssetCode, self.AssetName)


class AssetSubdivision(models.Model):
    AssetID = models.ForeignKey('Asset', on_delete=models.RESTRICT, null=True, blank=True,
                                verbose_name='تجهیز')
    AssetChildID = models.ForeignKey('AssetClass', on_delete=models.RESTRICT, null=True, blank=False,
                                     verbose_name='زیر تجهیز')
    AssetSubdivisionFatherID = models.ForeignKey('self', on_delete=models.RESTRICT, null=True,
                                                 blank=True, verbose_name='کلاس پدر')
    fakelocation=models.IntegerField(verbose_name='مکان فيک', blank=True)
    AssetClassCodeChain = models.CharField(max_length=500, verbose_name='رشته کد کلاس')
    AssetClassNameChain = models.CharField(max_length=500, verbose_name='رشته نام کلاس')
    idChain = models.CharField(max_length=500, verbose_name='رشته اي دي')
    AssetCode = models.CharField(max_length=500, verbose_name='کد تجهيز')
    AssetName = models.CharField(max_length=500, verbose_name='نام تجهيز')
    tree = models.IntegerField(blank=True, verbose_name='وضعیت درخت')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'زیر مجموعه'
        verbose_name_plural = 'زیر مجموعه'


def save_Asset(sender, instance, created, **kwargs):
    if created:
        if instance.status == 0:
            AssetSubdivision.objects.create(AssetID=instance, AssetChildID=instance.AssetClassID, tree=1,
                                            fakelocation=instance.LocationID.id, AssetClassCodeChain=instance.AssetClassID.AssetClassCode,
                                            AssetClassNameChain=instance.AssetClassID.AssetClassName, AssetCode=instance.AssetCode, AssetName=instance.AssetName)
            cn = AssetClassSubdivision.objects.filter(AssetClassFatherID=instance.AssetClassID)
            ma = AssetSubdivision.objects.filter(AssetID=instance, AssetChildID=instance.AssetClassID, tree=1)
            for i in cn:
                chn = range(i.AssetClassChildNumber)
                for j in chn:
                    cchain="_".join([ma[0].AssetClassCodeChain, i.AssetClassChildID.AssetClassCode])
                    nchain="_".join([ma[0].AssetClassNameChain, i.AssetClassChildID.AssetClassName])
                    ichain=str(ma[0].id)
                    AssetSubdivision.objects.create(AssetChildID=i.AssetClassChildID, AssetSubdivisionFatherID=ma[0], tree=0,
                                                    fakelocation=instance.LocationID.id, AssetClassCodeChain=cchain,
                                                    AssetClassNameChain=nchain, idChain=ichain, AssetCode=instance.AssetCode, AssetName=instance.AssetName)
                    cnn = AssetClassSubdivision.objects.filter(AssetClassFatherID=i.AssetClassChildID)
                    maa = AssetSubdivision.objects.filter(AssetChildID=i.AssetClassChildID, AssetSubdivisionFatherID=ma[0])
                    for z in cnn:
                        chnn = range(z.AssetClassChildNumber)
                        for x in chnn:
                            cchainn="_".join([cchain, z.AssetClassChildID.AssetClassCode])
                            nchainn="_".join([nchain, z.AssetClassChildID.AssetClassName])
                            ichainn="_".join([ichain, str(maa[0].id)])
                            AssetSubdivision.objects.create(AssetChildID=z.AssetClassChildID,
                                                            AssetSubdivisionFatherID=maa[0], tree=0, fakelocation=instance.LocationID.id, AssetClassCodeChain=cchainn,
                                                            AssetClassNameChain=nchainn, idChain=ichainn, AssetCode=instance.AssetCode, AssetName=instance.AssetName)
                            cnnn = AssetClassSubdivision.objects.filter(AssetClassFatherID=z.AssetClassChildID)
                            maaa = AssetSubdivision.objects.filter(AssetChildID=z.AssetClassChildID,
                                                                   AssetSubdivisionFatherID=maa[0])
                            for y in cnnn:
                                chhnn = range(y.AssetClassChildNumber)
                                for m in chhnn:
                                    cchainnn="_".join([cchainn, y.AssetClassChildID.AssetClassCode])
                                    nchainnn="_".join([nchainn, y.AssetClassChildID.AssetClassName])
                                    ichainnn="_".join([ichainn, str(maaa[0].id)])
                                    AssetSubdivision.objects.create(AssetChildID=y.AssetClassChildID,
                                                                    AssetSubdivisionFatherID=maaa[0], tree=0, fakelocation=instance.LocationID.id, AssetClassCodeChain=cchainnn,
                                                                    AssetClassNameChain=nchainnn, idChain=ichainnn, AssetCode=instance.AssetCode, AssetName=instance.AssetName)
                                    cnnnn = AssetClassSubdivision.objects.filter(AssetClassFatherID=y.AssetClassChildID)
                                    maaaa = AssetSubdivision.objects.filter(AssetChildID=y.AssetClassChildID, AssetSubdivisionFatherID=maaa[0])
                                    for n in cnnnn:
                                        chhnnn = range(n.AssetClassChildNumber)
                                        for r in chhnnn:
                                            cchainnnn="_".join([cchainnn, n.AssetClassChildID.AssetClassCode])
                                            nchainnnn="_".join([nchainnn, n.AssetClassChildID.AssetClassName])
                                            ichainnnn="_".join([ichainnn, str(maaaa[0].id)])
                                            AssetSubdivision.objects.create(AssetChildID=n.AssetClassChildID,
                                                                            AssetSubdivisionFatherID=maaaa[0], tree=0, fakelocation=instance.LocationID.id, AssetClassCodeChain=cchainnnn,
                                                                            AssetClassNameChain=nchainnnn, idChain=ichainnnn, AssetCode=instance.AssetCode, AssetName=instance.AssetName)
                                            cnnnnn = AssetClassSubdivision.objects.filter(AssetClassFatherID=n.AssetClassChildID)
                                            maaaaa = AssetSubdivision.objects.filter(AssetChildID=n.AssetClassChildID, AssetSubdivisionFatherID=maaaa[0])
                                            for v in cnnnnn:
                                                chhnnnn = range(v.AssetClassChildNumber)
                                                for c in chhnnnn:
                                                    cchainnnnn="_".join([cchainnnn, v.AssetClassChildID.AssetClassCode])
                                                    nchainnnnn="_".join([nchainnnn, v.AssetClassChildID.AssetClassName])
                                                    ichainnnnn="_".join([ichainnnn, str(maaaaa[0].id)])
                                                    AssetSubdivision.objects.create(AssetChildID=v.AssetClassChildID,
                                                                                    AssetSubdivisionFatherID=maaaaa[0], tree=0, fakelocation=instance.LocationID.id, AssetClassCodeChain=cchainnnnn,
                                                                                    AssetClassNameChain=nchainnnnn, idChain=ichainnnnn, AssetCode=instance.AssetCode, AssetName=instance.AssetName)
                                                    cnnnnnn = AssetClassSubdivision.objects.filter(AssetClassFatherID=v.AssetClassChildID)
                                                    maaaaaa = AssetSubdivision.objects.filter(AssetChildID=v.AssetClassChildID, AssetSubdivisionFatherID=maaaaa[0])
                                                    for b in cnnnnnn:
                                                        chhnnnnn = range(b.AssetClassChildNumber)
                                                        for s in chhnnnnn:
                                                            cchainnnnnn="_".join([cchainnnnn, b.AssetClassChildID.AssetClassCode])
                                                            nchainnnnnn="_".join([nchainnnnn, b.AssetClassChildID.AssetClassName])
                                                            ichainnnnnn="_".join([ichainnnnn, str(maaaaaa[0].id)])
                                                            AssetSubdivision.objects.create(AssetChildID=b.AssetClassChildID,
                                                                                            AssetSubdivisionFatherID=maaaaaa[0], tree=0, fakelocation=instance.LocationID.id, AssetClassCodeChain=cchainnnnnn,
                                                                                            AssetClassNameChain=nchainnnnnn, idChain=ichainnnnnn, AssetCode=instance.AssetCode, AssetName=instance.AssetName)
        elif instance.status == 1:
            AssetSubdivision.objects.filter(id=instance.fakesub).update(AssetID=instance, AssetCode=instance.AssetCode, AssetName=instance.AssetName)
        
                                                
                                    
                                    
                                    


post_save.connect(save_Asset, sender=Asset)

class AssetSubdivisionSparePart(models.Model):
    AssetSubdivisionID = models.ForeignKey('AssetSubdivision', on_delete=models.RESTRICT, null=True, blank=False,
                                           verbose_name='تجهیز')
    SparePartID = models.ForeignKey('SparePart', on_delete=models.RESTRICT, null=True, blank=True, verbose_name='قطعات یدکی')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی زیر مجموعه'
        verbose_name_plural = 'ویژگی های زیر مجموعه'


class AssetSpecificData(models.Model):
    AssetSubdivisionID = models.ForeignKey('AssetSubdivision', on_delete=models.RESTRICT, null=True, blank=False,
                                           verbose_name='تجهیز')
    SpecificDataID = models.ForeignKey('SpecificData', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='ویژگی')
    SpecificAmount = models.IntegerField(verbose_name='مقدار ویژگی', null=True, blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

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
    SparePartDimensionCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد بعد')
    SparePartDimensionName = models.CharField(max_length=200, verbose_name='نام بعد')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'بعد قطعه'
        verbose_name_plural = 'بعد قطعات'

    def __str__(self):
        return "{}-{}".format(self.SparePartDimensionCode, self.SparePartDimensionName)


class SparePartCategory(models.Model):
    SparePartCategoryCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد خانواده قطعه')
    SparePartCategoryName = models.CharField(max_length=200, verbose_name='نام خانواده قطعه')
    SparePartCategoryFather = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True,
                                                verbose_name='خانواده قطعه  پدر')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'خانواده قطعه'
        verbose_name_plural = 'خانواده های قطعه'

    def __str__(self):
        return "{}-{}".format(self.SparePartCategoryCode, self.SparePartCategoryName)


class SparePart(models.Model):
    SparePartCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد قطعه')
    SparePartName = models.CharField(max_length=200, verbose_name='نام قطعه')
    SparePartCategoryID = models.ForeignKey('SparePartCategory', on_delete=models.RESTRICT, null=True, blank=False,
                                            verbose_name='خانواده قطعه')
    SparePartDimensionID = models.ForeignKey('SparePartDimension', on_delete=models.RESTRICT, null=True, blank=False,
                                             verbose_name='بعد قطعه')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'قطعه'
        verbose_name_plural = 'قطعات'

    def __str__(self):
        return "{}-{}".format(self.SparePartCode, self.SparePartName)


def upload_path(instance, filename):
    return '/'.join(['Files', str(instance.DocumentCode), filename])


class Document(models.Model):
    DocumentCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد فایل')
    DocumentName = models.CharField(max_length=200, verbose_name='نام فایل')
    DocumentDescription = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    FileAddress = models.FileField(upload_to=upload_path, verbose_name='فایل')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'قایل'
        verbose_name_plural = 'فایل ها'

    def __str__(self):
        return "{}-{}".format(self.DocumentCode, self.DocumentName)


class AssetClassDocument(models.Model):
    DocumentID = models.ForeignKey('Document', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='فایل')
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='تجهیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'قایل تجهیز'
        verbose_name_plural = 'فایل های تجهیز'

    def __str__(self):
        return "{}-{}".format(self.DocumentID, self.AssetClassID)


class TaskType(models.Model):
    TaskTypeCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد نوع وظیفه')
    TaskTypeName = models.CharField(max_length=200, verbose_name='نام نوع وظیفه')
    TaskTypeDescription = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'نوع وظیفه'
        verbose_name_plural = 'انواع وظیفه'

    def __str__(self):
        return "{}-{}".format(self.TaskTypeCode, self.TaskTypeName)


class JobCategory(models.Model):
    JobCategoryCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد نوع شغل')
    JobCategoryName = models.CharField(max_length=200, verbose_name='نام نوع شغل')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

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
    TaskCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد وظیفه')
    TaskName = models.CharField(max_length=200, verbose_name='نام وظیفه')
    TaskDescription = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    FrequencyName = models.CharField(max_length=1, choices=Frequency, verbose_name='نام تناوب', null=True, blank=True)
    FrequencyAmount = models.IntegerField(verbose_name='مقدار تناوب', null=True, blank=True)
    DurationOfDo = models.IntegerField(verbose_name='مدت زمان انجام', null=True, blank=True)
    Functor = models.CharField(max_length=1, choices=fun, verbose_name='مسئول', null=True, blank=True)
    TaskTypeID = models.ForeignKey('TaskType', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='نوع وظیفه')
    JobCategoryID = models.ForeignKey('JobCategory', on_delete=models.RESTRICT, null=True, blank=True, verbose_name='نوع شغل')
    AssetClassID = models.ForeignKey('AssetClass', on_delete=models.RESTRICT, null=True, blank=False,
                                           verbose_name='کلاس تجهیز')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظایف'

    def __str__(self):
        return "{}-{}".format(self.TaskCode, self.TaskName)


class Department(models.Model):
    DepartmentCode = models.CharField(max_length=100, verbose_name='کد دپارتمان')
    DepartmentName = models.CharField(max_length=200, verbose_name='نام دپارتمان')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'دپارتمان'
        verbose_name_plural = 'دپارتمان ها'

    def __str__(self):
        return "{}-{}".format(self.DepartmentCode, self.DepartmentName)


class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT, null=True, blank=True, verbose_name='یوزر')
    PersonnelCode = models.CharField(max_length=100, verbose_name='کد پرسنل')
    PersonnelNetCode = models.CharField(max_length=100, verbose_name='کد نت پرسنل')
    PersonnelName = models.CharField(max_length=200, verbose_name='نام پرسنل')
    PersonnelFamily = models.CharField(max_length=200, verbose_name='فامیل پرسنل')
    PersonnelMobile = models.CharField(max_length=100, verbose_name='شماره پرسنل', null=True, blank=True)
    DepartmentID = models.ForeignKey('Department', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='دپارتمان')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'پرسنل'
        verbose_name_plural = 'پرسنل'

    def __str__(self):
        return "{}-{}".format(self.PersonnelCode, self.PersonnelName)


class PersonnelJobCategory(models.Model):
   JobCategoryID = models.ForeignKey('JobCategory', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='نوع شغل')
   PersonnelID = models.ForeignKey('Personnel', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='پرسنل')
   Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
   Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

   class Meta:
      ordering = ['-Create']
      verbose_name = 'شغل پرسنل'
      verbose_name_plural = 'شغل های پرسنل'
 
   def __str__(self):
      return "{}-{}".format(self.JobCategoryID, self.PersonnelID)


class TypeWr(models.Model):
    TypeWrCode = models.CharField(max_length=100, verbose_name='کد نوع درخواست کار')
    TypeWrName = models.CharField(max_length=200, verbose_name='نام نوع درخواست کار')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

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
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'اولویت درخواست کار'
        verbose_name_plural = 'اولویت های درخواست کار'

    def __str__(self):
        return "{}-{}".format(self.WorkPriorityCode, self.WorkPriorityName)


class Supplier(models.Model):
    SupplierCode = models.CharField(max_length=100, verbose_name='کد تامین کننده')
    SupplierName = models.CharField(max_length=200, verbose_name='نام تامین کننده')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تامین کننده'
        verbose_name_plural = 'تامین کنندگان'

    def __str__(self):
        return "{}-{}".format(self.SupplierCode, self.SupplierName)


class SupplierSpecific(models.Model):
    SupplierSpecificCode = models.CharField(max_length=100, verbose_name='کد ویژگی تامین کننده')
    SupplierSpecificName = models.CharField(max_length=200, verbose_name='نام ویژگی تامین کننده')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی تامین کننده'
        verbose_name_plural = 'ویژگی های تامین کننده'

    def __str__(self):
        return "{}-{}".format(self.SupplierSpecificCode, self.SupplierSpecificName)


class SupplierSpecificData(models.Model):
    SupplierID = models.ForeignKey('Supplier', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='تامین کننده')
    SupplierSpecificID = models.ForeignKey('SupplierSpecific', on_delete=models.RESTRICT, null=True, blank=False,
                                           verbose_name='ویژگی')
    SpecificAmount = models.CharField(max_length=50, verbose_name='مقدار ویژگی')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ویژگی های تامین کننده'
        verbose_name_plural = 'ویژگی های تامین کنندگان'

    # def __str__(self):
    #   return "{}-{}".format(self.SupplierSpecificCode, self.SupplierSpecificName)


class WorkRequest(models.Model):
    WRDate = models.DateField(verbose_name='تاریخ')
    WRTime = models.TimeField(verbose_name='ساعت')
    WRDateOfRegistration = models.DateField(verbose_name='تاریخ ثبت')
    WRTimeOfRegistration = models.TimeField(verbose_name='زمان ثبت')
    WRDescription = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    AssetSubdivisionID = models.ForeignKey('AssetSubdivision', on_delete=models.RESTRICT, null=True, blank=False,
                                           verbose_name='تجهیز')
    FailureModeID = models.ForeignKey('FailureMode', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='نوع خرابی')
    WorkPriorityID = models.ForeignKey('WorkPriority', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='اولویت')
    TypeWrID = models.ForeignKey('TypeWr', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='نوع')
    StatusID = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, blank=True, verbose_name='وضعيت')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'درخواست کار'
        verbose_name_plural = 'درخواست کار ها'

    def __str__(self):
        return "WR%06d" % self.id


class WorkOrder(models.Model):
    WODateOfRegistration = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    WODescription = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    DateOfPlanStart = models.DateField(null=True, blank=True, verbose_name='تاریخ شروع برنامه')
    DateOfPlanFinish = models.DateField(null=True, blank=True, verbose_name=' برنامهتاریخ پایان')
    DateOfStart = models.DateField(null=True, blank=True, verbose_name='تاریخ شروع')
    DateOfFinish = models.DateField(null=True, blank=True, verbose_name='تاریخ پایان')
    WorkRequestID = models.ForeignKey('WorkRequest', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='درخواست کار')
    StatusID = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, blank=True, verbose_name='وضعيت')
    DepartmentID = models.ForeignKey('Department', on_delete=models.RESTRICT, null=True, blank=True, verbose_name='دپارتمان')
    WorkOrderType = models.TextField(verbose_name='نوع', null=True, blank=True)
    WOTemplateCode = models.TextField(verbose_name='کد برنامه', null=True, blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'دستور کار'
        verbose_name_plural = 'دستور کار ها'

    def __str__(self):
        return "WR%06d-WO%06d".format(self.WorkRequestID, self.id)


class WOSupplier(models.Model):
    WorkStartDate = models.DateField(verbose_name='تاریخ شروع')
    WorkFinishDate = models.DateField(verbose_name='تاریخ پایان')
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='دستور کار')
    SupplierID = models.ForeignKey('Supplier', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='تامین کنده')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تامین کننده دستور کار'
        verbose_name_plural = 'تامین کننده های دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.SupplierID)


class WOPersonnel(models.Model):
    WorkDate = models.DateField(verbose_name='تاریخ انجام')
    WorkTime = models.IntegerField(verbose_name='مدت زمان انجام')
    WOTaskID = models.ForeignKey('WOTask', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='دستور کار وظيفه')
    PersonnelID = models.ForeignKey('Personnel', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='پرسنل')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'پرسنل دستور کار'
        verbose_name_plural = 'پرسنل های دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.PersonnelID)


class Delay(models.Model):
    DelayCode = models.CharField(max_length=100, verbose_name='کد تاخیر')
    DelayName = models.CharField(max_length=200, verbose_name='نام تاخیر')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

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
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='دستور کار')
    DelayID = models.ForeignKey('Delay', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='تاخیر')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تاخیر دستور کار'
        verbose_name_plural = 'تاخیر های دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.DelayID)


class WOSparePart(models.Model):
    WOTaskID = models.ForeignKey('WOTask', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='وظيفه دستورکار')
    SparePartID = models.ForeignKey('SparePart', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='قطعه')
    SparePartAmount = models.IntegerField(verbose_name='تعداد قطعه')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'قطعه دستور کار'
        verbose_name_plural = 'قطعات دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.SparePartID)


class WOTask(models.Model):
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='دستور کار')
    TaskID = models.ForeignKey('AssetClassTask', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='وظیفه')
    WOTaskSituationOfDo = models.CharField(max_length=50, verbose_name='وضعیت انجام')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'وظیفه دستور کار'
        verbose_name_plural = 'وظایف دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkOrderID, self.TaskID)


class WOTemplateType(models.Model):
    WOTemplateTypeCode = models.CharField(max_length=100, verbose_name='کد نوع برنامه')
    WOTemplateTypeName = models.CharField(max_length=200, verbose_name='نام نوع برنامه')
    WOTemplateTypeDescription = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

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
    WOTemplateAlarmDay = models.IntegerField(verbose_name='روز اعلام تناوب', null=True, blank=True)
    WOTemplateAlarmHour = models.IntegerField(verbose_name='ساعت اعلام تناوب', null=True, blank=True)
    DepartmentID = models.ForeignKey('Department', on_delete=models.RESTRICT, verbose_name='دپارتمان')
    WOTemplateTypeID = models.ForeignKey('WOTemplateType', on_delete=models.RESTRICT, verbose_name='نوع')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'تناوب دستور کار'
        verbose_name_plural = 'تناوب های دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WOTemplateCode, self.WOTemplateName)


class WOTemplateSchualing(models.Model):
    WOTemplateSchualingStartDate = models.DateTimeField(verbose_name='روز شروع برنامه')
    WOTemplateSchualingFinishDate = models.DateTimeField(verbose_name='روز پایان برنامه')
    AmountFrequency = models.IntegerField(verbose_name='مقدار')
    Status = models.BooleanField(default=False, verbose_name='وضعیت')
    WOTemplateID = models.ForeignKey('WOTemplate', on_delete=models.RESTRICT, verbose_name='دستور کار')
    FrequencyName = models.CharField(max_length=100, verbose_name='تناوب')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'برنامه ریزی شده'
        verbose_name_plural = 'برنامه ریزی شده ها'

    def __str__(self):
        return "{}-{}".format(self.WOTemplateID, self.FrequencyName)

def save_WOTemplateSchualing(sender, instance, created, **kwargs):
        if instance.Status == True:
            cf = instance.FrequencyName
            tis = instance.WOTemplateSchualingStartDate
            alarm = tis - timedelta(days=instance.WOTemplateID.WOTemplateAlarmDay, hours=instance.WOTemplateID.WOTemplateAlarmHour)
            while tis <= instance.WOTemplateSchualingFinishDate:
                print(tis)
                print('a', alarm)
                TemplateSchualingDate.objects.create(SchualingDate = tis ,WOTemplateSchualingID = instance, SchedualingAlarmDate = alarm )
                if cf == 'D':
                    tis = tis + timedelta(days=instance.AmountFrequency)
                    alarm = tis - timedelta(days=instance.WOTemplateID.WOTemplateAlarmDay, hours=instance.WOTemplateID.WOTemplateAlarmHour)
                elif cf == 'W':
                    tis = tis + timedelta(weeks=instance.AmountFrequency)
                    alarm = tis - timedelta(days=instance.WOTemplateID.WOTemplateAlarmDay, hours=instance.WOTemplateID.WOTemplateAlarmHour)
                elif cf == 'M':
                    tis = tis + relativedelta(months=instance.AmountFrequency)
                    alarm = tis - timedelta(days=instance.WOTemplateID.WOTemplateAlarmDay, hours=instance.WOTemplateID.WOTemplateAlarmHour)
                elif cf == 'Y':
                    tis = tis + relativedelta(years=instance.AmountFrequency)
                    alarm = tis - timedelta(days=instance.WOTemplateID.WOTemplateAlarmDay, hours=instance.WOTemplateID.WOTemplateAlarmHour)
                elif cf == 'H':
                    tis = tis + timedelta(hours=instance.AmountFrequency)
                    alarm = tis - timedelta(days=instance.WOTemplateID.WOTemplateAlarmDay, hours=instance.WOTemplateID.WOTemplateAlarmHour)



post_save.connect(save_WOTemplateSchualing, sender=WOTemplateSchualing)



class TemplateSchualingDate(models.Model):
    SchualingDate = models.DateTimeField(verbose_name='روز برنامه')
    SchedualingAlarmDate = models.DateTimeField(verbose_name='روز اعلام برنامه')
    WOTemplateSchualingID = models.ForeignKey('WOTemplateSchualing', on_delete=models.RESTRICT, verbose_name='برنامه')
    StatusOfDo = models.BooleanField(default=False, verbose_name='وضعیت انجام')
    WorkOrderID = models.ForeignKey('WorkOrder', null=True, blank=True, on_delete=models.RESTRICT, verbose_name='دستور کار')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'برنامه ریزی '
        verbose_name_plural = 'برنامه ریزی ها'

    def __str__(self):
        return "{}-{}".format(self.SchualingDate, self.WOTemplateSchualingID)

class WOTemplateAsset(models.Model):
   WOTemplateID = models.ForeignKey('WOTemplate', on_delete=models.RESTRICT, verbose_name='برنامه')
   AssetSubdivisionID = models.ForeignKey('AssetSubdivision', on_delete=models.RESTRICT,
                                           verbose_name='تجهیز')
   Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
   Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

   class Meta:
      ordering = ['-Create']
      verbose_name = 'تجهيز برنامه'
      verbose_name_plural = 'تجهيزات برنامه'
 
   def __str__(self):
      return "{}-{}".format(self.WOTemplateID, self.AssetSubdivisionID)


class WOTemplateActivity(models.Model):
   WOTemplateAssetID = models.ForeignKey('WOTemplateAsset', on_delete=models.RESTRICT, verbose_name='تجهيز برنامه')
   TaskID = models.ForeignKey('AssetClassTask', on_delete=models.RESTRICT, verbose_name='وظيفه')
   Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
   Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

   class Meta:
      ordering = ['-Create']
      verbose_name = 'وظايف تجهيز برنامه'
      verbose_name_plural = 'وظايف تجهيزات برنامه'
 
   def __str__(self):
      return "{}-{}".format(self.WOTemplateAssetID, self.TaskID)


class WorkRequestFailureCause(models.Model):
    WorkRequestID = models.ForeignKey('WorkRequest', on_delete=models.RESTRICT, null=True, related_name='WorkRequest',
                                           blank=False,
                                           verbose_name='درخواست کار')
    FailureCauseID = models.ForeignKey('FailureCause', on_delete=models.RESTRICT, null=True, related_name='FailureCause',
                                          blank=False,
                                          verbose_name='علت خرابي')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'علت خرابي درخواست کار'
        verbose_name_plural = 'علل خرابي دستور کار'

    def __str__(self):
        return "{}-{}".format(self.WorkRequestID, self.FailureCauseID)

class Status(models.Model):
    StatusCode = models.CharField(max_length=100, validators=[alphanumeric], verbose_name='کد وضعيت')
    StatusName = models.CharField(max_length=200, verbose_name='نام وضعيت')
    StatusCondition = models.CharField(max_length=200, verbose_name='شرايط')
    OpCl = models.CharField(max_length=100, null=True, blank=True, verbose_name='وضعيت')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'وضعيت'
        verbose_name_plural = 'انوع وضعيت'

    def __str__(self):
        return "{}-{}".format(self.StatusCode, self.StatusName)


def save_WRS(sender, instance, created, **kwargs):
    if created:
        st = WorkflowLevelStatus.objects.filter(WorkflowLevelID = 1, WorkflowLevelStatusPeriority = 0)
        WRStatus.objects.create(WorkRequestID=instance, StatusID=st[0].StatusID, StatusDate=datetime.date(datetime.now()), StatusTime=datetime.time(datetime.now()))


post_save.connect(save_WRS, sender=WorkRequest)

def save_WOS(sender, instance, created, **kwargs):
    if created:
        st = WorkflowLevelStatus.objects.filter(WorkflowLevelID = 4, WorkflowLevelStatusPeriority = 0)
        WOStatus.objects.create(WorkOrderID=instance, StatusID=st[0].StatusID, StatusDate=datetime.date(datetime.now()), StatusTime=datetime.time(datetime.now()))


post_save.connect(save_WOS, sender=WorkOrder)

class WRWORelationStatus(models.Model):
    StatusWOID = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, related_name='WorkOrder',
                                           blank=False,
                                           verbose_name='دستور کار')
    StstusWRID = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, related_name='WorkRequest',
                                          blank=False,
                                          verbose_name='درخواست کار')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'ارتباط وضعيت'
        verbose_name_plural = 'ارتباط وضعيت ها'

    def __str__(self):
        return "{}-{}".format(self.StatusWOID, self.StstusWRID)

class WRStatus(models.Model):
    StatusID = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='وضعيت')
    WorkRequestID = models.ForeignKey('WorkRequest', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='درخواست کار')
    StatusDate = models.DateField(verbose_name='تاریخ ثبت')
    StatusTime = models.TimeField(verbose_name='زمان ثبت')
    StatusDescription = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'وضعيت درخواست کار'
        verbose_name_plural = 'وضعيت هاي درخواستت کار'

    def __str__(self):
        return "{}-{}".format(self.StatusID, self.WorkRequestID)


class WOStatus(models.Model):
    StatusID = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='وضعيت')
    WorkOrderID = models.ForeignKey('WorkOrder', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='دستور کار')
    StatusDate = models.DateField(verbose_name='تاریخ ثبت')
    StatusTime = models.TimeField(verbose_name='زمان ثبت')
    StatusDescription = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'وضعيت دستور کار'
        verbose_name_plural = 'وضعيت هاي دستور کار'

    def __str__(self):
        return "{}-{}".format(self.StatusID, self.WorkOrderID)

def save_WRupdate(sender, instance, created, **kwargs):
    if created:
        WorkRequest.objects.filter(id=instance.WorkRequestID.id).update(StatusID=instance.StatusID)

post_save.connect(save_WRupdate, sender=WRStatus)

def save_WOupdate(sender, instance, created, **kwargs):
    if created:
        WorkOrder.objects.filter(id=instance.WorkOrderID.id).update(StatusID=instance.StatusID)
        req = WorkOrder.objects.filter(id=instance.WorkOrderID.id)
        if req[0].WorkRequestID:
            rst = WRWORelationStatus.objects.filter(StatusWOID=instance.StatusID.id)
            WRStatus.objects.create(WorkRequestID=req[0].WorkRequestID, StatusID=rst[0].StstusWRID, StatusDate=datetime.date(datetime.now()), StatusTime=datetime.time(datetime.now()))

post_save.connect(save_WOupdate, sender=WOStatus)


class WorkflowLevel(models.Model):
    WorkflowLevelName = models.CharField(max_length=200, verbose_name='نام سطح')
    WorkflowLevelType = models.CharField(max_length=200, verbose_name='نوع سطح')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'سطح وضعيت'
        verbose_name_plural = 'سطوح وضعيت'

    def __str__(self):
        return "{}".format(self.WorkflowLevelName)


class WorkflowLevelStatus(models.Model):
    StatusID = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='وضعيت')
    WorkflowLevelID = models.ForeignKey('WorkflowLevel', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='سطح')
    WorkflowLevelStatusPeriority = models.IntegerField(verbose_name='اولويت', blank=True)
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'کار سطح وضعيت'
        verbose_name_plural = 'کار سطوح وضعيت'

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.StatusID, self.WorkflowLevelID)

class WorkflowLevelStatusShow(models.Model):
    StatusID = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='وضعيت')
    WorkflowLevelStatusID = models.ForeignKey('WorkflowLevelStatus', on_delete=models.RESTRICT, null=True, blank=False, verbose_name='سطح')
    Create = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ایجاد')
    Update = jmodels.jDateTimeField(auto_now=True, null=True, blank=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        ordering = ['-Create']
        verbose_name = 'نشان کار سطح وضعيت'
        verbose_name_plural = 'نشان کار سطوح وضعيت'

    def __str__(self):
        return "{}-{}".format(self.StatusID, self.WorkflowLevelID)
