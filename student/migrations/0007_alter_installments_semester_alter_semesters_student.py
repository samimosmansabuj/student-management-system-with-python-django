# Generated by Django 4.2.6 on 2023-10-24 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_student_admision_id'),
        ('student', '0006_alter_installments_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installments',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester', to='student.semesters'),
        ),
        migrations.AlterField(
            model_name='semesters',
            name='Student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Students', to='account.student'),
        ),
    ]