# Generated by Django 4.0.4 on 2022-05-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_exam_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_given',
            name='correct',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam_given',
            name='incorrect',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
