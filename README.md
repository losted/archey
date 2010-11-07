Archey 3
========

Archey 3 is a system infomation printer, designed to be used when taking screenshots of computer desktops to provide additional infomation about the operating system setup. Archey is designed to be used for Arch linux, and it acordingly prints out the Arch linux logo along side the system infomation.

Display Variables
-----------------

Archey displays, as of 25/10/2010, the following by default:

-  Operating system
-  Hostname
-  Kernel Version
-  Uptime
-  Core temp (requires sensors)
-  Window Manager
-  Desktop Enviroment
-  Number of packages installed
-  Avalible Ram
-  CPU Model
-  Shell
-  CLI Text Editor
-  Number of songs in MPD library
-  Space avalible on root filesystem

The items that are displayed can be configured via -d|--display command line argument. Some examples are given below:

archey3 -d 'ram.fs:/home.mpd:albums,localhost,8800.env:IP'

would display the current ram usage, info on the /home partition, the number of mpd albums, and the IP adress env variable.

The MPD Display function
------------------------

The MPD function takes the following arguments:

1. Stat name. This can be songs, artists, albums
2. Hostname. Optional
3. Port Number. Optional.

The Sensor Display function
---------------------------

The Sensor function takes the following argument:

1. Sensors. This will be given as the first argument to the sensors binary, and the output will be parsed.

The ENV Display function
------------------------

The ENV function takes the following argument:

1. Variable name. The variable name will then be looked up via the genenv() function

The uname Display function
--------------------------

The uname function takes the following arguments:

1. Flag. This can be one of:
        
    * a - System Infomation
    * s - Kernel Name
    * n - Hostname
    * r - Kernel Release
    * v - Kernel Version
    * m - Machine Hardwear name
    * p - Processor type
    * i - Hardwear platform

The File System Display function
--------------------------------

The File System function takes the following arguments:

1. Partition path. The path to the partition to display

The WM/DE Display function
--------------------------

The WM/DE Display function takes no arguments