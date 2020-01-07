
#  Milestone 4- Django Full Stack Project| Professional Photography (e-commerce) website
Quick Links

[UX](https://github.com/blueag8/Photography_Website/blob/master/README.md#ux)

[UI](https://github.com/blueag8/Photography_Website/blob/master/README.md#ui) /Wireframes

[Data Schema](https://github.com/blueag8/Photography_Website/blob/master/README.md#data-schema)

[Features](https://github.com/blueag8/Photography_Website/blob/master/README.md#features)

[Technologies](https://github.com/blueag8/Photography_Website/blob/master/README.md#technologies-used)

[Local Deployment](https://github.com/blueag8/Photography_Website/blob/master/README.md#requirements-to-run-code-locally)

[Future Implementations](https://github.com/blueag8/Photography_Website/blob/master/README.md#future-implementations)

[Testing](https://github.com/blueag8/Photography_Website/blob/master/README.md#future-implementations)

[Credits](https://github.com/blueag8/Photography_Website/blob/master/README.md#credits)


## Website

https://henkdeweerdphotography.herokuapp.com/

**GitHub repository**

https://github.com/blueag8/Photography_Website


## About The Project

This is the final Project for the Code Institute Full Stack Web Development Course.

The aim is to design and build a full-stack website around the business logic. We are required to show an authentication mechanism, payment facilities and a locally managed dataset which stores products or services.

This is a Website built using Python, Django, HTML, CSS, JavaScript logic for Frontend and a relational database.

Initially, when I began the project, whilst following the Code Institute's Tutorial on developing an E-commerce site ("Putting it all together"), I had a different project in mind. "Toolbox" is an app that I still wish to pursue, but after having spoken with Henk, I decided that building this site for Henk will better meet the requirements for assessment. I had not adjusted the project/app name as I have been limited on time to meet a deadline and was preventing the introduction of any bugs that may have been created as a result of this change.
 
# UX

The goal is to be the voice and advocate for the user's needs while balancing the business goals. Providing a meaningful and relevant experience to the user through a website that is easy to navigate,  use of intuitive design and is visually appealing.

**External User Story**
Discover and purchase photographs from a professional photographer.

**Site Owners Potential/Story**
Earn Money selling products and showcase/promote work and events/exhibits to a public audience.

Customer requirements:
Henk would like an eCommerce style website. 
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
![Map](https://res.cloudinary.com/blueag8/image/upload/v1578415910/photography_website/Map.png)
![Home Page](https://res.cloudinary.com/blueag8/image/upload/v1578415910/photography_website/Home.png)![About](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/About.png)

![Cart](https://res.cloudinary.com/blueag8/image/upload/v1578415910/photography_website/Cart.png)
![Contact Us](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Contact.png)![Portfolio](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Portfolio.png)

![Shop](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Shop.png)![Payement Confirmation](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Payment_Confirmation.png)![Order Form](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Continue_to_Payment.png)
![Payment Form](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Payment_Form.png)

![Mobile responsive](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Mobile_Mockup_home.png)![Mobile responsive](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Mobile_Contact.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Mobile_Shop.png)![Mobile responsive](https://res.cloudinary.com/blueag8/image/upload/v1574999841/Photography%20website/Mobile_Mockup4.png)![Mobile Responsive](https://res.cloudinary.com/blueag8/image/upload/v1574999840/Photography%20website/Payment_ConfirmationMobile.png)

For testing/development, SQLite was used and for deployment to Heroku, Postgresql was used. 

## Data Schema

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

 - Register, sign in, log out of an account
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

# Deployment

This project was developed using the
[gitpod.io](https://gitpod.io/workspaces/)

1. Create a virtual environment. This can be achieved this via the CLI by typing 
`virtualenv -p python3 [name of your virtual env]`
  Alternatively, I chose to create an env.py file to store my private credentials and to ensure  that is was not published to the public repository, this file was added to gitignore via the command:

    env.py > .gitignore

2. To activate the virtual env
`source <name of virtual env>/bin/activate`

   ( source bin/activate if you created the env.py)
    

3. Once inside the activated virtualenv install Django. You may need to use the command "cd .. " to ensure you are in the root directory then use the command "pip3 install Django ==1.11.24". If using Gitpod I found that if in the virtualenv the "pip3" install [command] didn't work, and using the "easy_install"[command] worked.

4. Create a new project by running the command   `Django-admin startproject [project_name] . `  (the . is used to ensure you are in the root directory).5. Next, run the command 
`python3 manage.py migrate` this will initialise the application and create a default database.
8. CLI installation commands

     pip3 install django-bootstrap-modal-forms
     
     pip3 install django-forms-bootstrap
    
    pip3 install pillow
    
    pip3 install stripe

9. If deploying to Heroku you will need a requirements.txt file so use the command:

pip3 freeze > requirements.txt

10.  Create a Procfile
web: gunicorn <app_name>
(Gunicorn for Heroku deployment)

11. If you don't already have a Heroku account [Sign-up Here](https://signup.heroku.com/)
12. For stripe access, you will need to register an account and obtain both a publishable key and a Secret Key which will be stored in an environment variable.  This can be done [[here](https://dashboard.stripe.com/login)]


## Requirements to run code locally:

1. Clone or download repository from https://github.com/blueag8/Photography_Website.git
2. Create a virtual environment.
3. Source bin/activate
4. pip3 install -r requirements.txt
5. set up your environment variables ie. SECRET_KEY [create your own  ](https://miniwebtool.com/django-secret-key-generator/)
7. python3 manage.py runserver
8. python3 manage.py makemigrations
9. python3 manage.py migrate
10. python3 manage.py createsuperuser

*If deploying via Heroku and using Gitpod*:

I found that pip3 install was not working as I had hoped for the installation and access of Heroku via the command line.
I used the command 

    npm install -g heroku --classic 
rather than pip3 .

Login to Heroku if using the CLI 

    heroku login
    
You will need to create or sign in to any third-party accounts and access your keys then set up your config variables in the settings.

These will include:

 - DATABASE_URL (if not using sqlite)
 - SECRET_KEY
  - API_SECRET
 - API_KEY
 - HOST
 - IP
 - STRIPE_PUBLISHABLE
 - STRIPE_SECRET
 - CLOUD_NAME (if using Cloudinary for image storage)
 - CLOUDINARY_URL

 

## Future Implementations

 1. Automated message bot.
 2. Provide an external link to photos enlarged. Ie the Cloudinary link could open in a new tab, or use a modal to display the enlarged photo for viewing.
 3. Images need resizing and adjustments for best optimization.
 5. Email copy or order form to the customer. (Perhaps use a modal to show order back to the customer rather than the alert).
 6. Reset password page HTML and CSS also to redirect to home after submission.
 7. Set up an external email account (emails currently only go to Backend testing).
 8. Admin access pages made more "user-friendly" as Henk will be maintaining it himself.
 9. Filters need to be added for categories as per Henks wishes.
 10. Background images for individual pages need adjusting in the templates which extend from the base.html. 
11. Update URL- If the user is not logged in for checkout, then after login, redirect back to the cart rather than to home.
12. Add favicon image for branding 
13. Headings and Site Map for marketing
14. Additional content added to pages ie About/Bio
15. Offer the choice of sizes and create a function to adjust the price following the selection of size.

# Testing

### Manual
Tested on multiple devices using both Chrome Dev Tools on desktop and tested on a mobile phone.  iPhone 6/7/8 and Ipad Responsive.


**Scenarios**

 - Register as a new user
 - Register as a user that already exists.
 - Login using correct details.
 - Login using invalid credentials.
 - Logout
 - Click on the logo to be taken back to home
 - Check all links are valid
 - Send email using Backend
 - Adjust price filter and check valid products are filtered/returned.
 - Shop as an authorised user
 - add to cart
 - adjust quantity
 - go to checkout
 - checkout update cart
 -  payment form
 - check required fields are requested
 - card error messages -incorrect card details, payment declined, expiry date
 - Shop as unauthorised user
 - add to cart
 - adjust quantity
 - go to checkout
 - checkout login required
   
 - Reset password 
 
Note: Debug was set to True during this process to receive feedback. 
 
 - Check forms intelligently handle invalid or empty/required fields.

 
CRUD 
 - Create a product
 - View a product
 - Edit a product
 - Delete a product
 

STRIPE 
 
Test card details:
 
CARD number

4242 4242 4242 4242

NAME

Any 

CVC (any three numbers)

111

EXPIRY (must be after current date)

01/2021

There is a lot more testing I would like to integrate, including more of the automated testing. 

I have created a Travis.yml file but am currently having issues passing the build. 
Due to time constraints and passing a deadline I am happy to submit as is for assessment.  

Through extensive manual testing, I conclude that the site is user-friendly and works as expected. 

I will be forking this project and continuing to work on it for Henk. 

## Bugs
There were several issues when attempting to deploy to Heroku.

> django.core.exceptions.ImproperlyConfigured: You're using the
> staticfiles app without having set the STATIC_ROOT setting to a 
> filesystem path. !     Error while running '$ python manage.py
> collectstatic --noinput'.

 Solution was to add :   

    DISABLE_COLLECTSTATIC=1 

 to the Heroku config variable settings

Forgot to remove env from the settings.py resulted in an error
>     import env
> 
>    ModuleNotFoundError: No module named 'env'

Issues migrating from SQL to PostgreSQL 
I found solved by following the instructions from 

[How to migrate data from SQLite to PostgreSQL in django](https://dev.to/coderasha/how-to-migrate-data-from-sqlite-to-postgresql-in-django-182h) By Coderasha

Solutions included resetting migrations. I referred to this helpful link.

[How to reset migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)
Simple is Better than Complex by By **Vitor Freitas**

There is a current bug in the "Products app" model.py. When making a migration an error report shows the response:
" invalid literal for int() with base 10:" 

***Validation***

[https://travis-ci.com/] current status![build:started](https://travis-ci.com/blueag8/Photography_Website.svg?branch=master)

https://jshint.com/ (Check Javascript)

https://w3c.github.io/developers/tools/ (CSS, HTML)

<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

[Image testing via Cloudinary Web Speed Test](https://webspeedtest.cloudinary.com/)

 **HTML** validation still has one outstanding error:
 "*Element “style” not allowed as child of element “body” in this context"*

# Credits

**Acknowledgements:**
Thank you to the student care team at the Code Institute for your own going support and patience.

To my mentor Antonio Rodriguez, a pleasure to speak to. Thank you for helping me fix the bugs and encouraging me to keep going. Incredibly patient and extremely helpful. 

Code Institute Tutorials

The Code Institute Slack Community

Inspiration was taken from 
https://colinprior.co.uk/

**Images**
By Henk DeWeerd

**Logo**
Designed by Naomi Wickham using Google-fonts.

**Referenced** following documentation, tutorials and sites:

https://stripe.com (Payment API)
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


*Naomi Wickham 2020*

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkzNDUwMTM5MiwtMTg3NDQ5NTI0NSwxOT
AxNDkwODU5LC00NDg3MzA4ODgsMTczMDYxNDUsMTI3OTU5ODAw
NiwzOTc5OTAyMTAsLTE0NTc4MDg1ODYsLTIwNzgyMTk3ODEsMT
U1NjQ0OTM1MSwyNDc1Mjc3MzEsLTU5MDk5NTk2MywtMTUxNDc2
OTU0LDE1MDk3ODIxMTUsLTU0MzI1NjE5LDE0OTIyMzg3MDAsMT
U5OTY5MjAwNywxNDkyMjM4NzAwLDE3MDIwOTE2NTgsNDEzNTkw
ODAxXX0=
-->