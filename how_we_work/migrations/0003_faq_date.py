# Generated by Django 4.0.3 on 2022-04-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('how_we_work', '0002_alter_faq_id_alter_howwework_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
