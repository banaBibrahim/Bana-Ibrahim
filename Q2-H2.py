import cv2

def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)
    count = 0

    while True:
        success, image = vidObj.read()
        if not success:
            break

        cv2.imwrite("frame%d.jpg" % count, image)
        count += 1

        # اختياري: طباعة قيمة success
        print('تم قراءة إطار جديد:', success)

    vidObj.release()

if __name__ == '__main__':
    video_path = "C:\\Users\\BANA.IB\\Desktop\\Bana Documents\\Short-Video-Maker_Lead.mp4"
    FrameCapture(video_path)




