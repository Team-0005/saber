from django.db import models

# Create your models here.
class Admin(models.Model):
    a_email = models.CharField(db_column='A_email', primary_key=True, max_length=50)  # Field name made lowercase.
    a_password = models.CharField(db_column='A_password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Psychologist(models.Model):
    p_email = models.CharField(db_column='P_email', primary_key=True, max_length=50)  # Field name made lowercase.
    p_password = models.CharField(db_column='P_password', max_length=50)  # Field name made lowercase.
    p_f_name = models.CharField(db_column='P_F_name', max_length=45)  # Field name made lowercase.
    p_l_name = models.CharField(db_column='P_L_name', max_length=45)  # Field name made lowercase.
    p_phone_no = models.CharField(db_column='P_phone_No', max_length=13)  # Field name made lowercase.
    current_job_title = models.CharField(max_length=45)
    scfhs_no = models.CharField(db_column='SCFHS_No', max_length=10)  # Field name made lowercase.
    scfhs_file = models.TextField(db_column='SCFHS_file')  # Field name made lowercase.
    req_status = models.IntegerField(verbose_name="رقم الطلب")
    a_email = models.ForeignKey(Admin, models.DO_NOTHING, db_column='A_email', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psychologist'        