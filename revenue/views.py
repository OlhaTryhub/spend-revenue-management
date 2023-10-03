from django.db.models import Sum, F
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import RevenueStatistic
from .serializers import RevenueStatisticSerializer


class RevenueStatisticViewSet(viewsets.ModelViewSet):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueStatisticSerializer

    @action(detail=False, methods=["GET"])
    def aggregate_by_date_name(self, request):
        aggregated_data = (
            self.queryset
            .values("date", "name")
            .annotate(total_revenue=Sum("revenue"),
                      total_spend=Sum(F("spend__spend")),
                      total_impressions=Sum(F("spend__impressions")),
                      total_clicks=Sum(F("spend__clicks")),
                      total_conversion=Sum(F("spend__conversion"))
                      )
        )
        return Response(aggregated_data)
