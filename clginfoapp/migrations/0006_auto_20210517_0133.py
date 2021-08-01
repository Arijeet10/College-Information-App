# Generated by Django 3.1.1 on 2021-05-16 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clginfoapp', '0005_auto_20210517_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admi',
            name='College_ID',
        ),
        migrations.AddField(
            model_name='admi',
            name='Name',
            field=models.ForeignKey(db_column='Name', default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clginfoapp.clgdetails', to_field='Name'),
        ),
        migrations.AlterField(
            model_name='clgdetails',
            name='Name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]