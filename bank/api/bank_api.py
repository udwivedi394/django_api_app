import json

from django.db import transaction
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.exceptions import APIException
from rest_framework.views import APIView

from bank.api.bank_api_processor import BranchDetails, BranchFinderInCity
from bank.api.serializers import BranchIFSCInputSerializer, BranchFinderInputSerializer


@method_decorator(transaction.non_atomic_requests, name='dispatch')
class BranchDetailer(APIView):
    def get(self, request):
        try:
            response = self._process_request(request)
            response_json = json.dumps(response)
        except Exception as e:
            raise APIException(str(e))
        return HttpResponse(response_json, status=200)

    def _process_request(self, request):
        serializer = BranchIFSCInputSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        ifsc = serializer.validated_data['ifsc']
        return BranchDetails().execute(ifsc=ifsc)


@method_decorator(transaction.non_atomic_requests, name='dispatch')
class BranchFinder(APIView):
    def get(self, request):
        try:
            response = self._process_request(request)
            response_json = json.dumps(response)
        except Exception as e:
            raise APIException(str(e))
        return HttpResponse(response_json, status=200)

    def _process_request(self, request):
        serializer = BranchFinderInputSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        city = serializer.validated_data['city']
        return BranchFinderInCity().execute(name=name, city=city)
