# Generated by Django 4.0.3 on 2022-04-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='hustle_plays',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stats',
            name='memo',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='assists',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='blockshots',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='good_screens',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='offensive_rebounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='rebounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='scores',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='screen_assists',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='threepoints',
            field=models.IntegerField(null=True),
        ),
    ]
