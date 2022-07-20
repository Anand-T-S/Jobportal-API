from django.urls import path, include
from Users import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path("employer/", include("Employer.urls")),
    path("candidate/", include("Candidate.urls")),
]+router.urls
