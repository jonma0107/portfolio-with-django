# Generated by Django 4.2.7 on 2023-12-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_alter_posttranslation_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttranslation',
            name='title',
            field=models.CharField(max_length=150, null=True, verbose_name='titulo'),
        ),
    ]