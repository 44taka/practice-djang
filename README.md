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

## ネスト要素のあるレスポンス

https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8

これが一番参考になった。
https://qiita.com/ping2shi2/items/805113d68860b540ad52


{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2Mjk3NzMxMCwianRpIjoiYTU5NWJlYjEzNzA0NGYyOTllZTYxMGQ0YmNiYzYzOWIiLCJ1c2VyX2lkIjoxfQ.E0Y4q5XKaFIVXIJ-bL52IbnX0-OfNI_iW7Mylo5HoRI",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyODk0NTEwLCJqdGkiOiIxMjg0YWM1MTc2YmQ0N2ZjYWViNDNhZTE2MDEzN2ExNSIsInVzZXJfaWQiOjF9.wyr9svGpE50FPYxInE_PETAWQV0HKXuR4iOwvEvUij4"
}


curl --location --request GET 'http://localhost:8000/api/auth/users/me' \
--header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyODk0NTEwLCJqdGkiOiIxMjg0YWM1MTc2YmQ0N2ZjYWViNDNhZTE2MDEzN2ExNSIsInVzZXJfaWQiOjF9.wyr9svGpE50FPYxInE_PETAWQV0HKXuR4iOwvEvUij4'
