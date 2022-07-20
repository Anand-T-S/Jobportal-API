from django.shortcuts import render
from Candidate.models import CandidateProfile
from Candidate.serializers import CandProfileSerializer, CandJobListSerializer, CandApplicationSerializer
from Employer.models import Jobs, Applications
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import action

# Create your views here.


class CandidateProfileMV(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = CandidateProfile
    serializer_class = CandProfileSerializer
    queryset = CandidateProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CandProfileSerializer(data=request.data, context={"user": request.user})
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class CandJobsListMV(ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = Jobs
    serializer_class = CandJobListSerializer
    queryset = Jobs.objects.all()

    @action(["GET"], detail=True)
    def apply_now(self, request, *args, **kwargs):
        applicant = self.request.user
        job_id = self.get_object()
        Applications.objects.create(applicant=applicant, job=job_id)
        return Response({"msg": "ok"})


class CandApplicationMV(ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = Applications
    serializer_class = CandApplicationSerializer
    queryset = Applications.objects.all()

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)
