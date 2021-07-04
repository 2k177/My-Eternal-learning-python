# Click Python Module

In this section, i have tried few repeatedly used Click implementations.
Using click,a command line Interface is created for getting the data from the API and store it in the config file(api_click.py).

ref : https://click.palletsprojects.com/en/7.x/

------------------------------------------------------------------------
## Commands and Groups
### Callback Invocation
------------------------------------------------------------------------
click_group.py 
#### Output:

click_group.py
Usage: click_group.py [OPTIONS] COMMAND [ARGS]...

Options:
  --debug / --no-debug
  --help                Show this message and exit.

Commands:
  sync 

C:\DS\click_complete>python click_group.py --debug sync\
Debug mode is on\
Synching\
------------------------------------------------------------------------
## Description:
1. The callback fires whenever a subcommand fires.<br />
2. An outer command runs when an inner command runs<br />
------------------------------------------------------------------------
------------------------------------------------------------------------

## click_multiCommandChaning.py 
#### output

------------------------------------------------------------------------

C:\DS\click_complete>python click_multiCommandChaning.py --help
Usage: click_multiCommandChaning.py [OPTIONS] COMMAND1 [ARGS]... [COMMAND2
                                    [ARGS]...]...

Options:
  --help  Show this message and exit.

Commands:
  bdist_wheel
  sdist

C:\DS\click_complete>python click_multiCommandChaning.py sdist bdist_wheel
sdist called
bdist_wheel called

------------------------------------------------------------------------
## Description
1. invoke more than one subcommand in one go.
2. When using multi command chaining you can only have one command (the last) use nargs=-1 on an argument. 
3. It is also not possible to nest multi commands below chained multicommands

------------------------------------------------------------------------
------------------------------------------------------------------------

## click_passcontext.py
### output
------------------------------------------------------------------------
C:\DS\click_complete>python click_passcontext.py --help
Usage: click_passcontext.py [OPTIONS] COMMAND [ARGS]...

Options:
  --debug / --no-debug
  --help                Show this message and exit.

Commands:
  sync

C:\DS\click_complete>python click_passcontext.py --debug
Usage: click_passcontext.py [OPTIONS] COMMAND [ARGS]...
Try 'click_passcontext.py --help' for help.

Error: Missing command.

C:\DS\click_complete>python click_passcontext.py sync
Debug is off

C:\DS\click_complete>python click_passcontext.py --debug sync
Debug is on

------------------------------------------------------------------------
### Description:
1. Each time a command is invoked, a new context is created and linked with the parent context.
2. Contexts are passed to parameter callbacks together with the value automatically.

--------------------------------------------------------------------------













