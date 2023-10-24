from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
url='https://www.cdc.gov.tw/Category/QAPage/jWgjO_d826X_F9TURP2_Qg'
url='https://www.cdc.gov.tw/Category/QAPage/kdRH13t_DqJHL4n3N0RVHg'
url='https://www.cdc.gov.tw/Category/QAPage/RJ6gxWhhbZIqMrTMBlWPlQ'
url='https://www.cdc.gov.tw/Category/QAPage/ALa_tyl2m3b5ipRjMLeNYw'
url='https://www.cdc.gov.tw/Category/QAPage/ulaTihAlZvJpKgnS0fwLlA'
url='https://www.cdc.gov.tw/Category/QAPage/73XYTJQLONnIQaCBBi5YVw'
url='https://www.cdc.gov.tw/Category/QAPage/lqCWXtsI9LEtKhDwC2F1Pg'
url='https://www.cdc.gov.tw/Category/QAPage/UVXtkUrPYdBmTg3eDN93Bg'
url='https://www.cdc.gov.tw/Category/QAPage/13K3yAPUM94d5sI7bvV2Fw'
url='https://www.cdc.gov.tw/Category/QAPage/LmRZzs6MSkn4VTFMyirDCw'
url='https://www.cdc.gov.tw/Category/QAPage/uUSIgpZM2ozkQg6ZMKGGeA'
source = urllib.request.urlopen(url).read()
decoded_src=source.decode('utf-8')


soup = BeautifulSoup(decoded_src, 'html.parser')
questions = soup.body.find_all('span', attrs={'class': 'word'})


count_qa=0
QA_list=soup.body.find_all('p')
QA_list=soup.body.find_all('div', attrs={'class', 'panel panel-default'})

title=soup.head.find('title').text.replace('/',' ')
out_file_name=title+".xlsx"
print(out_file_name)
qa_text_out=[]
questions=[]
answers=[]
for QA in QA_list:
    if 'style' not in QA.attrs:
        count_qa+=1

        question=QA.find('span',attrs={'class':'word'})
        question=question.string.strip()
        question=''.join(question.split('.')[1:])[1:]

        print("Q:"+question)

        answer=QA.find('div',attrs={'class':'panel-body'})
        answer=answer.text.strip() #刪除空格
        answer=answer[:-50]

        questions.append(question)
        answers.append(answer)

        print("A:"+answer)
        qa_text_out.append((question,answer))


df=pd.DataFrame({'question':questions,'answer':answers})


print(df)
writer = pd.ExcelWriter(out_file_name, engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet1')
writer._save()


