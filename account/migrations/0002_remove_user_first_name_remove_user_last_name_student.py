# Generated by Django 4.2.6 on 2023-10-19 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('teacher_id', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('date_of_birth', models.DateField(blank=True)),
                ('phone_number', models.TextField()),
                ('join_date', models.DateTimeField()),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=5)),
                ('address', models.TextField(blank=True)),
                ('religion', models.CharField(blank=True, choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Chirstian', 'Chirstian'), ('Buddist', 'Buddist'), ('Others', 'Others')], max_length=10)),
                ('teacher_image', models.ImageField(blank=True, upload_to='teacher/img/')),
                ('job_experience', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.user',),
        ),
    ]
