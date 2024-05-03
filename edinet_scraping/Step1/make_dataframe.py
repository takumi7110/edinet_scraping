import pandas as pd
import get_document_list 

def make_dataframe(DATE, TYPE, API_KEY):
    res_ison=get_document_list.get_list(DATE, TYPE, API_KEY)
    raw_submission_df=pd.DataFrame(res_ison['results'])

    """
    重要なカラム
    docID: 書類を特定するID
    edinetCode: 企業ごとに割り振られたコード
    secCode: 証券コード
    filerName: 企業名
    docDescription: 提出書類のタイトル
    """

    submission_df=raw_submission_df[['docID', 'edinetCode', 'secCode', 'filerName', 'docDescription']]
    return submission_df