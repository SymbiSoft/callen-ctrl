# __author__ = 'martiancode'
# version = '0.7 beta'
# filename = 'A_Redial_semifinal2.py'
# app_name = 'callen-ctrl'
# license = 'Apache Version 2.0' a copy of the License can be obtained at http://www.apache.org/licenses/LICENSE-2.0
    
    
# def index(req):
##   return "Test successful";
## 
## ## Original code I've tried on the N70
## start_loop = 1
## while start_loop:
## 	telephone.dial("0109928855")
## 	timer = e32.Ao_timer()
## 	interval = 15
## 
## 	timer.after(interval) # sleep for 15 seconds
## 	telephone.hang_up()
## 	timer.cancel()

## A try to enhance it
import e32
import telephone
import appuifw
import graphics

def redial(contact, duration):
	telephone.dial(contact)
	timer = e32.Ao_timer()
	timer.after(duration)
	telephone.hang_up()

contact = appuifw.query(u'Enter number to redial ?', 'text')

duration = appuifw.query(u'For how long ?', 'number')

interval = appuifw.query(u'Amount of time to wait between redials ?', 'number')

nu = appuifw.query(u'How many times to redial ?', 'number')

start_loop = 0

while (start_loop < nu) :
	timer1 = e32.Ao_timer()
	timer1.after(globals()['interval'])
	redial(globals()['contact'], globals()['duration'])
	
	start_loop += 1
	if start_loop == nu :
		break
	print "Done"
print "#Notice that number of Dones equals times to redial minus one#"