
#Bashplates	

#### Author 
Peter Malmberg  <peter.malmberg@gmail.com>
#### Licence
MIT
#### Description
Bashplates is a template to ease rapid development of bash shellscripts.

## Features
- Handler for commands
- Built in Documantation handling of commands
- logfile function
- Simple error/message handling
- Check if root user
- Check for required programs
- lock file feature
- Trap handling
- Cleanup handling
- ANSI Color codes


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
- ##    Documentation tag for userdefined function
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
 - `bpm`       bashplate project management script
 - `history.txt` history file 
 - `README.md` this documentation

# TODO
- Add verbose option
- Add variable documentation option.
- Use logrotate for logs
- Mail feature


# Bash scripting tips and tricks

- Use long options when scripting(`ls --all` vs`ls -a`). This makes
  readabilty much easier and you will reduce serching documentation
	to understand what yout code does.
- Use {} to surround your variables to avoid name confusion.
  
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





