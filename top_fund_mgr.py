import json
import pandas
import requests


def get_top_fund_managers(topk, out='stdout', filepath=None):
    url = 'https://fundmobapi.eastmoney.com/FundMApi/FundMangerBaseList.ashx?deviceid=fundmanager2016&version=4.3.0&product=EFund&plat=Iphone&COMPANYCODES=&MFTYPE=&SortColumn=Y&Sort=desc&pageIndex=1&pageSize=%d' % topk
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception("get top fund managers failed")
    json_data = resp.content.decode('utf-8')
    mgrs = json.loads(json_data)['Datas']
    if out == 'stdout':
        for m in mgrs:
            print(m)
            print("*********************************")
        return

    mgrs = json.dumps(mgrs).encode('utf-8')
    df = pandas.read_json(path_or_buf=mgrs, orient='records', encoding='utf-8')
    if out == 'excel':
        df.to_excel(filepath)


if __name__ == '__main__':
    topk = 100
    get_top_fund_managers(topk, out='excel', filepath='top_%d_managers.xlsx' % topk)
