import discord
import datetime
import os
from discord.ext import tasks
import pandas as pd
from tabulate import tabulate
from keep_alive import keep_alive

"""
Variables for discord server - Modify as needed:
    send_to_channel: The channel ID to send the message
    role_tag_id: The ID of the role to tag in the message put into <>, can be replaced with any string if you want
"""
send_to_channel = 0
role_tag_id = ""




def create_f1_norm(fp1_t, fp2_t, fp3_t, q_t, r_t, racedate, name):
    """
    Input times for each session as tuples (HH,MM)
    Input racedate as tuple (YYYY, MM, DD)
    Input name as string
    Returns DataFrame with cols: Session, Day, Time, Date, Name
    """
    return pd.DataFrame(data = {'Session': ['FP1', 'FP2', 'FP3', 'Qualifying', 'Race'], \
                                  'Day': ['Friday', 'Friday', 'Saturday', 'Saturday', 'Sunday'], \
                                      'Time': [datetime.time(fp1_t[0],fp1_t[1]), datetime.time(fp2_t[0],fp2_t[1]), datetime.time(fp3_t[0],fp3_t[1]), datetime.time(q_t[0],q_t[1]), datetime.time(r_t[0],r_t[1])], \
                                      'Date': [datetime.date(racedate[0], racedate[1], racedate[2])], \
                                      'Name': [name]})

def create_f1_sprint(fp1_t, q_t, fp2_t, spr_t, r_t, racedate, name):
    """
    Input times for each session as tuples (HH,MM)
    Input racedate as tuple (YYYY, MM, DD)
    Input name as string
    Returns DataFrame with cols: Session, Day, Time, Date, Name
    """
    return pd.DataFrame(data = {'Session': ['FP1', 'Qualifying', 'FP2', 'Sprint', 'Race'], \
                                  'Day': ['Friday', 'Friday', 'Saturday', 'Saturday', 'Sunday'], \
                                      'Time': [datetime.time(fp1_t[0],fp1_t[1]), datetime.time(q_t[0],q_t[1]), datetime.time(fp2_t[0],fp2_t[1]), datetime.time(spr_t[0],spr_t[1]), datetime.time(r_t[0],r_t[1])], \
                                      'Date': [datetime.date(racedate[0], racedate[1], racedate[2])], \
                                      'Name': [name]})
    
def create_f2(fp_t, q_t, sr1_t, sr2_t, fr_t, racedate, name):
    """
    Input times for each session as tuples (HH,MM)
    Input racedate as tuple (YYYY, MM, DD)
    Input name as string
    Returns DataFrame with cols: Session, Day, Time, Date, Name
    """
    return pd.DataFrame(data = {'Session': ['Practice', 'Qualifying', 'Sprint Race 1', 'Sprint Race 2', 'Feature Race'], \
                               'Day': ['Friday', 'Friday', 'Saturday', 'Saturday', 'Sunday'], \
                               'Time': [datetime.time(fp_t[0], fp_t[1]), datetime.time(q_t[0], q_t[1]), datetime.time(sr1_t[0], sr1_t[1]), datetime.time(sr2_t[0], sr2_t[1]), datetime.time(fr_t[0], fr_t[1])], \
                                      'Date': [datetime.date(racedate[0], racedate[1], racedate[2])], \
                                      'Name': [name]})

def create_indy (q_t, r_t, racedate, name):
    """
    Input times for each session as tuples (HH,MM)
    Input racedate as tuple (YYYY, MM, DD)
    Input name as string
    Returns DataFrame with cols: Session, Day, Time, Date, Name
    """
    return pd.DataFrame(data = {'Session': ["Qualifying", "Race"], \
                                'Day': ["Saturday", "Sunday"], \
                                'Time': [datetime.time(q_t[0], q_t[1]), datetime.time(r_t[0], r_t[1])], \
                                      'Date': [datetime.date(racedate[0], racedate[1], racedate[2])], \
                                      'Name': [name]})
        
def create_indy500_q (q1_t, q2_t, q3_t, racedate, name):
    """
    Input times for each session as tuples (HH,MM)
    Input racedate as tuple (YYYY, MM, DD)
    Input name as string
    Returns DataFrame with cols: Session, Day, Time, Date, Name
    """
    return pd.DataFrame(data = {'Session': ["Qualifying", "Qualifying - Last Row", "Qualifying - Fast 9"], \
                                'Day': ["Saturday", "Sunday", "Sunday"], \
                                'Time': [datetime.time(q1_t[0], q1_t[1]), datetime.time(q2_t[0], q2_t[1]), datetime.time(q3_t[0], q3_t[1])], \
                                      'Date': [datetime.date(racedate[0], racedate[1], racedate[2])], \
                                      'Name': [name]})

def create_indy500_r (r_t, racedate, name):
    """
    Input times for each session as tuples (HH,MM)
    Input racedate as tuple (YYYY, MM, DD)
    Input name as string
    Returns DataFrame with cols: Session, Day, Time, Date, Name
    """
    return pd.DataFrame(data = {'Session': ["Indianapolis 500 - Race"], \
                                'Day': ["Sunday"], \
                                'Time': [datetime.time(r_t[0], r_t[1])], \
                                      'Date': [datetime.date(racedate[0], racedate[1], racedate[2])], \
                                      'Name': [name]})


def create_dtm(q1_t, r1_t, q2_t, r2_t, racedate, name):
    """
    Input times for each session as tuples (HH,MM)
    Input racedate as tuple (YYYY, MM, DD)
    Input name as string
    Returns DataFrame with cols: Session, Day, Time, Date, Name
    """
    return pd.DataFrame(data = {'Session': ["Qualifying 1", "Qualifying 2", "Race 1", "Race 2"], \
                                'Day': ["Saturday", "Saturday", "Sunday", "Sunday"], \
                                'Time': [datetime.time(q1_t[0], q1_t[1]), datetime.time(r1_t[0], r1_t[1]), datetime.time(q2_t[0], q2_t[1]), datetime.time(r2_t[0], r2_t[1])], \
                                      'Date': [datetime.date(racedate[0], racedate[1], racedate[2])], \
                                      'Name': [name]})



f1_sessions_bah = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,3,20), "Bahrain")
f1_sessions_sau = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,3,27), "Saudi Arabia")
f1_sessions_aus = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,4,10), "Australia")
f1_sessions_emr = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,4,24), "Formula 1 Pirelli Gran Premio del Made in Italy e dell'Emilia Romagna 2022")
f1_sessions_mia = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,5,8), "Miami")
f1_sessions_spa = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,5,22), "Spain")
f1_sessions_mon = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,5,29), "Monaco")
f1_sessions_aze = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,6,12), "Azerbaijan")
f1_sessions_can = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,6,19), "Canada")
f1_sessions_bri = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,7,3), "Great Britain")
f1_sessions_atr = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,7,10), "Austria")
f1_sessions_fre = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,7,24), "France")
f1_sessions_hun = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,7,31), "Hungary")
f1_sessions_bel = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,8,28), "Belgium")
f1_sessions_ned = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,9,4), "Netherlands")
f1_sessions_ita = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,9,11), "Italy 2: Judgement day")
f1_sessions_rus = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,9,25), "Russia")
f1_sessions_sin = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,10,2), "Singapore")
f1_sessions_jap = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,10,9), "Japan")
f1_sessions_usa = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,10,23), "USA 2: This time it's personal")
f1_sessions_mex = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,10,30), "Mexico")
f1_sessions_bra = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,11,13), "Brazil")
f1_sessions_abu = create_f1_norm((00,00), (00,00), (00,00), (00,00), (00,00), (2022,11,20), "Abu Dhabi")
f1_season = [f1_sessions_bah, f1_sessions_sau, f1_sessions_aus, f1_sessions_emr, f1_sessions_mia, f1_sessions_spa, f1_sessions_mon, f1_sessions_aze, f1_sessions_can, f1_sessions_bri, f1_sessions_atr, f1_sessions_fre, f1_sessions_hun, f1_sessions_bel, f1_sessions_ned, f1_sessions_ita, f1_sessions_rus, f1_sessions_sin, f1_sessions_jap, f1_sessions_usa, f1_sessions_mex, f1_sessions_bra, f1_sessions_abu]

f2_sessions_bah = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 3, 19), "Bahrain")
f2_sessions_sau = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 3, 26), "Saudi Arabia")
f2_sessions_imo = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 4, 23), "Imola")
f2_sessions_spa = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 5, 21), "Spain")
f2_sessions_mon = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 5, 28), "Monaco")
f2_sessions_aze = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 6, 11), "Azerbaijan")
f2_sessions_bri = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 7, 2), "Britain")
f2_sessions_aut = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 7, 9), "Austria")
f2_sessions_hun = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 7, 30), "Hungary")
f2_sessions_bel = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 8, 27), "Belgium")
f2_sessions_ned = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 9, 3), "Netherlands")
f2_sessions_ita = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 9, 10), "Italy")
f2_sessions_rus = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 9, 24), "Russia")
f2_sessions_abu = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 11, 19), "Abu Dhabi")
f2_season = [f2_sessions_bah, f2_sessions_sau, f2_sessions_imo, f2_sessions_spa, f2_sessions_mon, f2_sessions_aze, f2_sessions_bri, f2_sessions_aut, f2_sessions_hun, f2_sessions_bel, f2_sessions_ned, f2_sessions_ita, f2_sessions_rus, f2_sessions_abu]
                               
f3_sessions_bah = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 3, 19), "Bahrain")
f3_sessions_imo = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 4, 23), "Imola")
f3_sessions_spa = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 5, 21), "Spain")
f3_sessions_bri = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 7, 2), "Britain")
f3_sessions_aut = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 7, 9), "Austria")
f3_sessions_hun = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 7, 30), "Hungary")
f3_sessions_bel = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 8, 27), "Belgium")
f3_sessions_ned = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 9, 3), "Netherlands")
f3_sessions_ita = create_f2((0,0), (0,0), (0,0), (0,0), (0,0), (2022, 9, 10), "Italy")
f3_season = [f3_sessions_bah, f3_sessions_imo, f3_sessions_spa, f3_sessions_bri, f3_sessions_aut, f3_sessions_hun, f3_sessions_bel, f3_sessions_ned, f3_sessions_ita]

indy_sessions_stp = create_indy((0,0), (0,0), (2022, 2, 27), "St Petersburg")
indy_sessions_tx = create_indy((0,0), (0,0), (2022, 3, 20), "Texas Motor Speedway")
indy_sessions_lng = create_indy((0,0), (0,0), (2022, 4, 10), "Long Beach")
indy_sessions_bar = create_indy((0,0), (0,0), (2022, 5, 27), "Barber Motorsports Park")
indy_sessions_ims = create_indy((0,0), (0,0), (2022, 5, 27), "Indianapolis Motor Speedway (Road Course)")
indy_sessions_500_q = create_indy500_q((0,0), (0,0), (0,0), (2022, 5, 27), "106th Indy 500 - Qualifying")
indy_sessions_500_r = create_indy500_r((0,0), (2022, 5, 27), "106th Indy 500 - Race")
indy_sessions_bel = create_indy((0,0), (0,0), (2022, 6, 27), "Belle Isle")
indy_sessions_rda = create_indy((0,0), (0,0), (2022, 6, 27), "Road America")
indy_sessions_ohi = create_indy((0,0), (0,0), (2022, 7, 27), "Mid-Ohio")
indy_sessions_tor = create_indy((0,0), (0,0), (2022, 7, 27), "Toronto")
indy_sessions_io1 = create_indy((0,0), (0,0), (2022, 7, 27), "Iowa Speedway Race 1")
indy_sessions_io2 = create_indy((0,0), (0,0), (2022, 7, 27), "Iowa Speedway Race 2")
indy_sessions_ims2 = create_indy((0,0), (0,0), (2022, 7, 27), "Indianapolis Motor Speedway (Road Course)")
indy_sessions_nas = create_indy((0,0), (0,0), (2022, 8, 27), "Nashville")
indy_sessions_wwt = create_indy((0,0), (0,0), (2022, 8, 27), "World Wide Technology Raceway")
indy_sessions_por = create_indy((0,0), (0,0), (2022, 9, 27), "Portland International Raceway")
indy_sessions_lgs = create_indy((0,0), (0,0), (2022, 9, 27), "Laguna Seca")
indy_season = [indy_sessions_stp, indy_sessions_tx, indy_sessions_lng, indy_sessions_bar, indy_sessions_ims, indy_sessions_500_q, indy_sessions_500_r, indy_sessions_bel, indy_sessions_rda, indy_sessions_ohi, indy_sessions_tor, indy_sessions_io1, indy_sessions_io2, indy_sessions_ims2, indy_sessions_nas, indy_sessions_wwt, indy_sessions_por, indy_sessions_lgs]

dtm_sessions_por = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 5, 1, "Portimao"))
dtm_sessions_lau = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 5, 22, "Lausitzring"))
dtm_sessions_tba = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 6, 5, "TBA"))
dtm_sessions_imo = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 6, 19, "Imola"))
dtm_sessions_nor = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 7, 3, "Norisring"))
dtm_sessions_nur = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 8, 28, "Nurburgring"))
dtm_sessions_spa = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 9, 11, "Spa Francorchamps"))
dtm_sessions_rbr = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 9, 25, "Red Bull Ring"))
dtm_sessions_hoc = create_dtm((0,0), (0,0), (0,0), (0,0), (2022, 10, 9, "Hockenheimring"))
dtm_season = [dtm_sessions_por, dtm_sessions_lau, dtm_sessions_tba, dtm_sessions_imo, dtm_sessions_nor, dtm_sessions_nur, dtm_sessions_spa, dtm_sessions_rbr, dtm_sessions_hoc]

f1_rounds = pd.DataFrame(data = {'Round': [], \
                                 'raceDate': [], \
                                 'Sessions': []})
f2_rounds = pd.DataFrame(data = {'Round': [], \
                                 'raceDate': [], \
                                 'Sessions': []})
f3_rounds = pd.DataFrame(data = {'Round': [], \
                                 'raceDate': [], \
                                 'Sessions': []})
indy_rounds = pd.DataFrame(data = {'Round': [], \
                                 'raceDate': [], \
                                 'Sessions': []})
dtm_rounds = pd.DataFrame(data = {'Round': [], \
                                 'raceDate': [], \
                                 'Sessions': []})
for i in f1_season:
    f1_rounds = f1_rounds.append({'Round': i["Name"][0],
                    'raceDate': i["Date"][0],
                    'Sessions': i.drop(columns = ["Name", "Date"])}, ignore_index=True)
for i in f2_season:
    f2_rounds = f2_rounds.append({'Round': i["Name"][0],
                    'raceDate': i["Date"][0],
                    'Sessions': i.drop(columns = ["Name", "Date"])}, ignore_index=True)
for i in f3_season:
    f3_rounds = f3_rounds.append({'Round': i["Name"][0],
                    'raceDate': i["Date"][0],
                    'Sessions': i.drop(columns = ["Name", "Date"])}, ignore_index=True)
for i in indy_season:
    indy_rounds = indy_rounds.append({'Round': i["Name"][0],
                    'raceDate': i["Date"][0],
                    'Sessions': i.drop(columns = ["Name", "Date"])}, ignore_index=True)
for i in dtm_season:
    dtm_rounds = dtm_rounds.append({'Round': i["Name"][0],
                    'raceDate': i["Date"][0],
                    'Sessions': i.drop(columns = ["Name", "Date"])}, ignore_index=True)
    
def run(date):
  print("foo")
  if date.weekday() == 3 and datetime.datetime.now().hour == 0:
    print("bar")
    f1_this_week = f1_rounds[date <= f1_rounds["raceDate"]]
    f1_this_week = f1_this_week[f1_this_week["raceDate"] <= date + datetime.timedelta(days=7)]
    f1_this_week = f1_this_week.assign(Series = "F1")
    
    f2_this_week = f2_rounds[date <= f2_rounds["raceDate"]]
    f2_this_week = f2_this_week[f2_this_week["raceDate"] <= date + datetime.timedelta(days=7)]
    f2_this_week = f2_this_week.assign(Series = "F2")
    
    f3_this_week = f3_rounds[date <= f3_rounds["raceDate"]]
    f3_this_week = f3_this_week[f3_this_week["raceDate"] <= date + datetime.timedelta(days=7)]
    f3_this_week = f3_this_week.assign(Series = "F3")
    
    indy_this_week = indy_rounds[date <= indy_rounds["raceDate"]]
    indy_this_week = indy_this_week[indy_this_week["raceDate"] <= date + datetime.timedelta(days=7)]
    indy_this_week = indy_this_week.assign(Series = "Indycar")
    
    dtm_this_week = dtm_rounds[date <= dtm_rounds["raceDate"]]
    dtm_this_week = dtm_this_week[dtm_this_week["raceDate"] <= date + datetime.timedelta(days=7)]
    dtm_this_week = dtm_this_week.assign(Series = "DTM")
    
    racing = f1_this_week.append(f2_this_week, ignore_index=True).append(f3_this_week, ignore_index=True).append(indy_this_week, ignore_index=True).append(dtm_this_week, ignore_index=True)


    s=[]
    if len(racing)>=1:
      s.append("Attention " + role_tag_id + " - Race Schedule for this wekeend: \n") 
      for i in range(len(racing)):
          s.append("Series: " + racing["Series"][i] + "\n")
          s.append("Round: " + racing["Round"][i] + "\n")
          s.append("Timetable: \n```" + tabulate(racing["Sessions"][i], showindex=False, tablefmt="fancy_grid", headers="keys") + "```\n")
    else:
      s.append("No races this week :(")
            
    return(s)
  else:
    return([""])



client = discord.Client()
@tasks.loop(hours=1)
async def test():
  msg = run(datetime.date.today())
  if msg != [""]:
    channel = client.get_channel(send_to_channel)
    for i in msg:
      await channel.send(i)

@client.event
async def on_ready():
    test.start()


keep_alive()
client.run(os.getenv('TOKEN'))
