clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./mcider.egg-info
	rm -rf ./test/tmp/*
	pip uninstall mcider

install:
	python setup.py install

test:
	nosetests ./test/unit/

.PHONY: clean install test
