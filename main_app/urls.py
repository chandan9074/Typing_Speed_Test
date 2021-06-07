from django.urls import path

from .views import QuotesAPIView, RecordsAPIView, CreateRecordAPIView

urlpatterns = [
    path("quotes/<int:pk>/", QuotesAPIView.as_view()),
    path("records/<int:pk>/", RecordsAPIView.as_view()),
    path("create_record/", CreateRecordAPIView.as_view()),
]