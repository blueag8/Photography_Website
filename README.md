
#  Milestone 4- Django Full Stack Project| Professional Photography (e-commerce) website


view Heroku app [here]



GitHub repository [here]

https://github.com/blueag8/

## About The Project

This is the final Project for the Code Institute and the main technologies that will be used include:
 
HTML, CSS, JavaScript, Python+Django.
Relational Database
Stripe Payments
Additional Libraries

Git and GitHub are used for version control,

Gitpod IDE
AWS Cloud9 used for development.

View [here]


Deployment via "Heroku"* 

*See further below for more on deployment.

## The Idea



# UX
**External User Story**



**Site Owners Potential**

The possibility to provide users with the ability to get an ingredients list to build a shopping list and to add items to a shopping cart. 

Reports could be made to provide feedback on the age-specific recipes being favourited, advertising can also be customized to target 'age' specific audiences.

Login/registration features will provide the site owner with a customer database which in future can be used to build and maintain customer relationships. 

## Development Process
create virtualenv
virtualenv -p python3 .
source bin/activate
easy_install 
migrate

**Wireframes**
![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Home.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Map.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/About.png)
## Data Schema![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Cart.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Contact.png)![enter image description here](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Portfolio.png)[https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Home.png](https://res.cloudinary.com/blueag8/image/upload/v1574999839/Photography%20website/Payment_Conf.png)
**The Schema used for storing this data in MongoDB is as follows:**


**Recipe**


**Category**


##  Features

*Future possible implementations/opportunities*


## Technologies Used

 - HTML checked with [https://validator.w3.org/nu/#textarea](https://validator.w3.org/nu/#textarea)
 - CSS for styling and checked using https://jigsaw.w3.org/css-validator/validator<p><a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" /> </a></p>


 -   jQuery- to simplify DOM manipulation. 

 - Heroku 0.1.4- used as a platform for deployment
 - Git and GitHub- used for version control. 
 

**Process**

**Responsive Design and styling**

Because of the time restraints and encountering many issues with the functionality of the application, which caused delays, the responsive design has much yet to be desired. 
Layout is 'OK' on portrait mobile but not if viewed in landscape. Desktop layout is 'better' but not ideal.
 
Images need resizing and adjusting still for a sharper and better image quality. 

The Yellow used for "7 months +" is quite harsh on the users eye. An alternative colour will be more visually pleasing.

## Testing

 - The application was tested on mobile (Honor PCT-L29 by Huawei) and desktop
 - Checked add form successfully submits data to the MongoDB Storage
 - Checked edit form returns previously saved data and allows new input to successfully update data in the database
 - Checked button functionality cancel returns user to previous page, "Go back to Recipes" returns users to the list of recipes previously viewed. "Share", "Update" and "Delete" Buttons successfully trigger modals and the confirmation buttons within the modals, successfully alter data in the database
 - Checked delete function removes data from the database
 - Checked recipes are saved and loaded within specialized categories in which they should be assigned
 - Checked app is intuitive for the user (added modals to help the user know that entries/edits have been successful)
 -Ensured that these were clear and obvious. 
 -Checked images maintain ratio on different view sizes
 -Used the print function in app.py to test code functionality using Werkzeug debugger
 
**Process/Challenges **


**Issues encountered** 


## Deployment

Requirements to run code locally:

1. Clone the repository at 
https://github.com/blueag8/babyappytite.git
2. Install Python 3.6 using the command $pip3 install python
3. Install Flask-Pymongo using the command $pip3 
install flask-pymongo
4. Create a requirements.txt file by using the command $pip3 freeze --local > requirements.txt
5.  Create a Procfile with the command $echo web: python app.py 
6. Install Heroku via the CLI with $sudo install Heroku --classic
7. Heroku config vars need to be set 

Port 0.0.0.0
IP 8080
MONGO_URI

For the purpose of assesment the following configs are required:
Database Name= "Baby_Recipes"
MONGO URI ="mongodb+srv://blueag8:mongo8@cluster0-iodau.mongodb.net/Baby_Recipes?retryWrites=true&w=majority"

line 167.  in app.py

(for testing  purposes set debug to =True.) 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)

# Credits

**Acknowledgements:**

Mentor Antonio Rodriguez

Code Institue module and tutorials

Slack Channel :




**Images**
**Referenced** following documentation, tutorials and code checking sites:

https://jshint.com/
https://www.w3schools.com




<!--stackedit_data:
eyJoaXN0b3J5IjpbMjkyOTMxNjgzLC05NTMwODE4MzYsNDg5Nj
AxMjM1XX0=
-->