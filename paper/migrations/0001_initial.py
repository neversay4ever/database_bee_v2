# Generated by Django 2.2 on 2020-03-24 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pipeline', '0001_initial'),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='标题')),
                ('journal', models.CharField(blank=True, max_length=50, null=True, verbose_name='杂志')),
                ('authors', models.CharField(blank=True, max_length=100, null=True, verbose_name='作者')),
                ('abstract', models.TextField(blank=True, null=True, verbose_name='摘要')),
                ('fulltext_file_path', models.CharField(blank=True, max_length=100, null=True, verbose_name='全文文件地址')),
                ('paper_data_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper', to='data.Data', verbose_name='文章相关的数据')),
                ('paper_pipeline_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper', to='pipeline.Pipeline', verbose_name='文章相关的数据')),
            ],
            options={
                'verbose_name': '文章详情',
                'verbose_name_plural': '文章详情',
            },
        ),
    ]
