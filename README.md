# Battalion Server Updator
*Only tested on Debian 9*

The Battalion server updator is a very basic python script made to make updating a Battation1994 server easier.
This script also provides the ablity to:

  - Install Battalion LinuxServer Binaries
  - Update previously installed Binaries
  - Keeps custom loadouts on update
  - Create new start.sh scripts for servers easily

I made this for personal use, and learned python to do so. Any suggestions and improvements please contact me :)

### Installation 
*Only tested on Debian 9*

The updator script requires Python v3. Go ahead and install that:

```sh
sudo apt-get update
sudo apt-get install python3.6
```

(Optional) If you want to easily update this script when I push changes, install with git.
```sh
sudo apt-get install git
git clone https://github.com/jvanst/battalion-dedicated-server.git ~
```

Now you should have `linux_server.py`

### Commands

Installing Battalion server binaries:

```sh
python3 linux_server.py install 
```

Installs binaries to `binaries/`

Updating Battalion server binaries:

```sh
python3 linux_server.py update 
```

Checks to see if your version is the latest. Downloads new version automatically and replaces files. Keeps your custom loadout files. Originals can be found in `Battalion/Loadouts_original`

Create new server startup scripts:
```sh
python3 linux_server.py create
```

New server.sh scripts are placed into `servers/`, and initialized with the default config also located there.

##### Version 0.1.0

I will continue updating this script to fix bugs and issues.