# Generated by Django 2.2.12 on 2020-05-31 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20200531_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationentry',
            old_name='toYear',
            new_name='toDateShown',
        ),
        migrations.RemoveField(
            model_name='educationentry',
            name='fromYear',
        ),
        migrations.RemoveField(
            model_name='workentry',
            name='fromYear',
        ),
        migrations.RemoveField(
            model_name='workentry',
            name='toYear',
        ),
        migrations.AddField(
            model_name='educationentry',
            name='fromDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='educationentry',
            name='fromDateShown',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationentry',
            name='toDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='workentry',
            name='fromDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='workentry',
            name='fromDateShown',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workentry',
            name='toDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='workentry',
            name='toDateShown',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
