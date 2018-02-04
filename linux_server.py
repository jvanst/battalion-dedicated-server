# Battalion 1944 Linux Server Updating Script
# By: jvast
# Version: 0.1.0

import os, shutil, stat
import argparse
import urllib.request
import zipfile

# Wiki URL
wiki_url = 'http://wiki.battaliongame.com'
# Download URL
download_url = 'https://storage.googleapis.com/battalion_public/BattalionLinuxServer_'
# Server Folder
server_folder = 'binaries'
# Scripts Directory
scripts = "servers"

# Functions

# Check version from wiki
def check_version():
    with urllib.request.urlopen(wiki_url) as webpage:
        source = webpage.read().decode('utf-8')
        index = source.find('Current Version:')
        wiki_version = source[index+17:index+22]
        return wiki_version

# Download files from wiki
def download_files(version):
    print('Downloading v' + version + ' ...      ', end='')
    urllib.request.urlretrieve(download_url + version + '.zip', 'server_files_' + version + '.zip')
    print("[DONE]")
    return 'server_files_' + version + '.zip'

# Unzip files from wiki
def unzip(zip_location):
    print('Extracting ...      ', end='')
    zip_ref = zipfile.ZipFile(zip_location, 'r')
    zip_ref.extractall('server_files')
    zip_ref.close()
    print("[DONE]")

# Install server binaries
def install():
    wiki_version = check_version()
    zip_location = download_files(wiki_version)
    unzip(zip_location)
    os.remove(zip_location)

    shutil.copytree('server_files/LinuxServer', server_folder)
    shutil.rmtree('server_files')

    file = open('current_version.txt', 'w+')
    file.write(wiki_version)
    file.close()

    os.system('chmod 755 -R ' + server_folder)

# Update server binaries
def update():
    wiki_version = check_version()

    file = open('current_version.txt', 'r')
    host_version = file.readline()
    file.close()

    if host_version != wiki_version:
        print('Server update released')

        zip_location = download_files(wiki_version)
        unzip(zip_location)
        os.remove(zip_location)

        print('Backing up loadouts')
        shutil.move('server_files/LinuxServer/Battalion/Loadouts/', 'server_files/LinuxServer/Battalion/Loadouts_orignal/')
        shutil.copytree(server_folder + '/Battalion/Loadouts/', 'server_files/LinuxServer/Battalion/Loadouts/')
        shutil.rmtree(server_folder)

        shutil.copytree('server_files/LinuxServer', server_folder)
        shutil.rmtree('server_files')

        file = open('current_version.txt', 'w+')
        file.write(wiki_version)
        file.close()

    else:
        print('No updates available')

    os.system('chmod 755 -R ' + server_folder)

def create():
    script_name = input("Startup script name (Ex: server1): ")
    ip_address = input("Server IP Address (Ex: 45.687.212.45): ")
    port = input("Server Port (Ex: 7777): ")
    query_port = input("Server Query Port (Ex: 7778): ")

    if not os.path.exists(scripts):
        os.makedirs(scripts)    

    file = open(scripts + '/' + script_name + '.sh', 'w+')
    file.write('../' + server_folder + '/Battalion/Binaries/Linux/BattalionServer /Game/Maps/Final_Maps/Derailed?Game=/Script/ShooterGame.BombGameMode?listen -broadcastip="' + ip_address + '" -PORT=' + port + ' -QueryPort=' + query_port + ' -log -defgameini="../../../../servers/config-' + script_name + '.ini"')
    file.close()

    shutil.copy(server_folder + '/' + '/DefaultGame.ini', scripts + '/' + 'config-' + script_name + '.ini')

    os.system('chmod 755 -R ' + scripts)

# Main Entry Point

parser = argparse.ArgumentParser()
parser.add_argument('type', help="install | update | create")
args = parser.parse_args()

if args.type == 'install':
    install()

if args.type == 'update':
    update()

if args.type == 'create':
    create()



