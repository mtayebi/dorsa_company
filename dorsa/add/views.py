from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AddModel
from .serializers import AddSerializer, TotalSerializer
from .throttling import CustomRateThrottle
from permissions import CustomBasePermission


class Add(APIView):
    throttle_classes = [CustomRateThrottle]

    def get(self, request):
        first_number = request.GET.get('a')
        second_number = request.GET.get('b')

        if first_number.isnumeric() and second_number.isnumeric():
            context = {"result": int(first_number) + int(second_number)}
            AddModel.objects.create(first_number=first_number, second_number=second_number,
                                    total=int(first_number) + int(second_number))
            return Response(context)

        context = {"result": "can not add none numeric values"}
        return Response(context)


class History(APIView):
    permission_classes = [CustomBasePermission]

    def get(self, request):
        history = AddModel.objects.all()
        serialized_data = AddSerializer(instance=history, many=True).data
        # print(serialized_data['first_number'], "<<<<<<<<<<<")
        return Response(serialized_data)


class TotalValues(APIView):
    permission_classes = [CustomBasePermission]

    def get(self, request):
        total_values = AddModel.objects.all()
        serializers_data = TotalSerializer(instance=total_values, many=True).data
        return Response(serializers_data)
