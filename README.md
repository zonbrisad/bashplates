
#Bashplates	

#### Author 
Peter Malmberg  <peter.malmberg@gmail.com>
#### Licence
MIT
#### Description
Bashplates is a small collection of templates to speed the development
of bash shellscripts.

## Features
- ANSI Color codes
- Handler for subcommands
- A simple message log function
- Simple error/message handling
- Check if root user
- Check for required programs
- lock file feature
- Trap handling
- Cleanup handling

## Files
A template for shellscripts with subcommands. It contains a help
command that parses itself for documentation. 

## Built in commands
- help    - Help information
- ihelp   - Help information about internal commands
- log     - View log 
- version - version information
- info    - show various script information
 
## Documentation

### Add new command to file
Adding a new documented command to a script is very easy.

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


## TODO
- Add verbose option


### Links to informative sites

[1](https://gist.github.com/KylePDavis/3901321)
[2](https://gist.github.com/KylePDavis/3f8c511838a36f2528d7)
[3](http://natelandau.com/boilerplate-shell-script-template/)
[4](http://linuxcommand.org/lc3_new_script.php)