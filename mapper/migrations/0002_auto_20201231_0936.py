# Generated by Django 3.1.3 on 2020-12-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='Reference_parent',
            new_name='Reference',
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='Reference_student',
            new_name='section',
        ),
        migrations.AddField(
            model_name='visitor',
            name='aadhar',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='visitor',
            name='otherIdentity',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
