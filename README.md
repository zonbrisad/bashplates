
# Bashplates

![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) 

#### Author 
Peter Malmberg  <peter.malmberg@gmail.com>
#### License
MIT


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

  - [About](#about)
  - [Features](#features)
  - [Requirements](#requirements)
    - [Runtime](#runtime)
    - [Development](#development)
  - [Download and Installation](#download-and-installation)
    - [Download](#download)
    - [Installation](#installation)
    - [Bashplate settings](#bashplate-settings)
  - [Getting started](#getting-started)
    - [bp command](#bp-command)
    - [Create new script](#create-new-script)
  - [Built in commands](#built-in-commands)
  - [Internal(hidden) commands](#internalhidden-commands)
    - [ihelp](#ihelp)
    - [iinfo](#iinfo)
    - [`iview`](#iview)
    - [ivars](#ivars)
  - [Examples](#examples)
  - [Documentation](#documentation)
    - [Documentation tags](#documentation-tags)
    - [Standard subcommand function documentation](#standard-subcommand-function-documentation)
    - [Conditional subcommand function documentation](#conditional-subcommand-function-documentation)
  - [Log](#log)
    - [Activate log feature](#activate-log-feature)
    - [Usage](#usage)
    - [View log](#view-log)
    - [Monitor log](#monitor-log)
  - [Files](#files)
  - [History](#history)
  - [TODO](#todo)
  - [References and tutorials](#references-and-tutorials)
- [Example scripts](#example-scripts)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



## About

Bashplates is a tool for quickly creating advanced and feature rich shellscripts. It is essentialy a template that provides a number of selfcontained features like subcommand handler, documentation parser, logging, pretty printouts etc.. 


## Features (not exhaustive)

- Subcommand handler
- Documentation parser
- Error/message handling
- Logfile 
- Configuration file 
- Lock file 
- Signal traps
- File operations (cp, mv, rm, etc)
- File editing 
- User input
- Execution hooks
- Few external dependencies (grep, sed, awk, date, tail, tput)


## Requirements

### Runtime
- bash
- basic commands like grep, sed, awk, date, tail etc

### Development
- shellcheck

## Download and Installation

### Download

Bashplates is available at [github](https://github.com/zonbrisad/bashplates.git).

```bash
$ git clone https://github.com/zonbrisad/bashplates.git
```

### Installation

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
The following output should appear.

![alt text][bp]


### Bashplate settings
Bashplates does have some configuration settings. To view these settings use the `bp info` command as below.

```bash
$ bp iinfo
```
![alt text][bp-info]

Set your personal like below.

```bash
$ bp BP_NAME "John Doe"
$ bp BP_EMAIL "john.doe@foo.bar"
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
- log     - View log file
- mlog    - View log file live
- version - Show version information

## Internal(hidden) commands
All bashplates based scripts have four internal "hidden" commands who all start with
the letter i. These commands are always hidden to the user and are
there as a aid the developer. The commands are `ihelp` `iinfo` `iview` `ivars`.

### ihelp
`ihelp` is by far the most important internal command. It reveals all
internal commands and all internal functions. 

```bash
$ bp ihelp bpRead
```

### iinfo
`iinfo` presents various information about the script

### `iview`
`iview` 

### ivars
List all internal variables.


## Examples
Included in the package is an example command `bpexample`. 


## Documentation

BP has a very simple tag based documentation feature that is acivated 
when invoking `scriptname help` subcommand. It will output formated list of all subcommands available and a short description of their function.
 
### Documentation tag
- ##D   Documentation tag for internal functions
- ##C   Conditional documentation tag
- ##-   Separator line tag


### Standard subcommand function documentation
In the example below the standard way to document a command function is shown.

```bash
myCommand() { ##D Command description
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

## Log

BP has an builtin log feature. It can be activated by uncommenting the `BP_LOGFILE` variable in the settings section.

```bash
##V logfile (uncomment to use logfile)
BP_LOGFILE=${BP_SELF_DIR}/${BP_SELF}.log
```

Many builtin functions like fileoperations and queries will now automaticly log their actions to file


### Usage

To log a message to file use any of the commands below. 
```bash
bpLogOk       "msg"
bpLogInfo     "msg"
bpLogWarning  "msg"
bpLogError    "msg"
bpLogCritical "msg"
```

It is also possible to log via the following commands. In additiont to
log a message to a logfile these commands will also print the message
on the terminal.

```bash
bpOk       "msg"
bpInfo     "msg"
bpWarning  "msg"
bpError    "msg"
bpCritical "msg"
```
						
### View log

There is a builtin log view command that will colorize output for
easier interpretation.

```bash
$ bpexample log
```
![alt text][bp-log]


### Monitor log

To monitor the logfile simply enter the "mlog" command and `tail` will be run on the logfile

```bash
  bpexample mlog
```

## Files

- `bpexample  ` example bashplate script
- `templates/bashplate` bashplate template
- `bp`        bashplate project management script
- `doc/HISTORY.md` history file 
- `README.md` this documentation


## History

[HISTORY.md](/doc/HISTORY.md)

## Bugs
- [ ] bpEscapeFilter does not work correctly
- [x] bpPrintDesc zero length description bug
- [ ] bpPrintDesc formats key/desc wrong when including terminal characters in key
- [ ] Fixing bpExit code handling in subcommand dispatcher

## TODO
- [ ] Add option parser
- [ ] Add verbose/debug option
- [ ] Add quiet option
- [ ] Add color suppression option
- [ ] Add warning/guard question(Are you sure?) to bpReadBool question (bpReadGuardBool?)
- [X] Add override editor for "ied" command
- [ ] Add trim string function
- [x] Select from list function
- [x] Merge bpLine and bpTextLine to bpPrintLine
- [x] Reformat messages to "straigt columns"
- [x] rename bpRead to bpReadStr(ing)
- [x] rename all bpRead?? to more apropriate
- [x] Change color of time and date in log view command from green/dark green to something else t.ex. magenta
- [x] Add keyword change function to bpdev
- [ ] Add color theme override to setup file
- [x] Format/fold long description texts
- [x] Remove settings command and include it into bpset
- [ ] Update bpAssertProg to using bpHasCmd
- [ ] A more comprahensive cheat sheet
- [ ] Add exit codes to cheat sheet https://www.redhat.com/sysadmin/exit-codes-demystified
- [ ] multi column output (cheat sheet)
- [x] Logg query answers
- [x] Add color to queries


## Sugestions
 - Plugin system
 - automatic completion generator
 - Mail feature
 - dictionary functions?
 - Use logrotate for logs
 - Rename iview to iv
 - Rename ivars to ivar or iva 
 - Rename iinfo to ii
 - Rename icheck to ic
 - Allow dynamic generation of subcommands via for example a generator function
 - History cache for Query commands to allow questions to remember
   answers between runs
 - Rewrite hook system to elliminate hook variables

## References and tutorials

[Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html#Programmable-Completion)
[Internal Variables](https://tldp.org/LDP/abs/html/internalvariables.html)
[BASH arithmetics](https://www.shell-tips.com/bash/math-arithmetic-calculation/#gsc.tab=0)
[Best Practices for Writing Bash Scripts](http://kvz.io/blog/2013/11/21/bash-best-practices/)
[What are the best practices for writing shell scripts?](https://www.quora.com/What-are-the-best-practices-for-writing-shell-scripts)
[Command completion](https://opensource.com/article/18/3/creating-bash-completion-script)

# Example scripts

[Simple bash shell script template](https://gist.github.com/KylePDavis/3901321)
[bashsimplecurses](https://github.com/metal3d/bashsimplecurses)
[BOILERPLATE SHELL SCRIPT TEMPLATE](http://natelandau.com/boilerplate-shell-script-template/)
[bash3boilerplate](https://github.com/kvz/bash3boilerplate/blob/master/main.sh)
[Self-contained auto-updating rsync-based backup script](https://gist.github.com/KylePDavis/3f8c511838a36f2528d7)
[This is a shell script template generator](http://linuxcommand.org/lc3_new_script.php)
[Charm gum](https://github.com/charmbracelet/gum)

[bp]: https://github.com/zonbrisad/bashplates/raw/master/doc/bp.png "bp"
[bp-ihelp]: https://github.com/zonbrisad/bashplates/raw/master/doc/bp-ihelp.png "bp ihelp"
[bp-ihelp-cmd]: https://github.com/zonbrisad/bashplates/raw/master/doc/bp-ihelp-cmd.png "bp ihelp bpRead"
[bp-vhelp]: https://github.com/zonbrisad/bashplates/raw/master/doc/bp-vhelp.png "bp vhelp"
[bp-info]:  https://github.com/zonbrisad/bashplates/raw/master/doc/bp-info.png "bp info"
[bp-log]:https://github.com/zonbrisad/bashplates/raw/master/doc/bp-log.png "bp log"
