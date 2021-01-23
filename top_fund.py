from init import *


def get_top_funds(url):
    html = get_html(url)
    collection = get_mongo_collection('fund_rank')
    doc = pq(html)
    items = doc('html body div.mainFrame div.dbtable table#dbtable tbody tr').items()
    for item in items:
        list = []
        infors = item.find('td').items()
        for i, infor in enumerate(infors):
            list.append(str(infor.text().strip()))
            if i == 2:
                href = infor.find('a').attr('href')
                list.append(href)

        information = {
            'index': list[1],
            '代码': list[2],
            '网址': list[3],
            '简称': list[4],
            '日期': list[5],
            '单位净值': list[6],
            '累计净值': list[7],
            '日增长绿': list[8],
            '近一周': list[9],
            '近一月': list[10],
            '近三月': list[11],
            '近六月': list[12],
            '近一年': list[13],
            '近两年': list[14],
            '近三年': list[15],
            '今年来': list[16],
            '成立来': list[17],
            '自定义': list[18],
            '手续费': list[19],
        }
        print(json.dumps(information))
        collection.insert_one(information)


if __name__ == '__main__':
    url = 'http://fund.eastmoney.com/data/fundranking.html'
    get_top_funds(url)
