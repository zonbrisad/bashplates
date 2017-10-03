
# Bashplates	

#### Author 
Peter Malmberg  <peter.malmberg@gmail.com>
#### License
MIT
#### Description
Bashplates is a bash scipt template to enabel quick development of
subcommandbased shellscripts.

## Features
- Handler for commands
- Built in Documantation handling of commands (help command)
- logfile function
- Simple error/message handling
- Check if root user
- Check for required installed programs
- lock file feature
- Trap handling
- Cleanup handling
- ANSI Color codes
- Numerous internal variables setup on default
- Execution hooks
- default function

## Built in commands
- help    - Show help information about user define subcommands + some internal commands
- ihelp   - Help information about internal commands
- log     - View log file
- version - Show version information
- info    - show various script information (for debug use)
 
## Documentation

BP has a very simple tag based documentation feature that is acivated 
when invoking `scriptname help` subcommand. It will output formated list of all subcommands
and a short description of their function.
 

### Documentation tags
- *##*    Documentation tag for userdefined function
- ##D   Documentation tag for internal functions
- ##C   Conditional documentation tag
- ##-   Separator line tag


### Standard subcommand function documentation
In the example below the standard way to document a command function is shown.

```bash
myCommand() { ## Command description
  do-stuff
}
```

### Conditional subcommand function documentation
In the example below the description will only appear if MYVAR is declared.

```bash
myCommand() { ##C MYVAR Command description
  do-stuff
}
```

## Installation

Bashplates can be installed on your system to enable rapid creation of
new scripts. 
There are two install options.
- install
- install-local


### Download

Get bashplates from github with the following command.

```bash
$ git clone https://github.com/zonbrisad/bashplates.git
```


### Local installation

Local installation will install bp on your personal useraccount. It is
convenient if you do not have root access on the machine you are
installing it on.

```bash
$ cd bashplates
$ ./bp install-local
```

Make sure that ~/bin is in the path.


### System wide installation

This option will install bp system wide. Bp will in this way be
available to all users. Requires root access. 

```bash
$ cd bashplates
$ sudo ./bp install
```

Make sure that /usr/local/bin is in the path.


## Create new script

To create a new script type the command bellow.  The new script will
be created in the directory you are currently standing in.

```bash
$ bp new
```

# Files
 - `example  ` example bashplate script
 - `bashplate` bashplate template
 - `bp`        bashplate project management script
 - `history.txt` history file 
 - `README.md` this documentation

# TODO
- Add verbose option
- Add variable documentation option.
- Use logrotate for logs
- Mail feature
- Remove option


# References and tutorials

[Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html#Programmable-Completion)

[Best Practices for Writing Bash Scripts](http://kvz.io/blog/2013/11/21/bash-best-practices/)

[What are the best practices for writing shell scripts?](https://www.quora.com/What-are-the-best-practices-for-writing-shell-scripts)


# Example scripts

[Simple bash shell script template](https://gist.github.com/KylePDavis/3901321)

[BOILERPLATE SHELL SCRIPT TEMPLATE](http://natelandau.com/boilerplate-shell-script-template/)

[bash3boilerplate](https://github.com/kvz/bash3boilerplate/blob/master/main.sh)

[Self-contained auto-updating rsync-based backup script](https://gist.github.com/KylePDavis/3f8c511838a36f2528d7)

[This is a shell script template generator](http://linuxcommand.org/lc3_new_script.php)

