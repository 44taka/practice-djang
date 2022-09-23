# practice-django

DjangoでAPIを作ってた色々試してみるためのリポジトリ。

## 作ったもの

JWTを使ったプチ認証つきCRUD機能があるREST API

## 使ってるもの

- Python 3.10.6
- Django 4.1.1
- Django REST framework 3.13.1
- PostgreSQL

## 使用方法

```
# コンテナ起動
docker-compose up -d
```

## 参考サイト

- docker構築、プロジェクト駆逐
  - https://docs.docker.com/samples/django/
  - https://www.djangoproject.com/download/
- Django REST frameworkについて
  - 全般
    - https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8
    - https://qiita.com/okoppe8/items/c58bb3faaf26c9e2f27f
  - ビュー、シリアライザ周り
    - https://www.django-rest-framework.org/api-guide/serializers/
    - https://note.crohaco.net/2018/django-rest-framework-serializer/
    - https://note.crohaco.net/2018/django-rest-framework-view/
    - https://itc.tokyo/django/restframework-viewset/
  - レスポンス周り
    - https://qiita.com/ping2shi2/items/805113d68860b540ad52
  - カスタムユーザー周り
    - https://daeudaeu.com/django-abstractuser/
    - https://itc.tokyo/django/user/
  - エラーハンドリング周り
    - https://qtatsu.hatenablog.com/entry/2020/06/15/122819
  - ログイン、認証周り
    - https://qiita.com/KueharX/items/eef29ae0c5c238cbf61c
    - https://nmomos.com/tips/2019/07/24/django-jwt-authentication/
    - https://www.kueharx.com/2021/05/djoserdjango-rest-framework.html
    - https://zenn.dev/maru44/articles/8c22bbd6954ea6
- その他
  - JWT周り
    - https://qiita.com/knaot0/items/8427918564400968bd2b


https://di-acc2.com/programming/python/10325/

## コマンドメモ（自分用）

Djangoのプロジェクト作成

```
django-admin startproject [プロジェクト名] [作成ディレクトリパス]
```

Djangoのアプリケーション作成

```
cd [Djangoのプロジェクトルートディレクトリ]
python manage.py startapp [アプリケーション名]
```
