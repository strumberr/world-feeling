from flask import Flask, render_template, request # Import Flask Class
app = Flask(__name__) # Create an Instance
#from function import good_neutral_bad
import time
from flask import request
from flask import jsonify
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


tz_Madrid = pytz.timezone('Europe/Madrid')
datetime_Madrid = datetime.now(tz_Madrid)
datetime_madrid = datetime_Madrid.strftime("%H:%M:%S")
date_today = str(date.today())


@app.route('/', methods=["GET", "POST"]) # Route the Function
def main(): # Run the function
  if request.method == "GET":
	  return render_template("index.html", result="How are you feeling?")
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

    elif "bad" in request.form.keys():
      f = open("feelings.txt", "a")
      bad2 = "bad \n"
      f.write(bad2)
      f.close()
      f = open("feelings_time.txt", "a")
      bad2 = date_today + " - " + datetime_madrid + " - bad \n"
      f.write(bad2)
      f.close()

    elif "neutral" in request.form.keys():
      f = open("feelings.txt", "a")
      neutral2 = "neutral \n"
      f.write(neutral2)
      f.close()
      f = open("feelings_time.txt", "a")
      neutral2 = date_today + " - " + datetime_madrid + " - neutral \n"
      f.write(neutral2)
      f.close()

    # Pass that input to the bot and get a result

    # result = good_neutral_bad(input)

    
    # render the index.html template but this time with result
    # which can be access in the template
    return render_template("feeling.html")





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


    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Good', 'Neutral', 'Bad'
    sizes = [good_degrees, neutral_degrees, bad_degrees]
    explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    print("Refreshing Graph...")


    return plt.savefig('static/plot.jpg', format="jpg", dpi=72)
  except:
    pass





sched = BackgroundScheduler(daemon=True)
sched.add_job(good_neutral_bad,'interval',seconds=5)
sched.start()

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)