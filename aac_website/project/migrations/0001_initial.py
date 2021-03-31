# Generated by Django 3.1.4 on 2021-01-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('summary', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('team_members', models.TextField(blank=True, max_length=500, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='project')),
                ('source_code', models.URLField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('tags', models.ManyToManyField(to='project.Tags')),
            ],
        ),
    ]
