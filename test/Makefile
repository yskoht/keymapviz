test:
	python test.py

test-update-snapshot:
	python test.py -u

setup:
	git clone --depth 1 https://github.com/qmk/qmk_firmware.git

clean:
	rm -rf *.c *.json input/*.bac
	git checkout input/*.c

allclean: clean
	rm -rf qmk_firmware

