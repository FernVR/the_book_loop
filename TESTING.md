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

### Automated Testing
I ended up stretched for time and couldn't carry out as much automated testing as I would've wanted, but I managed to test the bookstore and basket views files.
Testing functions can be found in these files:

[basket/Tests](basket/test_views.py)

[bookstore/Tests](bookstore/test_views.py)

![Test Results](docs/testing-media/automated-testing.png)


<details><summary>Automated testing</summary> <img src="docs/testing-media/automated-testing.png"></details>


## Manual Testing
Extensive Manual Testing was carried out during the duration of this project. I tried to test each feature/link upon creating them, I have also included screenshots of the testing grids I created.


### Header Navigation / Footer

<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/nav-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/nav-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/nav-responsive-design.jpeg"></details>

<details><summary>Forms </summary> <img src="docs/testing-media/manual-testing/nav-forms.jpeg"></details>


### Home Page

<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/home-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/home-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/home-responsive-design.jpeg"></details>

<details><summary>Forms </summary> <img src="docs/testing-media/manual-testing/home-forms.jpeg"></details>


### Bookstore 
<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/bookstore-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/bookstore-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/bookstore-responsive-design.jpeg"></details>


### Book Detail 

<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/book-detail-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/book-detail-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/book-detail-responsive-design.jpeg"></details>

<details><summary>Forms </summary> <img src="docs/testing-media/manual-testing/book-detail-forms.jpeg"></details>


### Basket

<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/basket-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/basket-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/basket-responsive-design.jpeg"></details>


### Checkout

<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/checkout-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/checkout-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/checkout-responsive-design.jpeg"></details>

<details><summary>Forms </summary> <img src="docs/testing-media/manual-testing/checkout-forms.jpeg"></details>


### Sign up/ Sign In/ Sign Out Pages

<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/sign-up-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/sign-up-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/sign-up-responsive-design.jpeg"></details>

<details><summary>Forms </summary> <img src="docs/testing-media/manual-testing/sign-up-forms.jpeg"></details>


### Customer Service

<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/customer-service-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/customer-service-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/customer-service-responsive-design.jpeg"></details>

<details><summary>Forms </summary> <img src="docs/testing-media/manual-testing/customer-service-forms.jpeg"></details>


### Profile Page

<details><summary>Links and Buttons </summary> <img src="docs/testing-media/manual-testing/profile-links-buttons.jpeg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-media/manual-testing/profile-display-images.jpeg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-media/manual-testing/profile-responsive-design.jpeg"></details>

<details><summary>Forms </summary> <img src="docs/testing-media/manual-testing/profile-forms.jpeg"></details>


## Bugs

### Resolved Bugs
Complete list of all resolved bugs can be found in detail within the issues within the 'bug' label, they can all be found here: [Github Issues - Bugs](https://github.com/FernVR/the_book_loop/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

### Unresolved Bugs
I didn't have time to fix a few bugs within this project so close to the due date, just minor UI issues.
These issues are marked with a 'wontfix' label and their detailed issues can be found here: [Github Issues - Bugs - wontfix](https://github.com/FernVR/the_book_loop/issues?q=is%3Aissue+is%3Aclosed+label%3Awontfix)


## Browser Compatibility
<details><summary>Browser Compatibility Grid </summary> <img src="docs/testing-media/browser-compatibility.jpg"></details>

## Lighthouse Test Result
 I generated a Google Lighthouse report and got these results:

 <details><summary>Home Result</summary></summary><img src="docs/testing-media/lightouse/lightouse-result.png"></details>
 <details><summary>Home Performance</summary></summary><img src="docs/testing-media/lightouse/lightouse-home-performance.png"></details>
 <details><summary>Home SEO</summary></summary><img src="docs/readme-media/screenshots/lighthouse-seo-passed.png"></details>
 <details><summary>Home Best Practises</summary></summary><img src="docs/testing-media/lightouse/home-best-practises.png"></details>
 <details><summary>Bookstore Result</summary></summary><img src="docs/testing-media/lightouse/bookstore-lightouse.png"></details>
 <details><summary>Bookstore Accessibility</summary></summary><img src="docs/testing-media/lightouse/bookstore-accessibility.png"></details>
 <details><summary>Bookstore Performance</summary></summary><img src="docs/testing-media/lightouse/bookstore-performance.png"></details>
 <details><summary>Bookstore Best Practises</summary></summary><img src="docs/testing-media/lightouse/bookstore-best-practices.png"></details>
 <details><summary>Bookstore SEO</summary></summary><img src="docs/testing-media/lightouse/bookstore-seo.png"></details>

 * I received some lower performance scores and tried to make changes to the image sizing to hopefully fix these issues - unfortunately the book covers I added were in PNG and I didn't have time to convert them, like I did for the background images.

 * I tried to ensure SEO and Accessibility scores were 100 across all pages.

 * Not sure what to do about the 'Best Practices' scores, I didn't have much time to make changes here so close to the deadline.

 
