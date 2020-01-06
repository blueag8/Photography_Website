
#  Milestone 4- Django Full Stack Project| Professional Photography (e-commerce) website


view Heroku app [here]

https://henkdeweerdphotography.herokuapp.com/

GitHub repository [here]

https://github.com/blueag8/Photography_Website


## About The Project

This is the final Project for the Code Institute Full Stack Web Development Course.

The aim is to design and build a full-stack website around business logic. We are required to show an authentication mechanism, payment facilities and a locally managed dataset which stores products or services.

UI
Data Modeling
Multiple Apps
Django-Backend
Relational database Schema
Use of Stripe/e-commerce

This is a Website built using Python+Django, HTML, CSS, JavaScript logic for Frontend and a relational Database.

Frameworks

Bootstrap
Font-Awesome Icons
Google-Fonts


Git and GitHub are used for version control,

Gitpod IDE
AWS Cloud9 used for development.

View [here]


Deployment via "Heroku"* for the purpose of assessment.


# UX
**External User Story**

Discover and purchase photographs from a professional photographer.


**Site Owners Potential/Story**

Earn Money selling products and showcase/promote work and events/exhibits to a public audience.

Customer requirements:

Shop
 -3 Photo sizes
 -Unframed 
 -No Borders
-Signed

Image Galleries
 Filter Options :
 ALL (would like to view All as an option)
 Landscape
 Travel (could have further filter options within this category)
	-India
	-France
	-Vietnam
	-Taiwan
Family
Minimalist
South Australia
Australia
Portraits
Window to the world
Books 

Bio/About

Contact details

Order Form

Contact Form

Links to Facebook Page and Flickr profiles

Possible Future implementations
links to exhibitions
list past exhibits
Live Chat box

## Development Process

**Wireframes**
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Map.png)
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Home.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/About.png)
## Data Schema![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Cart.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Contact.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Portfolio.png)

![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Shop.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Payment_Confirmation.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Continue_to_Payment.png)
**Recipe**![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Payment_Form.png)

![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Mobile_Mockup_home.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Mobile_Contact.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Mobile_Shop.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Mobile_Mockup4.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Payment_ConfirmationMobile.png)
**Category**


##  Features

*Future possible implementations/opportunities*


## Technologies Used


 - Git and GitHub- used for version control. 
 

**Process**

**Responsive Design and styling**


## Testing

**Process/Challenges **


**Issues encountered** 


## Deployment

This project was developed using the
[gitpod.io](https://gitpod.io/workspaces/)

1. create a virtual environment. I acheived this via the CLI by typing "virtualenv -p python3 [name of your virtual env]" 
2. activate the virtual env use "source bin/activate"
3. Once inside the activated virtualenv install django. You may need to use the command "cd .. " to ensure you are in the root directory then use the command "pip3 install django ==1.11.24". If using gitpod I found that if in the virtualenv the "pip3" install [command] didn't work, and using the "easy_install"[command] worked.
4. Create new project by running command "django-admin startproject [project_name] . " (the . is used to ensure you are in the root directory).
5. Next run the command "python3 manage.py migrate" this will initialise the application and create a default database.

pip3 install django-bootstrap-modal-forms
pip3 install django-forms-bootstrap
pip3 install pillow
pip3 install stripe

pip3 freeze > requirements.txt

for stripe you will need to obtain a both a publishable key and a Secret Key which will be stored in and environment variable. 

I chose to create an env.py file and ensured that is was not published to the public repository by using gitignore.

This command was "env.py > .gitignore"



Requirements to run code locally:
clone or download repository from https://github.com/blueag8/Photography_Website.git

activate  virtual environment
source bin/activate



<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>
        


# Credits

**Acknowledgements:**
Thank you to the student care team at the Code Institute. 
Mentor Antonio Rodriguez

Code Institue module and tutorials

Slack Code-Institute

https://colinprior.co.uk 


**Images**
**Referenced** following documentation, tutorials and code checking sites:

https://stripe.com
https://www.gitpod.io
https://jshint.com/
https://www.w3schools.com
https://fonts.google.com
https://stackedit.io/
https://dev.to/coderasha/how-to-migrate-data-from-sqlite-to-postgresql-in-django-182h
https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

https://pypi.org/project/django-bootstrap-modal-forms/
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjY5OTYzMTI2LC0yMDk4NDQ3MTcsMTMzMD
YyODc1NywxOTUzNjIyNTcsLTk1MzA4MTgzNiw0ODk2MDEyMzVd
fQ==
-->

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1Mzg3ODMyOTEsMTI2MTUyOTk5NiwtMT
g4NDYwOTEwLDM1MzAxMzEwMywxNzg1OTY0MzM1LDIwODEzODQ4
MDIsLTQxMjgwNjIwNF19
-->