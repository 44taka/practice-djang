# practice-django




## docker-compose構築

https://docs.docker.com/samples/django/
https://www.djangoproject.com/download/

https://di-acc2.com/programming/python/10325/

## コマンド

Djangoのプロジェクト作成

```
django-admin startproject [プロジェクト名] [作成ディレクトリパス]
```

Djangoのアプリケーション作成

```
cd [Djangoのプロジェクトルートディレクトリ]
python manage.py startapp [アプリケーション名]
```

https://jnuank.hatenablog.com/entry/2020/12/16/235345

## シリアライザについて

データの入出力を担うもの。
DBテーブル（モデル）の値を伝えるためのバリデーションチェックや値をセットする。
出力する際に適切なレスポンスの形式（jsonやxmlなど）に変換してくれる。

https://www.django-rest-framework.org/api-guide/serializers/
https://note.crohaco.net/2018/django-rest-framework-serializer/
https://note.crohaco.net/2018/django-rest-framework-view/

## ネスト要素のあるレスポンス

https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8

これが一番参考になった。
https://qiita.com/ping2shi2/items/805113d68860b540ad52

https://daeudaeu.com/django-abstractuser/
https://itc.tokyo/django/user/


https://yamayou-1.hatenablog.com/entry/2022/03/06/172335
https://qtatsu.hatenablog.com/entry/2020/06/15/122819
https://qiita.com/okoppe8/items/c58bb3faaf26c9e2f27f
https://itc.tokyo/django/restframework-viewset/

https://qiita.com/KueharX/items/eef29ae0c5c238cbf61c
https://nmomos.com/tips/2019/07/24/django-jwt-authentication/

https://qiita.com/knaot0/items/8427918564400968bd2b
https://www.kueharx.com/2021/05/djoserdjango-rest-framework.html
https://zenn.dev/maru44/articles/8c22bbd6954ea6

## エラーハンドリング

https://qtatsu.hatenablog.com/entry/2020/06/15/122819