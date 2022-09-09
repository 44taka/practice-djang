from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import UserInfoModel
from api.serializers.user_info import UserInfoSerializer


class UserInfoDetailView(APIView):
    """
    ユーザ詳細情報取得、更新、削除
    """
    def get_object(self, pk):
        try:
            return UserInfoModel.objects.get(pk=pk)
        except UserInfoModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user_info = self.get_object(pk)
        serializer = UserInfoSerializer(user_info)
        return Response(serializer.data)

    def put(self, request, pk):
        user_info = self.get_object(pk)
        serializer = UserInfoSerializer(user_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_info = self.get_object(pk)
        user_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


