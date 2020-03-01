from django.db import models

# Create your models here.

# Strain info


class Strain(models.Model):
    PART_OF_GUT_CHOICES = [
        # "frozen_gut+glycerol"、“midgut”、“hindgut”、"ileum"、“rectum”
        ('frozen_gut+glycerol', 'frozen_gut+glycerol'),
        ('midgut', 'midgut'),
        ('hindgut', 'hindgut'),
        ('ileum', 'ileum'),
        ('rectum', 'rectum')
    ]
    isolation_id = models.CharField(verbose_name=(
        "分离菌ID"), max_length=50, null=True, blank=True)
    strain_sample_detail = models.ForeignKey('sample.Sample', verbose_name=(
        "菌株样本来源"), on_delete=models.CASCADE, related_name='strain', null=True, blank=True)
    strain_id = models.CharField(verbose_name=(
        "菌株甘油管ID"), max_length=50, null=True, blank=True)
    strain_box_id = models.CharField(verbose_name=(
        "菌株的盒子ID"), max_length=50, null=True, blank=True)
    strain_usage = models.CharField(verbose_name=(
        "菌株使用情况"), max_length=50, null=True, blank=True)
    strain_store = models.CharField(verbose_name=(
        "菌株保存方式"), max_length=50, null=True, blank=True)
    stock_microbe = models.CharField(verbose_name=(
        "收菌液体"), max_length=50, null=True, blank=True)
    stock_date = models.DateField(verbose_name=(
        "收菌日期"), auto_now=False, auto_now_add=False, null=True, blank=True)
    part_of_gut = models.CharField(verbose_name=(
        "肠道部位"), max_length=50, choices=PART_OF_GUT_CHOICES, null=True, blank=True)
    isolation_media = models.CharField(verbose_name=(
        "培养基类型"), max_length=50, null=True, blank=True)
    culture_type = models.CharField(verbose_name=(
        "培养条件"), max_length=50, null=True, blank=True)
    culture_temperature = models.CharField(verbose_name=(
        "培养温度"), max_length=10, null=True, blank=True)
    culture_time = models.CharField(verbose_name=(
        "培养时间/h"), max_length=10, null=True, blank=True)
    isolate_by_who = models.CharField(verbose_name=(
        "分离者姓名"), max_length=50, null=True, blank=True)
    strain_phylum = models.CharField(verbose_name=(
        "门"), max_length=50, null=True, blank=True)
    strain_class = models.CharField(verbose_name=(
        "纲"), max_length=50, null=True, blank=True)
    strain_order = models.CharField(verbose_name=(
        "目"), max_length=50, null=True, blank=True)
    strain_family = models.CharField(verbose_name=(
        "科"), max_length=50, null=True, blank=True)
    strain_genus = models.CharField(verbose_name=(
        "属"), max_length=50, null=True, blank=True)
    strain_tophit = models.CharField(verbose_name=(
        "比对上菌种"), max_length=200, null=True, blank=True)
    similarity_16s = models.IntegerField(
        verbose_name=("16s相似度-整数%"), null=True, blank=True)
    blast_website = models.CharField(verbose_name=(
        "比对网站"), max_length=100, null=True, blank=True)
    ab1_quality = models.CharField(verbose_name=(
        "测序质量"), max_length=5, null=True, blank=True)
    blast_by_who = models.CharField(verbose_name=(
        "比对人"), max_length=20, null=True, blank=True)
    data_16s_filename = models.CharField(verbose_name=(
        "测序文件名(seq & ab1)"), max_length=100, null=True, blank=True)
    isolation_notes = models.TextField(
        verbose_name=("分离菌备注信息"), null=True, blank=True)
    record_by_who = models.CharField(verbose_name=(
        "记录添加人"), max_length=50, null=True, blank=True)
    record_datetime = models.DateTimeField(verbose_name=(
        "记录添加时间"), auto_now_add=True)

    class Meta:
        verbose_name = '菌株信息总表'
        verbose_name_plural = '菌株信息总表'

    def __str__(self):
        if self.isolation_id == None:
            return 'nothing'
        return self.isolation_id
