# Generated by Django 3.2.9 on 2021-11-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_rename_sevice_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_event', models.CharField(max_length=50)),
                ('tutor', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Experts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('experience', models.IntegerField()),
                ('activity_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_news', models.CharField(max_length=50)),
                ('definition', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_seminar', models.CharField(max_length=50)),
                ('tutor', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_tip', models.CharField(max_length=50)),
                ('author_of_tip', models.CharField(max_length=50)),
                ('definition', models.TextField()),
            ],
        ),
    ]
