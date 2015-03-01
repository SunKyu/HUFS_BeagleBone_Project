#Beaglebone Black Project

**HUFS Begalebone Black IOT Project**
##Installation
If first time to install ubuntu  
```
$ cd /opt
$ git clone https://github.com/SunKyu/HUFS_BeagleBone_Project.git
$ sudo chmod 755 init.sh
$ ./init.sh
```


dd the Daemon to `/etc/init.d`
```
$ cd pybluez/examples/test  
$ sudo cp beta /etc/init.d/  
$ sudo update-rc.d beta defaults  
```

and then enter the passwords  
run `vim` and `:PluginInstall`

