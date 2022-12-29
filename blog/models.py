from django.db import models

# Create your models here.


class Admin(models.Model):
    # Field name made lowercase.
    a_email = models.CharField(
        db_column='A_email', primary_key=True, max_length=50)
    # Field name made lowercase.
    a_password = models.CharField(db_column='A_password', max_length=50)

    class Meta:
        managed = False
        db_table = 'admin'


class Psychologist(models.Model):
    # Field name made lowercase.
    p_email = models.CharField(
        db_column='P_email', primary_key=True, max_length=50, verbose_name="الإيميل")
    # Field name made lowercase.
    p_password = models.CharField(db_column='P_password', max_length=250)
    # Field name made lowercase.
    p_f_name = models.CharField(
        db_column='P_F_name', max_length=45, verbose_name="الاسم الأول")
    # Field name made lowercase.
    p_l_name = models.CharField(
        db_column='P_L_name', max_length=45, verbose_name="اللقب")
    # Field name made lowercase.
    p_phone_no = models.CharField(db_column='P_phone_No', max_length=13)
    current_job_title = models.CharField(max_length=45)
    # Field name made lowercase.
    scfhs_no = models.CharField(db_column='SCFHS_No', max_length=10)
    # Field name made lowercase.
    scfhs_file = models.FileField(
        db_column='SCFHS_file', upload_to="blog/static/blog/files/")
    req_status = models.IntegerField(verbose_name="حالة الطلب")
    # Field name made lowercase.
    p_code = models.CharField(
        db_column='P_code', max_length=4, blank=True, null=True)

    def __str__(self):
        return self.p_f_name

    class Meta:
        managed = False
        db_table = 'psychologist'
