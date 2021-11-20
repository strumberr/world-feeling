from flask import Flask, render_template, request # Import Flask Class
app = Flask(__name__) # Create an Instance
#from function import good_neutral_bad
import time
import requests
import json
from flask import abort, request, jsonify
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
mpl.rc('figure', max_open_warning = 0)
import os
from datetime import datetime
import pytz
from datetime import date
import time
from datetime import date
from datetime import datetime
import sqlite3
con = sqlite3.connect('database.db', check_same_thread=False)



def create_db(IP, Location, Day, Time, Feeling):
    with con:
        cur = con.cursor()

        cur.execute("INSERT INTO alldata VALUES (?, ?, ?, ?, ?);", (IP, Location, Day, Time, Feeling))

        ## call commit on the connection...
        con.commit()








now = datetime.now()
datetime_madrid2 = now.strftime("%H:%M:%S")
datetime_madrid = datetime_madrid2
print(datetime_madrid)

date_today2 = date.today()
date_today = str(date_today2)






@app.route('/', methods=["GET", "POST"]) # Route the Function
def main(): # Run the function
  if request.method == "GET":

    good_neutral_bad()
    cur = con.cursor()
    last_row2 = cur.execute('select Location, Feeling from alldata').fetchall()[-1]
    last_row1 = list(last_row2)
    last_1 = last_row1[0]
    last_2 = last_row1[1]
    last_row = "Location: " + last_1 + " ... " + "Feeling: " + last_2

    return render_template("index.html", lastentry = last_row)
  else:
    # get the input from the template that the user submitted
    if "good" in request.form.keys():
      f = open("feelings.txt", "a")
      good2 = "good \n"
      f.write(good2)
      f.close()
      f = open("feelings_time.txt", "a")
      good2 = date_today + " - " + datetime_madrid + " - good \n"
      f.write(good2)
      f.close()


      if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = (request.environ['REMOTE_ADDR'])
        print(ip)
        f = open("ipaddress.txt", "a")
        ipaddress = ip + "\n"
        f.write(ipaddress)
        f.close()
      else:
        ip1 = (request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy
        print(ip1)
        f = open("ipaddress.txt", "a")
        ipaddress = ip1 + "\n"
        f.write(ipaddress)
        f.close()

        ip_address = ip1

        # URL to send the request to
        request_url = 'https://geolocation-db.com/jsonp/' + ip_address
        # Send request and decode the result
        response = requests.get(request_url)
        result = response.content.decode()
        # Clean the returned string so it just contains the dictionary data for the IP address
        result = result.split("(")[1].strip(")")
        # Convert this data into a dictionary
        result  = json.loads(result)
        result2 = json.dumps(result)
        result3 = result2.split()
        print(result3[3])
        f = open("alldata.txt", "a")
        ipaddress = "IP = " + ip1 + " -- Location = " + result3[3] + " -- Day = " + date_today + " -- Time = " + datetime_madrid + " -- Feeling = good" + "\n"
        f.write(ipaddress)
        f.close()
      location2 = str(result3[3].replace('"', ''))
      location = location2.replace(',', '')
      create_db(ip1, location, date_today, datetime_madrid, "good")

      






      


    elif "bad" in request.form.keys():
      f = open("feelings.txt", "a")
      bad2 = "bad \n"
      f.write(bad2)
      f.close()
      f = open("feelings_time.txt", "a")
      bad2 = date_today + " - " + datetime_madrid + " - bad \n"
      f.write(bad2)
      f.close()


      if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = (request.environ['REMOTE_ADDR'])
        print(ip)
        f = open("ipaddress.txt", "a")
        ipaddress = ip + "\n"
        f.write(ipaddress)
        f.close()
      else:
        ip1 = (request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy
        print(ip1)
        f = open("ipaddress.txt", "a")
        ipaddress = ip1 + "\n"
        f.write(ipaddress)
        f.close()

        ip_address = ip1

        # URL to send the request to
        request_url = 'https://geolocation-db.com/jsonp/' + ip_address
        # Send request and decode the result
        response = requests.get(request_url)
        result = response.content.decode()
        # Clean the returned string so it just contains the dictionary data for the IP address
        result = result.split("(")[1].strip(")")
        # Convert this data into a dictionary
        result  = json.loads(result)
        result2 = json.dumps(result)
        result3 = result2.split()
        print(result3[3])
        f = open("alldata.txt", "a")
        ipaddress = "IP = " + ip1 + " -- Location = " + result3[3] + " -- Day = " + date_today + " -- Time = " + datetime_madrid + " -- Feeling = bad" + "\n"
        f.write(ipaddress)
        f.close()
      location2 = str(result3[3].replace('"', ''))
      location = location2.replace(',', '')
      create_db(ip1, location, date_today, datetime_madrid, "bad")







    elif "neutral" in request.form.keys():
      f = open("feelings.txt", "a")
      neutral2 = "neutral \n"
      f.write(neutral2)
      f.close()
      f = open("feelings_time.txt", "a")
      neutral2 = date_today + " - " + datetime_madrid + " - neutral \n"
      f.write(neutral2)
      f.close()


      if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = (request.environ['REMOTE_ADDR'])
        print(ip)
        f = open("ipaddress.txt", "a")
        ipaddress = ip + "\n"
        f.write(ipaddress)
        f.close()
      else:
        ip1 = (request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy
        print(ip1)
        f = open("ipaddress.txt", "a")
        ipaddress = ip1 + "\n"
        f.write(ipaddress)
        f.close()

        ip_address = ip1

        # URL to send the request to
        request_url = 'https://geolocation-db.com/jsonp/' + ip_address
        # Send request and decode the result
        response = requests.get(request_url)
        result = response.content.decode()
        # Clean the returned string so it just contains the dictionary data for the IP address
        result = result.split("(")[1].strip(")")
        # Convert this data into a dictionary
        result  = json.loads(result)
        result2 = json.dumps(result)
        result3 = result2.split()
        print(result3[3])
        f = open("alldata.txt", "a")
        ipaddress = "IP = " + ip1 + " -- Location = " + result3[3] + " -- Day = " + date_today + " -- Time = " + datetime_madrid + " -- Feeling = neutral" + "\n"
        f.write(ipaddress)
        f.close()
      location2 = str(result3[3].replace('"', ''))
      location = location2.replace(',', '')
      create_db(ip1, location, date_today, datetime_madrid, "neutral")




  
    
    # render the index.html template but this time with result
    # which can be access in the template
    good_neutral_bad()
    cur = con.cursor()
    last_row2 = cur.execute('select Location, Feeling from alldata').fetchall()[-1]
    last_row1 = list(last_row2)
    last_1 = last_row1[0]
    last_2 = last_row1[1]
    last_row = "Location: " + last_1 + " ... " + "Feeling: " + last_2
    return render_template("feeling.html", lastentry = last_row)


@app.route("/backhome")
def back_home():
  return render_template('index.html')



@app.route('/contact', methods=["GET", "POST"])
def contact_form():
  
    name = request.form.get("name")
    f = open("contact.txt", "a")
    name2 = "NAME - " + str(name) + "\n"
    f.write(name2)
    f.close()

    email = request.form.get("email")
    f = open("contact.txt", "a")
    email2 = "EMAIL - " + str(email) + "\n"
    f.write(email2)
    f.close()


    message = request.form.get("message")
    f = open("contact.txt", "a")
    message2 = "MESSAGE - " + str(message) + "\n \n \n"
    f.write(message2)
    f.close()


    if "submit" in request.form.keys():
      return render_template("contactsuccess.html")




    return render_template("contact.html")








def good_neutral_bad():
  try:
    file = open("feelings.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    total = (360 / line_count) 

    file = open("feelings.txt", "r")
    data = file.read()
    occurrences_good = data.count("good")
    occurrences_neutral = data.count("neutral")
    occurrences_bad = data.count("bad")

    good_degrees = occurrences_good * total
    neutral_degrees = occurrences_neutral * total
    bad_degrees = occurrences_bad * total


    colors = ['#AF40FF','#5B42F3','#00DDEB']


    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Good', 'Neutral', 'Bad'
    sizes = [good_degrees, neutral_degrees, bad_degrees]
    explode = (0.02, 0.02, 0.02)  # only "explode" the 2nd slice (i.e. 'Hogs')


    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            startangle=90, colors=colors, textprops={'fontsize': 20})
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    print("Refreshing Graph...")



    return plt.savefig('static/plot.png', format="png", dpi=72)
  except:
    pass



app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)