# Generated by Django 4.0.4 on 2022-04-19 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
