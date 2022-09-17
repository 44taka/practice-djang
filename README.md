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