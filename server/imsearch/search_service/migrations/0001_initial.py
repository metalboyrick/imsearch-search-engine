# Generated by Django 3.2.2 on 2021-05-14 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('image_path', models.CharField(max_length=155, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('label_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('label_name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('rel_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('rel_name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='ImageRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_id_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='label_id_1', to='search_service.label')),
                ('label_id_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='label_id_2', to='search_service.label')),
                ('rel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_service.relationship')),
            ],
        ),
        migrations.CreateModel(
            name='ImageLabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_service.image')),
                ('label_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_service.label')),
            ],
        ),
    ]
