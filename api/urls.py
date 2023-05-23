from django.urls import path

from api import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('risk_report/', views.RiskReportView.as_view(), name='risk-report'),
    path('token/', views.AppTokenView.as_view(), name='token'),
    path('push/', views.PushView.as_view(), name='push'),
    path('get_risk_factor/', views.GetRiskFactor.as_view(), name='get-risk-factor')
]
