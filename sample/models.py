from django.db import models

# Create your models here.

# Sample Info


class Sample(models.Model):
    DISSECT_CHOICES = [
        ('活', '活'),
        ('死', '死'),
        ('未知', '未知')
    ]
    HEADCHEST_STORE_CHOICES = [
        # “直接冻存“、”95%酒精“、”RNAlater “、”shiled “、”未保存“、”针插标本“
        ('未保存', '未保存'),
        ('直接冻存', '直接冻存'),
        ('95%酒精', '95%酒精'),
        ('甘油', '甘油'),
        ('RNAlater', 'RNAlater'),
        ('针插标本', '针插标本')
    ]
    ABDOMEN_STORE_CHOICES = [
        # “直接冻存“、”95%酒精“、”RNAlater “、”shiled “、”未保存“
        ('未保存', '未保存'),
        ('直接冻存', '直接冻存'),
        ('95%酒精', '95%酒精'),
        ('RNAlater', 'RNAlater'),
        ('shiled', 'shiled')
    ]
    GUT_STORE_CHOICES = [
        # “直接冻存“、”95%酒精“、”RNAlater “、”shiled “、”未保存“、”25%甘油“
        ('未保存', '未保存'),
        ('直接冻存', '直接冻存'),
        ('95%酒精', '95%酒精'),
        ('RNAlater', 'RNAlater'),
        ('shiled', 'shiled'),
        ('25%甘油', '25%甘油'),
    ]
    LEG_STORE_CHOICES = [
        # “直接冻存“、”95%酒精“、”RNAlater “、”shiled “、”未保存“、”25%甘油“
        ('未保存', '未保存'),
        ('直接冻存', '直接冻存'),
        ('95%酒精', '95%酒精'),
        ('RNAlater', 'RNAlater'),
        ('shiled', 'shiled'),
        ('25%甘油', '25%甘油'),
    ]
    BEE_TYPE_CHOICES = [
        # 限定输入内容：“drone”、“worker”、“queen”、“male”、“female”、“unknown”
        # 注释：“drone”仅仅适用于社会性蜜蜂中的雄性；“worker”仅适用于社会性蜜蜂中的工蜂；“female”适用于非社会性蜜蜂中的雌性个体；“male”适用于非社会蜜蜂中的雄性个体；“forager”适用于社会性分工蜜蜂中的外出采集蜂；“nurse bee”适用于社会性分工蜜蜂中的内勤蜂；“queen”适用于社会性蜜蜂中的蜂王。
        ('drone', 'drone'),
        ('worker', 'worker'),
        ('queen', 'queen'),
        ('male', 'male'),
        ('female', 'female'),
        ('unknown', 'unknown')
    ]
    LIFE_STYLE_CHOICES = [
        # “活框”、“木桶”、“wild”、“unknown”
        ('活框', '活框'),
        ('木桶', '木桶'),
        ('wild', 'wild'),
        ('unknown', 'unknown')
    ]
    LIFE_STAGE_CHOICES = [
        # 限定输入内容："adult"、"larva"、“pupo”；注释：“larva”适用于蜜蜂幼虫期，不同龄期可在备注列加以说明；“pupo”使用与不同发育蛹期，具体阶段按照蜜蜂发育时期分为白眼期、粉眼期、红眼期、黑眼期，具体信息填写在备注列。
        ('adult', 'adult'),
        ('larva', 'larva'),
        ('pupo', 'pupo')
    ]
    sample_id = models.CharField(verbose_name=(
        "样本ID"), max_length=50, null=True, blank=True)
    dissection_state = models.CharField(verbose_name=(
        "解剖前状态"), max_length=20, choices=DISSECT_CHOICES, null=True, blank=True)
    multi_or_not = models.BooleanField(verbose_name=("是否多只同管"), default=False)
    multi_num = models.IntegerField(
        verbose_name=("同管样本数量"), null=True, blank=True)
    sample_box_id = models.CharField(verbose_name=(
        "蜜蜂样本盒子ID"), max_length=50, null=True, blank=True)
    headchest_id = models.CharField(verbose_name=(
        "头胸部ID"), max_length=50, null=True, blank=True)
    headchest_store = models.CharField(verbose_name=(
        "头胸部存储"), max_length=20, choices=HEADCHEST_STORE_CHOICES, null=True, blank=True)
    headchest_usage = models.CharField(
        verbose_name=("头胸部使用情况"), max_length=50, null=True, blank=True)
    abdomen_id = models.CharField(verbose_name=(
        "腹部ID"), max_length=50, null=True, blank=True)
    abdomen_store = models.CharField(verbose_name=(
        "腹部存储"), max_length=20, choices=ABDOMEN_STORE_CHOICES,  null=True, blank=True)
    abdomen_usage = models.CharField(
        verbose_name=("腹部使用情况"), max_length=50, null=True, blank=True)
    gut_id = models.CharField(verbose_name=(
        "肠道ID"), max_length=50, null=True, blank=True)
    gut_store = models.CharField(verbose_name=(
        "肠道存储"), max_length=20, choices=GUT_STORE_CHOICES, null=True, blank=True)
    gut_usage = models.CharField(
        verbose_name=("肠道使用情况"), max_length=50, null=True, blank=True)
    leg_id = models.CharField(verbose_name=(
        "腿部ID"), max_length=50, null=True, blank=True)
    leg_store = models.CharField(verbose_name=(
        "腿部存储"), max_length=20, choices=LEG_STORE_CHOICES, null=True, blank=True)
    leg_usage = models.CharField(verbose_name=(
        "腿部使用情况"), max_length=50, null=True, blank=True)
    sample_phylum = models.CharField(verbose_name=(
        "门"), max_length=50, null=True, blank=True)
    sample_class = models.CharField(verbose_name=(
        "纲"), max_length=50, null=True, blank=True)
    sample_order = models.CharField(verbose_name=(
        "目"), max_length=50, null=True, blank=True)
    sample_family = models.CharField(verbose_name=(
        "科"), max_length=50, null=True, blank=True)
    sample_genus = models.CharField(verbose_name=(
        "属"), max_length=50, null=True, blank=True)
    sample_species = models.CharField(verbose_name=(
        "种"), max_length=50, null=True, blank=True)
    sample_subspecies = models.CharField(verbose_name=(
        "亚种"), max_length=50, null=True, blank=True)
    sample_breed = models.CharField(verbose_name=(
        "品种"), max_length=50, null=True, blank=True)
    identifier_name = models.CharField(verbose_name=(
        "鉴定人姓名"), max_length=50, null=True, blank=True)
    identifier_email = models.EmailField(verbose_name=(
        "鉴定人邮箱"), max_length=254, null=True, blank=True)
    identifier_institution = models.CharField(
        verbose_name=("鉴定人工作单位"), max_length=254, null=True, blank=True)
    barcode_result = models.CharField(verbose_name=(
        "barcode信息"), max_length=254, null=True, blank=True)
    exact_site = models.CharField(verbose_name=(
        "确切地址"), max_length=100, null=True, blank=True)
    continent_ocean = models.CharField(verbose_name=(
        "大陆/大洋"), max_length=20, null=True, blank=True)
    country = models.CharField(verbose_name=(
        "国家"), max_length=20, null=True, blank=True)
    state_province = models.CharField(verbose_name=(
        "州/省"), max_length=50, null=True, blank=True)
    city = models.CharField(verbose_name=(
        "城市"), max_length=20, null=True, blank=True)
    county = models.CharField(verbose_name=(
        "县"), max_length=20, null=True, blank=True)
    latitude = models.FloatField(verbose_name=("纬度"), null=True, blank=True)
    longitude = models.FloatField(verbose_name=("经度"), null=True, blank=True)
    elevation = models.IntegerField(verbose_name=("海拔"), null=True, blank=True)
    geo_notes = models.TextField(
        verbose_name=("地理位置补充描述"), null=True, blank=True)
    collector_name = models.CharField(verbose_name=(
        "采集人姓名"), max_length=50, null=True, blank=True)
    collection_date = models.DateField(verbose_name=(
        "采集日期"), auto_now=False, auto_now_add=False, null=True, blank=True)
    bee_type = models.CharField(
        verbose_name=("蜜蜂类型"), max_length=20, choices=BEE_TYPE_CHOICES, null=True, blank=True)
    life_style = models.CharField(
        verbose_name=("饲养方式"), max_length=20, choices=LIFE_STYLE_CHOICES, null=True, blank=True)
    life_stage = models.CharField(
        verbose_name=("个体阶段"), max_length=20, choices=LIFE_STAGE_CHOICES, null=True, blank=True)
    beekeeper = models.CharField(verbose_name=(
        "养蜂人信息"), max_length=50, null=True, blank=True)
    apiary_id = models.IntegerField(
        verbose_name=("蜂场号-整数ID"), null=True, blank=True)
    hive_id = models.IntegerField(
        verbose_name=("蜂箱号-整数ID"), null=True, blank=True)
    host_origin = models.CharField(verbose_name=(
        "蜜蜂来源"), max_length=50, null=True, blank=True)
    hive_year = models.IntegerField(
        verbose_name=("蜂箱年数"), null=True, blank=True)
    decapping_freq = models.CharField(verbose_name=(
        "取蜜频率"), max_length=50, null=True, blank=True)
    feeding_or_not = models.BooleanField(
        verbose_name=("是否喂糖水"), null=True, blank=True)
    feeding_description = models.TextField(
        verbose_name=("喂糖水描述"), null=True, blank=True)
    habitat_type = models.CharField(verbose_name=(
        "生境信息"), max_length=50, null=True, blank=True)
    habitat_photo_filename = models.CharField(verbose_name=(
        "生境照片文件名"), max_length=50, null=True, blank=True)
    presticide_or_not = models.BooleanField(
        verbose_name=("有无农药"), null=True, blank=True)
    flower_species = models.CharField(verbose_name=(
        "访花种类"), max_length=50, null=True, blank=True)
    flower_photo_filename = models.CharField(verbose_name=(
        "访华照片文件名"), max_length=50, null=True, blank=True)
    sample_notes = models.TextField(
        verbose_name=("样本备注信息"), null=True, blank=True)
    record_by_who = models.CharField(verbose_name=(
        "记录添加人"), max_length=50, null=True, blank=True)
    record_datetime = models.DateTimeField(verbose_name=(
        "记录添加时间"), auto_now_add=True)

    class Meta:
        verbose_name = '蜜蜂样本总表'
        verbose_name_plural = '蜜蜂样本总表'

    def __str__(self):
        return self.sample_id


class SampleSummary(Sample):
    class Meta:
        proxy = True
        verbose_name = '蜜蜂样本统计'
        verbose_name_plural = '蜜蜂样本统计'
