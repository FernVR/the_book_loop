# Testing 
Back to [README.md](README.md) file.

![Main Image - I am Responsive screenshot](docs/readme-media/am-i-responsive-store.png)

# Contents 
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [Javascript](#javascript)
    - [Python](#python)

- [Python Unit Testing](#python-unit-testing)

- [Automated Testing](#automated-testing)

- [Manual Testing](#manual-testing)
    - [Home Page](#home-page)
    - [Bookstore]()
    - [Book Detail]()
    - [Basket]()
    - [Checkout]()
    - [Sign up/ Sign In/ Sign Out Pages](#sign-up-sign-in-sign-out-pages)
    - [Customer Service Form]()
    - [Profile Page]()
    
- [User Story Testing](#user-story-testing)
    - [Developer User Stories](#developer-user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Registered User Stories](#resgistered-user-stories)
    - [Admin User Stories](#admin-user-stories)

- [UI](#ui)

- [Bugs](#bugs)

- [Browser Compatibility](#browser-compatibility)

- [Lighthouse Test Result](#lighthouse-test-result)

## Code Validation
### HTML 
I used [The W3C Markup Validation Service](https://validator.w3.org/) to validate all HTML pages by inputting the source code into the direct input field, these were my results:

<details><summary>Home Page Result</summary><img src="docs/testing-media/validation-results/home-html-val.png"></details>
<details><summary>Bookstore Page Result</summary><img src="docs/testing-media/validation-results/bookstore-html-val.png"></details>
<details><summary>Book Detail Page Result</summary><img src="docs/testing-media/validation-results/book-detail-html-val.png"></details>
<details><summary>Customer Service Page Result</summary><img src="docs/testing-media/validation-results/customer-service-html-val.png"></details>
<details><summary>Profile Page Result</summary><img src="docs/testing-media/validation-results/profile-html-val.png"></details>

### CSS
I used [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate my style.css file, I got these results:

![CSS Validator Results](docs/testing-media/validation-results/css-result.png)

### Javascript
I used [JSHint](https://jshint.com/) to validate my style.css file, I got these results:

<details><summary>stripe.js</summary><img src="docs/testing-media/validation-results/stripe-js.png"></details>
<details><summary>wishlist.js</summary><img src="docs/testing-media/validation-results/wishlist-js.png"></details>
<details><summary>rating-slider.js</summary><img src="docs/testing-media/validation-results/rating-slider-js.png"></details>
<details><summary>image-preview.js</summary><img src="docs/testing-media/validation-results/image-preview-js.png"></details>
<details><summary>delete-book.js</summary><img src="docs/testing-media/validation-results/delete-book-js.png"></details>

### Python
I used [The CI Python Linter](https://pep8ci.herokuapp.com/) to validate my python files, I got these results:

<details><summary>basket/contexts.py</summary><img src="docs/testing-media/validation-results/basket-contexts-py.png"></details>
<details><summary>basket/urls.py</summary><img src="docs/testing-media/validation-results/basket-urls-py.png"></details>
<details><summary>basket/views.py</summary><img src="docs/testing-media/validation-results/basket-views-py.png"></details>
<details><summary>bookstore/models.py</summary><img src="docs/testing-media/validation-results/bookstore-models-py.png"></details>
<details><summary>bookstore/views.py</summary><img src="docs/testing-media/validation-results/bookstore-views-py.png"></details>
<details><summary>checkout/views.py</summary><img src="docs/testing-media/validation-results/checkout-views-py.png"></details>
<details><summary>customer-service/views.py</summary><img src="docs/testing-media/validation-results/customer-service-views-py.png"></details>
<details><summary>home/views.py</summary><img src="docs/testing-media/validation-results/home-views-py.png"></details>
<details><summary>profile/views.py</summary><img src="docs/testing-media/validation-results/profile-views-py.png"></details>

## Python Unit Testing
Results for testing report can be found in [test_report.txt](test_report.txt) which I generated using the 'python manage.py test -v 2 > test_report.txt' command in the terminal.

<details><summary>Python Unittest Result</summary> <img src=""></details>


### Automated Testing
Testing functions can be found in these files:
[appname/Test Forms](appname/tests.py)
[appname/Test Forms](appname/tests.py)
[appname/Test Forms](appname/tests.py)
[appname/Test Forms](appname/tests.py)
[appname/Test Forms](appname/tests.py)

<details><summary>Automated testing</summary> <img src=""></details>

## Manual Testing
Extensive Manual Testing was carried out during the duration of this project. I tried to test each feature/link upon creating them, I have also included screenshots of the testing grids I created.
### Home Page
copy this structure for each page:
<details><summary>Links and Buttons </summary> <img src=""></details>

<details><summary>Display and Images</summary> <img src=""></details>

<details><summary>Responsive Design Grid </summary> <img src=""></details>

### Bookstore 
"" ""

### Book Detail 

### Basket

### Checkout

### Sign up/ Sign In/ Sign Out Pages

### Customer Service

### Profile Page


## User Story Testing

### Developer User Stories
### Visitor User Stories
### Resgistered User Stories
### Admin User Stories

## UI

## Bugs
### Resolved Bugs
### Unresolved Bugs

## Browser Compatibility
<details><summary>Browser Compatibility Grid </summary> <img src=""></details>

## Lighthouse Test Result
 I generated a Google Lighthouse report and got this result:

 ![Lighthouse Result]()
