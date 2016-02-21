# {App Name, More Smart}
**Resources:**  
MLDB.ai - ($1000)   
Nuance - API 4 NLP,   
Smooch.io - API for text based transactions,   
Breather - for help with Node.js
Dottech - free dottech *moresmart.tech*

**Problem:** Students are the best at teaching students, they understand where they are coming from and can interface on the most identifyable lvl. TAs are bad at teaching, Tutors can be expensive and also don't often know the specific ideas that are needed for university specific courses. 

When joining the app, app qs you about which courses you've taken.

**UFlow:**  
1. Make Request  
&nbsp;&nbsp;1.i. Select item you need help with.  
&nbsp;&nbsp;1.ii. Select what you're offering {volunteer xp,cash}   
&nbsp;&nbsp;&nbsp;(average offer is suggested)  
2. Presented with a list-view of nearest people with those skills.  
&nbsp;&nbsp;2.i. list-view is sorted by review and proximity  
2.a. select from map-view    

OR 

2.b. Select auto-matching to request the best teacher based on [proximity,reviews,best cost/offer match]  
3. App sends a request to best n teachers  
4. teachers accept or decline requests
5. App Manages having requests out for 

**Implementation**  
Flask Backend:  
	API: 	Request {Class:,Subject:,Price:,Location:}
			Logic 

Smooch:  
&nbsp;&nbsp;In order to register a number to a user to smooch, ask them to text a confirmation code to #, to validate UID  
&nbsp;&nbsp;is not client 2 client, only business 2 client  
&nbsp;&nbsp;Use smooch to text contact info for each user to each other (once teacher accepts)  
&nbsp;&nbsp;**VALIDATION**SMOOCH->#, #-> Server, validated, continue to Request page

Google Oath Creds:

{"web":{"client_id":"250698810056-6b02gvftla1ek0j0p343fdkrnn1l6afl.apps.googleusercontent.com","project_id":"moresmart-1227","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"LkuC7lG8mVIsgQrzrDTDGVDC","redirect_uris":["http://localhost:5000"],"javascript_origins":["http://localhost:5000"]}}

**Field Deployment**
Demo with U of T.  
Validation: Survey students as to whether this was more useful for students or if TAs were more useful.