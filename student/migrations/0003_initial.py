# Generated by Django 4.2.6 on 2023-10-24 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0005_student_semester'),
        ('student', '0002_remove_installment_2nd_semesters_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='first_installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
            ],
        ),
    ]
