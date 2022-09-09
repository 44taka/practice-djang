# Generated by Django 4.1 on 2022-09-04 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=50, unique=True)),
                ('password', models.CharField(db_index=True, max_length=100)),
                ('info', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'user_info_tbl',
            },
        ),
    ]
