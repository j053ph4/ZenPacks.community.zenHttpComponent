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
                        fields: [
            {name: 'uid'},
            {name: 'severity'},
            {name: 'status'},
            {name: 'name'},{name: 'port'},
                {name: 'ssl'},
                {name: 'eventComponent'},
                {name: 'url'},
                
            {name: 'usesMonitorAttribute'},
            {name: 'monitor'},
            {name: 'monitored'},
            {name: 'locking'},
            ]
        ,
                        columns:[{
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
        },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Name'),
            sortable: true,
            width: 70
        },{
                    id: 'port',
                    dataIndex: 'port',
                    header: _t('Port'),
                    sortable: true,
                    width: 160
                },{
                    id: 'ssl',
                    dataIndex: 'ssl',
                    header: _t('SSL'),
                    sortable: true,
                    width: 160
                },{
                    id: 'eventComponent',
                    dataIndex: 'eventComponent',
                    header: _t('Alias'),
                    sortable: true,
                    width: 160
                },{
                    id: 'url',
                    dataIndex: 'url',
                    header: _t('URL'),
                    sortable: true,
                    width: 160
                },{
            id: 'monitored',
            dataIndex: 'monitored',
            header: _t('Monitored'),
            sortable: true,
            width: 65
        },{
            id: 'locking',
            dataIndex: 'locking',
            header: _t('Locking'),
            renderer: Zenoss.render.locking_icons,
            sortable: true,
            width: 65
        }]
                    });
                    ZC.HttpComponentPanel.superclass.constructor.call(this, config);
                }
            });
            
            Ext.reg('HttpComponentPanel', ZC.HttpComponentPanel);
            ZC.registerName('HttpComponent', _t('Monitored URL'), _t('Monitored URLs'));
            
            })(); 

