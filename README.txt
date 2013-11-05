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

    Zenoss Versions Supported: 3.x,4.x (4.2.4 for version 2.1)
    External Dependencies: None
    ZenPack Dependencies: None
    Installation Notes: zopectl restart; zenhub restart after installing this
ZenPack.
    Configuration: None

History:

Change History:

1.0 initial release

1.1 added wrapper script to handle various check_http arguments

1.2
    added dmd method manage_addHttpComponent
    added component attributes "httpUsesSSL" and "httpIp"

1.3 added support for adding arbitrary check_http flags

1.4
    changed path in wrapper script to use $ZENHOME
    changed default parser to 'nagios' from 'auto'

2.0
    added Zenoss 4.X support
    new dependency on "ConstructionKit" ZenPack to simplify current/future development
    <https://github.com/j053ph4/ZenPacks.community.ConstructionKit>
    Template now closely resembles that of HttpMonitor ZenPack

2.1
	added support for ConstructionKit 2.0
	removed support for Zenoss 3.x
	added relation to IpService
	improved javascript add component handling
	improved layout/sorting in details pane
	ability to select target event class from layout pane

Tested: This ZenPack was tested with versions 3.2.1, 4.2.3, 4.2.4

Source: https://github.com/j053ph4/ZenPacks.community.zenHttpComponent

Known issues:
