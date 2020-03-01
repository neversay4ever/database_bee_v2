from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from djangoql.admin import DjangoQLSearchMixin
from django.core import serializers

# Register your models here.
from .models import Sample, SampleSummary
from django.db.models import Count


class CustomModelAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.fields if field.name != "id"]
        self.search_fields = [
            field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


@admin.register(Sample)
class SampleAdmin(CustomModelAdmin):
    list_filter = ['identifier_name', 'collector_name', 'gut_store', 'gut_usage', 'multi_or_not',
                   'dissection_state', 'bee_type', 'life_style',
                   'feeding_or_not', 'presticide_or_not', 'continent_ocean', 'country', 'state_province', 'sample_class',
                   'sample_order', 'sample_family', 'sample_genus', 'sample_species', 'sample_subspecies', 'sample_breed']
    date_hierarchy = 'collection_date'

    def save_model(self, request, obj, form, change):
        obj.record_by_who = request.user
        super().save_model(request, obj, form, change)


@admin.register(SampleSummary)
class SampleSummaryAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    change_list_template = 'admin/sample_summary_change_list.html'
    list_filter = ['identifier_name', 'collector_name', 'gut_store', 'gut_usage', 'multi_or_not',
                   'dissection_state', 'bee_type', 'life_style',
                   'feeding_or_not', 'presticide_or_not', 'continent_ocean', 'country', 'state_province', 'sample_class',
                   'sample_order', 'sample_family', 'sample_genus', 'sample_species', 'sample_subspecies', 'sample_breed']
    date_hierarchy = 'collection_date'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'country_total': Count('country'),
            'province_total': Count('state_province'),
            'city_total': Count('city'),
            'county_total': Count('county'),

        }
        country_num = qs.exclude(country=None).values('country').annotate(
            total=Count('country')).order_by('-total')
        response.context_data['country_name'] = [
            i['country'] for i in country_num]
        response.context_data['country_count'] = [
            i['total'] for i in country_num]
        response.context_data['country_total'] = qs.exclude(country=None)

        province_num = qs.exclude(state_province=None).values('state_province').annotate(
            total=Count('state_province')).order_by('-total')
        response.context_data['province_name'] = [
            i['state_province'] for i in province_num]
        response.context_data['province_count'] = [
            i['total'] for i in province_num]
        response.context_data['province_total'] = qs.exclude(
            state_province=None)

        city_num = qs.exclude(city=None).values('city').annotate(
            total=Count('city')).order_by('-total')
        response.context_data['city_name'] = [
            i['city'] for i in city_num]
        response.context_data['city_count'] = [
            i['total'] for i in city_num]
        response.context_data['city_total'] = qs.exclude(city=None)

        county_num = qs.exclude(county=None).values('county').annotate(
            total=Count('county')).order_by('-total')
        response.context_data['county_name'] = [
            i['county'] for i in county_num]
        response.context_data['county_count'] = [
            i['total'] for i in county_num]
        response.context_data['county_total'] = qs.exclude(county=None)

        sample_class_num = qs.exclude(sample_class=None).values('sample_class').annotate(
            total=Count('sample_class')).order_by('-total')
        response.context_data['sample_class_name'] = [
            i['sample_class'] for i in sample_class_num]
        response.context_data['sample_class_count'] = [
            i['total'] for i in sample_class_num]
        response.context_data['sample_class_total'] = qs.exclude(
            sample_class=None)

        sample_order_num = qs.exclude(sample_order=None).values('sample_order').annotate(
            total=Count('sample_order')).order_by('-total')
        response.context_data['sample_order_name'] = [
            i['sample_order'] for i in sample_order_num]
        response.context_data['sample_order_count'] = [
            i['total'] for i in sample_order_num]
        response.context_data['sample_order_total'] = qs.exclude(
            sample_order=None)

        sample_class_num = qs.exclude(sample_class=None).values('sample_class').annotate(
            total=Count('sample_class')).order_by('-total')
        response.context_data['sample_class_name'] = [
            i['sample_class'] for i in sample_class_num]
        response.context_data['sample_class_count'] = [
            i['total'] for i in sample_class_num]
        response.context_data['sample_class_total'] = qs.exclude(
            sample_class=None)

        sample_order_num = qs.exclude(sample_order=None).values('sample_order').annotate(
            total=Count('sample_order')).order_by('-total')
        response.context_data['sample_order_name'] = [
            i['sample_order'] for i in sample_order_num]
        response.context_data['sample_order_count'] = [
            i['total'] for i in sample_order_num]
        response.context_data['sample_order_total'] = qs.exclude(
            sample_order=None)

        sample_family_num = qs.exclude(sample_family=None).values('sample_family').annotate(
            total=Count('sample_family')).order_by('-total')
        response.context_data['sample_family_name'] = [
            i['sample_family'] for i in sample_family_num]
        response.context_data['sample_family_count'] = [
            i['total'] for i in sample_family_num]
        response.context_data['sample_family_total'] = qs.exclude(
            sample_family=None)

        sample_genus_num = qs.exclude(sample_genus=None).values('sample_genus').annotate(
            total=Count('sample_genus')).order_by('-total')
        response.context_data['sample_genus_name'] = [
            i['sample_genus'] for i in sample_genus_num]
        response.context_data['sample_genus_count'] = [
            i['total'] for i in sample_genus_num]
        response.context_data['sample_genus_total'] = qs.exclude(
            sample_genus=None)

        sample_species_num = qs.exclude(sample_species=None).values('sample_species').annotate(
            total=Count('sample_species')).order_by('-total')
        response.context_data['sample_species_name'] = [
            i['sample_species'] for i in sample_species_num]
        response.context_data['sample_species_count'] = [
            i['total'] for i in sample_species_num]
        response.context_data['sample_species_total'] = qs.exclude(
            sample_species=None)

        sample_subspecies_num = qs.exclude(sample_subspecies=None).values('sample_subspecies').annotate(
            total=Count('sample_subspecies')).order_by('-total')
        response.context_data['sample_subspecies_name'] = [
            i['sample_subspecies'] for i in sample_subspecies_num]
        response.context_data['sample_subspecies_count'] = [
            i['total'] for i in sample_subspecies_num]
        response.context_data['sample_subspecies_total'] = qs.exclude(
            sample_subspecies=None)

        sample_breed_num = qs.exclude(sample_breed=None).values('sample_breed').annotate(
            total=Count('sample_breed')).order_by('-total')
        response.context_data['sample_breed_name'] = [
            i['sample_breed'] for i in sample_breed_num]
        response.context_data['sample_breed_count'] = [
            i['total'] for i in sample_breed_num]
        response.context_data['sample_breed_total'] = qs.exclude(
            sample_breed=None)

        return response
