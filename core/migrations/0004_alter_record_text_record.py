# Generated by Django 3.2.12 on 2022-04-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_record_text_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='text_record',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
