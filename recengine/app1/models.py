# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
class Customer1(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    sumofprofile = models.CharField(max_length=300, db_column='sumOfProfile') # Field name made lowercase.
    month = models.CharField(max_length=300)
    entity = models.CharField(max_length=120)
    utilitydunsnumber = models.CharField(max_length=120)
    utilityaccountnumber = models.CharField(max_length=120)
    commodityid = models.FloatField()
    meternumber = models.FloatField()
    jan = models.FloatField()
    feb = models.FloatField()
    mar = models.FloatField()
    apr = models.FloatField()
    may = models.FloatField()
    jun = models.FloatField()
    jul = models.FloatField()
    aug = models.FloatField()
    sem = models.FloatField()
    oct = models.FloatField()
    nov = models.FloatField()
    december = models.FloatField()
    valuesperday = models.CharField(max_length=120, db_column='valuesPerDay', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'customer1'

class Customer2(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    entity = models.CharField(max_length=300)
    utility = models.CharField(max_length=300)
    utilityduns = models.CharField(max_length=120)
    utilityaccountnumber = models.CharField(max_length=120)
    commodityid = models.CharField(max_length=120)
    meternumberfixed = models.CharField(max_length=120)
    servicestart = models.DateField()
    contractexpiration = models.DateField()
    accounttype = models.CharField(max_length=120)
    rateclasscode = models.CharField(max_length=120)
    profiletype = models.CharField(max_length=120)
    producttype = models.CharField(max_length=120)
    iso = models.CharField(max_length=120)
    loadzone = models.CharField(max_length=120)
    plc = models.FloatField()
    nits = models.FloatField()
    currentrate = models.FloatField()
    annualvolume = models.FloatField()
    column1 = models.FloatField(db_column='Column1') # Field name made lowercase.
    class Meta:
        db_table = u'customer2'

