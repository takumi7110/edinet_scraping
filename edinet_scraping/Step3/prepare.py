from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
import edinet_scraping.Step2.download_XBRL as download_XBRL

parser = EdinetXbrlParser()
# Step2で特定した XBRL ファイルのパスを選択
def prepare(docID):
    xbrl_path = download_XBRL.download_XBRL(docID)[0]
    parsed_xbrl = parser.parse_file(xbrl_path)

    return parsed_xbrl