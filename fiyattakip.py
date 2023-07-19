import smtplib
import time

import requests
from bs4 import BeautifulSoup

url = input("Hepsiburada üzerindeki URL'ini Giriniz: ")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

def fiyatkontrol():
	page = requests.get(url,headers=headers)
	soup = BeautifulSoup(page.content,"html.parser")
	title = soup.find(id='product-name').get_text().strip()
	title = title[0:18]
	print(title)
	fiyat = soup.find(id='offering-price')
	content = fiyat.attrs.get('content')
	price = float(content)
	print(price)
	istenilen = int(input("Mail Bilgilendirmesi için Fiyat Belirleyin: "))
	if(price < istenilen):
		mail(title)
 
def mail(title):
   sender = 'tamer.akdeniz3@gmail.com'
   reciever = input("Yönlendirmek İstediğiniz Mail Adresini Giriniz: ")
   try: 
      server = smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.login(sender,'nqtsxkbphtigjnbd')
      subject = 'Takip ettiginiz ' + title + ' adli urun istediginiz fiyata dustu!'
      body = subject + '\n' + 'Urun Linki: ' + url
      mailContent = f"To:{reciever}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
      server.sendmail(sender,reciever,mailContent)
      print('Mail Gonderildi!')
   except smtplib.SMTPException as i:
      print(i)
   finally:
      server.quit()
      
while(1):
   fiyatkontrol()
   time.sleep(3600*24)