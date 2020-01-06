
#  Milestone 4- Django Full Stack Project| Professional Photography (e-commerce) website


view Heroku app [here]

https://henkdeweerdphotography.herokuapp.com/

GitHub repository [here]

https://github.com/blueag8/Photography_Website


## About The Project

This is the final Project for the Code Institute Full Stack Web Development Course.

The aim is to design and build a full-stack website around business logic. We are required to show an authentication mechanism, payment facilities and a locally managed dataset which stores products or services.

This is a Website built using Python+Django, HTML, CSS, JavaScript logic for Frontend and a relational Database.

Initally, when I began the project, whilst following the Code Institute's Tutorial on developing an E-commerce site ("Putting it all together"), I had a different project in mind. "Toolbox" is an app that I still wish to pursue, but after having spoke with Henk, I decided that building this site for Henk will better meet the requirements for  the purpose of assessment. I had not adjusted the project/app name as I have been limited on time to meet a deadline and was preventing the introduction of any bugs that may have been created as a result of this change.
 
# UX

The goal is to  be the voice and advocate for the users needs while balancing the business goals. Providing a meaningful and relevent experience to the user through a website that is easy to navigate,  use of intuitive design and is visually appealing.

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

Henk would like to take inspiration from this website:
[https://colinprior.co.uk/](https://colinprior.co.uk/)
## UI
**Wireframes**
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Map.png)
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Home.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/About.png)
## Data Schema![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Cart.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Contact.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Portfolio.png)

![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Shop.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Payment_Confirmation.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Continue_to_Payment.png)
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Payment_Form.png)

![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Mobile_Mockup_home.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Mobile_Contact.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Mobile_Shop.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Mobile_Mockup4.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Payment_ConfirmationMobile.png)

## Front-end

## Back-end
For testing/development Sqlite was used and for deployment to Heroku, Postgresql  was used. 

Data Schema:

*Product Model*
Category
Name
Description
Image
Size
Price

*Product Order Model*
Product
Quantity
Price

*Order Form*
Customer details 

 - Name
 - Address
 - Phone Number
 
 Payment details
 
 - Card Number
 - Name on Card
 - Expiry date
 - Cvc 
 


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


## Development

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

9.  Create a Procfile
guni 
11. For stripe access you will need to register an account and obtain a both a publishable key and a Secret Key which will be stored in and environment variable.  This can be done [here]


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
I used the command 
"npm install -g heroku --classic "

Login to heroku if using the CLI "heroku login"

# Deployment

## Future Implementations
Automated message bot facilities.
Provide an external link to photos enlarged. Ie the cloudinary link could open in a new tab. Or use a model to enlarge the photo for viewing.
Better presentation of singular product/image page.
Images need improving.
Email copy or order form to customer. Perhaps use a modal to show order back to the customer rather than the alert.
Reset password page HTML and CSS also to redirect to home after submission.
Need to set up external email account. 
Admin access pages made more "user friendly" as Henk will be maintaing it himself.
Filters need to be added for categories as per Henks wishes.

Background images for individual pages need adjusting in the templates which extend from the base.html. 
HTML validation still has one outstanding error:
 "*Element “style” not allowed as child of element “body” in this context"*

# Testing
### Manual

## Bugs

<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>
        


# Credits

**Acknowledgements:**
Thank you to the student care team at the Code Institute for your own going support and patience.

to my mentor Antonio Rodriguez, a pleasure to speak to. Thank you for helping me fix the bugs and encouraging me to keep going. Incredibly patient and and extremly helpful. 

**Images**
By Henk DeWeerd
**Logo**
Designed by Naomi Wickham using Google-fonts.
**Referenced** following documentation, tutorials and code checking sites from:

https://stripe.com (Payment API)
https://jshint.com/ (Check Javascript)
https://w3c.github.io/developers/tools/ (Passed CSS 
https://www.w3schools.com
https://fonts.google.com(Fonts)
https://dev.to/coderasha/how-to-migrate-data-from-sqlite-to-postgresql-in-django-182h (Migrating a database from sqlite to postgresql for Heroku deployment)
https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html (Reset Migrations)
https://pypi.org/project/django-bootstrap-modal-forms/
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjY5OTYzMTI2LC0yMDk4NDQ3MTcsMTMzMD
YyODc1NywxOTUzNjIyNTcsLTk1MzA4MTgzNiw0ODk2MDEyMzVd
fQ==
-->

<!--stackedit_data:
eyJoaXN0b3J5IjpbNTIzNTg0OTE1LDE0ODQ0OTUzOTksMTc2Mz
U3MDMxNCwtNTUwMTcyMzMzLDMzOTQ0MTA1NSwxOTY3NzMzNzks
MjA3ODgwMjA4OSwtOTU4OTc0MTExLDE4NzEzMjExNTksMTEzOD
Q0NzQ5Nyw2MzA2OTY4MjUsLTczNzQ4MDY4NCw2MTI0ODExNDUs
MTI2MTUyOTk5NiwtMTg4NDYwOTEwLDM1MzAxMzEwMywxNzg1OT
Y0MzM1LDIwODEzODQ4MDIsLTQxMjgwNjIwNF19
-->