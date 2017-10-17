
# Bashplates	

#### Author 
Peter Malmberg  <peter.malmberg@gmail.com>
#### License
MIT
#### Description
Bashplates is a bashscript template generator to enable rappid development of
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


## Installation

### Download

Get bashplates from github with the following command.

```bash
$ git clone https://github.com/zonbrisad/bashplates.git
```

### Setting up environment

In order to use Bashplate the enivronment needs to be setup properly.
This is done by "sourcing" the `bp_init` script located in the project directory. For convenience
simply call the `bp_init` script in your .bashrc file.

```bash
$ source path_to_bashplates/bp_init
```

If everything is setup correctly test it by entering the `bp` command.
```bash
$ bp
```
Reference-style: 
![alt text][bp]

[bp]: https://github.com/zonbrisad/bashplates/doc/bp.png "bp command"


### Bashplate settings
Bashplates does have some configuration settings. To view these settings use the `bp info` command as below.

```bash
$ bp info
```

Set your personal like below.

```bash
$ bp setname "John Doe"
$ bp setemail "john.doe@foo.bar"
```

## Getting started

### bp command
The bp command is the main command that is used for creating new scripts, make sure it is working. Se Install section if not.

### Create new script

To create a new script type the command bellow.  The new script will
be created in the directory you are currently standing in.

```bash
$ bp new
```

## Built in commands
- help    - Show help information about user define subcommands + some internal commands
- ihelp   - Help information about internal commands
- vhelp   - Help information about internal variables
- log     - View log file
- mlog    - View log file live
- version - Show version information
- info    - show various script information 
 
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


# Files
 - `example  ` example bashplate script
 - `bashplate` bashplate template
 - `bp`        bashplate project management script
 - `history.txt` history file 
 - `README.md` this documentation

# TODO
- Add verbose option
- Use logrotate for logs
- Mail feature

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

