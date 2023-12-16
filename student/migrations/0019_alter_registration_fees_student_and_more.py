# Generated by Django 4.2.6 on 2023-11-05 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_student_admision_id'),
        ('student', '0018_alter_registration_fees_pay_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_fees',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Student', to='account.student'),
        ),
        migrations.AlterField(
            model_name='registration_fees',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='semester', to='student.semesters'),
        ),
    ]
