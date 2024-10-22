**English** | [中文](README_CN.md)

# mcdr_announcements

A plugin running on MCDR to send announcements on time.
<br/>
Run `pip install pyyaml` in cmd or powershell before loading this plugin.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yfy-dodo939/mcdr_announcements&type=Date)](https://star-history.com/#yfy-dodo939/mcdr_announcements&Date)

## Update Logs

### v1.3.0 Update
+ We refactored the logic of the timer part, so it now **supports viewing the remaining time until the next display**!
  ![Display](/src/v1.3.0_0_en.png)
+ Now after you have executed `!!an time <seconds>`, you no longer need to execute `!!an reload` to reload the plugin to refresh the timer!

### v1.2.2 Update
+ If pyyaml is not installed, `pip install pyyaml` will be automatically executed to try installing the missing library. (Known issues: Since the installation process is a non-blocking operation, the first time the plugin may run without the library)
+ Fixed the problem of redundant warnings or error messages appearing on the console when starting the server in version `v1.2.1`

### v1.2.1 Update
+ Plugins can now remember the enabled state when they were last exited, and restore it the next time they are launched.
+ The first announcement display after the plugin is loaded has been cancelled.
+ Optimized the timer and some details.
+ Optimized some prompt texts and added some hovering text prompts.
+ Added status display and other commands.

  `!!an help`: Same as `!!an`

  `!!an reload`: Reload the plugin
  
  `!!an status`: Show the current status

### v1.2.0 update
+ Added support for Chinese, the plug-in will automatically select the display language based on the server language preference.
+ The plug-in format is changed to `*.mcdr` packaging format, replacing the previous `*.py` single file format.

### v1.1.0 update

+ Now commands are allowed to configure instead of editing the yaml file. 

  `!!an`:  Show this help message list

  `!!an enable`:  Enable the timed announcement

  `!!an disable`:  Disable the timed announcement

  `!!an set <message>`:  Set the content of announcement

  <strong>Notice:</strong> `\n` for next line and `&` for the color text. If you use Chinese in this command, please add `-Dfile.encoding=UTF-8` in your start command. Such as `java -Dfile.encoding=UTF-8 -jar server.jar nogui`
  
  `!!an time <seconds>`:  Set the interval time (seconds/time)

+ The status is set to False by default now. Please enable it manually.
+ Only admin and owner can run commands.
