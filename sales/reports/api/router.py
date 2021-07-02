from rest_framework.routers import DefaultRouter

from sales.reports.api.view import TransactionReportViewSet

report_router = DefaultRouter()

report_router.register("transaction-report", TransactionReportViewSet, basename="transaction-report")
