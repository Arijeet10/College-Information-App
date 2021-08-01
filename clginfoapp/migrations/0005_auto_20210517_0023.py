# Generated by Django 3.1.1 on 2021-05-16 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clginfoapp', '0004_exams'),
    ]

    operations = [
        migrations.CreateModel(
            name='admi',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('admi_link', models.CharField(max_length=255)),
                ('College_ID', models.ForeignKey(db_column='College_ID', default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clginfoapp.clgdetails')),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
