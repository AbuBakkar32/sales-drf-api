from django.urls import path, include
from .views import SalesListCreateView, SalesRetrieveUpdateDestroyView, generate_PDF_report

urlpatterns = [
    path('sales/', SalesListCreateView.as_view(), name='sales-list-create'),
    path('sales/<int:pk>/', SalesRetrieveUpdateDestroyView.as_view(), name='sales-retrieve-update-destroy'),
    path('report/', generate_PDF_report, name='generate-report')
]
