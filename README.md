
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
- [Features (not exhaustive)](#features-not-exhaustive)
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
  - [iview](#iview)
  - [ivars](#ivars)
- [Examples](#examples)
- [Documentation](#documentation)
  - [Documentation tag](#documentation-tag)
  - [Standard subcommand function documentation](#standard-subcommand-function-documentation)
  - [Conditional subcommand function documentation](#conditional-subcommand-function-documentation)
- [Log](#log)
  - [Usage](#usage)
  - [View log](#view-log)
  - [Monitor log](#monitor-log)
- [Files](#files)
- [History](#history)
- [Bugs](#bugs)
- [TODO](#todo)
- [Sugestions](#sugestions)
  - [Less priority sugestions](#less-priority-sugestions)
- [Documentation overhaul(again)](#documentation-overhaulagain)
  - [Sugestion 1](#sugestion-1)
- [References and tutorials](#references-and-tutorials)
- [Example scripts](#example-scripts)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## About

Bashplates is a tool for quickly creating advanced and feature rich shellscripts. It is essentialy a template that provides a number of selfcontained features like subcommand handler, documentation parser, logging, pretty printouts etc..

## Features (not exhaustive)

- Subcommand handler
- Documentation parser
- Error handling
- Message output
- Logfile
- Configuration file
- Lock file
- Signal traps
- File operations (cp, mv, rm, etc)
- File editing
- User input
- Execution hooks
- Few external dependencies (grep, sed, awk, date, tail, tput, fold)

## Requirements

### Runtime

- bash
- basic commands like grep, sed, awk, date, tail, tput, fold etc

### Development

- shellcheck

## Download and Installation

### Download

Bashplates is available at [github](https://github.com/zonbrisad/bashplates.git).

```bash
git clone https://github.com/zonbrisad/bashplates.git
```

### Installation

In order to use Bashplate the enivronment needs to be setup properly.
This is done by "sourcing" the `bp_init` script located in the project directory. For convenience
simply call the `bp_init` script in your .bashrc file.

```bash
source path_to_bashplates/bp_init
```

If everything is setup correctly test it by entering the `bp` command.

```bash
bp 
```

The following output should appear.

![alt text][bp]

### Bashplate settings

Bashplates does have some configuration settings. To view these settings use the `bp info` command as below.

```bash
bp iinfo
```

![alt text][bp-info]

Set your personal like below.

```bash
bp BP_NAME "John Doe"
bp BP_EMAIL "john.doe@foo.bar"
```

## Getting started

### bp command

The bp command is the main command that is used for creating new scripts, make sure it is working. Se Install section if not.

### Create new script

To create a new script type the command bellow.  The new script will
be created in the directory you are currently standing in.

```bash
bp new
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
bp ihelp bpRead
```

### iinfo

`iinfo` presents various information about the script

### iview

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
bpexample log
```

![alt text][bp-log]

### Monitor log

To monitor the logfile simply enter the "mlog" command and `tail` will be run on the logfile

```bash
  bpexample mlog
```

## Files

- `bpexample` example bashplate script
- `templates/bashplate` bashplate template
- `bp`        bashplate project management script
- `doc/HISTORY.md` history file
- `README.md` this documentation

## History

[HISTORY.md](/doc/HISTORY.md)

## Bugs

- [x] bpEscapeFilter does not work correctly
- [x] bpPrintDesc zero length description bug
- [ ] bpPrintDesc formats key/desc wrong when including terminal characters in key
- [ ] Fixing bpExit code handling in subcommand dispatcher
- [ ] Fix PRE_SCRIPT_HOOK
- [x] `bp ascii` rows missing with 4 columns, columnize.py seems to be the problem
- [ ] `bp asciie` show missaligned columns
- [x] bp cs witch four column output looses rows
- [x] bp command completion does not work correct in some terminals (gnome terminal)

## TODO

- [ ] Add option parser
- [ ] Add verbose ??
- [ ] Add debug option
- [ ] Add quiet option
- [ ] Add color suppression option
- [ ] Add warning/guard question(Are you sure?) to bpReadBool question (bpReadGuardBool?)
- [X] Add override editor for "ied" command
- [ ] Add trim string function
- [ ] Add idiff internal command
- [ ] Add bpInfo message to bpMkDir and bpLn if file/link already exists
- [ ] Add a BP_TEMPLATE variable pointing to main bashplate template
- [ ] Add a log complete command command, like bpExecLog that logs the entire command string and exit code
- [ ] Add color theme override to setup file
- [ ] Add commenttype that is always dissabled but visible, like comment or "to be implemented" something like ##DN or ##DV
- [ ] Add errorcodes in cleartext in a large table
- [ ] Add basic regex cheatsheet
- [ ] Add basic BASH pattern matching cheatsheet
- [ ] Add cheatsheet for loops (for, while etc)
- [ ] Add brace expansion to cheatsheet <https://www.howtogeek.com/725657/how-to-use-brace-expansion-in-linuxs-bash-shell/>
- [x] Add internal BASH variables to cheatsheet  <https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html>
- [x] Add documentation of builtin commands to bp cheatsheet <https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html>
- [ ] Rename bpHasCmd to something like bpIsCmd/bpIsCommand see bpIsFunction
- [ ] Rename bpRemoveLineContainging to bpRemoveLine to better match bpReplaceLine
- [ ] Rename bpCallStack to bpPrintCallStack
- [x] Select from list function
- [x] Merge bpLine and bpTextLine to bpPrintLine
- [x] Reformat messages to "straigt columns"
- [x] rename bpRead to bpReadStr(ing)
- [x] rename all bpRead?? to more apropriate names
- [x] Change color of time and date in log view command from green/dark green to something else t.ex. magenta
- [x] Add keyword change function to bpdev
- [x] Format/fold long description texts
- [x] Remove settings command and include it into bpset
- [x] Update bpAssertProg to using bpHasCmd
- [x] A more comprehensive cheat sheet
- [x] Add exit codes to cheat sheet <https://www.redhat.com/sysadmin/exit-codes-demystified>
- [x] multi column output (cheat sheet)
- [x] Logg query answers
- [x] Add color to queries
- [ ] Logg exit code of executed commands
- [ ] logg when bpRun i called
- [ ] Added BP_SELF_NAME, to eventually replace BP_SELF
- [ ] Change BP_SELF to $BP_SELF_DIR/$BP_SELF_NAME, for clarity
- [ ] Declare local variables local by using local keyword `local MY_VAR=XXX`
- [ ] improved error/crash information printout <https://unix.stackexchange.com/questions/39623/trap-err-and-echoing-the-error-line>
- [ ] Improve output from bpCallStack
- [x] ascii table in hex
- [ ] Rewrite hook system to elliminate hook variables
- [ ] Rewrite bpFilterEscape so to not use external sed, if possible
- [ ] Rewrite bpColorizeUrl so to not use external sed, if possible
- [ ] Enable extended patternmatching `shopt -s extglob` per default
- [ ] Rename colors
- [ ] Remove/reduce usage of sed in favour of builtin filtercapabilties
- [ ] Add multicolumn output to ihelp
- [ ] Add line number to debug printout to show linenr from witch call was done, use BASH_LINENO and FUNCNAME
- [x] Replace extended ASCII table with something more sensible

## Sugestions

- Plugin system
- Automatic command completion generator
- Rename iview to iv
- Rename ivars to ivar or iva
- Rename iinfo to ii
- Rename icheck to ic
- Allow dynamic generation of subcommands via for example a generator function
- History cache for Query commands to allow questions to remember
   answers between runs
- move code from bp_init to bp
- presentation mode that shows separated in/out data in hex
- Enable certain commands as bpMkDir, bpLn, bpRm, bpMv, bpReplace, bpReplaceLine, bpRemoveLineContaining to execute as root using a variable like bpSudo=true
- Rename bpRun to bpDo and bpSudo
- Rename bpPrindDesc to bpPrintKeyVal
- Shift parameters(left) sent to command functions using shift to allow commandfunctions to be used internaly
- Built in support for setting terminal header via xtype
- make a function accessable but hidden from help view
- What about merging bpUserSettings() and bpInitSettings()

### Less priority sugestions

- make columnize.py to a sepparate project
- dictionary abstract datatype
- Mail feature
- Use logrotate for logs

## Documentation overhaul(again)

The documentation system is confusing and not particularly consistent. A new revised model is needed.

### Sugestion 1

- ##F for function documentation
- ##I for internal documentation
- ##- For line documentation
- ##V for variable documentation

Behaviour can be changed with different suffixes.

- C for conditional display.
A conditional function will therefore be ##FC "CONDVAR", and a conditional line is ##-C "CONDVAR"
Other useful suffixes might be deprecated and unavailable
- Add deprecated
- Add not enabled

## References and tutorials

[Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html#Programmable-Completion)
[Bash Variables](https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html)
[Internal Variables](https://tldp.org/LDP/abs/html/internalvariables.html)
[Bash builtin commands](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html)
[BASH arithmetics](https://www.shell-tips.com/bash/math-arithmetic-calculation/#gsc.tab=0)
[Brace expantion](https://www.howtogeek.com/725657/how-to-use-brace-expansion-in-linuxs-bash-shell/)
[Best Practices for Writing Bash Scripts](http://kvz.io/blog/2013/11/21/bash-best-practices/)
[What are the best practices for writing shell scripts?](https://www.quora.com/What-are-the-best-practices-for-writing-shell-scripts)
[Command completion](https://opensource.com/article/18/3/creating-bash-completion-script)
[Exit codes demystified](https://www.redhat.com/sysadmin/exit-codes-demystified)
[Bash exit code](https://www.cyberciti.biz/faq/linux-bash-exit-status-set-exit-statusin-bash/)
[Remove ANSI terminal codes](https://superuser.com/questions/380772/removing-ansi-color-codes-from-text-stream)
[Icecream](https://github.com/jtplaarj/IceCream-Bash/blob/main/src/ic.sh)

# Example scripts

[Simple bash shell script template](https://gist.github.com/KylePDavis/3901321)
[bashsimplecurses](https://github.com/metal3d/bashsimplecurses)
[BOILERPLATE SHELL SCRIPT TEMPLATE](http://natelandau.com/boilerplate-shell-script-template/)
[bash3boilerplate](https://github.com/kvz/bash3boilerplate/blob/master/main.sh)
[Self-contained auto-updating rsync-based backup script](https://gist.github.com/KylePDavis/3f8c511838a36f2528d7)
[This is a shell script template generator](http://linuxcommand.org/lc3_new_script.php)
[Charm gum](https://github.com/charmbracelet/gum)

[bp]: https://github.com/zonbrisad/bashplates/raw/master/doc/bp.png "bp"
[bp-info]:  https://github.com/zonbrisad/bashplates/raw/master/doc/bp-info.png "bp info"
[bp-log]:https://github.com/zonbrisad/bashplates/raw/master/doc/bp-log.png "bp log"
