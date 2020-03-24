from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django.db.models import Count
from django.db.models import Q

from .models import Sample
from .filters import SampleFilter


# for csv download
from djqscsv import render_to_csv_response

import pandas as pd
import geojson
import json
# Create your views here.


def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    geojson = {'type': 'FeatureCollection', 'features': []}
    for _, row in df.iterrows():
        feature = {'type': 'Feature',
                   'properties': {},
                   'geometry': {'type': 'Point',
                                'coordinates': []}}
        feature['geometry']['coordinates'] = [row[lon], row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson


class SampleHomeView(ListView):

    template_name = 'sample_home__.html'
    context_object_name = 'samples'
    paginate_by = 100
    queryset = Sample.objects.all()

    def get_queryset(self):
        qs = Sample.objects.all()

        q = self.request.GET.get('q', '')
        if q:
            qs = Sample.objects.filter(
                Q(sample_id__icontains=q) | Q(sample_box_id__icontains=q) | Q(
                    headchest_id__icontains=q) | Q(headchest_usage__icontains=q) | Q(abdomen_id__icontains=q) | Q(abdomen_usage__icontains=q) | Q(gut_id__icontains=q) | Q(gut_usage__icontains=q) | Q(leg_id__icontains=q) | Q(sample_phylum__icontains=q) | Q(sample_class__icontains=q) | Q(sample_order__icontains=q) | Q(sample_genus__icontains=q) | Q(sample_species__icontains=q) | Q(sample_subspecies__icontains=q) | Q(sample_breed__icontains=q) | Q(identifier_name__icontains=q) | Q(identifier_email__icontains=q) | Q(exact_site__icontains=q) | Q(country__icontains=q) | Q(state_province__icontains=q) | Q(city__icontains=q) | Q(county__icontains=q) | Q(latitude__icontains=q) | Q(longitude__icontains=q) | Q(elevation__icontains=q) | Q(collector_name__icontains=q) | Q(bee_type__icontains=q)
            )
        self.sample_filter = SampleFilter(
            self.request.GET, queryset=qs)
        return self.sample_filter.qs.order_by('id')

    def get(self, request, **kwargs):
        # check for format query key in url (my/url/?format=csv)
        self.format = request.GET.get('format', False)
        if self.format == 'csv':
            return render_to_csv_response(self.get_queryset())

        return super(SampleHomeView, self).get(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.

        count_gis = list(self.sample_filter.qs.exclude(latitude__isnull=True).values(
            'latitude', 'longitude', 'sample_species').annotate(count=Count('id')))
        df_count_gis = pd.DataFrame(count_gis).fillna('unkown')
        cols = ['count', 'sample_species']

        geo_json = df_to_geojson(df_count_gis, cols)
        context['sample_geo_json'] = geo_json

        sample_query = self.sample_filter.qs

        context['sample_count'] = sample_query.count()
        context['sample_strain_count'] = sample_query.filter(
            gut_usage='已分菌').count()
        context['sample_meta_count'] = sample_query.filter(
            gut_usage='meta').count()
        context['sample_no_latitude_count'] = sample_query.filter(
            latitude=None).count()

        context['sample_filter'] = self.sample_filter

        return context


class SampleDetailView(TemplateView):
    template_name = 'sample_detail.html'
