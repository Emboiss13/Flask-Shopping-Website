# Flask-Shopping-Website
On this project, I created a full-functioning shopping website for the brand Giuly's Studio, an Indie shopping store. I started with the brand's logo and identity for a homogenous design on the website. I then dove into the coding and used Flask, HTML, CSS, and JavaScript to bring my ideas to life. 

This Flask web application serves as a basic template for building a web application using the Flask framework. It includes user authentication, database integration using SQLAlchemy, and a simple structure to get you started with web development.


### 📄 __Init.py__ Features:
- **Flask Framework:** 
  The application is built using the Flask micro-framework, providing a lightweight and modular structure for web development.

- **SQLAlchemy Integration:** 
  Utilizes the SQLAlchemy library for easy and efficient database operations.
  The default database is SQLite, and you can modify the DB_NAME variable in the script to change the database file name.

- **User Authentication:** 
  Implements user authentication with the help of the Flask-Login extension.
  The application provides login and registration functionality.

- **Blueprint Structure:** 
  Organizes the application into two blueprints: views for general views and auth for authentication-related views.

- **Database Creation:** 
  Includes a function (create_database) to create the database if it does not exist.

___________
### 📄 auth.py Features:
With this section, users can sign up, log in, add products to their shopping cart, and complete a purchase.

1. 🔑***User Authentication***
- Users can sign up with a valid email, first name, and password.
- Passwords are securely hashed using the SHA-256 algorithm.
- Existing users can log in with their credentials.
- Sessions are used to keep track of the authenticated user.
  
2. ⌨️***Product Management***
- Products can be added to the database with information such as product name, price, image path, and carbon footprint.
- The product list is displayed in the shopping area, allowing users to browse available items.

3. 🛒***Shopping Cart***
- Users can add products to their shopping cart.
- The shopping cart is implemented using Flask sessions.
- Users can view their cart, remove items, and proceed to checkout.

4. 💵***Checkout and Payment***
- Users can proceed to the payment page to view their selected items and the total price.
- A payment success page is displayed after completing a purchase.

___________
### 📄 models.py Features:
The application includes two main models: User and Product. The User model is responsible for storing user-related information, while the Product model handles details about the products available in the application.

1. 👤***User Model***

  The User model is defined as a subclass of both "db.Model" and "UserMixin" from Flask-Login. 
  It includes the following fields:
  
  - id: Primary key for the user table.
  - email: Unique email address for each user.
  - password: Password for user authentication.
  - first_name: First name of the user.
  
    1.1 User Relationships
    - The User model may have additional relationships, such as a shopping cart linked to the customer database. However, the specific implementation of these relationships is left as a comment and should be defined based on the application's requirements.

2. 👗***Product Model***

  The Product model represents the products available in the e-commerce application. 
  It includes the following fields:
  
  - id: Primary key for the product table.
  - product_name: Name of the product.
  - price: Price of the product.
  - image_path: Path to the image of the product.
  - carbon_footprint: Integer representing the carbon footprint of the product.

___________
### 📄 views.py Features:
The application uses Flask's Blueprint to organize views and render HTML templates.

1. 🌐***Routes:***

The application defines several routes:
- /: Displays the home page.
- /about: Displays the about page.
- /contact: Displays the contact page.
- /thanks_contact: Displays a thank-you page after submitting the contact form.

2. 🖌️***Templates:***

HTML templates are stored in the templates folder and are rendered by the corresponding routes.

3. 🖼️***Static Files:***

The static folder contains static assets (e.g., stylesheets, images) used by the HTML templates.

_________

### Demo: 
If you'd like to see how the website acts on a browser, check this video I made: https://youtu.be/BHLdDcs4ulE 
