from django.urls import path
from .views import WebpageHomeView, WebpageAboutView, WebpageFreezerView, WebpageBrowserView, WebpageSearchView, WebpageStatisticView, WebpageRecordView

urlpatterns = [
    path('', WebpageHomeView.as_view(), name='webpage_home'),
    path('about/', WebpageAboutView.as_view(), name='webpage_about'),
    path('freezer/', WebpageFreezerView.as_view(), name='webpage_freezer'),
    path('browser', WebpageBrowserView.as_view(), name='webpage_browser'),
    path('search/', WebpageSearchView.as_view(), name='webpage_search'),
    path('statistic/', WebpageStatisticView.as_view(), name='webpage_statistic'),
    path('record/', WebpageRecordView.as_view(), name='webpage_record'),
]
