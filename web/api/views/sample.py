from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ValidationError

from api.models import SampleModel
from api.serializers.sample import SampleSerializer


class SampleView(ModelViewSet):
    # 許容するHTTPメソッドを指定
    http_method_names = ['get', 'post', 'put', 'delete']
    # 認証
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """
        一覧取得（GETメソッド）
        """
        sample = SampleModel.objects.all()
        serializer = SampleSerializer(sample, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """
        詳細取得（GETメソッド）
        """
        try:
            sample = SampleModel.objects.get(pk=pk)
            serializer = SampleSerializer(sample)
            return Response(serializer.data)
        except SampleModel.DoesNotExist:
            raise NotFound()

    def create(self, request):
        """
        新規登録処理（POSTメソッド）
        """
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        raise ValidationError(detail=serializer.errors)

    def update(self, request, pk):
        """
        更新処理（PUTメソッド）
        """
        try:
            sample = SampleModel.objects.get(pk=pk)
            serializer = SampleSerializer(sample, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            raise ValidationError(detail=serializer.errors)
        except SampleModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """
        更新処理（DELETEメソッド）
        """
        sample = SampleModel.objects.get(pk=pk)
        sample.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
