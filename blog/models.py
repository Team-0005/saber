from django.db import models

# Create your models here.
class Admin(models.Model):
    a_email = models.CharField(db_column='A_email', primary_key=True, max_length=50)  # Field name made lowercase.
    a_password = models.CharField(db_column='A_password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Psychologist(models.Model):
    p_email = models.CharField(db_column='P_email', primary_key=True, max_length=50, verbose_name="الإيميل")  # Field name made lowercase.
    p_password = models.CharField(db_column='P_password', max_length=50)  # Field name made lowercase.
    p_f_name = models.CharField(db_column='P_F_name', max_length=45, verbose_name="الاسم الأول")  # Field name made lowercase.
    p_l_name = models.CharField(db_column='P_L_name', max_length=45, verbose_name="اللقب")  # Field name made lowercase.
    p_phone_no = models.CharField(db_column='P_phone_No', max_length=13)  # Field name made lowercase.
    current_job_title = models.CharField(max_length=45)
    scfhs_no = models.CharField(db_column='SCFHS_No', max_length=10)  # Field name made lowercase.
    scfhs_file = models.FileField (db_column='SCFHS_file',upload_to="blog/static/blog/files/")  # Field name made lowercase.
    req_status = models.IntegerField(verbose_name="حالة الطلب")
    p_code = models.CharField(db_column='P_code', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'psychologist'        

       