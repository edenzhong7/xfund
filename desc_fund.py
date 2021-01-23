from init import *
import time


def get_fund_info(url):
    full_html = get_html(url)
    doc = html.fromstring(full_html)
    stock_holdings = doc.xpath('//*[@id="position_shares"]/div[1]/table/tbody/tr')
    for s in stock_holdings[1:]:
        row = []
        tds = s.xpath('td')
        row.append(tds[0].xpath('./a/@href')[0])
        for td in tds[:-1]:
            row.append(td.text_content().strip())
        print(' '.join(row))

    pure_val_history = doc.xpath('//*[@id="Li1"]/div[1]/table/tbody/tr')
    for h in pure_val_history[1:]:
        row = []
        tds = h.xpath('td')
        for td in tds:
            row.append(td.text_content().strip())
        print(' '.join(row))
    pure_val_url = doc.xpath('//*[@id="Li1"]/div[2]/a/@href')[0]
    print(pure_val_url)


def get_more_pure_values(url):
    browser = webdriver.Chrome()
    browser.get(url)
    records = []

    def _extract_pure_values(full_html):
        doc = html.fromstring(full_html)
        pure_val_history = doc.xpath('//*[@id="jztable"]/table/tbody/tr')
        for h in pure_val_history[1:]:
            row = []
            tds = h.xpath('td')
            for td in tds:
                row.append(td.text_content().strip())
            records.append(' '.join(row))

    for i in range(7):
        _extract_pure_values(browser.page_source)
        next_page_btu = browser.find_elements_by_xpath('//*[@id="pagebar"]/div[1]/label[8]')[0]
        next_page_btu.click()
        time.sleep(1)

    for r in records:
        print(r)


if __name__ == '__main__':
    # get_fund_info('http://fund.eastmoney.com/000409.html')
    get_more_pure_values('http://fundf10.eastmoney.com/jjjz_000409.html')