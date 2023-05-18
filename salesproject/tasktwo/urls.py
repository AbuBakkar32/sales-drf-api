from django.urls import path, include
from .views import SalesListCreateView, \
    SalesRetrieveUpdateDestroyView, \
    generate_PDF_report, \
    export_csv

urlpatterns = [
    path('sales/', SalesListCreateView.as_view(), name='sales-list-create'),
    path('sales/<int:pk>/', SalesRetrieveUpdateDestroyView.as_view(), name='sales-retrieve-update-destroy'),

    # API is used to generate the sales report in PDF format
    path('report/', generate_PDF_report, name='generate-report'),

    # API is used to export the sales data in CSV format
    path('csv/', export_csv, name='generate-csv')
]
