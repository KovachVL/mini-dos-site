# mini-dos-site
Hello! I made a program for dos attack. It is suitable if you want to attack Wordpress sites, or those sites that do not have an SSL certificate. To run the program you need to clone my project 
```
git clone https://github.com/KovachVL/mini-dos-site.git
```
You also need to create an .env file to include the following:
```
RM_HOST = YOUR_IP_FOR_SSH_ON_LINUX
RM_PORT = 22
RM_USER = YOUR_USER_FOR_SSH_ON_LINUX
RM_PASSWORD = YOUR_PASSWORD_FOR_SSH_ON_LINUX
```

To run the program you need Linux and using python3 main.py you will be prompted to enter the site you want to attack.
You can also change the range, let’s say it’s not 2 times to attack, but 5
