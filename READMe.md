## How to start Django

### Install python
1. Check if python is already installed <br/>
`$ python --version`

2. Download Python <br/>
    go to link -> [here](https://www.python.org/downloads/)\
    Window : make sure to check "Add python (version) to Path"


3. Check if python is installed properly <br/>
    Window :`$ python --version`\
    Mac os :`$ python3 --version`

4. Install pip <br />

    * *pip* is the package manager for python which is used for getting libraries<br/>
    Window : [here](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#:~:text=Download%20and%20Install%20pip%3A&text=Download%20the%20get%2Dpip.py,where%20the%20above%20file%20exists.&text=and%20wait%20through%20the%20installation,now%20installed%20on%20your%20system.)\
    Mac os : [here](https://www.geeksforgeeks.org/how-to-install-pip-in-macos/) or `$ sudo easy_install pip`

5. Check if pip is installed properly 

    Window : `$ python -m pip --version`\
    Mac os : `$ pip3 --version`
    \
    
----

### What is virtual Environment 

* The virtual environment is an environment which is used by Django to execute an application. It is recommended to create and execute a Django application in a separate environment. Python provides a tool virtualenv to create an isolated Python environment. 

### Configuration for Django 

#### --Mac Os

1. Install virtual environment <br/>
    `$ pip3 install pipenv`

2. Make new file <br/>
    `$ mkdir <dirName>`

3. Change directory <br/>
    `$ cd <dirName>`

4. Install Django with virtual environment<br/>
    `$ pipenv install django`

    (On termianl) Virtualenv location : <path> 
5. *Activate virtual environment*<br/>
    `$ pipenv shell`

6. Check if Django is installed properly <br/>
    `$ django-admin`\
    Then you will be albe to see command 

7. Strat Django project <br/>
    `$ django-admin startproject <projectName>`\
    You can check Django project is created in the same directory.

8. `$ python manage.py migrate`
    * migrate executes those SQL commands in the database file. So after executing migrate all the tables of your installed apps are created in your database file


----
#### --Window

**Using Powershell**<br/>

1. Make new file for project <br/>
    `mkdir <fileName>`

2. Change directory<br/>
    `cd <fileName>`

3. Install virtual environment<br/>
    `$ python -m venv env`\
    'env' file will be created in the directory

4. Install Django <br/>
    `$ python -m pip install django~=4.0.0`

5. *Activate virtual environment*<br/>
    `$ env\Scripts\activate`

6. Check if Django is installed properly <br/>
    `$ django-admin`\
    Then you will be albe to see command 

7. Strat Django project <br/>
    `$ django-admin startproject <projectName>`\
    You can check Django project is created in the same directory.

8. `$ python manage.py migrate` 
    * migrate executes those SQL commands in the database file. So after executing migrate all the tables of your installed apps are created in your database file

------

## start from uploaded file(DJango) on gitlab

1. activate virtual environment

2. Mac os : <br/>`pipenv install`<br/>Window :<br/> `python -m pipenv install` 

3. Mac os : <br/>`pipenv lock` <br/> Window : <br/> `python -m pipenv lock`

4. Mac os : <br/>`python3 manage.py runserver` Window : <br/> `python -m manage.py runserver`



--------

### Django official doc

[here](https://docs.djangoproject.com/en/4.0/)

-----------
### How to set up React
## How to Start React 

1. Install Node.js  [here](https://nodejs.org/en/)
    * It allows you to run javascript outside of the brower
2. Change directory where you want to start React
      
3. Insall React tool
  `$ npx create-react-app <dirName>`
    
4. Execute a script, set up pre-configuration   
 `$ npm start`
   
5. Install npm : download all dependencies    
 `$ npm install`
   
6. Developing server   
 `$ npm start`  


