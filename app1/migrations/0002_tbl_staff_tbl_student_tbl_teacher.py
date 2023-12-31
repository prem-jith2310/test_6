# Generated by Django 4.2.2 on 2023-07-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_staff',
            },
        ),
        migrations.CreateModel(
            name='tbl_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('school', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_student',
            },
        ),
        migrations.CreateModel(
            name='tbl_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_teacher',
            },
        ),
    ]
