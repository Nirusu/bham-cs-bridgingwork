# Generated by Django 2.2.12 on 2020-05-31 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TimeField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('fromYear', models.CharField(max_length=50)),
                ('toYear', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('fromYear', models.CharField(max_length=50)),
                ('toYear', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
