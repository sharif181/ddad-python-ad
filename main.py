import requests
import json
import cv2
import sqlite3
from Play_list import Playlist

# def readData():
#     readfile = open("data.txt","r")
#     for line in readfile.readlines():
#         print(line)
#     readfile.close()


def storeData(data):
    storeFile = open('data.txt','w')
    for item in data['play_list']:
        storeFile.write(item['primary_src']+'\n')
    storeFile.close()

def playVideo(url):
    cap = cv2.VideoCapture(url)
    while(True):
        ret,frame = cap.read()
        cv2.namedWindow("DDAD",cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("DDAD",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow('DDAD',frame)
        if(cv2.waitKey(20) & 0xFF == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

def saveInDatabase(data):
    for item in data['play_list']:
        playlist = Playlist(item['campaign_id'],item['campaign_title'],item['primary_src'],item['secondary_src'],item['duration'],item['priority'])
        conn = sqlite3.connect('playlist.db')
        c = conn.cursor()
        c.execute(""" CREATE TABLE if not exists plist (
            campaign_id integer,
            campaign_title text,
            primary_src text,
            secondary_src text,
            duration real,
            priority integer
            ) """)
        c.execute("INSERT INTO plist VALUES ('{}','{}','{}','{}','{}','{}')".format(playlist.getCamId(),playlist.getCamTitle(),playlist.getPrimarySrc(),playlist.getSecondarySrc(),playlist.getDuration(),playlist.getPriority()))
        conn.commit()
        conn.close()

def videUrls():
    conn = sqlite3.connect('playlist.db')
    c = conn.cursor()
    c.execute("SELECT * FROM plist")
    return c.fetchall()

def main():
    # r = requests.get('http://dev.ddad-bd.com/api/campaigns/index/123456')
    # data = r.json()
    # saveInDatabase(data)

    # Play video using Text files urls
    # storeData(data)
    # urls = open('data.txt','r')
    # for url in urls.readlines():
    #     url = str.rstrip(url)
    #     playVideo(url)

    
    #playing videos using SqlitDB
    temp = videUrls()
    for t in temp:
        url = t[2]
        playVideo(url)


if __name__ =="__main__":
    main()
 

