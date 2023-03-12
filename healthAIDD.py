#!/usr/bin/env python
# coding: utf-8

import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') # Face detection engine
smile = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml') # mouth/smile detection

def overlay(gray, frame):
    faces = face.detectMultiScale(gray,scaleFactor=1.08,minNeighbors=6)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,228,121),1)
        
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        
        smiles = smile.detectMultiScale(roi_gray, scaleFactor = 1.8, minNeighbors = 27)
        
        if(len(smiles)!=0):
            for(x_s,y_s,w_s,h_s) in smiles:
                cv2.rectangle(roi_color,(x_s,y_s-50),((x_s+w_s),(y_s+h_s)),(0,255,0),1)
                cv2.putText(roi_color,"Pass",(x_s,y_s-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
        else:
            smiles = smile.detectMultiScale(roi_gray, scaleFactor = 1.55, minNeighbors = 18)
            for(x_s,y_s,w_s,h_s) in smiles:
                cv2.rectangle(roi_color,(x_s,y_s-50),((x_s+w_s),(y_s+h_s)),(0,0,255),1)
                cv2.putText(roi_color,"Attention Required",(x_s,y_s-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
                
        #Using more control flow and detection methods,
        #illness sympomns can be grouped to provide more accuracy
    return frame


vid = cv2.VideoCapture(0)
while(True):
    retval, frame = vid.read()
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    overlayed_frame = overlay(gray_img,frame)
    
    cv2.imshow('healthAIDDSim',overlayed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()





