# Contents
[Database](#database)  
[HTTP Requests](#http)
- [Users](#users)
- [Orgs](#orgs)
- [Topics](#topics)
- [Candidates](#candidates)

<a id="database"></a>
# Database
**org table:**
- org name
- admins
- users
- topics
- candidates

**users table:**
- password
- orgs
- name
- email

**candidates table:**
- topic
- name
- description
- avg rating
- ratings
- voters

**topics table:**
- topic id
- description
- anonymity


**To implement later:**
- Comments
- Other voting systems (ranking, binary)
- admin can add / remove people from topics


<a id="http"></a>
# HTTP Requests

<a id="users"></a>
## Users
**POST** /users/  
name: str  
email: str  
password: str  
Status codes: 200 OK, 201 Created, 400 Bad Request  
Returns: json {uid: str, success: bool}  
Creates a user. Each email has to be unique.

**GET** /users/[id]/name  
Status codes: 200 OK, 404 Not Found  
Returns: str, the full name of the user

**GET** /users/[id]/orgs/  
Status codes: 200 OK, 404 Not Found  
Returns: str array, the list of organizations that a user is a part of.
 
**PUT** /users/[id]/password  
password: str  
Status codes: 200 OK, 400 Bad Request, 401 Unauthorized, 404 Not Found  
Resets user's password

<a id="orgs"></a>
## Orgs
**PUT** /orgs/[name]  
Status codes: 200 OK, 201 Created  
Returns: json {success: bool}
Creates an organization. The creator is an admin.

**GET** /orgs/[name]/admins/  
Status codes: 200 OK, 404 Not Found  
Returns: str array, a list of the administrators (uids) of an organization

**GET** /orgs/[name]/users/  
Status codes: 200 OK, 403 Forbidden, 404 Not Found  
Returns: str array, a list of the users (uids) of an organization

**POST** /orgs/[name]/users/  
id: str, the uid  
action: str, "add" or "remove"  
Status codes: 200 OK, 400 Bad Request, 403 Forbidden, 404 Not Found  
Returns: None  
Adds or removes a user from an organization based on action.
 
**POST** /orgs/[name]/admins/  
id: str, the uid  
action: str, "add" or "remove"  
Status codes: 200 OK, 400 Bad Request, 403 Forbidden, 404 Not Found  
Returns: None  
Adds or removes an administrator from the organization based on action.
 
**DELETE** /orgs/[name]  
Status codes: 200 OK, 403 Forbidden, 404 Not Found  
Returns: None  
Deletes an organization with the specified name.

<a id="topis"></a>
## Topics
**POST** /orgs/[name]/topics/  
name: str  
description: str  
anon: bool  
return topic id  
Status codes: 201 Created, 400 Bad Request, 403 Forbidden, 404 Not Found  
Returns: None  
Creates a topic with the specified name and description. Anonymous if anon is true. User must be administrator of the organization to create a topic.
 
**GET** /orgs/[name]/topics/[tid]/anon  
Status codes: 200 OK, 403 Forbidden, 404 Not Found  
Returns: bool, the anonymity of topic

**GET** /orgs/[name]/topics/  
Status codes: 200 OK, 403 Forbidden, 404 Not Found  
Returns: str array, a list of the topic ids that an organization contains

**DELETE** /orgs/[name]/topics/[tid]  
Status codes: 200 OK, 403 Forbidden, 404 Not Found  
Returns: None  
Deletes a topic with the specified id. User must be administrator.

<a id="candidates"></a>
## Candidates
**POST** /orgs/[name]/candidates/  
name: str  
description: str  
topic: str, topic id  
Status codes: 201 Created, 400 Bad Request, 403 Forbidden, 404 Not Found  
Returns: candidate id  
Add candidate; the topic id has to exist
 
**GET** /orgs/[name]/candidates/  
topic: str, the topic id  
Status codes: 200 OK, 400 Bad Request, 403 Forbidden, 404 Not Found  
Returns: json, as a list of dicts sorted by average rating, and each dict contains:  
name: str  
description: str  
avg\_rating: float  
all\_ratings: int array  
all\_voters: str array of uids  
For an anonymous topic, the list of all voters should be sorted alphabetically. Otherwise, the order of all ratings and all voters should correspond - kept in the order they were added.

**PUT** /orgs/[name]/candidates/[id]/description  
description: str  
Status codes: 200 OK, 403 Forbidden, 404 Not Found  
Returns: None  
Edits candidate description

**POST** /orgs/[name]/candidate/[id]/ratings  
rating: int, from 1 to 5  
Status codes: 200 OK, 400 Bad Request, 403 Forbidden, 404 Not Found  
Returns: None  
Adds vote to candidate. If the user has already voted for this candidate, this overrides their old rating.
 
**DELETE** /orgs/[name]/candidates/[id]  
Status codes: 200 OK, 403 Forbidden, 404 Not Found  
Returns: None  
Deletes candidate.
