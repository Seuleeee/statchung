# Generated by Django 4.0.3 on 2022-04-15 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('create_datetime', models.DateTimeField(auto_created=True, null=True)),
                ('update_datetime', models.DateTimeField(null=True)),
                ('create_user', models.CharField(max_length=20, null=True)),
                ('update_user', models.CharField(max_length=20, null=True)),
                ('board_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=300)),
                ('likes', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'BOARD',
            },
        ),
        migrations.CreateModel(
            name='EditDashboard',
            fields=[
                ('dashboard_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'EDIT_DASHBOARD',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('create_datetime', models.DateTimeField(auto_created=True, null=True)),
                ('update_datetime', models.DateTimeField(null=True)),
                ('create_user', models.CharField(max_length=20, null=True)),
                ('update_user', models.CharField(max_length=20, null=True)),
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=512)),
                ('nickname', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'USER',
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('position', models.CharField(blank=True, max_length=2)),
                ('scores', models.IntegerField(blank=True)),
                ('rebounds', models.IntegerField(blank=True)),
                ('offensive_rebounds', models.IntegerField(blank=True)),
                ('assists', models.IntegerField(blank=True)),
                ('screen_assists', models.IntegerField(blank=True)),
                ('good_screens', models.IntegerField(blank=True)),
                ('blockshots', models.IntegerField(blank=True)),
                ('threepoints', models.IntegerField(blank=True)),
                ('hustle_plays', models.IntegerField(blank=True)),
                ('memo', models.TextField(blank=True, max_length=500)),
                ('board', models.ForeignKey(db_column='board_id', on_delete=django.db.models.deletion.CASCADE, related_name='board', to='stats.board')),
            ],
            options={
                'db_table': 'RECORDS',
            },
        ),
        migrations.CreateModel(
            name='EditDashboardOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('record_nm', models.CharField(max_length=10)),
                ('dashboard', models.ForeignKey(db_column='dashboard_id', on_delete=django.db.models.deletion.CASCADE, related_name='dashboard', to='stats.editdashboard')),
            ],
            options={
                'db_table': 'EDIT_DASHBOARD_ORDER',
            },
        ),
    ]
