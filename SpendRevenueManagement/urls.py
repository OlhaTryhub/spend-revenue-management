from django.urls import path, include

urlpatterns = [
    path("revenue/", include("revenue.urls")),
    path("spend/", include("spend.urls")),
]
