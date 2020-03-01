from django.views.generic import TemplateView
import os
import csv
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from database_bee.settings import BASE_DIR

freezer_csv = os.path.join(BASE_DIR, 'sample/freezer.csv')
with open(freezer_csv) as csv_file:
    df_freezer = pd.read_csv(csv_file)
    df_freezer["freezer"] = "freezer"
    fig_freezer = px.treemap(df_freezer, path=['freezer', '编号1', '编号2', '编号3', '编号4', '编号5', '存储内容'], values='count', color='count',
                             color_continuous_scale='Blugrn_r')
    fig_freezer.update_layout(
        margin=dict(l=20, r=20, b=20, t=55, pad=4),
        title=dict(text="冰箱结构"), font=dict(size=15))
    freezer_plt_div = plot(fig_freezer, output_type='div', include_plotlyjs=False,
                           show_link=False, link_text="")


class WebpageHomeView(TemplateView):
    template_name = 'webpage_home.html'


class WebpageAboutView(TemplateView):
    template_name = 'webpage_about.html'


class WebpageFreezerView(TemplateView):
    template_name = 'webpage_freezer.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WebpageFreezerView, self).get_context_data(
            *args, **kwargs)
        context['freezer_plt_div'] = freezer_plt_div
        return context


class WebpageBrowserView(TemplateView):
    template_name = 'webpage_browser.html'


class WebpageSearchView(TemplateView):
    template_name = 'webpage_search.html'


class WebpageStatisticView(TemplateView):
    template_name = 'webpage_statistic.html'


class WebpageRecordView(TemplateView):
    template_name = 'webpage_record.html'
