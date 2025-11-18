# Kenro Django サンプル

https://kenro.connpass.com/event/371009/

堅牢.py #1

## セットアップ

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

これは `my_proj.settings.account.settings` における `dataclass` ベースによる設定値管理を実装するデモンストレーションです。
