from django.urls import path, include
from rest_framework import routers
from .views import RevenueStatisticViewSet

app_name = "revenue"

router = routers.DefaultRouter()
router.register("statistics", RevenueStatisticViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "aggregate-by-date-name/",
        RevenueStatisticViewSet.as_view({"get": "aggregate_by_date_name"}),
        name="aggregate-by-date-name"),
]
