import requests

#エンドポイント
url = "https://disclosure.edinet-fsa.go.jp/api/v2/documents.json"

"""
リクエストパラメータ
DATE: ファイル日付(YYYY-MM-DD形式)（必須） 
TYPE: 取得情報  1: メタデータのみ取得(デフォルト)
               2: 提出書類一覧及びメタデータを取得
API_KEY: APIキー
"""

DATE = "ファイル日付"
TYPE=1
API_KEY = "APIキーを入力"

query = {
  "date" : DATE,
  "type" : TYPE,
  "Subscription-Key" : API_KEY
}

# 書類一覧APIの呼び出し
res = requests.get(url, params=query)

# レスポンス（JSON）の表示
print(res.text)