from django.shortcuts import render
from Employer.models import User
from Employer.serializers import EmpProfileSerializer, EmpJobsSerializer, JobApplicationSerializer
from Employer.models import EmployerProfile, Jobs, Applications
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import action

# Create your views here.


class EmployerProfileMV(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = EmployerProfile
    serializer_class = EmpProfileSerializer
    queryset = EmployerProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = EmpProfileSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class EmpJobsMV(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = Jobs
    serializer_class = EmpJobsSerializer
    queryset = Jobs.objects.all()

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by("-created_date")

    def create(self, request, *args, **kwargs):
        serializer = EmpJobsSerializer(data=request.data, context={"user": request.user})
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)

    # @action(["GET"], detail=True)
    # def applications(self, request, *args, **kwargs):
    #     job_id = self.get_object()
    #     print(job_id)
    #     appli = Applications.objects.filter(job=job_id, status="applied")
    #     serializer = JobApplicationSerializer(appli, many=True)
    #     return Response(serializer.data)


class JobApplicationMV(ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = Applications
    serializer_class = JobApplicationSerializer
    queryset = Applications.objects.all()

    def get_queryset(self):
        return Applications.objects.filter(status="applied")

