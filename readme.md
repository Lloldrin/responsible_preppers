# Responsible Preppers

This is a webshop for selling gear aimed at the prepper community.

## UX

![UX Example](https://github.com/Lloldrin/responsible-preppers/blob/master/assets/readme/responsiveness.PNG)

### User Stories
 
* Buyer: I'm looking for high quality gear with clear descriptions and easy site navigation. 

* Store Owner: I want to easily add and modify products. I also want to be able to track orders, automate payments and easily track what products are selling well.

### Trello
Much of the development process can be seen on the page Trello: [Here](https://trello.com/b/UuKlJ56j/milestone-project-4)

### Strategy
The site is meant to provide users with knowledge and products to help with prepping. It’s meant to show that prepping is about actually being prepared. This is a far broader concept than hoarding non-perishable food items and medical supplies. Reliable Preppers purpose is to both sell high quality items to help with prepping as well as give instructions on how to use the items.

Brand Values for Responsible Preppers are: Reliable, Knowledgeable, Helpful

### Scope

The Store will be divided into two parts. The actual store and a resource archive.

#### Scope of the Store:
* Products
* Categories
* Cart
* Checkout
* Blog - Knowledgeable

The Store will sell high quality items to help with prepping. They will all be tested by us personally to make sure that they fulfill our requirements on quality, ease of use and price. We will also record youtube videos that showcase the items and show the customers how to use them.

#### Scope of the Resource Archive:
* Upload downloadable PDFs in ISO A4 size for users to download and print.

The Resource archive will contain printable checklists, posters and other things for customers to download. All non-food products listed will be supplied by the store but the resources will be made available for free for everyone. This is both to help everyone get into prepping but also to give the store a good reputation for seriousness as well as a helpful attitude.

### Structure 
The store is the main revenue stream of the site and will be featured prominently on the front page, but the Resource Archive is also an important pillar and will be easy to navigate and link to.

On the very top will be the logo and navigation, on the bottom is a footer linking to social media and showing general information about the site (trustworthiness, contact information etc)

Navigation includes “Home”, “Shop”, “Resources”. The Cart will also be displayed in the navigation bar.

#### Front Page
Starts with a carousel showing featured categories in the store. 

#### Store
Ease of navigation is key. Sort by categories and make sure it’s easy for users to know where they currently are as well as how to get back to a previous tier. It’s also important to not have too many products. It’s more important that the available products are properly tested and proven to work reliably than to fill the store with more choices.

#### Resource Archive
It will be a series of cards divided into categories with clear instructions on how to download the cards so that even tech non savvy customers will be able to use the resources.

### Skeleton

![Wireframe1](https://github.com/Lloldrin/responsible-preppers/blob/master/assets/readme/home_page.jpg)
![Wireframe2](https://github.com/Lloldrin/responsible-preppers/blob/master/assets/readme/product_page.jpg)
![Wireframe3](https://github.com/Lloldrin/responsible-preppers/blob/master/assets/readme/product_detail.jpg)
![Wireframe4](https://github.com/Lloldrin/responsible-preppers/blob/master/assets/readme/cart_page.jpg)

### Surface
The color scheme will be reminiscent of hiking in the mountains. Many prepper sites have a feel of doom and gloom. Responsible Preppers are here to make sure that people see the value of prepping, but to also make them understand that if you’ve properly prepared then a scenario where you have to be self sufficient then it’s not supposed to feel like a doom and gloom scenario. If you are properly prepared then you should almost feel like it was unnecessary because everything in your life almost stayed the same. This is in case of minor emergencies, not in true SHTF scenarios, but those are exceedingly rare and is not the focus for a large portion of everyday preppers.

To help move prepping away from the doom and gloom the colors will be sombre but not aggressive, invoking a feeling of nature and calm.

## Features

### Existing Features

* **Navigation:** All navigation on the site points towards the store. On top is the navbar with all the categories as well as the search bar. In the footer are links to the general categories and the front page is a hero-image carousel with links to the store. All to give the customers an obvious call to action. 

* **Database-query:** The database is handled with postgres through django. All the database operations are handled from Django.

* **Responsiveness:** Since the site is built on Bootstrap 4 it's fully responsive and works on mobile, tablets and desktops. Elements change width and some elements are not rendered if the page is too small. 

### Features Left to Implement

* **Resource Archive:** The Resource Archive is not yet implemented. The store is currently a minimum viable product and works as a full fledged webshop. But the stretch goals of the shop is yet to be implemented. 

## Technologies Used
 
* **HTML**
* **CSS** 
* **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** 
    * This project extensivly uses JavaScript for most of the page
* **[jQuery](https://jquery.com)** 
    * This project extensivly uses jQuery throughout the entire page
* **[Bootstrap](https://getbootstrap.com/)**
	* This project uses Bootstrap 4 for graphical elements as well as the grid system.
* **Visual Studio Code** 
    * This is the IDE used to create the page
* **Flex**
    * This project uses flex as part of Materialize.
* **Git** 
    * For version control
* **[ami.responsivedesign.is](http://ami.responsivedesign.is/)**
    * To show the UX example.
* **Browsers** 
    * For testing
    * Chrome
    * Firefox
    * Safari
	
* **Code Institute** 
    A lot of the code is either heavily inspired or copied from Code Insitutes learning material on Django. Most code is written by hand but follows the steps laid out by Code Institute. Stripe payments and email handling follows to the letter. The rest follows closely. 

## Testing

The website has been tested in the following ways: 

### Automated Tests

* **[HTML Validator](https://www.freeformatter.com/html-validator.html)**
    * The HTML gives several errors. These are all related to the use of Django. 
        * **Example:** Non-space characters found without seeing a doctype first. Expected e.g. “<!DOCTYPE html>”. 
        From line 1, column 1 to line 1, column 17
        Code Extract:
        {% load static %}↩↩<!d  <- Is valid use of Django, but the validator has issues. The other bugs shown in validator has been fixed. 
        * It also has issues as most paged don't have a doctype, head or body since those are inherited from the base.html

* **[CSS Validator](https://jigsaw.w3.org/css-validator/validator)**
    * Passed with no errors.

* **[Responsive Tester](https://www.responsinator.com/?url=https%3A%2F%2Fmilestone-3-hikers-cuisine.herokuapp.com%2Findex)**
    * Showed an error with the navigation buttons on the hero image. Fixed. 

### User Testing

* Several users were asked to try the site and break it in various ways.
   
### Browsers 
* Desktop
    * Chrome 
    * Safari
    * Firefox 
* Mobile
    * Huawei P30 Pro
        * Chrome
        * DuckDuckGo
    * iPhone 10 
        * Safari  
    * Samsung Galaxy S8 
        * Chrome  

## Deployment

The site is hosted on Heroku.

* To deploy the app a GitHub repository was created [here](https://github.com/Lloldrin/responsible_preppers)
    * This was linked to a Heroku app following the guide found [here](https://devcenter.heroku.com/articles/github-integration)
* The site uses the Master branch of the repository
    * It will update automatically with new commits to the master branch
* To ensure that Heroku loads the app correctly the page must contain:
    * requirements.txt - This tells Heroku what libraries are needed for the site to run.
    * Procfile - This tells Heroku how to run the app.
* Static files and images are hosted on Amazon Web Services through 3S
    * This follows the guide found [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) and Code Institutes course.
 
Since the site relies on environment variables that are not open it's not possible to run the site locally with full functionality. 