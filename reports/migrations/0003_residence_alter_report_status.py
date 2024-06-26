# Generated by Django 4.2.10 on 2024-03-30 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_document_report_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residence_type', models.CharField(max_length=200)),
                ('residence', models.CharField(max_length=200)),
                ('building', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='New', max_length=20),
        ),
    ]
