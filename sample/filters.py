from .models import Sample
from django_filters import FilterSet
from django_filters import filters
from django.db.models import Count

samples = Sample.objects.all()


def make_choice(column_name):
    column_list = [i[column_name] for i in samples.values(
        column_name).annotate(Count('id'))if i[column_name] is not None]
    column_choice = ((x, x) for x in column_list)
    return list(column_choice)


class SampleFilter(FilterSet):
    gut_usage = filters.ChoiceFilter(
        choices=make_choice('gut_usage'))
    sample_phylum = filters.ChoiceFilter(choices=make_choice('sample_phylum'))
    sample_class = filters.ChoiceFilter(
        choices=make_choice('sample_class'))
    sample_order = filters.ChoiceFilter(choices=make_choice('sample_order'))
    sample_family = filters.ChoiceFilter(
        choices=make_choice('sample_family'))
    sample_genus = filters.ChoiceFilter(choices=make_choice('sample_genus'))
    sample_species = filters.ChoiceFilter(
        choices=make_choice('sample_species'))
    sample_subspecies = filters.ChoiceFilter(
        choices=make_choice('sample_subspecies'))
    sample_breed = filters.ChoiceFilter(
        choices=make_choice('sample_breed'))
    identifier_name = filters.ChoiceFilter(
        choices=make_choice('identifier_name'))

    exact_site = filters.ChoiceFilter(choices=make_choice('exact_site'))
    continent_ocean = filters.ChoiceFilter(
        choices=make_choice('continent_ocean'))
    country = filters.ChoiceFilter(choices=make_choice('country'))
    state_province = filters.ChoiceFilter(
        choices=make_choice('state_province'))
    city = filters.ChoiceFilter(
        choices=make_choice('city'))
    county = filters.ChoiceFilter(
        choices=make_choice('county'))
    latitude = filters.ChoiceFilter(
        choices=make_choice('latitude'))
    longitude = filters.ChoiceFilter(
        choices=make_choice('longitude'))
    elevation = filters.ChoiceFilter(
        choices=make_choice('elevation'))
    collector_name = filters.ChoiceFilter(
        choices=make_choice('collector_name'))

    class Meta:
        model = Sample
        fields = '__all__'


# def departments(request):
#     if request is None:
#         return Department.objects.none()

#     company = request.user.company
#     return company.department_set.all()


# class EmployeeFilter(filters.FilterSet):
#     department = filters.ModelChoiceFilter(queryset=departments)

    # dissection_state = models.CharField(verbose_name=(
    #     "解剖前状态"), max_length=20, choices=DISSECT_CHOICES, null=True, blank=True)
    # multi_or_not = models.BooleanField(verbose_name=("是否多只同管"), default=False)
    # multi_num = models.IntegerField(
    #     verbose_name=("同管样本数量"), null=True, blank=True)
    # sample_box_id = models.CharField(verbose_name=(
    #     "蜜蜂样本盒子ID"), max_length=50, null=True, blank=True)
    # headchest_id = models.CharField(verbose_name=(
    #     "头胸部ID"), max_length=50, null=True, blank=True)
    # headchest_store = models.CharField(verbose_name=(
    #     "头胸部存储"), max_length=20, choices=HEADCHEST_STORE_CHOICES, null=True, blank=True)
    # headchest_usage = models.CharField(
    #     verbose_name=("头胸部使用情况"), max_length=50, null=True, blank=True)
    # abdomen_id = models.CharField(verbose_name=(
    #     "腹部ID"), max_length=50, null=True, blank=True)
    # abdomen_store = models.CharField(verbose_name=(
    #     "腹部存储"), max_length=20, choices=ABDOMEN_STORE_CHOICES,  null=True, blank=True)
    # abdomen_usage = models.CharField(
    #     verbose_name=("腹部使用情况"), max_length=50, null=True, blank=True)
    # gut_id = models.CharField(verbose_name=(
    #     "肠道ID"), max_length=50, null=True, blank=True)
    # gut_store = models.CharField(verbose_name=(
    #     "肠道存储"), max_length=20, choices=GUT_STORE_CHOICES, null=True, blank=True)
    # gut_usage = models.CharField(
    #     verbose_name=("肠道使用情况"), max_length=50, null=True, blank=True)
    # leg_id = models.CharField(verbose_name=(
    #     "腿部ID"), max_length=50, null=True, blank=True)
    # leg_store = models.CharField(verbose_name=(
    #     "腿部存储"), max_length=20, choices=LEG_STORE_CHOICES, null=True, blank=True)
    # leg_usage = models.CharField(verbose_name=(
    #     "腿部使用情况"), max_length=50, null=True, blank=True)
    # sample_phylum = models.CharField(verbose_name=(
    #     "门"), max_length=50, null=True, blank=True)
    # sample_class = models.CharField(verbose_name=(
    #     "纲"), max_length=50, null=True, blank=True)
    # sample_order = models.CharField(verbose_name=(
    #     "目"), max_length=50, null=True, blank=True)
    # sample_family = models.CharField(verbose_name=(
    #     "科"), max_length=50, null=True, blank=True)
    # sample_genus = models.CharField(verbose_name=(
    #     "属"), max_length=50, null=True, blank=True)
    # sample_species = models.CharField(verbose_name=(
    #     "种"), max_length=50, null=True, blank=True)
    # sample_subspecies = models.CharField(verbose_name=(
    #     "亚种"), max_length=50, null=True, blank=True)
    # sample_breed = models.CharField(verbose_name=(
    #     "品种"), max_length=50, null=True, blank=True)
    # identifier_name = models.CharField(verbose_name=(
    #     "鉴定人姓名"), max_length=50, null=True, blank=True)
    # identifier_email = models.EmailField(verbose_name=(
    #     "鉴定人邮箱"), max_length=254, null=True, blank=True)
    # identifier_institution = models.CharField(
    #     verbose_name=("鉴定人工作单位"), max_length=254, null=True, blank=True)
    # barcode_result = models.CharField(verbose_name=(
    #     "barcode信息"), max_length=254, null=True, blank=True)
    # exact_site = models.CharField(verbose_name=(
    #     "确切地址"), max_length=100, null=True, blank=True)
    # continent_ocean = models.CharField(verbose_name=(
    #     "大陆/大洋"), max_length=20, null=True, blank=True)
    # country = models.CharField(verbose_name=(
    #     "国家"), max_length=20, null=True, blank=True)
    # state_province = models.CharField(verbose_name=(
    #     "州/省"), max_length=50, null=True, blank=True)
    # city = models.CharField(verbose_name=(
    #     "城市"), max_length=20, null=True, blank=True)
    # county = models.CharField(verbose_name=(
    #     "县"), max_length=20, null=True, blank=True)
    # latitude = models.FloatField(verbose_name=("纬度"), null=True, blank=True)
    # longitude = models.FloatField(verbose_name=("经度"), null=True, blank=True)
    # elevation = models.IntegerField(verbose_name=("海拔"), null=True, blank=True)
    # geo_notes = models.TextField(
    #     verbose_name=("地理位置补充描述"), null=True, blank=True)
    # collector_name = models.CharField(verbose_name=(
    #     "采集人姓名"), max_length=50, null=True, blank=True)
    # collection_date = models.DateField(verbose_name=(
    #     "采集日期"), auto_now=False, auto_now_add=False, null=True, blank=True)
    # bee_type = models.CharField(
    #     verbose_name=("蜜蜂类型"), max_length=20, choices=BEE_TYPE_CHOICES, null=True, blank=True)
    # life_style = models.CharField(
    #     verbose_name=("饲养方式"), max_length=20, choices=LIFE_STYLE_CHOICES, null=True, blank=True)
    # life_stage = models.CharField(
    #     verbose_name=("个体阶段"), max_length=20, choices=LIFE_STAGE_CHOICES, null=True, blank=True)
    # beekeeper = models.CharField(verbose_name=(
    #     "养蜂人信息"), max_length=50, null=True, blank=True)
    # apiary_id = models.IntegerField(
    #     verbose_name=("蜂场号-整数ID"), null=True, blank=True)
    # hive_id = models.IntegerField(
    #     verbose_name=("蜂箱号-整数ID"), null=True, blank=True)
    # host_origin = models.CharField(verbose_name=(
    #     "蜜蜂来源"), max_length=50, null=True, blank=True)
    # hive_year = models.IntegerField(
    #     verbose_name=("蜂箱年数"), null=True, blank=True)
    # decapping_freq = models.CharField(verbose_name=(
    #     "取蜜频率"), max_length=50, null=True, blank=True)
    # feeding_or_not = models.BooleanField(
    #     verbose_name=("是否喂糖水"), null=True, blank=True)
    # feeding_description = models.TextField(
    #     verbose_name=("喂糖水描述"), null=True, blank=True)
    # habitat_type = models.CharField(verbose_name=(
    #     "生境信息"), max_length=50, null=True, blank=True)
    # habitat_photo_filename = models.CharField(verbose_name=(
    #     "生境照片文件名"), max_length=50, null=True, blank=True)
    # presticide_or_not = models.BooleanField(
    #     verbose_name=("有无农药"), null=True, blank=True)
    # flower_species = models.CharField(verbose_name=(
    #     "访花种类"), max_length=50, null=True, blank=True)
    # flower_photo_filename = models.CharField(verbose_name=(
    #     "访华照片文件名"), max_length=50, null=True, blank=True)
    # sample_notes = models.TextField(
    #     verbose_name=("样本备注信息"), null=True, blank=True)
    # record_by_who = models.CharField(verbose_name=(
    #     "记录添加人"), max_length=50, null=True, blank=True)
