# Generated by Django 4.2.6 on 2023-10-21 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installment_2nd',
            name='semesters',
        ),
        migrations.RemoveField(
            model_name='installment_3rd',
            name='semesters',
        ),
        migrations.RemoveField(
            model_name='installment_4th',
            name='semesters',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='students',
        ),
        migrations.DeleteModel(
            name='installment_1st',
        ),
        migrations.DeleteModel(
            name='installment_2nd',
        ),
        migrations.DeleteModel(
            name='installment_3rd',
        ),
        migrations.DeleteModel(
            name='installment_4th',
        ),
        migrations.DeleteModel(
            name='semester',
        ),
    ]