
user profile managment (back)
## Retrieve User Profile
**Endpoint:** `GET /api/accounts/<UserID>/`

**Description:** Retrieves the profile information for the specified user.

### Request:
- **Method:** `GET`
- **URL Parameters:**
  - `UserID` (string): The ID of the user.

### Response:
```json
{
    "UserName": "TestUser",
    "UserEmail": "testuser@example.com",
    "UserBio": "Testing Bio",
    "UserPFP": "imageUserID1.jpg",
    "UserCV": "linkUserID1.com"
}


## update and change  User Profile
**Endpoint:** `post /api/accounts/<UserID>/`

**Description:** change specfic fields the profile information for the specified user.

### Request:
- **Method:** `POST`
- **URL Parameters:**
  - `UserID` (string): The ID of the user.

### Response:
```json
{
    "UserName": "UpdatedTestUser",
    "UserEmail": "updateduser@example.com",
    "UserBio": "Updated bio for the user",
    "UserPFP": "newImageUserID1.jpg",
    "UserCV": "newLinkUserID1.com"
}

**Endpoint:** `Delete /api/accounts/<UserID>/`

**Description:** delete the profile.

### Request:
- **Method:** `delete`
- **URL Parameters:**
  - `UserID` (string): The ID of the user.

### Response:
```json
{
    "message": "Profile deleted successfully!"
}
# Postman Tests

# Test Cases:
1. Retrieve User Profile
   - Request: `GET /api/accounts/TestUser1/`
   - Response: 200 OK
   - Result: Passed

2. Update User Profile
   - Request: `POST /api/accounts/TestUser1/`
   - Response: 200 OK
   - Result: Passed

some tests using coverage
src\CampusLink\__init__.py                0      0   100%
src\CampusLink\settings.py               19      0   100%
src\CampusLink\urls.py                    4      0   100%
firebase_config\firebase_helpers.py      17      4    76%
manage.py                                17      6    65%


contentsharing 
Postman Tests
Test Cases:
1. Create a New Post
Request:
POST /api/posts/
Body Type: form-data
Key-Value Pairs:
PostDesc: "This is a new post"
PostComments: 56
PostLikes: 9
PostTags: []
image: Select an image file to upload
Expected Response:
json
{
    "message": "Post created successfully!",
    "PostID": "PostID101",
    "PostImageURL": "https://imgur.com/abc123"
}
Status: 200 OK
Test Outcome: Passed
2. Retrieve All Posts
Request:
GET /api/posts/
Expected Response:
json
{
    "PostID101": {
        "PostDesc": "This is a new post",
        "PostComments": 56,
        "PostLikes": 9,
        "PostTags": [],
        "PostImageURL": "https://imgur.com/abc123",
        "PostTimestamp": "2024-11-29 13:31:27"
    }
}
Status: 200 OK
Test Outcome: Passed
3. Retrieve a Specific Post
Request:
GET /api/posts/PostID101/
Expected Response:
json
{
    "PostID101": {
        "PostDesc": "This is a new post",
        "PostComments": 56,
        "PostLikes": 9,
        "PostTags": [],
        "PostImageURL": "https://imgur.com/abc123",
        "PostTimestamp": "2024-11-29 13:31:27"
    }
}
Status: 200 OK
Test Outcome: Passed
4. Update a Post
Request:
POST /api/posts/PostID101/
Body Type: form-data
Key-Value Pairs:
PostDesc: "Updated description for PostID101"
PostComments: 100
PostLikes: 15
PostTags: ["UpdatedTag"]
image: Select a new image file to upload
Expected Response:
json
{
    "message": "Post updated successfully!"
}
Status: 200 OK
Test Outcome: Passed
5. Delete a Post
Request:
DELETE /api/posts/PostID101/
Expected Response:
json
{
    "message": "Post deleted successfully!"
}
Status: 200 OK

