from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import xml.etree.ElementTree as ET  
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
from selenium.webdriver.support import expected_conditions as EC

# 날씨정보 출력하기
# 충청남도 천안시서북구 부성1동

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
    top.geometry('450x700')
    label1 = Label(top, text='오늘의 날씨 정보', font=('Arial', 20)).pack()
    weather_text = crawl()
    txt = tk.Text(top, height=24, font=('맑은 고딕', 9))
    txt.pack()
    txt.insert(tk.CURRENT, weather_text)
    Button(top, text='닫기', command=top.destroy).pack(pady=10)

# 버스 남은 시간
def open_window1(event):
    global images
    top = Toplevel()
    top.title('버스 남은 시간')
    top.geometry('450x700')
    label1 = Label(top, text='버스 실시간 위치').pack()
    Label(top, image=photo1).pack()
    Button(top, text='닫기', command=top.destroy).pack(pady=10)

# 버스 실시간 위치
def clickImage(event):
    global images
    top = Toplevel()
    top.title('버스 실시간 위치')
    top.geometry('450x700')
    label1 = Label(top, text='버스 실시간 위치').pack()
    Label(top, image=photo2).pack()
    Button(top, text='닫기', command=top.destroy).pack(pady=10)

    
def clickImage3(event):

    service = Service('chromedriver.exe')                       # Chrome 드라이버 서비스 생성
    driver = webdriver.Chrome(service=service)                  # Chrome 웹 드라이버 생성    
    #window = tk.Tk()                                           # Tkinter 윈도우 생성   
    driver.get('https://www.youtube.com/watch?v=AnETRZ2bsB0')   # 웹 페이지 로드
    try:
        # 요소가 로드될 때까지 대기
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.bus_list'))
        )
        element_screenshot = element.screenshot_as_png             # 스크린샷 캡처
        image = ImageTk.PhotoImage(data=element_screenshot)        # 스크린샷을 Tkinter 이미지로 변환

        # 이미지를 Tkinter 레이블에 표시
        #label = tk.Label(window, image=image)
        #label.pack()

    except Exception as e:
        print(f"Error: {e}")

    # Tkinter 윈도우 업데이트
    #window.mainloop()

    driver.quit()


# 네이버 14번 버스 정보 말해주기
# 실시간 화면을 어떻게 보여줘야 하지 //
# 네이버 링크로 연결되는거 말고 ㅋ냅쳐본이라도 보여주고 싶은데
# 실시간 화면 캡쳐-> 사용자 보여주기 -> 초기화

def open_window2(event):                                
    service = Service('chromedriver.exe')                       # Chrome 드라이버 서비스 생성
    driver = webdriver.Chrome(service=service)                  # Chrome 웹 드라이버 생성    
    #window = tk.Tk()                                           # Tkinter 윈도우 생성   
    driver.get('https://map.naver.com/v5/entry/bus-station/368572?c=16,0,0,0,dh')   # 웹 페이지 로드

    try:
        # 요소가 로드될 때까지 대기
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.bus_list'))
        )
        element_screenshot = element.screenshot_as_png             # 스크린샷 캡처
        image = ImageTk.PhotoImage(data=element_screenshot)        # 스크린샷을 Tkinter 이미지로 변환

        # 이미지를 Tkinter 레이블에 표시
        #label = tk.Label(window, image=image)
        #label.pack()

    except Exception as e:
        print(f"Error: {e}")

    # Tkinter 윈도우 업데이트
    #window.mainloop()

    driver.quit()                                                   # 웹 드라이버 종료

def open_window3(event):                                
    service = Service('chromedriver.exe')                       # Chrome 드라이버 서비스 생성
    driver = webdriver.Chrome(service=service)                  # Chrome 웹 드라이버 생성    
    #window = tk.Tk()                                           # Tkinter 윈도우 생성   
    driver.get('https://map.naver.com/v5/entry/bus-route/1400102?c=11,0,0,0,dh')   # 웹 페이지 로드

    try:
        # 요소가 로드될 때까지 대기
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.bus_list'))
        )
        element_screenshot = element.screenshot_as_png             # 스크린샷 캡처
        image = ImageTk.PhotoImage(data=element_screenshot)        # 스크린샷을 Tkinter 이미지로 변환

        # 이미지를 Tkinter 레이블에 표시
        #label = tk.Label(window, image=image)
        #label.pack()

    except Exception as e:
        print(f"Error: {e}")

    # Tkinter 윈도우 업데이트
    #window.mainloop()

    driver.quit()                                                   # 웹 드라이버 종료


# 기본 화면 출력
w = Tk()
w.title("버스정류장 키오스크 첫 화면")
w.geometry("450x700")

# 버스 정보 출력
#label = Label(w, text=' 100번 버스 탑승자리입니다.', foreground='red', font=('Arial', 20), borderwidth=2, relief='solid')
#label.place(x=50, y=0)
image4 = Image.open("C:/Users/Master/Downloads/1. 상단 버스 알림.png")
image4 = image4.resize((450, 50))
photo4 = ImageTk.PhotoImage(image4)
lbl4 = Label(w, image=photo4)
#lbl4.bind("<Button>", open_window)
lbl4.place(x=0, y=0)

# 아이콘 or 사진 정보들


image = Image.open("C:/Users/Master/Downloads/2. 상단 버스 알림.png")
image = image.resize((450, 60))
photo = ImageTk.PhotoImage(image)
lbl = Label(w, image=photo)
lbl.bind("<Button>", open_window)
lbl.place(x=0, y=50)

image1 = Image.open("C:/Users/Master/Downloads/3. 버스 도착 예정시간 등.png")          # 이미지 로드
image1 = image1.resize((450, 200))                                  # 이미지 크기 조정
photo1 = ImageTk.PhotoImage(image1)                                 # 이미지를 PhotoImage로 변환
lbl1 = Label(w, image=photo1)                                       # 이미지를 포함한 레이블 생성
lbl1.bind("<Button>", open_window2)
lbl1.place(x=0, y=105)

image2 = Image.open("C:/Users/Master/Downloads/4. 버스 실시간 위치 지도.png")
image2 = image2.resize((450, 200))
photo2 = ImageTk.PhotoImage(image2)

lbl2 = Label(w, image=photo2)
lbl2.bind("<Button>", open_window3)
lbl2.place(x=0, y=300)
image3 = Image.open("C:/Users/Master/Downloads/5. 광고.png")           # 영상대신 이미지로 넣어두기!
image3 = image3.resize((450, 200))
photo3 = ImageTk.PhotoImage(image3)

lbl3 = Label(w, image=photo3)
lbl3.bind("<Button>", clickImage3)
lbl3.place(x=0, y=500)

# 창 크기 고정
#w.geometry('700x1000')

mainloop()
