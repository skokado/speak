# 堅牢.py #1

堅牢.py #1
https://kenro.connpass.com/event/371009/

Title『モノリスDjangoにおける堅牢性の追求』

[Google Slide](https://docs.google.com/presentation/d/e/2PACX-1vQrXQD8m1aiWdqSWWWBF-XxtGy1eH66FdSB4TubHwuR6C1rNv4-Fv_oQneXZX-hhECS-CjP8oZWky-H/pub?start=false&loop=false&delayms=3000)

このディレクトリは、Django のモジュラモノリス構成のサンプル、
および `dataclass` を併用して Django 設定値管理に型を活用するデモンストレーションの実装です。

# How to run

```bash
$ git clone https://github.com/skokado/speak.git
$ cd speak/kenro-py-1
$ uv sync
$ uv run manage.py runserver
```

その後、http://127.0.0.1:8000/api/docs を開いてAPI仕様書を確認してください。

`account` と `payment` の2つのDjangoアプリがあり、それぞれ `v1` と `v2` バージョンで利用可能です。

実行

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/account/' \
  -H 'accept: application/json'
```

コンソールに以下の出力が表示されます:

```
DEBUG: settings.cognito_app_client_id='dummy',settings.cognito_user_pool_id='dev_dummy_pool_id'
```
