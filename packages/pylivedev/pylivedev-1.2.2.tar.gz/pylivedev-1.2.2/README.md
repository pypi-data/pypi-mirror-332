![PyLiveDev](https://ouroboroscoding.s3.us-east-2.amazonaws.com/logos/PyLiveDev_128.png)

[![pypi version](https://img.shields.io/pypi/v/pylivedev.svg)](https://pypi.org/project/pylivedev) ![MIT License](https://img.shields.io/pypi/l/pylivedev.svg)

Python Live Development tool.

## Description

I created **PyLiveDev** because I work a lot in the microservices/REST space and found constantly having to run/restart services while developing and keeping track of multiple logs in separate windows, to be, quite frankly, a pain in my ass.

Inspired by live updates while using create-react-app in development, I wanted to see if there was a way I could make a python program run multiple services and keep track of the files imported. This way if anything changed it could automatically restart those services and save time while developing. As a bonus, piping all stdout/stderr to one screen so I could immediately see if I wrote bad code or was returning something unexpected.

It works by you creating a JSON configuration file called `.pylivedev` in the root of your python project and adding an Object member for each unique process, then running `pylivedev` from the root of your project.

## Install

```console
foo@bar:~$ pip install pylivedev
```

## Warning

If you are using PyLiveDev on a Linux kernel 2.6+, you may at some point run
into an issue where you see red errors like the following:

```File "some/path.py" could not be tracked: (24, 'inotify instance limit reached')```

```File "some/path.py" could not be tracked: (28, 'inotify watch limit reached')```

This is due to limits in an underlying library. When this happens adjust
the following settings in your `/etc/sysctl.conf` file (will require root
access):

```
fs.inotify.max_user_instances=256
fs.inotify.max_user_watches=16384
```

The defaults are 128 and 8192, so adjust accordingly then reboot. Increase as
necessary until PyLiveDev stops reporting issues tracking files.

Note, that if you use vscode, it will try to track every single file in a
project, be aware of how many files/folders in your projects, and make sure you
hide things like node_modules if you're using node in your projects. Many node
based auto-build development systems, create-react-app, vite, nextjs, and others
will also watch files, so it's a common problem for developers.

## Run

```console
foo@bar:~$ pylivedev
```

## Configuration

```json
{
	"rest": {
		"command": "rest",
		"mode": "module",
		"tracked": false,
		"python": "/venv/my_project/bin/python",
		"arguments": ["-v"],
		"additional_files": ["config.json"],
		"unbuffered": true,
		"verbose": false
	}
}
```

| Name | Type | Mandatory | Description |
| ------ | ------ | ------ | ------ |
| command | String | Yes | The name of the script or module to run as a process. e.g. "services.rest", "main.py" |
| mode | "module" \| "script" \| "exe" | No | Tells pylivedev whether you are trying to run a stand alone script, a python module, or a binary (or non-parsable) application. Defaults to "script". |
| tracked | Boolean | No | When true, proccess is tracked via file changes. Use false for static or external modules. Defaults to true. Will be ignored if mode is set to "exe". |
| python | String | No | The full path to the python intepreter to use to run your process. Defaults to the python interpreter running pylivedev. |
| arguments | String[] | No | An array of additional arguments passed to the process. |
| additional_files | String[] | No | An array of additional files to be watched/observed for changes. |
| unbuffered | Boolean | No | Run the processed unbuffered, defaults to true. |
| verbose | Boolean | No | Runs pylivedev in verbose mode to give more information on what is happening, what imports were found, what files have changed, etc. Defaults to false. |

## Defaults

You can also use the special `__default__` member to store values that will be the same across processes. Anything in the proccess config will always overwrite the defaults.

```json
{
	"__default__": {
		"python": "/venv/my_project/bin/python",
		"mode": "module",
		"additional_files": ["config.json"],
	},

	"main": {
		"command": "nodes.rest.main"
	},

	"admin": {
		"command": "nodes.rest.admin"
	},

	"external": {
		"command": "nodes.external"
	},

	"websocket": {
		"command": "daemons.websocket"
	}
}
```

The above would work for a file structure like the following

	my_project/
	|-- daemons/
		|-- __init__.py
		|-- websocket.py
	|-- nodes/
		|-- rest/
			|-- __init__.py
			|-- admin.py
			|-- main.py
		|-- __init__.py
		|-- external.py
	|-- records/
		|-- __init__.py
	|-- .pylivedev
	|-- config.json

If, for example, nodes/rest/main.py imported the following:

```python
from time import time
from . import Rest
from records import User

class Main(Rest):
	pass
```

**PyLiveDev** would end up with the following list of files to watch/observe for changes

- config.json
- nodes/rest/main.py
- nodes/rest/\_\_init\_\_.py
- records/\_\_init\_\_.py

Any time any of these files is saved/changed on the system, **PyLiveDev** would shut down the "main" process, re-parse the module looking for imports, and then restart the process.

***Note*** system and pip imports will not be added to the list, like `time` in the above example. In most cases system files don't change often and it would waste resources to watch them. If you update a pip library, or update python, it's best to shut down **PyLiveDev** [CRTL-C] and restart it.