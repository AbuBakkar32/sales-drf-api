from django.shortcuts import render
from rest_framework import generics
from .models import SalesModel
from .serializers import SalesSerializer


# Create your views here.
class SalesListCreateView(generics.ListCreateAPIView):
    queryset = SalesModel.objects.all()
    serializer_class = SalesSerializer


class SalesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesModel.objects.all()
    serializer_class = SalesSerializer


"""" 
Create an API that will generate a PDF report from the given dataset. The report should include the below information:
    1. Total number of orders count per year
    2. Total count of distinct customers
    3. Top 3 customers who have ordered the most with their total amount of transactions.
    4. Customer Transactions per Year (from the beginning year to last year)
    5. Most selling items sub-category names
    6. Region basis sales performance pie chart
    7. Sales performance line chart over the years 
"""
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from django.db.models import Count, Sum, Max
from .models import SalesModel
import matplotlib.pyplot as plt


def generate_PDF_report(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    # 1. Total number of orders count per year
    orders_per_year = SalesModel.objects.values('order_date__year').annotate(count=Count('id')).order_by(
        'order_date__year')
    orders_per_year_data = [(str(item['order_date__year']), str(item['count'])) for item in orders_per_year]
    orders_per_year_table = Table([['Year', 'Total Orders']] + orders_per_year_data)
    orders_per_year_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                               ('FONTSIZE', (0, 0), (-1, 0), 12),
                                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(Paragraph('<b>1. Total number of orders count per year:</b>', styles['Heading2']))
    elements.append(orders_per_year_table)
    elements.append(Spacer(1, 20))

    # 2. Total count of distinct customers
    distinct_customers_count = SalesModel.objects.values('customer_id').distinct().count()
    elements.append(Paragraph('<b>2. Total count of distinct customers:</b> {}'.format(distinct_customers_count),
                              styles['Heading2']))
    elements.append(Spacer(1, 20))

    # 3. Top 3 customers who have ordered the most with their total amount of transactions
    top_customers = SalesModel.objects.values('customer_id', 'customer_name').annotate(
        total_sales=Sum('sales')).order_by('-total_sales')[:3]
    top_customers_data = [(item['customer_name'], str(item['total_sales'])) for item in top_customers]
    top_customers_table = Table([['Customer Name', 'Total Sales']] + top_customers_data)
    top_customers_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('FONTNAME', (0, 0), (-3, 1), (-1, -1), colors.beige),
                                             ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(
        Paragraph('<b>3. Top 3 customers who have ordered the most with their total amount of transactions:</b>',
                  styles['Heading2']))
    elements.append(top_customers_table)
    elements.append(Spacer(1, 20))

    # 4. Customer Transactions per Year (from the beginning year to last year)
    customer_transactions_per_year = SalesModel.objects.values('customer_name', 'order_date__year').annotate(
        total_sales=Sum('sales')).order_by('customer_name', 'order_date__year')
    customer_transactions_per_year_data = [
        (item['customer_name'], str(item['order_date__year']), str(item['total_sales'])) for item in
        customer_transactions_per_year]
    customer_transactions_per_year_table = Table(
        [['Customer Name', 'Year', 'Total Sales']] + customer_transactions_per_year_data)
    customer_transactions_per_year_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                                              ('FONTSIZE', (0, 0), (-1, 0), 12),
                                                              ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                                              ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                                              ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(Paragraph('<b>4. Customer Transactions per Year (from the beginning year to last year):</b>',
                              styles['Heading2']))
    elements.append(customer_transactions_per_year_table)
    elements.append(Spacer(1, 20))

    # 5. Most selling items sub-category names
    most_selling_subcategories = SalesModel.objects.values('sub_category').annotate(count=Count('id')).order_by(
        '-count')[:5]
    most_selling_subcategories_data = [(item['sub_category'], str(item['count'])) for item in
                                       most_selling_subcategories]
    most_selling_subcategories_table = Table([['Sub-Category', 'Total Sales']] + most_selling_subcategories_data)
    most_selling_subcategories_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                                          ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                                          ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                                          ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                                          ('FONTSIZE', (0, 0), (-1, 0), 12),
                                                          ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                                          ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                                          ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(Paragraph('<b> 5. Most selling items sub-category names:</b>', styles['Heading2']))
    elements.append(most_selling_subcategories_table)
    elements.append(Spacer(1, 20))

    # 6. Region basis sales performance pie chart
    sales_per_region = SalesModel.objects.values('region').annotate(total_sales=Sum('sales'))
    region_labels = [item['region'] for item in sales_per_region]
    region_sales = [item['total_sales'] for item in sales_per_region]

    plt.pie(region_sales, labels=region_labels, autopct='%1.1f%%')
    plt.title('Sales Performance per Region')
    plt.axis('equal')
    plt.savefig('sales_performance_pie_chart.png')
    plt.close()

    elements.append(Paragraph('<b>6. Region basis sales performance pie chart:</b>', styles['Heading2']))
    elements.append(Spacer(1, 10))
    elements.append(
        Paragraph('<img src="sales_performance_pie_chart.png" width="400" height="300"/>', styles['BodyText']))
    elements.append(Spacer(1, 20))

    # 7. Sales performance line chart over the years
    sales_per_year = SalesModel.objects.values('order_date__year').annotate(total_sales=Sum('sales')).order_by(
        'order_date__year')
    years = [item['order_date__year'] for item in sales_per_year]
    total_sales = [item['total_sales'] for item in sales_per_year]

    plt.plot(years, total_sales, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Total Sales')
    plt.title('Sales Performance over the Years')
    plt.savefig('sales_performance_line_chart.png')
    plt.close()

    elements.append(Paragraph('<b>7. Sales performance line chart over the years:</b>', styles['Heading2']))
    elements.append(Spacer(1, 10))
    elements.append(
        Paragraph('<img src="sales_performance_line_chart.png" width="400" height="300"/>', styles['BodyText']))
    elements.append(Spacer(1, 20))

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
