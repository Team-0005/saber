# Generated by Django 4.1.3 on 2022-12-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('a_email', models.CharField(db_column='A_email', max_length=50, primary_key=True, serialize=False)),
                ('a_password', models.CharField(db_column='A_password', max_length=50)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Psychologist',
            fields=[
                ('p_email', models.CharField(db_column='P_email', max_length=50, primary_key=True, serialize=False)),
                ('p_password', models.CharField(db_column='P_password', max_length=50)),
                ('p_f_name', models.CharField(db_column='P_F_name', max_length=45)),
                ('p_l_name', models.CharField(db_column='P_L_name', max_length=45)),
                ('p_phone_no', models.CharField(db_column='P_phone_No', max_length=13)),
                ('current_job_title', models.CharField(max_length=45)),
                ('scfhs_no', models.CharField(db_column='SCFHS_No', max_length=10)),
                ('scfhs_file', models.TextField(db_column='SCFHS_file')),
                ('req_status', models.IntegerField()),
            ],
            options={
                'db_table': 'psychologist',
                'managed': False,
            },
        ),
    ]
