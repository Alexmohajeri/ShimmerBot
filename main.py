import discord
import datetime
import os
from discord.ext import tasks
import pandas as pd
from tabulate import tabulate
from keep_alive import keep_alive



"""
Bot currently set up for 2021 seasons of F1, F2, F3, DTM and Indycar
"""

"""
Variables for discord server: Modify as needed:
send_to_channel: The channel ID to send the message
role_tag_id: The ID of the role to tag in the message put into <>, can be replaced with any string if you want
"""
send_to_channel = 663485832556052488
role_tag_id = "<@&728611834856341645>"






def create_f1_norm(fp1_t, fp2_t, fp3_t, q_t, r_t):
    """
    Input times for each session as tuples (HH,MM)
    Returns DataFrame with cols: Session, Day, Time
    """
    return pd.DataFrame(data = {'Session': ['FP1', 'FP2', 'FP3', 'Qualifying', 'Race'], \
                                  'Day': ['Friday', 'Friday', 'Saturday', 'Saturday', 'Sunday'], \
                                      'Time': [datetime.time(fp1_t[0],fp1_t[1]), datetime.time(fp2_t[0],fp2_t[1]), datetime.time(fp3_t[0],fp3_t[1]), datetime.time(q_t[0],q_t[1]), datetime.time(r_t[0],r_t[1])]})

def create_f1_sprint(fp1_t, q_t, fp2_t, spr_t, r_t):
    """
    Input times for each session as tuples (HH,MM)
    Returns DataFrame with cols: Session, Day, Time
    """
    return pd.DataFrame(data = {'Session': ['FP1', 'Qualifying', 'FP2', 'Sprint', 'Race'], \
                                  'Day': ['Friday', 'Friday', 'Saturday', 'Saturday', 'Sunday'], \
                                      'Time': [datetime.time(fp1_t[0],fp1_t[1]), datetime.time(q_t[0],q_t[1]), datetime.time(fp2_t[0],fp2_t[1]), datetime.time(spr_t[0],spr_t[1]), datetime.time(r_t[0],r_t[1])]})
    
def create_f2(fp_t, q_t, sr1_t, sr2_t, fr_t):
    """
    Input times for each session as tuples (HH,MM)
    Returns DataFrame with cols: Session, Day, Time
    """
    return pd.DataFrame(data = {'Session': ['Practice', 'Qualifying', 'Sprint Race 1', 'Sprint Race 2', 'Feature Race'], \
                               'Day': ['Friday', 'Friday', 'Saturday', 'Saturday', 'Sunday'], \
                               'Time': [datetime.time(fp_t[0], fp_t[1]), datetime.time(q_t[0], q_t[1]), datetime.time(sr1_t[0], sr1_t[1]), datetime.time(sr2_t[0], sr2_t[1]), datetime.time(fr_t[0], fr_t[1])]})

def create_indy (q_t, r_t):
    """
    Input times for each session as tuples (HH,MM)
    Returns DataFrame with cols: Session, Day, Time
    """
    return pd.DataFrame(data = {'Session': ["Qualifying", "Race"], \
                                'Day': ["Sunday", "Sunday"], \
                                'Time': [datetime.time(q_t[0], q_t[1]), datetime.time(r_t[0], r_t[1])]})
        
def create_dtm(q1_t, r1_t, q2_t, r2_t):
    """
    Input times for each session as tuples (HH,MM)
    Returns DataFrame with cols: Session, Day, Time
    """
    return pd.DataFrame(data = {'Session': ["Qualifying 1", "Qualifying 2", "Race 1", "Race 2"], \
                                'Day': ["Saturday", "Saturday", "Sunday", "Sunday"], \
                                'Time': [datetime.time(q1_t[0], q1_t[1]), datetime.time(r1_t[0], r1_t[1]), datetime.time(q2_t[0], q2_t[1]), datetime.time(r2_t[0], r2_t[1])]})


f1_sessions_rus = create_f1_norm((9,30), (13,00), (10,00), (13,00), (13,00))    
f1_sessions_tur = create_f1_norm((10,30), (14,00), (11,00), (14,00), (14,00))    
f1_sessions_usa = create_f1_norm((17,30), (21,00), (19,00), (22,00), (20,00))    
f1_sessions_mex = create_f1_norm((17,30), (21,00), (17,00), (20,00), (19,00))    
f1_sessions_bra = create_f1_sprint((15,30), (19,00), (15,00), (17,30), (17,00))    
f1_sessions_sau = create_f1_norm((13,30), (17,00), (14,00), (17,00), (17,30))    
f1_sessions_abu = create_f1_norm((9,30), (13,00), (10,00), (13,00), (13,00))


f2_sessions_rus = create_f2((10,0), (16,25), (10,30), (16,45), (11,20))
f2_sessions_sau = create_f2((13,45), (18,20), (15,30), (21,40), (17,25))
f2_sessions_abu = pd.DataFrame(data = {'Session': ['Practice', 'Qualifying', 'Sprint Race 1', 'Sprint Race 2', 'Feature Race'], \
                               'Day': ['Friday', 'Friday', 'Saturday', 'Saturday', 'Sunday'], \
                               'Time': ["TBC", "TBC", "TBC", "TBC", "TBC"]})

                               
f3_sessions_rus = create_f2((8,55), (13,00), (8,35), (13,40), (9,55))


indy_sessions_ls = create_indy((20,0), (22,0))
indy_sessions_lb = create_indy((20,0), (20,0))


dtm_sessions_assen = create_dtm((9,15), (12,30), (9,0), (12,30))
dtm_sessions_hockenheim = create_dtm((9,15), (12,30), (9,0), (12,30))
dtm_sessions_norisring = create_dtm((9,15), (12,30), (9,0), (12,30))

f1_rounds = pd.DataFrame(data = {'Round': ["Russia", "Turkey", "USA", "Mexico", "Brazil", "Saudi Arabia", "Abu Dhabi"], \
                                 'raceDate': [datetime.date(2021, 9, 26), datetime.date(2021, 10, 10), datetime.date(2021, 10, 24), datetime.date(2021, 11, 7), datetime.date(2021, 11, 14), datetime.date(2021, 12, 5), datetime.date(2021, 12, 12)], \
                                 'Sessions': [f1_sessions_rus, f1_sessions_tur, f1_sessions_usa, f1_sessions_mex, f1_sessions_bra, f1_sessions_sau, f1_sessions_abu]})

f2_rounds = pd.DataFrame(data = {'Round': ["Russia", "Saudi Arabia", "Abu Dhabi"], \
                                 'raceDate': [datetime.date(2021, 9, 26), datetime.date(2021, 12, 5), datetime.date(2021, 12, 12)], \
                                 'Sessions': [f2_sessions_rus, f2_sessions_sau, f2_sessions_abu]})
    
f3_rounds = pd.DataFrame(data = {'Round': ["Russia"], \
                                 'raceDate': [datetime.date(2021, 9, 26)], \
                                 'Sessions': [f3_sessions_rus]})
    
indy_rounds = pd.DataFrame(data = {'Round': ["Laguna Seca", "Long Beach"], \
                                   'raceDate': [datetime.date(2021, 9, 19), datetime.date(2021, 9, 26)], \
                                   'Sessions': [indy_sessions_ls, indy_sessions_lb]})
    
dtm_rounds = pd.DataFrame(data = {'Round': ["Assen", "Hockenheim", "Norisring"], \
                                  'raceDate': [datetime.date(2021, 9, 19), datetime.date(2021, 10, 3), datetime.date(2021, 10, 10)], \
                                  'Sessions': [dtm_sessions_assen, dtm_sessions_hockenheim, dtm_sessions_norisring]})
    
def run(date):
  print("foo")
  if date.weekday() == 2 and datetime.datetime.now().hour == 13:
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
