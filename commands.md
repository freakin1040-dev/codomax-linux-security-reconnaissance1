# Linux Fundamentals — Command Reference

| Command | Meaning | Example |
|---|---|---|
| `pwd` | Print current directory | `pwd` |
| `ls -la` | List files, including hidden files | `ls -la` |
| `whoami` | Current username | `whoami` |
| `mkdir lab` | Create a directory | `mkdir lab` |
| `cd lab` | Change directory | `cd lab` |
| `touch notes.txt` | Create an empty file | `touch notes.txt` |
| `cp a.txt b.txt` | Copy a file | `cp notes.txt copy.txt` |
| `mv a.txt b.txt` | Rename/move a file | `mv copy.txt old-copy.txt` |
| `cat notes.txt` | Print file content | `cat notes.txt` |
| `id` | Show UID, GID, and groups | `id` |
| `groups` | Show group memberships | `groups` |
| `ps` | Show processes attached to terminal | `ps` |
| `ps aux` | Show system process list | `ps aux` |
| `top` | Interactive process monitor | `top` (`q` exits) |

## Demonstrated in the learner's screenshot
- `pwd` returned `/home/srikr123`.
- `whoami` returned `srikr123`.
- Created directory `internship`.
- Entered `~/internship`.
- Created `notes.txt`.
- `ls -l` displayed the file with initial mode `-rw-r--r--`.
- `id` displayed the learner's UID, GID, and supplementary groups.

One mistyped command (`ls -`) returned an error; the learner corrected it with `ls -l`. This is normal command-line practice.
