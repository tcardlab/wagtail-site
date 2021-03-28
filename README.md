# wagtail-site
My first website built with django-wagtail and vue! (2018)

## How to run:
    # Env Windows (or use conda)
    $ python3 -m venv mysite\env
    $ mysite\env\Scripts\activate.bat
    
    # Env Mac/Unix (or use conda)
    $ python3 -m venv mysite/env
    $ source mysite/env/bin/activate
    
    # Install
    $ cd { path to repo }
    $ pip install -r requirements.txt
    
    # Initialize site
    $ python manage.py migrate
    $ python manage.py createsuperuser
    
    # Run
    $ python manage.py runserver

## Preview
I have never published this site and cannot guarantee an easy start up.
So, I have provided some screen shots.
### Home Page
![Home Page](https://raw.githubusercontent.com/tcardlab/wagtail-site/master/media/readme_images/home.png)
<!--![Home Page](./media/readme_images/home.png)-->

### About Page
![Home Page](https://raw.githubusercontent.com/tcardlab/wagtail-site/master/media/readme_images/about.png)

![Quora Feed](https://raw.githubusercontent.com/tcardlab/wagtail-site/master/media/readme_images/Quora.png)

### Blog Index Page 
![Blog Index](https://raw.githubusercontent.com/tcardlab/wagtail-site/master/media/readme_images/blogIndex.png)
