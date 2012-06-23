serve: clean
	./manage.py runserver_plus

clean:
	find . -name "*.pyc" | xargs /bin/rm -f
