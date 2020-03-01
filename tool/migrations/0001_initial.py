# Generated by Django 2.2.9 on 2020-02-23 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pipeline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='分析工具名称')),
                ('tool_description', models.TextField(blank=True, null=True, verbose_name='分析工具描述')),
                ('tool_parameter', models.CharField(blank=True, max_length=100, null=True, verbose_name='分析工具参数')),
                ('tool_notes', models.TextField(blank=True, null=True, verbose_name='分析备注信息')),
                ('tool_pipeline_order', models.IntegerField(blank=True, null=True, verbose_name='分析工具在流程中的顺序')),
                ('tool_pipeline_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tool', to='pipeline.Pipeline', verbose_name='分析工具相关流程')),
            ],
            options={
                'verbose_name': '分析工具',
                'verbose_name_plural': '分析工具',
            },
        ),
    ]
