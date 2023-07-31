from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import xml.etree.ElementTree as ET  
from datetime import datetime, timedelta
import urllib.request

# 날씨정보 출력하기
#충청남도 천안시서북구 부성1동

def crawl():
    r = urllib.request.urlopen("https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4413358000")
    xml_text = r.read().decode()
    xml_root = ET.fromstring(xml_text)
    announce_time = datetime.strptime(xml_root.find('.//tm').text, '%Y%m%d%H%M')
    result = xml_root.find('.//item/category').text + '\n'
    result += f"발표: {announce_time.strftime('%Y-%m-%d-%H:%M')}" + "\n"
    for each in xml_root.findall('.//data'):
        forecast_data = announce_time + timedelta(days=int(each.find('day').text))
        result += f"{forecast_data.strftime('%d')}일 "\
                  f"{each.find('hour').text:>02}시, "\
                  f"{float(each.find('temp').text):.1f}°C, "\
                  f"{each.find('wfKor').text}, "\
                  f"강수확률: {each.find('pop').text}%, "\
                  f"습도: {each.find('reh').text}%, "\
                  f"풍속: {float(each.find('ws').text):.1f}m/s\n"
    return result

# 날씨 알려주는 버튼 

def open_window(event):
    global images
    top = Toplevel()
    top.title('오늘의 날씨')
    top.geometry('600x600')
    label1 = Label(top, text='오늘의 날씨 정보', font=('Arial', 20)).pack()
    weather_text = crawl()
    txt = tk.Text(top, height=24, font=('맑은 고딕', 9))
    txt.pack()
    txt.insert(tk.CURRENT, weather_text)
    Button(top, text='닫기', command=top.destroy).pack(pady=10)

#버스 실시간 위치 출력 버튼
def open_window1(event):
    global images
    top = Toplevel()
    top.title('버스 실시간 위치')
    top.geometry('600x600')
    label1 = Label(top,text='버스 실시간 위치').pack()
    #images = ImageTK.PhotoImage(Image.open('C:/Users/Master/Desktop/zldhtmzm/캡쳐.png'))
    Label(top,image = photo1).pack()
    Button(top, text='닫기', command=top.destroy).pack(pady = 10)
    
#버스 노선 정보 출력 버튼
def open_window2(event):
    global images
    top = Toplevel()
    top.title('버스 노선 정보')
    top.geometry('600x600')
    label1 = Label(top,text='버스 노선 정보').pack()
    #images = ImageTK.PhotoImage(Image.open('C:/Users/Master/Desktop/zldhtmzm/캡쳐.png'))
    Label(top,image = photo2).pack()
    Button(top, text='닫기', command=top.destroy).pack(pady = 10)

def clickImage(event):
    messagebox.showinfo("마우스", "그래 안그래")

# 기본 화면 출력
w = Tk()
w.title("버스정류장 키오스크 첫 화면")
w.geometry("700x1000")

#버스 정보 출력
label = Label(w, text=' 100번 버스 탑승자리입니다.', foreground='red', font=('Arial', 30), borderwidth=2, relief='solid')
label.place(x=0, y=0)

# 아이콘 or 사진 정보들
photo = PhotoImage(file="C:/Users/Master/Desktop/zldhtmzm/11.png")
lbl = Label(w, image=photo)
lbl.bind("<Button>", open_window)
lbl.place(x=600, y=0)

photo1 = PhotoImage(file="C:/Users/Master/Desktop/zldhtmzm/캡쳐1.png")
lbl1 = Label(w, image=photo1)
lbl1.bind("<Button>", open_window1)
lbl1.place(x=0, y=55)

photo2 = PhotoImage(file="C:/Users/Master/Desktop/zldhtmzm/캡쳐.png")
lbl2 = Label(w, image=photo2)
lbl2.bind("<Button>", open_window2)
lbl2.place(x=0, y=255)

photo3 = PhotoImage(file="C:/Users/Master/Desktop/zldhtmzm/캡처3.png")
lbl3 = Label(w, image=photo3)
lbl3.bind("<Button>", clickImage)
lbl3.place(x=0, y=505)

mainloop()
