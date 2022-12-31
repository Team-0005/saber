from django.db import models
from tests.models import Diagnosis, PsychoTest
from blog.models import Psychologist
# Create your models here.


class Patient(models.Model):
    pt_id = models.AutoField(primary_key=True)
    pt_phone_no = models.CharField(max_length=13)
    pt_name = models.CharField(max_length=250)
    pt_gender = models.CharField(max_length=6)
    pt_edu_level = models.CharField(max_length=60)
    pt_birth_date = models.DateField()
    pt_code = models.CharField(max_length=4, blank=True, null=True)
    pt_plan = models.CharField(max_length=1000, blank=True, null=True)
    # Field name made lowercase.
    p_email = models.ForeignKey(
        Psychologist, models.DO_NOTHING, db_column='P_email', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    pt = models.ForeignKey(Patient, models.DO_NOTHING)
    fk_diagnosis = models.ForeignKey(Diagnosis, models.DO_NOTHING)
    test = models.ForeignKey(PsychoTest, models.DO_NOTHING)
    test_result = models.IntegerField(blank=True, null=True)
    test_status = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'result'
