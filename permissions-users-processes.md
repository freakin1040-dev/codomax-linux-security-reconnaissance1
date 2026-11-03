# Permissions, Users, Groups, and Processes

## File permissions
Linux permission symbols:
- `r` read = 4
- `w` write = 2
- `x` execute = 1

Permission digits are added for each class:
- `7` = `rwx` (4+2+1)
- `5` = `r-x` (4+1)
- `4` = `r--`

Example:
```bash
chmod 755 notes.txt
ls -l notes.txt
```
Expected mode for a regular file: `-rwxr-xr-x`. Use this only on a practice file.

## Users and groups
```bash
whoami
id
groups
```
`whoami` shows the current username. `id` shows numeric user/group IDs and group memberships. `groups` lists group names.

## Processes
```bash
ps
ps aux
top
```
`ps` gives a process snapshot. `ps aux` gives a broader process listing. `top` updates process information interactively; press `q` to quit.

## Administrator privileges
```bash
sudo whoami
```
If the account is permitted to use sudo, the command should print `root`. Use elevated privileges only when required.
