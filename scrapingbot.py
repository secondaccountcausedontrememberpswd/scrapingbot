from bs4 import BeautifulSoup
import requests
import telepot
import time 
import datetime

#CONFIGURAZIONE


boolean = False #NON TOCCARE
delay_time = 30 #QUA PUOI MODFICARE OGNI QUANTO TEMPO(SECONDI) DEVE AVVENIRE LA VERIFICA
check_list = [] #NON TOCCARE
bot_token=''    #CAMBIA
chat_id=       #CAMBIA (INT)

#MAN MANO CHE VENGONO CREATE PAGINE QUINDI 9-10 TU DEVI MODIFICARE I MULTIPLI DI 60 DAL PRIMO, AD ESEMPIO SE VIENE CREATA PA PAGINA 9, TU PRENDI IL PRIMO URL E VAI A CAMBIARE ALLA FINE CON 360+60 E ANCHE GLI ALTRI DUE CON 420+60 QUINDI AL POSTO DI 360 METTI 420 E AL POSTO DI 420 METTI 480 AL POSTO DI 480 METTI 540 E COSI VIA MAN MANO CHE SUL SITO SI CREANO PAGINE IN PIU
url_val = ['https://www.emp-online.it/casa-lifestyle/articoli-per-la-casa/statuette/funko-pop/?srule=top-sellers&start=360&sz=60','https://www.emp-online.it/casa-lifestyle/articoli-per-la-casa/statuette/funko-pop/?srule=top-sellers&start=420&sz=60','https://www.emp-online.it/casa-lifestyle/articoli-per-la-casa/statuette/funko-pop/?srule=top-sellers&start=480&sz=60']
now = datetime.datetime.now()

def send(prod_link):
    bot = telepot.Bot(bot_token)
    bot.sendMessage(chat_id, prod_link)


def run(url):
    try:
        page = requests.get(url)
    except:
        print('Problema con la pagina, prova a cambiare il delay')
        print(page.status_code)
        exit()
    soup = BeautifulSoup(page.text, 'html.parser')
    product_list_items= soup.find_all('div', class_ = 'product-tile')
    for p in product_list_items:
        a_tag = p.a
        link = a_tag['href']
        try:
            check_list.index(link)
            boolean = False
            if(k!=0):
                print('no new products found')
            else:
                pass
        except ValueError:
            check_list.append(link)
            bolean = True
            c_link =  'https://www.emp-online.it'+link #OTTIENI IL LINK COMPLETO
            if(k!=0):
                print('Found!\n')
                send(c_link)
                if(now.hour == 23):
                    if(now.minute > 39) and (now.minute < 55):
                        send('POSSIBILE NUOVO PRODOTTO')
                    else:
                        send('POSSIBILE RESTOCK O ALTRO...VERIFICA!')
                else:
                    send("NON CREDO SIA NUOVO..VERIFICA!")
                
            else:
                pass
            
k=0
send('starting scraping...')        
while(True):
    for i in url_val:
        run(i)

    time.sleep(30)
    print('\nNew check\n')
    k=1

