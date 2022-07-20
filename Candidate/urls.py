from django.urls import path
from Candidate import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile", views.CandidateProfileMV, basename="cand-profile")
router.register("joblist", views.CandJobsListMV, basename="cand-joblist")
router.register("applications", views.CandApplicationMV, basename="cand-application")
urlpatterns = []+router.urls
