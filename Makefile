all:
	python render.py > README.md

clean:
	find . -name a.out | xargs rm -f 2>/dev/null
	find | egrep pyc$ | xargs rm -f 2>/dev/null
	find | egrep swp$ | xargs rm -f 2>/dev/null
