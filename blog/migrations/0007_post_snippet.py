# Generated by Django 3.1.7 on 2021-03-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210314_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click a link above to read post', max_length=255),
        ),
    ]
