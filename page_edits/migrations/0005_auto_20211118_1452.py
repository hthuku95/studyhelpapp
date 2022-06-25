# Generated by Django 3.0.4 on 2021-11-18 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_edits', '0004_howweworkchecklistitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privacypolicy',
            name='body',
        ),
        migrations.RemoveField(
            model_name='privacypolicy',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='privacypolicy',
            name='sub_heading',
        ),
        migrations.RemoveField(
            model_name='whatsappnumber',
            name='whatsapp',
        ),
        migrations.AddField(
            model_name='whatsappnumber',
            name='name',
            field=models.CharField(default='whatsapp', max_length=50),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='name',
            field=models.CharField(default='Privacy Policy', max_length=50),
        ),
    ]
