
#Bashplates	

#### Author 
Peter Malmberg  <peter.malmberg@gmail.com>
#### Licence
MIT
#### Description
Bashplates is a template to ease rapid development of bash shellscripts.

## Features
- Handler for subcommands
- Built in Documantation handling of subcommands
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

BP has a very simple but effective documentation feature
A user defined subcommand is simply documented as shown below with a
double hash. When invoking `scriptname help` the text after will be
shown as the description for that function. 

```bash
myFunction() { ## Command description
  do-stuff
}
```

### Script documentation
- ##    Documentation tag for userdefined function
- ##D   Documentation tag for internal functions
- ##C   Conditional documentation tag
- ##-   Separator line tag


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
  
# Links to informative sites

[(https://gist.github.com/KylePDavis/3901321)]

[2](https://gist.github.com/KylePDavis/3f8c511838a36f2528d7)

[3](http://natelandau.com/boilerplate-shell-script-template/)

[4](http://linuxcommand.org/lc3_new_script.php)

http://kvz.io/blog/2013/11/21/bash-best-practices/

https://github.com/kvz/bash3boilerplate/blob/master/main.sh

https://www.quora.com/What-are-the-best-practices-for-writing-shell-scripts
