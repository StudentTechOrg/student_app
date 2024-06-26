# Generated by Django 5.0.4 on 2024-04-19 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_students_city_students_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.students')),
            ],
        ),
    ]
