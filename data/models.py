from django.db import models

# Create your models here.


class Data(models.Model):
    PRODUCTION_CHOICES = [
        ('测序', '测序'),
        ('质谱', '质谱')
    ]
    project_name = models.CharField(verbose_name=(
        "项目名称"), max_length=50, null=True, blank=True)
    porject_manager = models.CharField(verbose_name=(
        "项目负责人"), max_length=50, null=True, blank=True)
    data_production_type = models.CharField(verbose_name=(
        "数据生产类型"), max_length=50, choices=PRODUCTION_CHOICES, null=True, blank=True)
    data_production_platform = models.CharField(verbose_name=(
        "数据生产平台"), max_length=50, null=True, blank=True)
    data_production_datetime = models.DateTimeField(verbose_name=(
        "数据生产时间"), auto_now=False, auto_now_add=False, null=True, blank=True)
    data_production_notes = models.TextField(
        verbose_name=("数据生产备注"), null=True, blank=True)
    data_type = models.CharField(verbose_name=(
        "原始数据类型"), max_length=50, null=True, blank=True)
    data_size = models.CharField(verbose_name=(
        "原始数据大小"), max_length=50, null=True, blank=True)
    md5_info = models.CharField(verbose_name=(
        "原始数据md5"), max_length=100, null=True, blank=True)
    file_server = models.CharField(verbose_name=(
        "数据存储服务器"), max_length=50, null=True, blank=True)
    file_path = models.CharField(verbose_name=(
        "数据存储路径"), max_length=50, null=True, blank=True)
    data_molecular_detail = models.ForeignKey(
        'molecular.Molecular', verbose_name=("分子的菌株来源"), related_name='data', on_delete=models.CASCADE, null=True, blank=True)
    record_by_who = models.CharField(verbose_name=(
        "记录添加人"), max_length=50, null=True, blank=True)
    record_datetime = models.DateTimeField(verbose_name=(
        "记录添加时间"), auto_now_add=True)

    class Meat:
        verbose_name = '原始数据'
        verbose_name_plural = '原始数据'

    def __str__(self):
        return self.data_type
