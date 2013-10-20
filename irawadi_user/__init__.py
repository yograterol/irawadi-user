""":mod:`irawadi_user` --  Python Library for manage system user in Linux.
   :author: Yohan Graterol (yograterol@fedoraproject.org)
"""
import subprocess as sub
import crypt


class UserExist(Exception):

    def __str__(self):
        return repr("User exist in the system.")


class UserNotExist(Exception):

    def __str__(self):
        return repr("User don't exist in the system.")


class GroupExist(Exception):

    def __str__(self):
        return repr("Group exist in the system.")


class GroupNotExist(Exception):

    def __str__(self):
        return repr("Group don't exist in the system.")


class ManageUser(object):
    cmd_exists_user = 'egrep "^{username}" /etc/passwd'
    cmd_exists_group = 'egrep "^{groupname}" /etc/group'

    def __init__(self):
        super(ManageUser, self).__init__()

    def _exec_command(self, cmd):
        action = sub.Popen(cmd, stdout=sub.PIPE, shell=True)
        (output, error) = action.communicate()
        return error or output

    def exists(self, **kwargs):
        """Check if exist a user or group in the system.

        Arg:
            **kwargs:
                user: The user name.
                group: The group name.
        Return:
            True: If the user exist.
            False: If the user don't exist.
        """
        cmd = ""

        if 'user' in kwargs:
            cmd = self.cmd_exists_user.format(username=kwargs['user'])
        elif 'group' in kwargs:
            cmd = self.cmd_exists_group.format(groupname=kwargs['group'])

        result = self._exec_command(cmd)
        if result:
            return True
        else:
            return False

    def create(self, **kwargs):
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
        if not self.exists(user=kwargs['user']):
            if 'p' in kwargs:
                kwargs['p'] = crypt.crypt(kwargs['p'], "22")
            cmd = 'adduser'

            for key, value in kwargs.iteritems():
                if not key is 'user':
                    cmd = cmd + ' -' + str(key) + ' ' + str(value)
                else:
                    cmd = cmd + ' ' + value

            self._exec_command(cmd)

            if self.exists(user=kwargs['user']):
                return True
            else:
                return False
        else:
            raise UserExist()

    def update_password(self, **kwargs):
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
        if self.exists(user=kwargs['user']):
            proc = sub.Popen(['passwd', kwargs['user'], '--stdin'], stdin=sub.PIPE)
            proc.stdin.write(kwargs['password'] + '\n')
            proc.stdin.write(kwargs['password'])
            proc.stdin.flush()
            return True
        else:
            raise UserNotExist()

    def delete(self, user):
        """Delete a user system.

        Arg:
            **kwargs:
                user: The user name.
        Return:
            True: If the user is deleted.
            False: If the user is't deleted.
        """
        if self.exists(user=user):
            cmd = 'userdel -r -f ' + user
            self._exec_command(cmd)
            return True
        else:
            raise UserNotExist()

    def create_group(self, group):
        """Create the group in the system.

        Arg:
            group: The group name.
        Return:
            True: If the group is created.
        Exception:
            GroupExist
        """
        if self.exists(group=group):
            cmd = 'groupadd', group
            self._exec_command(cmd)
            return True
        else:
            raise GroupExist()

    def update_group(self, **kwargs):
        """Modify the data group.

        Arg:
            **kwargs:
                g: The group ID of the given GROUP will be changed to GID.
                n: New group name.
                group: The group name.
        Return:
            True: If the group is updated.
        Exception:
            GroupNotExist
        """
        if self.exists(group=kwargs['group']):
            cmd = 'groupmod'

            for key, value in kwargs.iteritems():
                if not key is 'group':
                    cmd = cmd, '-' + str(key), str(value)
                else:
                    cmd = cmd, value

            self._exec_command(cmd)
            return True
        else:
            raise GroupNotExist()

    def delete_group(self, group):
        """Delete the group.

        Arg:
            group: The group name.
        Return:
            True: If the group is deleted.
        Exception:
            GroupNotExist
        """
        if self.exists(group=group):
            cmd = 'groupdel', group

            self._exec_command(cmd)
            return True
        else:
            raise GroupNotExist()
