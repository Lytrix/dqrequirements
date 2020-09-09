# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-09-03 20:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('criteria_id', models.AutoField(primary_key=True, serialize=False)),
                ('criteria_value', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CriteriaType',
            fields=[
                ('criteria_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('criteria_type_name', models.CharField(max_length=255, null=True)),
                ('criteria_description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataElement',
            fields=[
                ('data_element_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_element_name', models.CharField(max_length=255, null=True)),
                ('data_element_uri', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'data_element',
            },
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('dimension_id', models.AutoField(primary_key=True, serialize=False)),
                ('dimension_name', models.CharField(max_length=255, null=True)),
                ('dimension_description', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'dimension',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('product_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type_name', models.CharField(max_length=255, null=True)),
                ('product_description', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'product_type',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('Intakedate', models.DateField(default=datetime.datetime.now)),
                ('data_element', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_element', to='ibprojecten.DataElement')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='ibprojecten.Product')),
            ],
            options={
                'db_table': 'requirement',
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('scope_id', models.AutoField(primary_key=True, serialize=False)),
                ('scope_type', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScopeType',
            fields=[
                ('scope_id', models.AutoField(primary_key=True, serialize=False)),
                ('scope_name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubDimension',
            fields=[
                ('subdimension_id', models.AutoField(primary_key=True, serialize=False)),
                ('subdimension_scope', models.CharField(max_length=255, null=True)),
                ('subdimension_description', models.CharField(max_length=255, null=True)),
                ('subdimension_acceptance_criteria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acceptance_criteria', to='ibprojecten.Criteria')),
                ('subdimension_dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimension', to='ibprojecten.Dimension')),
            ],
            options={
                'db_table': 'subdimension',
            },
        ),
        migrations.CreateModel(
            name='SubDimensionType',
            fields=[
                ('subdimension_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('subdimension_type_name', models.CharField(max_length=255, null=True)),
                ('subdimension_type_description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='subdimension',
            name='subdimension_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subdimension_type', to='ibprojecten.SubDimensionType'),
        ),
        migrations.AddField(
            model_name='scope',
            name='scope_description',
            field=models.ManyToManyField(related_name='scope_type', to='ibprojecten.ScopeType'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_type', to='ibprojecten.ProductType'),
        ),
        migrations.AddField(
            model_name='criteria',
            name='criteria_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='criteria_type', to='ibprojecten.CriteriaType'),
        ),
    ]