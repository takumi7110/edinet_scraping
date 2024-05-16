import pandas as pd
import make_dataframe

def extract_information(DATE, TYPE, API_KEY):
    securities_report_infos = []

    for index, row in make_dataframe.make_dataframe(DATE,TYPE,API_KEY).iterrows():
        doc_desc = row['docDescription']

        if doc_desc is None:
            continue
        
        #提出書類のタイトルに「有価証券報告書」を含むもののうち、
        #「受益証券」を含まないものから情報を抽出する。
        if ('有価証券報告書' in doc_desc) and ('受益証券' not in doc_desc):
            row_to_dataframe = pd.DataFrame([row])
            securities_report_infos.append(row_to_dataframe)

    if len(securities_report_infos) == 0:
        print('有価証券報告書の提出情報がありません。')
    else:
        print(f'{len(securities_report_infos)} 件の有価証券報告書が抽出されました。')
        securities_report_info_df = pd.concat(securities_report_infos)
        return securities_report_info_df