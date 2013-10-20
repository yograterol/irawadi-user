============
Irawadi User
============

Python Library for manage system user in Linux.

Examples
========

```python
from irawadi_user import ManageUser
obj = ManageUser()

# For check a user or group
obj.exists(user='example') # or obj.exists(group='example')
```

Create a user
-------------

```python
obj.create(**kwargs)
"""Method for create users in the system.
    Arg:
        **kwargs:
            b: base directory for the home directory of
                   the new account.
            c: GECOS field of the new account.
            d: home directory of the new account.
            g: name or ID of the primary group of the new account.
            m: create the user's home directory.
            M: do not create the user's home directory.
            N: do not create a group with the same name as the user.
            p: password of the new account.
            s: login shell of the new account.
            u: user ID of the new account.
            user: User name.
    Return:
        True: If all is ok.
        False: If the user is't create.
    Exception:
        UserExist
"""
```

Update a user password
-------------

```python
obj.update_password(**kwargs)
"""Change the user password.

    Arg:
        **kwargs:
            user: The user name.
            password: The user password
    Return:
        True: If the user exist.
        False: If the user don't exist.
    Exception:
        UserNotExist
"""
```

Delete a user 
-------------

```python
obj.delete(user)
"""Delete a user system.
    Arg:
        **kwargs:
            user: The user name.
    Return:
        True: If the user is deleted.
        False: If the user is't deleted.
    Exception:
        UserNotExist
"""
```
