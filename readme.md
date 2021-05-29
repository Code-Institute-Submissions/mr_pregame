<p align="center"><img src="media/device_mockup.png" width="400"></p>


# **Mr. Pregame**
View the live project [HERE.](https://mrpregame.herokuapp.com/)

***

## **Introduction**

Mr. Pregame Sports Betting Management plans to be a one stop shop for all sports betting research and bet tracking. As the Sport Wagering industry legalizes and grows in the states, I find that in order to make educated decisions on which teams to bet on you have to bounce around to three or four different sites to get everything you need and then another app to track all the bets that you've made. My plan with Mr. Pregame was to simplify that whole process and offer all the services for free in one place. For users that want an expert opinion or skip the whole pregame research all together, using a subscription model Mr. Pregame offers expert analysis and guaranteed picks. 

Click [here](https://github.com/RyanRayn/mr_pregame) to view the GitHub repository for the project.

To test the payment transaction prodess please use:

* Credit card number: 4242 4242 4242 4242
* Expiration date: 04/24
* CVC: 242
* ZIP: 42424
***

## **User Experience (UX)**

**Strategy**

As the developer and also an avid sports bettor, I initially started the design process from the mindset of the user. As I would be developing a platform that I, myself was in need of. During this design process I quickly had to switch hats and start thinking from a developers view to take into consideration scalability, functionality and regular maintenence.

**General**

1. As the developer, I wanted to create a full-stack e-commerce site where users can add, edit and delete data.

2. As the developer, I want the website to function well and be fully responsive to demonstrate my coding abilities.

3. As the site owner, I would like as much data as possible autogenerated through API's.

**Aesthetic and UX**

4. As the developer, I want the site to be aestetically pleasing and easy to use to create a positive UX experience for users.

5. As the site owner, I want to create a brand that would welcoming and easy to market.

6. As the site owner, I want to create a rapport with the users and develop trust to eventually upgrade members to a paid membership that offers professional game analysis.

7. As the site owner, I want to create a complete hassle free environment for users through a ease of navigation and accessibility to cancel memberships.

8. As the site owner, I would like to automate as many functions as possible.

**Registration and Subscribing**

9. As a site user, I would like to easily register for an account.

10. As a site user, I would like my account to be secure.

11. As a site user, I would like access to my information to update and delete whenever I want.

12. As a site user, I would like to be able to cancel my subscription without a hassle.

**Navigation**

13. As the site owner, I would like users to be able to navigate in and out of every page without hitting the back arrow.

14. As the site owner, I would like users to always have access to the 'Subscribe' button if they aren't currently subscribed.

15. As the site owner, I would like all the daily games organized by sport/leagues.

**Checkout**

16. As a site user, I want to be able to easily and quickly enter my payment details, so I can checkout quickly, hassle free.

17. As a site user, I want my monthly subscription fee directly charged to my credit card without having to re-enter information.

**Admin**

18. As the site owner, I would like to quickly update game lines and stats.

19. As the site owner, I would like to easily write and show game breakdowns and picks for subscribers.

**Structure**

Base all the required features and data that needed to be shown for users, I decided I wanted to include the following pages on my website:

* The Home page welcomes the user to the site and presents the user with calls to action to subscribe for a paid membership.

* The log in and sign up pages allow users to log in and create their memebership.

* The Suscribe page allows users to enter all their billing info and start their monthly subscription.

* The Profile page (paid subscribers only) displays all the game picks for that given day. Profile page also has a link to edit profile information, email, passwords and cancel subscriptions. Coming soon, paid users will also have bet tracking available which will be displayed in the profile.

* The Games page is linked to an API call. From the home page when you hover on 'Games' a dropdown appears with all the leagues available,  MLB, NCAA Basketball, NBA or NFL. Once the user selects the league, data is pulled via API to display teams, times, locations, game lines as well as a button to go to the Matchup Page.

* The Matchup Page has all the data and stats for the teams involved in the game chosen. As well as game picks and a carousel that cycles through all the other games of that day.

**Wireframes**
* Wireframes were created using Balsamiq Wireframes and can be found [HERE.](https://github.com/RyanRayn/mr_pregame/blob/master/media/mr_pregame_wireframes.png)

**Color Scheme**
* I wanted to have a darker website so it is easier on the eyes while studying all the numbers and data so the primary background color is rgb(13, 29, 53). An opacity of 90% was also placed on all bright colors to tone them down a bit.

* The main colors used throughout the site are:
<p align="center"><img src="media/MrPregameColors.png" width="400"></p>

**Fonts**

* The two fonts used on Mr. Pregame are Oswald and Montserrat with sans-serif as a backup.

***

## **Information Architecture**

With all the different sports and teams there are several different models for data.

**Profiles App** 

The Profiles app models are primarily used for Stripe and subscription functionality.

*UserProfile*

In addition to Django's user model, a custom model was created as well, UserProfile, to store profile information.

* user : One to One relationship with Django's User
* full_name : Users full name for billing
* email : User email for billing
* active : Boolean field to keep track of active paid sub.
* stripe_customer_id : ID code Stripe assigns to each user
* membership_type : Paid or Free
* stripe_subscription_id : Id is assigned by Stripe when a paid subscription is created for the user
* phone_number : Phone for billing
* country : Address for billing
* postcode : Address for billing
* town_or_city : Address for billing
* street_address1 : Address for billing
* street_address2 : Address for billing

*Memberships*

Membership model is created as a part of the Stripe subscription plans.

* membership_type : Paid or Free
* price : 0 or $30/month
* stripe_plan_id : Id code to select membership on Stripe platform

**Management App**

The management app is the heart of Mr. Pregame. All of the teams, leagues and games data is stored here.

*League*

* Contains the four different leagues on offer which are foreign keys to the teams in the TeamName model.

*TeamName*

* name : Full name of each team
* abbreviation : Abbreviation of team names
* twitter_id : Each teams unique twitter id to be called on for the twitter API
* league : Foreign key

*Season*

A code created for each season to store data under.

* name : Name of season
* teams : Many to many field to the TeamName model

*BasketballTeamStats*

With 24 fields, this model is where game stats are stored from each individual game. This model contains two foreign keys...

* name : Foreign Key TeamName
* season : Foreign Key Season

*MLBGame*

Another big model that stores all the data from each individual Major League Baseball Game. This model also contains two foreign keys.

* name : Foreign Key TeamName
* season : Foreign Key Season

*StartingPitcher*

This model keeps track of all the starting pitching stats for each game. Contains two foreign keys.

* teams : Foreign Key TeamName
* season : Foreign Key Season

*MLBGameLine*

This model holds the betting info for each game that is collected from a sports betting API. This model also holds all of the game picks done by 'Mr. Pregame.

***

## **Features and Apps**

Mr. Pregame is a Django project comprised of five individual apps which contain multiple features.
