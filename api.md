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
Returns: str, the user id  
Creates a user. Each email has to be unique.

**GET** /users/[id]/name  
Returns: str, the full name of the user

**GET** /users/[id]/orgs/  
Returns: str array, the list of organizations that a user is a part of.
 
**PUT** /users/[id]/password  
password: str  
Resets user's password  

<a id="orgs"></a>
## Orgs
**PUT** /orgs/[name]  
Returns: None  
Creates an organization. The creator is an admin.

**GET** /orgs/[name]/admins/  
Returns: str array, a list of the administrators (uids) of an organization

**GET** /orgs/[name]/users/  
Returns: str array, a list of the users (uids) of an organization

**POST** /orgs/[name]/users/  
id: str, the uid  
action: str, "add" or "remove"  
Returns: None  
Adds or removes a user from an organization based on action.
 
**POST** /orgs/[name]/admins/  
id: str, the uid  
action: str, "add" or "remove"  
Returns: None  
Adds or removes an administrator from the organization based on action.
 
**DELETE** /orgs/[name]  
Returns: None  
Deletes an organization with the specified name.

<a id="topis"></a>
## Topics
**POST** /orgs/[name]/topics/  
name: str  
description: str  
anon: bool  
return topic id  
Returns: None  
Creates a topic with the specified name and description. Anonymous if anon is true. User must be administrator of the organization to create a topic.
 
**GET** /orgs/[name]/topics/[tid]/anon  
Returns: bool, the anonymity of topic

**GET** /orgs/[name]/topics/  
Returns: str array, a list of the topic ids that an organization contains

**DELETE** /orgs/[name]/topics/[tid]  
Returns: None  
Deletes a topic with the specified id. User must be administrator.

<a id="candidates"></a>
## Candidates
**POST** /orgs/[name]/candidates/  
name: str  
description: str  
topic: str, topic id  
Returns: candidate id  
Add candidate; the topic id has to exist
 
**GET** /orgs/[name]/candidates/  
topic: str, the topic id  
Returns: json, as a list of dicts sorted by average rating, and each dict contains:  
name: str  
description: str  
avg\_rating: float  
all\_ratings: int array  
all\_voters: str array of uids  
For an anonymous topic, the list of all voters should be sorted alphabetically. Otherwise, the order of all ratings and all voters should correspond - kept in the order they were added.

**PUT** /orgs/[name]/candidates/[id]/description  
description: str  
Returns: None  
Edits candidate description

**POST** /orgs/[name]/candidate/[id]/ratings  
rating: int, from 1 to 5  
Returns: None  
Adds vote to candidate. If the user has already voted for this candidate, this overrides their old rating.
 
**DELETE** /orgs/[name]/candidates/[id]  
Returns: None  
Deletes candidate.
