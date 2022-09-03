from rest_framework.generics import ListCreateAPIView

from api.models import SampleModel
from api.serializers.sample import SampleSerializer


class SampleView(ListCreateAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = SampleModel.objects.all()

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = SampleSerializer

    # 認証
    permission_classes = []
