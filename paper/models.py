from django.db import models

# Create your models here.


class Paper (models.Model):
    title = models.CharField(verbose_name=(
        "标题"), max_length=50, null=True, blank=True)
    journal = models.CharField(verbose_name=(
        "杂志"), max_length=50, null=True, blank=True)
    authors = models.CharField(verbose_name=(
        "作者"), max_length=100, null=True, blank=True)
    abstract = models.TextField(verbose_name=("摘要"), null=True, blank=True)
    fulltext_file_path = models.CharField(
        verbose_name=("全文文件地址"), max_length=100, null=True, blank=True)
    paper_data_detail = models.ForeignKey('data.Data', verbose_name=(
        "文章相关的数据"), related_name='paper', on_delete=models.CASCADE, null=True, blank=True)
    paper_pipeline_detail = models.ForeignKey('pipeline.Pipeline', verbose_name=(
        "文章相关的数据"), related_name='paper', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '文章详情'
        verbose_name_plural = '文章详情'

    def __str__(self):
        return self.title
