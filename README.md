# Django_REST_API_Travel_APP
First project using Django, Jinja, REST framework by implementing CURD(Create, Read, Update, Delete) methods, MVC architecture, Dynamic Web page, etc.





## Installation
The Code is written in Python 3.8.3 If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you 
can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after 
[cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

Visual Studio Code is the choice of IDE for this project. <br>
Jinja extension of version v0.0.8 was installed in VS Code <br>
pip --version => 19.2.3 <br>

asgiref==3.3.0 <br>
astroid==2.4.2 <br>
colorama==0.4.4 <br>
Django==3.1.3 <br>
djangorestframework==3.12.2 <br>
isort==5.6.4 <br>
lazy-object-proxy==1.4.3 <br>
mccabe==0.6.1 <br>
Pillow==8.0.1 <br>
psycopg2==2.8.6 <br>
pylint==2.6.0 <br>
pylint-django==2.3.0 <br>
pylint-plugin-utils==0.6 <br>
pytz==2020.4 <br>
six==1.15.0 <br>
sqlparse==0.4.1 <br>
toml==0.10.2 <br>
wrapt==1.12.1 <br>

``` bash
pip install -r requirements.txt
```

## Directory Tree 

![DT](https://user-images.githubusercontent.com/56732761/98570438-5a9e2e00-22ab-11eb-8a4c-307b433ff68c.PNG)

## Essential commands of Django

Django version used for this project django-admin --version =>3.1.3


django-admin help => To display usage information and a list of the commands provided by each application. <br>
django-admin startproject <project_name> => To create new project in Django 

Always execute below mentioned commands from the root location of the project(i.e. location were manage.py file is located) <br>

python manage.py startapp <appname> => To create new user defined app. <br>
python manage.py runserver => To run the Django web application <br>
python manage.py createsuperuser => Allows to creat user whihc will have master access for manuplating database. <br>
python manage.pt makemigrations => Always execute this command whenevr new model is registered or and changes are created followed by below given command. <br>
python manage.py migrate => After executing above command run this line to migrate. <br> 
python manage.py collectstatic --help => To know commands related to collecting static files like JavaScrit,images,CSS,HTML,etc. <br>

## Technologies Used
![](https://forthebadge.com/images/badges/made-with-python.svg)
[<img target="_blank" src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" width=200>](https://www.djangoproject.com/)
[<img target="_blank" src="http://3.bp.blogspot.com/-3xm0ftuElPM/Vg621Abo8UI/AAAAAAAAAYM/98WXzr3yY54/s320/restframework.png" width=300>](https://www.django-rest-framework.org/)
[<img target="_blank" src="https://jinja.palletsprojects.com/en/2.11.x/_images/jinja-logo.png" width=200>](https://palletsprojects.com/p/jinja/)
[<img target="_blank" src="https://www.sqlite.org/images/sqlite370_banner.gif" width=200>](https://www.sqlite.org/index.html)
[<img target="_blank" src="https://azurecomcdn.azureedge.net/cvt-9281d9db0c63a479d39019e02b1bc35d712622992174d8bb4dcb33f728511a17/images/page/products/visual-studio-code/vscode-logo.png" width=200>](https://code.visualstudio.com/)
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/330px-Postgresql_elephant.svg.png" width=200>](https://www.postgresql.org/)

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/tirth-pipalia/Django_REST_API_Travel_APP/issues/new)
by including your search query and the expected result. <br>

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/tirth-pipalia/Django_REST_API_Travel_APP/issues/new). 
Please include sample queries and their corresponding results. <br>


## License

[![Apache license](https://img.shields.io/badge/license-apache-blue?style=for-the-badge&logo=appveyor)](http://www.apache.org/licenses/LICENSE-2.0.txt)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at [Apache](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Credits
[Telusko](https://www.youtube.com/channel/UC59K-uG2A5ogwIrHw4bmlEg) <br>
[Django Documentation](https://docs.djangoproject.com/en/3.1/)<br>
[Rowhit Swami](https://gist.github.com/rowhitswami)
