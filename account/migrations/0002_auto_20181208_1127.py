# Generated by Django 2.1.4 on 2018-12-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('things', models.CharField(max_length=128)),
                ('cost', models.IntegerField()),
                ('buy_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='houseaccount',
            name='administrator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User'),
        ),
        migrations.AddField(
            model_name='buy',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.HouseAccount'),
        ),
        migrations.AddField(
            model_name='buy',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User'),
        ),
        migrations.AddField(
            model_name='accessmanager',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.HouseAccount'),
        ),
        migrations.AddField(
            model_name='accessmanager',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User'),
        ),
    ]
