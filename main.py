import requests
import json
import cv2

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


r = requests.get('http://dev.ddad-bd.com/api/campaigns/index/123456')
data = r.json()

storeData(data)
# readData()

def playVideo(url):
    cap = cv2.VideoCapture(url)
    cap.set(3,640)
    cap.set(4,480)
    while(True):
        ret,frame = cap.read()
        cv2.imshow('DDAD',frame)
        if(cv2.waitKey(20) & 0xFF == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()



urls = open('data.txt','r')
for url in urls.readlines():
    url = str.rstrip(url)
    playVideo(url)


