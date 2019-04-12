from rest_framework import serializers


class BranchIFSCInputSerializer(serializers.Serializer):
    ifsc = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class BranchFinderInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
