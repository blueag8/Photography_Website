
#  Milestone 4- Django Full Stack Project| Professional Photography (e-commerce) website


view Heroku app [here]

https://henkdeweerdphotography.herokuapp.com/

GitHub repository [here]

https://github.com/blueag8/Photography_Website


## About The Project

This is the final Project for the Code Institute Full Stack Web Development Course.

The aim is to design and build a full-stack website around business logic. We are required to show an authentication mechanism, payment facilities and a locally managed dataset which stores products or services.

This is a Website built using Python+Django, HTML, CSS, JavaScript logic for Frontend and a relational Database.

# UX
**External User Story**

Discover and purchase photographs from a professional photographer.

**Site Owners Potential/Story**

Earn Money selling products and showcase/promote work and events/exhibits to a public audience.

Customer requirements:
Henk would like an ecommerce style website. 
He would like to offer
 -Three choices in canvas/print size
 -Prints will be signed
 -All will be with no border
 
He would like to display his work in Image Galleries employing the following filter options :
 

 - ALL (would like to view "ALL" images as an option)
 Landscape
- Travel (could have further filter options within this category)
	-India
	-France
	-Vietnam
	-Taiwan
- Family
- Minimalist
- South Australia
- Australia
- Portraits
- Windows to the World exhibition
- Books 

In addition to this he would like to include:

Bio/About Page

Contact details/Contact Form

Order Form

External links to Facebook Page and Flickr profiles


## Development Process
Planning
**Wireframes**
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Map.png)
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Home.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/About.png)
## Data Schema![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Cart.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Contact.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Portfolio.png)

![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Shop.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Payment_Confirmation.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Continue_to_Payment.png)
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Payment_Form.png)

![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Mobile_Mockup_home.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Mobile_Contact.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Mobile_Shop.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Mobile_Mockup4.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Payment_ConfirmationMobile.png)

##  Features

 - Register, sign in, logout of an account
 -  Add, edit, delete products.
 (Authorised permissions)
 - Filter products by prices
 - Create an order
 - Make a payment
 - Contact Form

## Technologies Used

 - DJANGO
 - PYTHON
 - JAVASCRIPT
 - CSS
 - HTML
    
    
 - Gitpod IDE for development
 - Git and GitHub- used for version control
 - Heroku for deployment
 - Frameworks include:
    - Bootstrap
   - Font-Awesome Icons
   - Google-Fonts


## Deployment

This project was developed using the
[gitpod.io](https://gitpod.io/workspaces/)

1. create a virtual environment. I acheived this via the CLI by typing "virtualenv -p python3 [name of your virtual env]" 
2. I chose to create an env.py file and ensured that is was not published to the public repository by using gitignore.
This command was "env.py > .gitignore"
3. To activate the virtual env use "source bin/activate"
4. Once inside the activated virtualenv install django. You may need to use the command "cd .. " to ensure you are in the root directory then use the command "pip3 install django ==1.11.24". If using gitpod I found that if in the virtualenv the "pip3" install [command] didn't work, and using the "easy_install"[command] worked.
5. Create new project by running command "django-admin startproject [project_name] . " (the . is used to ensure you are in the root directory).
6. Next run the command "python3 manage.py migrate" this will initialise the application and create a default database.
7. CLI installation commands
pip3 install django-bootstrap-modal-forms
pip3 install django-forms-bootstrap
pip3 install pillow
pip3 install stripe
8. If deploying to Heroku you will need a requirements.txt file so use the command:
pip3 freeze > requirements.txt
9. For stripe access you will need to obtain a both a publishable key and a Secret Key which will be stored in and environment variable. 


## Requirements to run code locally:

1. Clone or download repository from https://github.com/blueag8/Photography_Website.git
2. Activate  a virtual environment.
3. Source bin/activate
4. pip3 install -r requirements.txt
5. python3 manage.py runserver
6. python3 manage.py makemigrations
7. python3 manage.py migrate
8. python3 manage.py createsuperuser

*If deploying via Heroku and using Gitpod*:

I found that pip3 install was not working as I had hoped for the installation and access of Heroku via the command line.
I userd "npm install -g heroku --classic "

Next you will need to heroku login



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
eyJoaXN0b3J5IjpbLTkzOTI3NTUxNCwtNTUwMTcyMzMzLDMzOT
Q0MTA1NSwxOTY3NzMzNzksMjA3ODgwMjA4OSwtOTU4OTc0MTEx
LDE4NzEzMjExNTksMTEzODQ0NzQ5Nyw2MzA2OTY4MjUsLTczNz
Q4MDY4NCw2MTI0ODExNDUsMTI2MTUyOTk5NiwtMTg4NDYwOTEw
LDM1MzAxMzEwMywxNzg1OTY0MzM1LDIwODEzODQ4MDIsLTQxMj
gwNjIwNF19
-->