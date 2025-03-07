from .lib import *
from .headers import *
#####
class bond(headers_list):
    @classmethod
    def trading_data(cls,start_date, end_date):
        today = date.today().strftime('%d/%m/%Y')
        year = date.today().strftime('%Y')
        #####
        url = "https://cbonds.hnx.vn/thong-ke-thi-truong/danh-sach"
        payload = [
            ("keySearch", f"{today}|{today}||1|1|{year}|{today}|{today}|{start_date}|{end_date}"),
            ("arrCurrentPage[]", "1"),
            ("arrCurrentPage[]", "2"),
            ("arrCurrentPage[]", "1"),
            ("arrNumberRecord[]", "5"),
            ("arrNumberRecord[]", "10000"),
            ("arrNumberRecord[]", "20")
        ]
        response = rq.post(url, headers=cls.cbonds_headers, data=payload, verify=False)
        numpage = re.findall(r'Tổng số <b>(.*?)</b> bản ghi', response.text)[0]
        #####
        url = "https://cbonds.hnx.vn/thong-ke-thi-truong/danh-sach"
        payload = [
            ("keySearch", f"{today}|{today}||1|1|{year}|{today}|{today}|{start_date}|{end_date}"),
            ("arrCurrentPage[]", "1"),
            ("arrCurrentPage[]", str(numpage)),
            ("arrCurrentPage[]", "1"),
            ("arrNumberRecord[]", "5"),
            ("arrNumberRecord[]", str(numpage)),
            ("arrNumberRecord[]", "20")
        ]
        response = rq.post(url, headers=cls.cbonds_headers, data=payload, verify=False)
        # Creat DataFrame
        data = re.sub(r'\s+', ' ', response.text)
        data = re.findall(r'<div id="register_bond" class="hidden">(.*?)</table>', data)\
        #####
        head = re.findall(r'<thead>(.*?)</thead>', data[0])
        head = re.findall(r'">(.*?)</th>', head[0])
        #####
        body = re.findall(r'<tbody>(.*?)</tbody>', data[0])
        body = re.findall(r'<tr>(.*?)</tr>', body[0])
        value = []
        for row in body:
            row = re.findall(r'">(.*?)</td>|<td>(.*?)</td>', row)
            row = [x[0] if x[0] != '' else x[1] for x in row]
            value.append(row)
        #####
        return pd.DataFrame(value, columns = head)