import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.in/Logitech-MK240-NANO-Mouse-Keyboard/dp/B01N4EV2TL/ref=sr_1_10?crid=29O18JRD6DWEJ&keywords=logitech+combo+keyboard+and+mouse&qid=1579103064&sprefix=logitech+comb%2Caps%2C293&sr=8-10'

headers={"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    price=price[2:7]
    cprice=price.split(",")
    fprice=float(cprice[0]+cprice[1])
    print(title.strip())
    print(fprice)
    if fprice<1000:
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('javedali0563@gmail.com','hmupehmhcrfukhdj')
    subject="price is fall down you may buy the product"
    body="check out the link:https://www.amazon.in/Logitech-MK240-NANO-Mouse-Keyboard/dp/B01N4EV2TL/ref=sr_1_10?crid=29O18JRD6DWEJ&keywords=logitech+combo+keyboard+and+mouse&qid=1579103064&sprefix=logitech+comb%2Caps%2C293&sr=8-10"
    msg=f"Subject: {subject} \n\n{body}"

    server.sendmail('javedali0563@gmail.com'
    ,'javedaliofficial0563@gmail.com',msg
    )
    print("HEY EMAIL HAS BEEN SENT!!!!!")
    server.quit()

check_price()
