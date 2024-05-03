import zipfile
import os
from glob import glob
import get_document

def download_XBRL(docID):
    # get_document.pyで返ってきたデータを zip 形式で保存する。
    zip_file_full_path = f'/content/{docID}.zip'
    with open(zip_file_full_path, 'wb') as f:
        for chunk in get_document.get_document(docID).iter_content(chunk_size=1024):
            f.write(chunk)
    
    # zip ファイルを解凍する
    os.makedirs(f'/content/{docID}', exist_ok=True)
    with zipfile.ZipFile(zip_file_full_path) as zip_f:
        zip_f.extractall(f'/content/{docID}')

    xbrl_expression = f'/content/{docID}/**/PublicDoc/**/*.xbrl'
    xbrl_paths = glob(xbrl_expression, recursive=True)
    
    return(xbrl_paths)