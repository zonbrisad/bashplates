
#Bashplates	

-------------------------------------------------------------------------
Author: Peter Malmberg  <peter.malmberg@gmail.com>
Licence: MIT

Description:
Bashplates is a small collection of templates to speed the development
of bash shellscripts.
-------------------------------------------------------------------------


## Files
A template for shellscripts with subcommands. It contains a help
command that parses itself for documentation. 

## Built in services
- ANSI Color codes
- Handler for subcommands
- A simple message log function
- Simple error/message handling
- Check if root user
- Check for required programs
- lock file feature
- Trap handling
- Cleanup handling


## Built in commands
- help    - Help information
- log     - View log 
- version - version information
- info    - show various script information


## TODO
- Add documentation to internal function/variables
- Conditional display of log command

## Documentation

### Add new command to file
Adding a new documented command to a script is very easy.

```bash
myFunction() { ## Command description
  do-stuff
}
```

### Links to informative sites

[1](https://gist.github.com/KylePDavis/3901321)
[2](https://gist.github.com/KylePDavis/3f8c511838a36f2528d7)
[3](http://natelandau.com/boilerplate-shell-script-template/)
[4](http://linuxcommand.org/lc3_new_script.php)
