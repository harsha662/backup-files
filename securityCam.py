import cv2
import random
import time
import dropbox
start_time = time.time()

def takeSnapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    number = random.randint(0,100)
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
        return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    access_token = 'k7hFWglJ5JsAAAAAAAAAATK0YUp8s_aoSuhB564d7kVSscn-8uPUxSsq9jXtr5Mu'
    file=img_name
    fileFrom=file
    fileto="/test1/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(fileFrom,'rb') as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.writeMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=1):
            name = takeSnapshot()
            uploadFile(name)
            
main()
