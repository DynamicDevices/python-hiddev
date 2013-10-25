hiddev: build/lib/hiddev

build/lib/hiddev: hiddev/__init__.py hiddev/__main__.py hiddev/monitorcontrol.py
	python3 setup.py build

install:
	python3 setup.py install

clean:
	python3 setup.py clean
	rm build/lib/hiddev/__init__.py
	rm build/lib/hiddev/__main__.py
	rm build/lib/hiddev/monitorcontrol.py
	rmdir build/lib/hiddev
	rmdir build/lib
	rmdir build

.PHONY: hiddev install clean
