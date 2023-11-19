# Version 1.40 beta 2
- Added columnize.py
- bp cs now columnizes output if terminal is wide enough
- Added documentation about exit codes

# Version 1.40 beta 1
- Added colored queries
- Added logged queries
- Added bpd script for handling project
- Added description formatting
- fix: set variable command 
- fix: bpPrintDesc zero input bug
- fix: iinfo missing line   
- updated init script
- updated config file management
- updated printvar
- new directory structure
- new examples added
- updated documnation


# Version 1.30 beta 2
- doc: major performace improvements for doc generation
- doc: added cheat cheet to bp
- Major change of internal variable/function names (Escape codes)


# Version 1.30 beta 1
- doc: Improved documentation system
- fix: bpCp, bpMv, bpRm etc. now return correct status and log messages
- fix: Internal variable names are more consistent
- fix: bpCleanup escape code bug
- many other bugfixes

# Version 1.20
- Adding simple template
- Added info hook
- Added pre/post help hook
- Added command as argument to cmd hooks
- Added settings file function
- Added mlog command
- Added bpRead and bpReadInt commands
- Added bpReplaceLine command
- Added bpFilterEscape
- Added bpColorizeFile
- Added bpColorizeUrl
- Added read yes no wuestions
- Added bpCd function
- Added ied command
- Added indented command printout
- Removed command help print output
- Removed bpAssertRequiredProgs
- Corrected colors on documentation lines
- Fixed sed color printout
- Check for existing file when creating new script
- New "subdued" colorscheme
- Improved documentation with screenshots
- Improved performance of command execution
- Major refactoring
- Changed variable names for clearity
- Changed names of hooks
- Changed documentation tags
- Added bprc program
	

# Version 1.11
- Added install feature
- Added meld compare feature (for developers of bashplates)
- introducing hooks
- finer controll over what to log
- internal namechanges
- new documentation tags
	
# Version 1.09
- Added postfunc
- Added prefunc
- Several namechanges
- Added assertRequiredProgs

# Version 1.08
- Added ##D internal documentation tag
- Added ##C conditional documentation tag

# Version 1.07
- Added line separator(##-) feature for help command
- Added error message when using log command without log active

# Version 1.06
- Added info command
- Code cleanup

# Version 1.05
- Changed script locked printout

# Version 1.04
- Added template verion variable
- Added lock file handling
- Added root user check
- Added required programs check
- fixed no command error
