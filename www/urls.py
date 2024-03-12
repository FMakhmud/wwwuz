from django.urls import path
from www.views import DirectionView, SiteListView, SiteLogRetrieveAPIView


urlpatterns = [
    path('direction/', DirectionView.as_view()),
    path('site/all/', SiteListView.as_view()),
    path('site/log/<int:pk>/', SiteLogRetrieveAPIView.as_view()),
    # path('', home_page, name='home'),
]
