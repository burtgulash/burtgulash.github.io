build-dir = a

.PHONY: all render css clean

all: render css
render: $(build-dir)
	./render.py
css: $(build-dir)
	sassc _styles/*.scss > css/style.css
$(build-dir):
	mkdir $(build-dir)
clean:
	-rm -r $(build-dir)
