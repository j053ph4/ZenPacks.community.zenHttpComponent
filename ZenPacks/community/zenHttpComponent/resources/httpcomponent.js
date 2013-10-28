
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }

    ZC.HttpComponentPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'HttpComponent',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "eventComponent"
                    }, 
                    {
                        "name": "getIpserviceLink"
                    }, 
                    {
                        "name": "port"
                    }, 
                    {
                        "name": "url"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "header": "Alias", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "eventComponent", 
                        "dataIndex": "eventComponent"
                    }, 
                    {
                        "header": "IP Service", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getIpserviceLink", 
                        "dataIndex": "getIpserviceLink"
                    }, 
                    {
                        "header": "Port", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "port", 
                        "dataIndex": "port"
                    }, 
                    {
                        "header": "URL", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "url", 
                        "dataIndex": "url"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.HttpComponentPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('HttpComponentPanel', ZC.HttpComponentPanel);
    ZC.registerName('HttpComponent', _t('Monitored URL'), _t('Monitored URLs'));
    
    })();

