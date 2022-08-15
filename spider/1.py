import requests
from fake_useragent import UserAgent


s = requests.session()

headers = {"User-Agent":UserAgent().random}


s.get('http://www.cwl.gov.cn',headers=headers)
res = s.get('http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=30&issueStart=&issueEnd=&dayStart=&dayEnd=',headers=headers)
print(res.text)