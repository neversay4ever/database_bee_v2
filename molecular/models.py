from django.db import models

# Create your models here.


class Molecular(models.Model):
    TYPE_CHOICES = [
        ('DNA', 'DNA'),
        ('RNA', 'RNA'),
        ('蛋白质', '蛋白质'),
        ('其它', '其它'),
    ]
    TISSUE_CHOICES = [
        #headchest, abdomen, gut, leg
        ('头胸部', '头胸部'),
        ('腹部', '腹部'),
        ('肠道', '肠道'),
        ('腿部', '腿部')
    ]
    project_name = models.CharField(verbose_name=(
        "项目名称"), max_length=50, null=True, blank=True)
    project_manager = models.CharField(verbose_name=(
        "项目负责人"), max_length=50, null=True, blank=True)
    molecular_type = models.CharField(
        verbose_name=("分子类型"), max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    molecular_volume = models.CharField(verbose_name=(
        "分子的体积"), max_length=50, null=True, blank=True)
    molecular_concentration = models.CharField(verbose_name=(
        "分子的浓度"), max_length=50, null=True, blank=True)
    molecular_store = models.CharField(verbose_name=(
        "分子的存储方法"), max_length=50, null=True, blank=True)
    molecular_box_id = models.CharField(verbose_name=(
        "分子的盒子ID"), max_length=50, null=True, blank=True)
    molecular_sample_detail = models.ForeignKey(
        'sample.Sample', verbose_name=("分子的样本来源"), related_name='molecular', on_delete=models.CASCADE, null=True, blank=True)
    molecular_strain_detail = models.ForeignKey(
        'strain.Strain', verbose_name=("分子的菌株来源"), related_name='molecular', on_delete=models.CASCADE, null=True, blank=True)
    return_or_not = models.BooleanField(
        verbose_name=("是否返样"), null=True, blank=True)
    return_volumn = models.CharField(verbose_name=(
        "返回的体积"), max_length=50, null=True, blank=True)
    return_concentration = models.CharField(verbose_name=(
        "返回的浓度"), max_length=50, null=True, blank=True)
    return_notes = models.TextField(
        verbose_name='返样备注信息', null=True, blank=True)
    record_by_who = models.CharField(verbose_name=(
        "记录添加人"), max_length=50, null=True, blank=True)
    record_datetime = models.DateTimeField(verbose_name=(
        "记录添加时间"), auto_now_add=True)

    class Meat:
        verbose_name = '分子样本总表'
        verbose_name_plural = '分子样本总表'

    def __str__(self):
        return self.molecular_type
