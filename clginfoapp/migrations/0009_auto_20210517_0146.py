# Generated by Django 3.1.1 on 2021-05-16 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clginfoapp', '0008_auto_20210517_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='clg_link',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=255)),
                ('Name', models.ForeignKey(db_column='Name', default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clginfoapp.clgdetails', to_field='Name')),
            ],
            options={
                'db_table': 'College admissions',
            },
        ),
        migrations.DeleteModel(
            name='admiss',
        ),
    ]