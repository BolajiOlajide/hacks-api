# Generated by Django 2.0.7 on 2018-07-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180729_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hack',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
