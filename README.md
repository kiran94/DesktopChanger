# DesktopChanger

Python application that gets a random wallpaper from https://www.reddit.com/r/EarthPorn/ and sets it to your desktop. Currently only working on MacOS. 

To set this up you can add the following line to your `.bash_profile` file to run it anytime. 

`alias wallpaper="python <PATH_TO_APPLICATION>`

Alternatively you can add this application as a cron job with the following steps: 
1. `env EDITOR=nano crontab -e`
2. Add your cron job with a path to where the application is
3. Verify with `crontab -l`
