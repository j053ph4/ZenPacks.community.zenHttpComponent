Developed by: Joseph Anderson
Description:

This zenpack allows monitored URLs to be managed as if they were device
components, using the standard GUI component management methods. It utilizes
the "check-http" Nagios plugin that ships with Zenoss, but the command plugin
arguments are the component attributes assigned at component creation. 

URLs can be added via the "add components" menu on the Device Status page, and
can be removed or otherwise modified using the menus in the Components Pane of
the Device Status page.

Special thanks to Jane Curry and all others who dug into the details of the
new GUI interface.  The "MenuExamples" zenpack was instrumental in the
creation of this Zenpack, which wouldn't have been possible without it.


Components:

The ZenPack has the following Objects

    HttpComponent Template provides a component-level modified version of the
standard "HttpMonitor" template that ships with Zenoss.

The ZenPack also provides:

    HTTPComponent Device Component
    Javascript code to support GUI management.

Installation:

Describe the install process if anything is needed before or after standard
ZenPack installation.

Requirements:

    Zenoss Versions Supported: 3.0
    External Dependencies: None
    ZenPack Dependencies: None
    Installation Notes: zopectl restart; zenhub restart after installing this
ZenPack.
    Configuration: None

History:

Change History:

    1.0 initial release

Tested: This ZenPack was tested with versions 3.2.1.

Source: https://github.com/j053ph4/ZenPacks.community.zenHttpComponent

Known issues:  
