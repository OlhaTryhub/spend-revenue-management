from _decimal import Decimal
from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import SpendStatistic
from .serializers import SpendStatisticSerializer


class SpendStatisticViewSet(viewsets.ModelViewSet):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendStatisticSerializer

    @action(detail=False, methods=["GET"])
    def aggregate_by_date_name(self, request):
        aggregated_data = (
            self.queryset
            .values("date", "name")
            .annotate(
                total_spend=Sum("spend"),
                total_impressions=Sum("impressions"),
                total_clicks=Sum("clicks"),
                total_conversion=Sum("conversion"),
                total_revenue=Coalesce(
                    Sum("revenuestatistic__revenue"), Decimal(0)
                )
            )
            .prefetch_related("revenuestatistic_set")
        )
        return Response(aggregated_data)
