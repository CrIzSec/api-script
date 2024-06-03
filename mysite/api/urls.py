from django.urls import path
from .views import RunScriptView, RunDecodeView

urlpatterns = [
    path('run-script/', RunScriptView.as_view(), name='run-script'),
    path('run-script/decode/', RunDecodeView.as_view(), name='decode'),
]
