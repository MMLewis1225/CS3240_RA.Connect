# Generated by Django 4.2.10 on 2024-04-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_residence'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='report',
            name='building',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='floor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='room',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]