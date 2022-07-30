# Secret Santa Picker Backend API

This document will outline the various resources that will be handled by the
Secret Santa Picker backend api.

---

## Users

### Methods and Endpoints

/users
    - GET - get all users
    - PUT - create a new user

/users/<id>
    - GET - get a single user
    - POST - update a single users data - all data must be supplied
    - DELETE - delete a single user

### Data

#### Single Resource

##### GET data

Respoonse:
'''json
{
    "status": "ok",
    "data": {
        "link": {
            "value": "https://www.secret-santa-picker/api/v1/users/12345",
        },
        "id": {
            "value": "12345",
        },
        "name": {
            "first": "Rory",
            "Last": "Houlihan"
        },
        "email": {
            "value": "me@myemail.com"
        },
        "created_ts": {
            "value": "2022-01-01 13:30:345"
        },
        "updated_ts": {
            "value": "2022-01-02 13:59:599"
        }
    }
}
'''

##### PUT & POST data

Request:
'''json
{
    "first name": "Rory",
    "last name": "Houlihan",
    "email": "me@myemail.com"
}
'''

Response: Same as GET

##### DELETE data

Request: None
Response:
'''josn
{
    "status": "ok",
    "message": "resource deleted"
}
'''

#### Resource Collection

##### GET data

Response:
'''json
{
    "status": "ok",
        "data": [
                {
                    "link": {
                        "value": "https://www.secret-santa-picker/api/v1/users/12345",
                    },
                    "id": {
                        "value": "12345",
                    },
                    "name": {
                        "first": "Rory",
                        "Last": "Houlihan"
                    },
                    "email": {
                        "value": "me@myemail.com"
                    },
                    "created_ts": {
                        "value": "2022-01-01 13:30:345"
                    },
                    "updated_ts": {
                        "value": "2022-01-02 13:59:599"
                    }
                },
        ...
        ]
}
'''

---

## Groups

### Methods and Endpoints

/groups
    - GET - get all groups
    - PUT - create a new group

/groups/<id>
    - GET - get a single group resource
    - POST - update a single groups data - must supply all pieces of data
    - Delete - delete a single group

### Data

#### Single Resource

##### GET data

Response
'''json
{
    "status": "ok",
    "data": {
        "link": {
            "value": "https://www.secret-santa-picker.com/api/v1/groups/12345"
        }
        "id": {
            "value": "12345",
        },
        "name": {
            "value": "Houlihan Family Secret Santa"
        },
        "owner": {
            "value": "12345",
            "link": {
                "value": "https://www.secret-santa-picker/api/v1/users/12345"
            }
        },
        "created_ts": {
            "value": "2022-01-01 13:30:345"
        },
        "updated_ts": {
            "value": "2022-01-02 13:59:599"
        }
    }
}
'''

##### PUT & POST data

Request:
'''json
{
    "name": "My Company Secret Santa Group",
    "owner": "12345",
}
'''

Response: Same as GET

##### DELETE data

Request: None
Response:
'''josn
{
    "status": "ok",
    "message": "resource deleted"
}
'''

#### Resource Collection

##### GET data

Response:
{
    "status": "ok",
    "data": [
       {
            "link": {
                "value": "https://www.secret-santa-picker.com/api/v1/groups/12345"
            }
            "id": {
                "value": "12345",
            },
            "name": {
                "value": "Houlihan Family Secret Santa"
            },
            "owner": {
                "value": "12345",
                "link": {
                    "value": "https://www.secret-santa-picker/api/v1/users/12345"
                }
            },
            "created_ts": {
                "value": "2022-01-01 13:30:345"
            },
            "updated_ts": {
                "value": "2022-01-02 13:59:599"
            }
        },
        ...
    ]
}


## Users groups

### Methods and Endpoints

/users/<id>/groups
    - GET - get a list of groups for a single user

### data

#### Resource Collection

{
    "status": "ok",
    "data" {
        "user": {
            "value": "12345",
            "link": "https://www.secret-santa-picker.com/api/v1/user/12345"
        },
        "groups": [
            {
                "value": "12345",
                "link": "https://www.secret-santa-picker.com/api/v1/groups/12345"
            },
            ....
        ]
    }
}


## Groups Users

### Methods and Endpoints

/groups/<id>/users

##
/groups/<id>/pairing/<year>


