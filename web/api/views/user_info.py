from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import UserInfoModel
from api.serializers.user_info import UserInfoSerializer


class UserInfoView(APIView):
    """
    ユーザ一覧取得、新規登録
    """
    def get(self, request):
        user_info = UserInfoModel.objects.all()
        serializer = UserInfoSerializer(user_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
