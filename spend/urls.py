from django.urls import path, include
from rest_framework import routers
from .views import SpendStatisticViewSet

app_name = "spend"

router = routers.DefaultRouter()
router.register("statistics", SpendStatisticViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "aggregate-by-date-name/",
        SpendStatisticViewSet.as_view({"get": "aggregate_by_date_name"}),
        name="aggregate-by-date-name"),
]
