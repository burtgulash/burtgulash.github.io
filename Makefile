build-dir = a

.PHONY: all render build-css clean

all: render build-css
render: $(build-dir)
	./render.py
build-css: $(build-dir)
	gulp build-css
$(build-dir):
	mkdir $(build-dir)
clean:
	-rm -r $(build-dir)
