import requests

#エンドポイント
END_POINT="https://disclosure.edinet-fsa.go.jp/api/v2"
url = f'{END_POINT}/documents.json'

def get_list(DATE, TYPE, API_KEY):
    """
    パラメータ
    date: ファイル日付(YYYY-MM-DD形式)（必須） 
    type: 取得情報  1: メタデータのみ取得(デフォルト)
                   2: 提出書類一覧及びメタデータを取得
    key: APIキー
    """
    query = {
      "date" : DATE,
      "type" : TYPE,
      "Subscription-Key" : API_KEY
    }

    # 書類一覧APIの呼び出し
    res = requests.get(url, params=query)

    # レスポンス（JSON）の表示
    res_json=res.json()
    return(res_json)