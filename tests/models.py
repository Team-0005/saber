from django.db import models

# Create your models here.
class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(db_column='diagnosis_ID', primary_key=True)  # Field name made lowercase.
    diagnosis_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'diagnosis'


class PsychoTest(models.Model):
    test_id = models.AutoField(db_column='test_ID', primary_key=True)  # Field name made lowercase.
    test_name = models.CharField(max_length=60)
    description = models.CharField(db_column='Description', max_length=400)  # Field name made lowercase.
    diagnosis_fk = models.ForeignKey(Diagnosis, models.DO_NOTHING, db_column='diagnosis_ID')  # Field name made lowercase.

    def __str__(self):
        return self.test_name

        
    class Meta:
        managed = False
        db_table = 'psycho_test'