from os.path import join
from ppadb.client import Client as Client
from pynput.keyboard import Key, Listener
from datetime import datetime
import os

folder = 'screen_shots'


def check_device():
	global current_device
	adb = Client(host='127.0.0.1', port=5037)
	devices = adb.devices()
	if len(devices) == 0:
		print('no device attached')
		print('exit')
		quit()
	else:
		current_device = devices[0]
		print(f"device found {current_device.serial} ")
		create_folder(folder)
		start()


def create_folder(directory):
	os.makedirs(directory, exist_ok=True)
	print('folder created')


def show(key):
	if key == Key.space:
		image = current_device.screencap()
		now = datetime.now().strftime("%d%m%Y%H:%M:%S")
		out_file_name = join(folder, now + '.png')
		print(out_file_name)
		with open(out_file_name, 'wb') as f:
			f.write(image)
			print(f"screen shot taken {f.name}")
	elif key == Key.esc:
		return False


def start():
	print('press space to take screen shot and esc to quit application')
	with Listener(on_press=show) as listener:
		try:
			listener.join()
		except:
			print('application quit')


if __name__ == '__main__':
	check_device()

