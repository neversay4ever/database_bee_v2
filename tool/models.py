from django.db import models

# Create your models here.


class Tool(models.Model):
    tool_name = models.CharField(verbose_name=(
        "分析工具名称"), max_length=50, null=True, blank=True)
    tool_description = models.TextField(
        verbose_name=("分析工具描述"), null=True, blank=True)
    tool_parameter = models.CharField(verbose_name=(
        "分析工具参数"), max_length=100, null=True, blank=True)
    tool_notes = models.TextField(
        verbose_name='分析备注信息', null=True, blank=True)
    tool_pipeline_detail = models.ForeignKey('pipeline.Pipeline', verbose_name=(
        "分析工具相关流程"), on_delete=models.CASCADE, related_name='tool', null=True, blank=True)
    tool_pipeline_order = models.IntegerField(
        verbose_name=("分析工具在流程中的顺序"), null=True, blank=True)

    class Meta:
        verbose_name = '分析工具'
        verbose_name_plural = '分析工具'

    def __str__(self):
        return self.tool_name
