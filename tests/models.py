from django.db import models

# Create your models here.


class Diagnosis(models.Model):
    # Field name made lowercase.
    diagnosis_id = models.AutoField(db_column='diagnosis_ID', primary_key=True)
    diagnosis_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'diagnosis'


class PsychoTest(models.Model):
    # Field name made lowercase.
    test_id = models.AutoField(db_column='test_ID', primary_key=True)
    test_name = models.CharField(max_length=60)
    # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=400)
    # Field name made lowercase.
    test_file = models.FileField(
        db_column='test_file', upload_to="blog/static/blog/files/", blank=True, null=True)
    diagnosis_fk = models.ForeignKey(
        Diagnosis, models.DO_NOTHING, db_column='diagnosis_ID', blank=True, null=True)

    def __str__(self):
        return self.test_name

    class Meta:
        managed = False
        db_table = 'psycho_test'
