from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django.db.models import Count
from django.db.models import Q

from .models import Sample
from .filters import SampleFilter


# for csv download
from djqscsv import render_to_csv_response

# figs for plotly
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

px.set_mapbox_access_token(
    "pk.eyJ1IjoibmV2ZXJzYXk0ZXZlciIsImEiOiJjazcxOW8yMDUwNGdyM21vaHpwdnZvajhnIn0.irEnBJE84kSZv4RcOMFalw")

# Create your views here.


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
            'latitude', 'longitude').annotate(count=Count('id')))
        df_count_gis = pd.DataFrame(count_gis)

        # begin of map plotly. world map to display sample count based on gis
        fig_map_count_gis = px.scatter_mapbox(df_count_gis, lat="latitude", lon="longitude",  color="count", size="count",
                                              color_continuous_scale=px.colors.cyclical.IceFire, size_max=20, zoom=3)
        fig_map_count_gis.update_layout(
            margin=dict(l=10, r=5, b=20, t=20),
            mapbox=dict(
                center=dict(
                    lat=28,
                    lon=110
                ),
            ),
        )
        map_count_gis_plt_div = plot(fig_map_count_gis, output_type='div', include_plotlyjs=False,
                                     show_link=False, link_text="")
        # end of map plotly

        count_geo = list(self.sample_filter.qs.exclude(continent_ocean__isnull=True).exclude(country__isnull=True).exclude(state_province__isnull=True).exclude(city__isnull=True).exclude(county__isnull=True).values(
            'continent_ocean', 'country', 'state_province', 'city', 'county').annotate(count=Count('id')))
        df_count_geo = pd.DataFrame(count_geo)

        # begin of barplot plotly. barplot to display sample count based on gis
        fig_continent_bar = px.bar(df_count_geo, x="count", y="continent_ocean", color='country', orientation='h',
                                   hover_data=['country'],
                                   title='Sample/Continent_ocean Stats')
        fig_continent_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        continent_bar_plt_div = plot(fig_continent_bar, output_type='div', include_plotlyjs=False,
                                     show_link=False, link_text="")

        fig_country_bar = px.bar(df_count_geo, x="count", y="country", color='state_province', orientation='h',
                                 hover_data=['state_province'],
                                 title='Sample/Country Stats')
        fig_country_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        country_bar_plt_div = plot(fig_country_bar, output_type='div', include_plotlyjs=False,
                                   show_link=False, link_text="")

        fig_province_bar = px.bar(df_count_geo, x="count", y="state_province", color='city', orientation='h',
                                  hover_data=['city'],
                                  title='Sample/State_province Stats')
        fig_province_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        province_bar_plt_div = plot(fig_province_bar, output_type='div', include_plotlyjs=False,
                                    show_link=False, link_text="")

        fig_city_bar = px.bar(df_count_geo, x="count", y="city", color='county', orientation='h',
                              hover_data=['county'],
                              title='Sample/City Stats')
        fig_city_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        city_bar_plt_div = plot(fig_city_bar, output_type='div', include_plotlyjs=False,
                                show_link=False, link_text="")
        # end of barplot

        # begin of treemap plotly. treemap to display sample count based on gis
        # in order to have a single root node
        df_count_geo["world"] = "world"
        fig_treemap_count_geo = px.treemap(df_count_geo, path=['world', 'continent_ocean', 'country', 'state_province', 'city', 'county'], values='count',
                                           color='count',
                                           color_continuous_scale='RdBu_r')
        fig_treemap_count_geo.update_layout(
            margin=dict(l=20, r=20, b=20, t=55, pad=4),
            title=dict(text="地理数量统计"), font=dict(size=15))
        treemap_count_geo_plt_div = plot(fig_treemap_count_geo, output_type='div', include_plotlyjs=False,
                                         show_link=False, link_text="")
        # end of treemap plotly

        count_taxonomy = list(self.sample_filter.qs.exclude(sample_phylum__isnull=True).exclude(sample_class__isnull=True).exclude(sample_order__isnull=True).exclude(sample_family__isnull=True).exclude(sample_genus__isnull=True).exclude(sample_species__isnull=True).exclude(sample_subspecies__isnull=True).exclude(sample_breed__isnull=True).values(
            'sample_phylum', 'sample_class', 'sample_order', 'sample_family', 'sample_genus', 'sample_species', 'sample_subspecies', 'sample_breed').annotate(count=Count('id')))

        df_count_taxonomy = pd.DataFrame(count_taxonomy)

        # begin of sunburst plotly. sunburst to display sample count based on taxonomy
        fig_sunburst_count_taxnomy = px.sunburst(pd.DataFrame(df_count_taxonomy), path=[
                                                 'sample_phylum', 'sample_class', 'sample_order', 'sample_family', 'sample_genus', 'sample_species', 'sample_subspecies', 'sample_breed'], values='count', color='sample_subspecies', hover_data=['count'],)
        fig_sunburst_count_taxnomy.update_layout(
            margin=dict(l=20, r=20, b=20, t=40, pad=4),
            title=dict(text="物种数量统计"), font=dict(size=15))
        sunburst_count_taxnomy_plt_div = plot(fig_sunburst_count_taxnomy, output_type='div', include_plotlyjs=False,
                                              show_link=False, link_text="")
        # end of sunburst plotly

        # begin of barplot plotly. barplot to display sample count based on gis
        fig_phylum_bar = px.bar(df_count_taxonomy, x="count", y="sample_phylum", color='sample_class', orientation='h',
                                hover_data=['sample_class'],
                                title='Sample/Phylum Stats')
        fig_phylum_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        phylum_bar_plt_div = plot(fig_phylum_bar, output_type='div', include_plotlyjs=False,
                                  show_link=False, link_text="")

        fig_class_bar = px.bar(df_count_taxonomy, x="count", y="sample_class", color='sample_order', orientation='h',
                               hover_data=['sample_order'],
                               title='Sample/Class Stats')
        fig_class_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        class_bar_plt_div = plot(fig_class_bar, output_type='div', include_plotlyjs=False,
                                 show_link=False, link_text="")

        fig_order_bar = px.bar(df_count_taxonomy, x="count", y="sample_order", color='sample_family', orientation='h',
                               hover_data=['sample_family'],
                               title='Sample/Order Stats')
        fig_order_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        order_bar_plt_div = plot(fig_order_bar, output_type='div', include_plotlyjs=False,
                                 show_link=False, link_text="")

        fig_family_bar = px.bar(df_count_taxonomy, x="count", y="sample_family", color='sample_genus', orientation='h',
                                hover_data=['sample_genus'],
                                title='Sample/Family Stats')
        fig_family_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        family_bar_plt_div = plot(fig_family_bar, output_type='div', include_plotlyjs=False,
                                  show_link=False, link_text="")

        fig_genus_bar = px.bar(df_count_taxonomy, x="count", y="sample_genus", color='sample_species', orientation='h',
                               hover_data=['sample_species'],
                               title='Sample/Class Stats')
        fig_genus_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        genus_bar_plt_div = plot(fig_genus_bar, output_type='div', include_plotlyjs=False,
                                 show_link=False, link_text="")

        fig_species_bar = px.bar(df_count_taxonomy, x="count", y="sample_species", color='sample_subspecies', orientation='h',
                                 hover_data=['sample_subspecies'],
                                 title='Sample/Species Stats')
        fig_species_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        species_bar_plt_div = plot(fig_species_bar, output_type='div', include_plotlyjs=False,
                                   show_link=False, link_text="")

        fig_subspecies_bar = px.bar(df_count_taxonomy, x="count", y="sample_subspecies", color='sample_breed', orientation='h',
                                    hover_data=['sample_breed'],
                                    title='Sample/Subspecies Stats')
        fig_subspecies_bar.update_layout(
            margin=dict(l=20, r=40, b=20, t=50))
        subspecies_bar_plt_div = plot(fig_subspecies_bar, output_type='div', include_plotlyjs=False,
                                      show_link=False, link_text="")
        # end of barplot

        context['map_count_gis_plt_div'] = map_count_gis_plt_div
        context['treemap_count_geo_plt_div'] = treemap_count_geo_plt_div
        context['sunburst_count_taxnomy_plt_div'] = sunburst_count_taxnomy_plt_div

        context['continent_bar_plt_div'] = continent_bar_plt_div
        context['country_bar_plt_div'] = country_bar_plt_div
        context['province_bar_plt_div'] = province_bar_plt_div
        context['city_bar_plt_div'] = city_bar_plt_div

        context['phylum_bar_plt_div'] = phylum_bar_plt_div
        context['class_bar_plt_div'] = class_bar_plt_div
        context['order_bar_plt_div'] = order_bar_plt_div
        context['family_bar_plt_div'] = family_bar_plt_div
        context['genus_bar_plt_div'] = genus_bar_plt_div
        context['species_bar_plt_div'] = species_bar_plt_div
        context['subspecies_bar_plt_div'] = subspecies_bar_plt_div

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
