import cv2,mouse,keyboard,time,PhotoText
from PIL import Image,ImageGrab
import numpy as np

ekran = None
gray = None

def FindAllItemPos(image,gray):
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    return w,h,zip(*loc[::-1])

def GetCordinates(image,gray):
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):

        defx = pt[0] + w / 2
        defy = pt[1] + h / 2
        return defx, defy
def FindCordinates(icon,image,imagetxt,grays):
    ClickOn(icon,grays,1)
    global gray
    getFullScreen()

    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):

        mouse.move(pt[0] + w / 2, pt[1] + h / 2, 1, 0.1)
        time.sleep(0.3)

        getFullScreen()

        if exists(imagetxt,gray):
            defx = pt[0] + w / 2
            defy = pt[1] + h / 2
            return defx,defy



def getFullScreen():
    global ekran, gray
    ekran = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
    gray = cv2.cvtColor(ekran, cv2.COLOR_BGR2GRAY)
def press(button):
    keyboard.press(button)
    time.sleep(0.1)
    keyboard.release(button)
    time.sleep(0.1)
def click(x,y,a=1):
    mouse.move(x, y, 1, 0.1)
    for i in range(a):
        time.sleep(0.1)
        mouse.press('left')
        time.sleep(0.1)
        mouse.release('left')
        time.sleep(0.1)
def clickWtime(x,y,c,a=1):
    mouse.move(x, y, 1, c)
    for i in range(a):
        time.sleep(0.1)
        mouse.press('left')
        time.sleep(0.1)
        mouse.release('left')
        time.sleep(0.1)
def exists(image,gray):
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    a = len(list(zip(*loc[::-1])))
    if (a != 0):
        return True
    elif (a == 0):
        return False

def ClickOn(image,gray,times):
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        click(pt[0] + w / 2,pt[1] + h / 2,times)
        return True
    return False

def upgrade(ench,grays,defx,defy,enchx,enchy,korumax,korumay,antikx,antiky):
    global gray
    if ench <= 7:
        ClickOn('images/UpIcon.PNG',grays,1)
        getFullScreen()
        click(defx,defy,2)
        ClickOn('images/EnchButton.PNG',gray,1)
        time.sleep(2)
        clickWtime(enchx + 8 , enchy,0.3,2)
        mouse.move(enchx - 20,enchy,1,0.4)
        time.sleep(1)
    if ench >7 and ench < 20:
        ClickOn('images/UpIcon.PNG', grays, 1)
        getFullScreen()
        click(antikx, antiky, 2)
        ClickOn('images/OtherIcon.PNG', grays, 1)
        getFullScreen()
        click(korumax, korumay, 2)
        ClickOn('images/EnchButton.PNG', gray, 1)
        time.sleep(2)
        clickWtime(enchx + 8, enchy, 0.3, 4)
        mouse.move(enchx - 20, enchy, 1, 0.4)
        time.sleep(1)


def main():
    getFullScreen()
    if exists('images/RappelzIcon.PNG',gray):
        ClickOn('images/RappelzIcon.PNG',gray,1)
        getFullScreen()
        if exists('images/RappelzTxt.PNG',gray):
            ClickOn('images/RappelzTxt.PNG',gray,1)
            getFullScreen()
            if not exists('images/Inventory.PNG',gray):
                press('ı')
                getFullScreen()

            ClickOn('images/UpIcon.PNG',gray,1)
            getFullScreen()

            defCubex,defCubey =FindCordinates('images/UpIcon.PNG','images/Cube.PNG','images/DefTxt.PNG',gray)

            antikx,antiky = FindCordinates('images/UpIcon.PNG','images/Antik.PNG','images/AntikTxt.PNG',gray)

            ClickOn('images/ItemIcon.PNG',gray,1)
            getFullScreen()

            ClickOn('images/EnchIcon.PNG',gray,1)
            getFullScreen()

            enchx,enchy = GetCordinates('images/EnchArea.PNG',gray)

            philox,philoy=FindCordinates('images/OtherIcon.PNG','images/Philo.PNG','images/PhiloTxt.PNG',gray)

            korumax,korumay = GetCordinates('images/koruma.PNG',gray)


            ClickOn('images/ItemIcon.PNG', gray, 1)
            getFullScreen()
            temp = FindAllItemPos('images/tst.PNG',gray)
            for pt in temp[2]:
                click(pt[0] + temp[0] / 2, pt[1] + temp[1] / 2,3)

                clickWtime(enchx + 8 , enchy,0.3,2)

                clickWtime(enchx - 20,enchy,0.3,0)

                time.sleep(1)
                getFullScreen()
                if exists('images/NoBonus.PNG',gray):
                    ClickOn('images/OtherIcon.PNG',gray,1)
                    getFullScreen()
                    click(philox,philoy,2)

                    ClickOn('images/EnchButton.PNG',gray,1)

                time.sleep(1)
                clickWtime(enchx - 20,enchy,0.4,0)
                time.sleep(1)
                getFullScreen()

                Posx, Posy = GetCordinates('images/pos.PNG', gray)

                img = np.array(ImageGrab.grab(bbox=(Posx + 8, Posy - 14, Posx + 50, Posy + 12)))
                gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                ench = PhotoText.GetText(gri)
                try:
                    if '+' in ench:
                        ench = ench.replace('+', '')
                    ench = int(ench)
                except:
                    ench = 0
                print("Burdayım")
                print(ench)

                while int(ench) < 20:
                    upgrade(int(ench),gray,defCubex,defCubey,enchx,enchy,korumax,korumay,antikx,antiky)


                    getFullScreen()
                    Posx, Posy = GetCordinates('images/pos.PNG', gray)

                    img = np.array(ImageGrab.grab(bbox=(Posx + 8, Posy - 14, Posx + 50, Posy + 12)))
                    gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    ench = PhotoText.GetText(gri)
                    try:
                        if '+' in ench:
                            ench = ench.replace('+','')
                        ench = int(ench)
                    except:
                        ench = 0

                    print(ench)
                clickWtime(enchx + 8, enchy, 0.3, 6)

                clickWtime(enchx - 20, enchy, 0.3, 2)

                ClickOn('images/ItemIcon.PNG',gray,1)


main()