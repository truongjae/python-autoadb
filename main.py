import subprocess
import cv2
from time import sleep as sl
import threading
from PIL import Image
from google.cloud import vision
import io,os

# import easyocr
# reader = easyocr.Reader(['en'])

class ADBAuto:
	def __init__(self,emulator):
		self.emulator = emulator
	def click(self,x,y):
		subprocess.call("adb -s %s shell input tap %s %s"%(self.emulator,str(x),str(y)))
	def scroll(self,x1,y1,x2,y2):
		subprocess.call("adb -s %s shell input swipe %s %s %s %s"%(self.emulator,str(x1),str(y1),str(x2),str(y2)))
	def press(self,x,y):
		subprocess.call("adb -s %s shell input touchscreen swipe %s %s %s %s 2000"%(self.emulator,str(x),str(y),str(x),str(y)))
	def screencap(self):
		os.system("adb -s %s exec-out screencap -p > screen%s.png"%(self.emulator,self.emulator))
	def switchApp(self):
		subprocess.call("adb -s %s shell input keyevent KEYCODE_APP_SWITCH"%(self.emulator))
	def home(self):
		subprocess.call("adb -s %s shell input keyevent 3"%(self.emulator))
	# def getLevel(self):
	# 	self.screencap()
	# 	img = cv2.imread("screen%s.png"%(self.emulator))
	# 	try:
	# 		crop_img = img[115:150,254:307]
	# 		os.remove("screen%s.png"%(self.emulator))
	# 		cv2.imwrite("screen%s.png"%(self.emulator),crop_img)
	# 		results = reader.readtext("screen%s.png"%(self.emulator))
	# 		text = ""
	# 		for i in results:
	# 			text+=i[1]
	# 		os.remove("screen%s.png"%(self.emulator))
	# 		return int(text)
	# 	except:
	# 		return 0

	def getLevel(self):
		self.screencap()
		filename = "screen%s.png"%(self.emulator)
		img = Image.open(filename)
		try:
			img = img.crop((258, 121, 300, 143))
			os.remove(filename)
			img.save(filename)
			list_name = ""
			os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'
			client = vision.ImageAnnotatorClient()
			with io.open(filename, 'rb') as image_file:
				content = image_file.read()
			image = vision.Image(content=content)
			response = client.text_detection(image=image)
			texts = response.text_annotations
			for text in texts:
				list_name = text.description
				break
			if response.error.message:
				raise Exception(
					'{}\nFor more info on error messages, check: '
					'https://cloud.google.com/apis/design/errors'.format(
						response.error.message))
			os.remove(filename)
			try:
				return int(list_name[0])
			except:
				sl(2)
				self.click(741,11)
				sl(2)
				return 0
		except:
			try:
				os.remove(filename)
			except:
				pass
			return 0
	
	# def openGame(self):
	# 	self.scroll(401,350,397,99) # scroll app menu
	# 	self.click(73,76) # click game
	# 	sl(45)
	# 	self.click(398,354) #click start
	# 	sl()
	# 	self.click(718,21) # click close pop up
	# 	sl(5)
	# 	self.scroll(626,226,460,222) #scroll mãng xà
	# 	sl(3)
	# def setupGame(self,fast):
	# 	self.click(528,218) #click mãng xà
	# 	sl(1)
	# 	self.click(558,360) #click total 400
	# 	sl(10)
	# 	if fast:
	# 		self.click(521,420) #click fast
	# def showInfo(self):
	# 	self.click(55,15) #click wall info
	# 	sl(5)
	# 	level = self.getLevel() #get level
	# 	self.click(715,13)
	# 	return level

	# def backHome(self):
	# 	self.click(63,17) # click home
	# 	sl(10)
	# def playGame(self):
	# 	self.press(665,401)# press spin
	# 	self.click(655,182) #click quay vo han
	# def autoGame(self):
	# 	self.openGame()
	# 	self.setupGame(True)

	# 	while True:
	# 		self.playGame()
	# 		sl(10)
	# 		self.backHome()
	# 		level = self.showInfo()
	# 		if  level < 10:
	# 			self.setupGame(False)
	# 		else:
	# 			break

	def openGame(self):
		self.scroll(401,350,397,99) # scroll app menu
		self.click(179,149) # click game
		sl(60)
		self.click(389,349) #click start
		sl(70)
		# self.switchApp()
		# sl(2)
		# self.click(391,181) #click game

		self.scroll(401,350,397,99) # scroll app menu
		self.click(179,149) # click game

		sl(15)
		self.click(617,162) #click quay
		sl(30)
		self.click(478,214) #click chon nhan vat
		sl(20)
		self.click(521,420) #click fast
		sl(2)
		self.playGame()
		sl(240)
		self.click(399,399) #click let's begin
		sl(15)
		self.click(768,25) #click close
		sl(3)
		self.backHome()
		self.click(391,181) #click continue
		sl(1)
		self.click(391,181) #click continue
		sl(1)
		self.click(391,181) #click continue
		sl(1)
		self.click(405,406) #click newbie
		sl(3)
		self.click(768,25) #click close
		sl(5)
		self.scroll(626,226,460,222) #scroll mãng xà
		sl(3)
		self.setupGame()
		sl(15)
		self.click(247,310) #click don't show again 
		sl(2)
		self.click(394,313) # click ok
		sl(3)
		self.playGame()
		sl(15)
		self.backHome()
		sl(5)
		self.click(335,342) #click collect
		sl(15)
		self.click(689,56) # click close
		sl(35)
		self.click(630,344) # click collect
		sl(30)
		self.click(726,14) # click close
		sl(5)
		self.setupGame()


		# self.click(718,21) # click close pop up
		# sl(5)
		# self.scroll(626,226,460,222) #scroll mãng xà
		# sl(3)
	def setupGame(self):
		self.click(528,218) #click mãng xà
		sl(2)
		self.click(558,360) #click total 400
		sl(15)
	def showInfo(self):
		self.click(55,15) #click wall info
		sl(8)
		level = self.getLevel() #get level
		self.click(715,13)
		return level

	def backHome(self):
		self.click(63,17) # click home
		sl(15)
	def playGame(self):
		self.press(665,401)# press spin
		self.click(655,182) #click quay vo han
	def autoGame(self):
		self.openGame()
		check=False
		while True:
			self.playGame()
			sl(14400)
			self.backHome()
			level = self.showInfo()
			if  level < 100:
				self.setupGame()
			else:
				break
		
# a = ADBAuto("emulator-5554")
# b = ADBAuto("emulator-5556")
# c = ADBAuto("emulator-5558")

# def auto1():
# 	a.autoGame()
# def auto2():
# 	b.autoGame()
# def auto3():
# 	c.autoGame()
# t1 = threading.Thread(target=auto1)
# t2 = threading.Thread(target=auto2)
# t3 = threading.Thread(target=auto3)
# t1.start()
# t2.start()
# t3.start()


# d = ADBAuto("emulator-5558")
# d.autoGame()


def configADB():
	subprocess.call("adb kill-server")
	sl(2)
	subprocess.call("adb start-server")
	sl(10)
	for i in range(10):
		sl(1)
		subprocess.call("adb devices")

n = int(input("Nhập số lượng luồng: "))
configADB()
emulator = "emulator-"
stt = 5554

arrThread = []
for i in range(n):
	name = emulator+str(stt)
	stt+=2
	auto = ADBAuto(name)
	t = threading.Thread(target = auto.autoGame)
	arrThread.append(t)

for i in arrThread:
	i.start()