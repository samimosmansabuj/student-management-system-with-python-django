# Generated by Django 4.2.6 on 2023-10-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_student_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='tuition_fees_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
