from django.db import models

# Create your models here.


class Pipeline(models.Model):
    pipeline_name = models.CharField(
        verbose_name=("分析流程名称"), max_length=50, null=True, blank=True)
    pipeline_description = models.TextField(
        verbose_name=("分析流程描述"), null=True, blank=True)
    pipeline_data_detail = models.ForeignKey(
        'data.Data', verbose_name=("数据分析的原始数据来源"), related_name='pipeline', on_delete=models.CASCADE, null=True, blank=True)
    pipeline_run_datetime = models.DateTimeField(verbose_name=(
        "数据分析日期"), auto_now=False, auto_now_add=False, null=True, blank=True)
    pipeline_run_by_who = models.CharField(verbose_name=(
        "分析执行人"), max_length=50, null=True, blank=True)
    result_description = models.TextField(
        verbose_name=("数据分析结果描述"), null=True, blank=True)
    result_data_size = models.CharField(verbose_name=(
        "分析结果文件大小"), max_length=50, null=True, blank=True)
    result_file_server = models.CharField(verbose_name=(
        "分析结果存储服务器"), max_length=50, null=True, blank=True)
    result_file_path = models.CharField(verbose_name=(
        "分析结果存储路径"), max_length=50, null=True, blank=True)
    pipeline_notes = models.TextField(
        verbose_name=("分析流程备注"), null=True, blank=True)

    class Meta:
        verbose_name = '分析流程'
        verbose_name_plural = '分析流程'

    def __str__(self):
        return self.pipeline_name
