# Generated by Django 4.0.4 on 2022-05-07 09:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_exam_details_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_details',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
