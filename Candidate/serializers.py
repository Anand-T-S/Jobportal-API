from rest_framework.serializers import ModelSerializer
from Candidate.models import CandidateProfile
from Employer.models import Jobs, Applications
from rest_framework import serializers


class CandProfileSerializer(ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = CandidateProfile
        exclude = ("user",)

    def create(self, validated_data):
        user = self.context.get("user")
        return CandidateProfile.objects.create(**validated_data, user=user)


class CandJobListSerializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'


class CandApplicationSerializer(ModelSerializer):
    class Meta:
        model = Applications
        fields = '__all__'
