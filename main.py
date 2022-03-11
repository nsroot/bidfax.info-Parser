import time
import requests
from bs4 import BeautifulSoup
from lxml import etree
import codecs
import csv
import MySQLdb
import wget
from PIL import Image


#links = input("აიღციე მანქანის მოდელი\n 1.Alfa Romeo \n 2.Aston Martin \n შეიყვანეთ რიცხვი არჩეული მოდელის : ")
#if links ==1:
#    carmodellink = 'alfa-romeo'
#if links ==2:
#    carmodellink = 'aston-martin'
id = 1
headers = {
    'authority': 'en.bidfax.info',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://en.bidfax.info/',
    'accept-language': 'tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
}

for pagenumber in range(1,99):

    r = requests.get('https://en.bidfax.info/bmw/page/'+ str(pagenumber) +'/', headers=headers)
    soup = BeautifulSoup(r.content,"lxml")

    cars = soup.find_all("div",attrs={"class":"col-xs-12 col-sm-6"})
    for car in cars:
        link = car.find("a",attrs={"class":"btn btn-default btn-more pull-right"})
        link = str(link)
        link = link[53:-26]
        if link is not '':
            reallink = link
        title = car.find("h2")
        title = str(title)
        title = title[4:-5]
        car_r = requests.get(reallink,headers=headers)
        car_soup = BeautifulSoup(car_r.content, "html.parser")
        carinfo = car_soup.find_all("div", attrs={"class": "full-side"})
        #Car Detail info
        #car main info
        carmain = etree.HTML(str(car_soup))
        carmark = carmain.xpath('//*[@id="dle-speedbar"]/span[2]/a/span')[0].text
        carmodel = carmain.xpath('//*[@id="dle-speedbar"]/span[3]/a/span')[0].text
        #Car description
        carinfo = str(carinfo)
        carprice = carmain.xpath('//*[@id="aside"]/div/div/span')[0].text
        auction = car_soup.find_all(class_="short-story")[0].text
        carstatus = carmain.xpath('//*[@id="aside"]/div/p[1]/img')[0].text
        lotnumber = car_soup.find_all(class_="blackfont")[2].text
        dateofsale = car_soup.find_all(class_="blackfont")[3].text
        year = car_soup.find_all(class_="blackfont")[4].text
        vincode = car_soup.find_all(class_="blackfont")[5].text
        condition = car_soup.find_all(class_="blackfont")[6].text
        engine = car_soup.find_all(class_="blackfont")[7].text
        mileage = car_soup.find_all(class_="blackfont")[8].text
        documents =car_soup.find_all(class_="blackfont")[10].text
        location =car_soup.find_all(class_="blackfont")[11].text
        primarydamage =car_soup.find_all(class_="blackfont")[12].text
        secondarydamge =car_soup.find_all(class_="blackfont")[13].text
        estimatedretailcost=car_soup.find_all(class_="blackfont")[14].text
        estimatedrepaircost =car_soup.find_all(class_="blackfont")[15].text
        transmission =car_soup.find_all(class_="blackfont")[16].text
        bodycolor =car_soup.find_all(class_="blackfont")[17].text
        drive =car_soup.find_all(class_="blackfont")[18].text
        fuel =car_soup.find_all(class_="blackfont")[19].text
        keys =car_soup.find_all(class_="blackfont")[20].text
        try:
            notes =car_soup.find_all(class_="blackfont")[21].text
        except:
            print(next)
        #Car Mark
        if carmark =="Alfa romeo":
            carmark ="8"
        if carmark =="Aston martin":
            carmark="9"
        #Car Model
        #Alfa Romeo
        if carmodel == "4c":
            carmodel = "21"
        if carmodel == "Giulia":
            carmodel = "22"
        if carmodel =="Stelvio":
            carmodel = "23"
        if carmodel =="Veloce":
            carmodel ="24"
        #Aston Martin
        if carmodel =="Db9":
            carmodel ="25"
        if carmodel =="Db11":
            carmodel ="26"
        if carmodel =="Dbx":
            carmodel ="27"
        if carmodel =="Rapide":
            carmodel ="28"
        if carmodel =="V12":
            carmodel ="29"
        if carmodel =="V8":
            carmodel ="30"
        if carmodel =="V8 vantage":
            carmodel ="31"
        if carmodel =="Vanquish":
            carmodel ="32"
        if carmodel =="Vantage":
            carmodel ="33"
        if carmodel =="Virage":
            carmodel ="34"
        #Audi
        img = car_soup.find("meta", property="og:image")
        imgurl = str(img["content"])
        imgs = imgurl.find(".jpg")
        imgurl = imgurl[:(imgs-1)]
        imgx = range(1,11)
        for n in imgx:
            try:
                imgurl = str(imgurl)
                n = str(n)
                imgurlget = imgurl+n+'.jpg'
                print(imgurlget)
                img_data = requests.get(imgurlget).content
                with open(vincode+'-'+n+'.jpg', 'wb') as handler:
                    time.sleep(2)
                    handler.write(img_data)
                n = int(n)
                print(n)
            except:
                print('დასრულდა')
        #sql
        #datas = [user_id,invoice_id,name,tel,carmark, carmodel,category_id,location_id, carprice, auction, lotnumber, dateofsale,year,vincode, condition, engine,mileage,documents,location,primarydamage,secondarydamge,estimatedrepaircost,transmission,bodycolor,drive,fuel,keys,notes,count_view,created_at,updated_at]
        #with open('car.csv', 'a', encoding='UTF8', newline='') as f:
        #    writer = csv.writer(f)
        #    writer.writerow(datas)
        print(id)
        db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                             user="root",  # your username
                             passwd="",  # your password
                             db="caibid")  # name of the data base

        cur = db.cursor()
        insert_stmt = (
            "INSERT INTO cars(id,brand_id, model_id,name,carprice,auction,lotnumber,dateofsale,year,vincode,engine,mileage,documents,location,primarydamage,secondarydamge,estimatedretailcost,estimatedrepaircost,transmission,bodycolor,drive,fuel,notes)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        )
        data = (id,carmark, carmodel,title,carprice,auction,lotnumber,dateofsale,year,vincode,engine,mileage,documents,location,primarydamage,secondarydamge,estimatedretailcost,estimatedrepaircost,transmission,bodycolor,drive,fuel,notes)
        imageable_type="App\Models\Car"
        photo1 = vincode+'-'+'1'+'.jpg'
        photo2 = vincode + '-' + '2' + '.jpg'
        photo3 = vincode + '-' + '3' + '.jpg'
        photo4 = vincode + '-' + '4' + '.jpg'
        photo5 = vincode + '-' + '5' + '.jpg'
        photo6 = vincode + '-' + '6' + '.jpg'
        photo7 = vincode + '-' + '7' + '.jpg'
        photo8 = vincode + '-' + '8' + '.jpg'
        photo9 = vincode + '-' + '9' + '.jpg'
        photo10 = vincode + '-' + '10' + '.jpg'
        insert_stmt1 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data1 = (photo1,imageable_type,id)
        insert_stmt2 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data2 = (photo2, imageable_type, id)
        insert_stmt3 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data3 = (photo3, imageable_type, id)
        insert_stmt4 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data4 = (photo4, imageable_type, id)
        insert_stmt5 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data5 = (photo5, imageable_type, id)
        insert_stmt6 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data6 = (photo6, imageable_type, id)
        insert_stmt7 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data7 = (photo7, imageable_type, id)
        insert_stmt8 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data8 = (photo8, imageable_type, id)
        insert_stmt9 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data9 = (photo9, imageable_type, id)
        insert_stmt10 = (
            "INSERT INTO images(url,imageable_type,imageable_id)"
            "VALUES (%s,%s,%s)"
        )
        data10 = (photo10, imageable_type, id)

        try:
            # Executing the SQL command
            cur.execute(insert_stmt, data)
            cur.execute(insert_stmt1, data1)
            cur.execute(insert_stmt2, data2)
            cur.execute(insert_stmt3, data3)
            cur.execute(insert_stmt4, data4)
            cur.execute(insert_stmt5, data5)
            cur.execute(insert_stmt6, data6)
            cur.execute(insert_stmt7, data7)
            cur.execute(insert_stmt8, data8)
            cur.execute(insert_stmt9, data9)
            cur.execute(insert_stmt10, data10)

            # Commit your changes in the database
            db.commit()

        except:
            # Rolling back in case of error
            db.rollback()

        print("Data inserted")
        # Closing the connection
        db.close()


