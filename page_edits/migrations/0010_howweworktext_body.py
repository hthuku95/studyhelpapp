# Generated by Django 3.0.4 on 2022-02-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_edits', '0009_auto_20220210_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='howweworktext',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
