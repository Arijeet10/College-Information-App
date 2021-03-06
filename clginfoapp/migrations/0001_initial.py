# Generated by Django 3.1.1 on 2020-10-07 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clgdetails',
            fields=[
                ('College_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Contact_no', models.BigIntegerField()),
                ('Affiliation', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('Hostel_facility', models.CharField(max_length=100)),
                ('Ratings', models.IntegerField()),
            ],
            options={
                'db_table': 'College Details',
            },
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('Course_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=100)),
                ('Course_fees', models.BigIntegerField()),
                ('College_ID', models.ForeignKey(db_column='College_ID', default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clginfoapp.clgdetails')),
            ],
            options={
                'db_table': 'Course Details',
            },
        ),
        migrations.CreateModel(
            name='seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(default=0, max_length=100)),
                ('seats_no', models.BigIntegerField()),
                ('College_ID', models.ForeignKey(db_column='College_ID', default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clginfoapp.clgdetails')),
                ('Course_ID', models.ForeignKey(db_column='Course_ID', default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clginfoapp.courses')),
            ],
            options={
                'db_table': 'Available Seats',
            },
        ),
    ]
