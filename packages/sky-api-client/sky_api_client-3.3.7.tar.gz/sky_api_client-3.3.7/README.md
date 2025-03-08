# Sky Api Client

Python client for RENXT APIs.

Developed by Uddesh at [Almabase](https://almabase.com)

## Installation

```
pip install sky_api_client
```

## Examples

1. Initialize the client

```python
from sky_api_client import SkyApi

sky_api = SkyApi('subscription_key', 'access_token')
```

2. Get list of all constituent

```python
list = sky_api.constituent.list()
```

## Available methods

1. List all constituents

```python
list = sky_api.constituent.list()
```

2. Get a specific constituent

```python
constituent = sky_api.constituent.get('constituent_id')
```

3. Create a new constituent

```python
new_constituent = sky_api.constituent.create({'first': '', 'last': ''})
```

4. Update an existing constituent

```python
updated_constituent = sky_api.constituent.update('constituent_id' ,{'first': '', 'last': ''})
```

5. Delete a constituent

```python
sky_api.constituent.delete('constituent_id')
```

6. List all entity constituents

```python
sky_api.address.list('constituent_id')
```

## Available Entities and Methods

1. address
   - list
   - get
   - create
   - update
   - delete
   - types
2. code_table
   - list
   - get
   - create
   - update
   - delete
3. constituent
   - list
   - get
   - create
   - update
   - delete
   - search
4. custom_field_category
   - list
5. custom_fields
   - list
   - create
   - update
   - delete
6. education
   - list
   - get
   - create
   - update
   - delete
7. email_addresses
   - list
   - create
   - update
   - delete
   - types
8. phone
   - list
   - get
   - create
   - update
   - delete
   - types
9. relationship
   - list
   - get
   - create
   - update
   - delete
10. table_entry
    - list
    - get
    - create
    - update
    - delete
11. subscription_webhook
    - list
    - get
    - create
    - delete
12. online_presence
    - list
    - create
    - get
    - update
    - delete
    - types
13. constituent_address
    - list
14. constituent_custom_field
    - list
15. constituent_education
    - list
16. constituent_email_address
    - list
17. constituent_online_presence
    - list
18. constituent_phone
    - list
19. constituent_relationship
    - list
20. action
    - list
    - create
    - get
    - update
    - delete
    - types
    - list_all
21. action_status
    - list

These entities can be used same as above example for `constituent`.

```python
email_address_list = sky_api.email_addresses.list()
```

> Note:- Current version doesn't have refresh token functionality.

# Updating Version

```
$ semversioner add-change --type patch --description "description for the change"
$ ./release
```
