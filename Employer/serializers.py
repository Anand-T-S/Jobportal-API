from rest_framework.serializers import ModelSerializer
from Employer.models import EmployerProfile, Jobs, Applications
from rest_framework import serializers


class EmpProfileSerializer(ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = EmployerProfile
        exclude = ("user",)

    def create(self, validated_data):
        user = self.context.get("user")
        return EmployerProfile.objects.create(**validated_data, user=user)


class EmpJobsSerializer(ModelSerializer):
    id = serializers.CharField(read_only=True)
    posted_by = serializers.CharField(read_only=True)

    class Meta:
        model = Jobs
        exclude = ("created_date",)

    def create(self, validated_data):
        user = self.context.get("user")
        return Jobs.objects.create(**validated_data, posted_by=user)


class JobApplicationSerializer(ModelSerializer):
    id = serializers.CharField(read_only=True)
    # applicant = serializers.CharField(read_only=True)
    # job = serializers.CharField(read_only=True)
    # date = serializers.CharField(read_only=True)

    class Meta:
        model = Applications
        fields = '__all__'
        depth = 1
