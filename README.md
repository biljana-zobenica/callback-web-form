# callback-web-form with [django](https://docs.djangoproject.com/en/3.2/)

This is a web application based on Django web framework. It represents a customer service support and include a contact form for submitting complains. Additionally, it insludes a built-in admin database, which is customized to receive, track, sort and modify these forms. The web app is stored on GitHub and works in a virtual environment, which should be set previously.

# Installation steps

- [x] DOWNLOAD PROJECT FILES

* go to the project repository
* "Code" -> download "ZIP" file
* UNZIP the project folder and navigate the same location in command prompt
* make a git repo for the project and connect it with your local project folder
Also, it is possible to clone this repo and pull it to your local disk. The results are the same.

- [x] SET UP VIRTUAL ENVIRONMENT

**pip install pipenv** 
> make sure to be in your project's location and install a virtual environment
In some cases, it is necessary to add pipenv in the system's [PATH](https://superuser.com/questions/1372793/the-script-is-installed-in-directory-which-is-not-path).

**pipenv install django**
> install django inside a virtual environment

**pipenv shell**
> activate python interpreter within the project and isolate its development

**django-admin startproject <project-name> .**
> create the project built-in files and structure
    
**django-admin startapp <app-name>**
> create an app built-in files and structure

- [x] RUN SERVER

**python manage.py runserver <port-number>**
> port number is by default 8000, so you can define yours.
> Our first django app is finally lanuched!
    
![install_worked](https://user-images.githubusercontent.com/32877624/130936293-7933138a-1f07-4b4f-81cc-460d8bb3a673.png)
