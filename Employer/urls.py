from django.urls import path
from Employer import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("profile", views.EmployerProfileMV, basename="emp-profile")
router.register("jobs", views.EmpJobsMV, basename="emp-job")
router.register("applications", views.JobApplicationMV, basename="emp-jobapplication")

urlpatterns = []+router.urls
