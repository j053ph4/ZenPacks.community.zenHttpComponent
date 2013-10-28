
(function() {
        
            function getPageContext() {
                return Zenoss.env.device_uid || Zenoss.env.PARENT_CONTEXT;
            }
        
            Ext.ComponentMgr.onAvailable('component-add-menu', function(config) {
                var menuButton = Ext.getCmp('component-add-menu');
                menuButton.menuItems.push({
                    xtype: 'menuitem',
                    text: _t('Add Monitored URL') + '...',
                    hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
                    handler: function() {
                        var win = new Zenoss.dialog.CloseDialog({
                            width: 300,
                            title: _t('Add Monitored URL'),
                            items: [{
                                xtype: 'form',
                                buttonAlign: 'left',
                                monitorValid: true,
                                labelAlign: 'top',
                                footerStyle: 'padding-left: 0',
                                border: false,
                                items:                         [
                            {
                                fieldLabel: 'Alias', 
                                allowBlank: 'false', 
                                name: 'eventComponent', 
                                width: 260, 
                                id: 'eventComponentField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'Port', 
                                allowBlank: 'false', 
                                name: 'port', 
                                width: 260, 
                                id: 'portField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'URL', 
                                allowBlank: 'false', 
                                name: 'url', 
                                width: 260, 
                                id: 'urlField', 
                                xtype: 'textfield'
                            }
                        ]

                                ,
                                buttons: [{
                                    xtype: 'DialogButton',
                                    id: 'zenHttpComponent-submit',
                                    text: _t('Add'),
                                    formBind: true,
                                    handler: function(b) {
                                        var form = b.ownerCt.ownerCt.getForm();
                                        var opts = form.getFieldValues();
                                        Zenoss.remote.zenHttpComponentRouter.addHttpComponentRouter(opts,
                                        function(response) {
                                            if (response.success) {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    title: _t('Monitored URL Added'),
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK'),
                                                        handler: function() { 
                                                            window.top.location.reload();
                                                            }
                                                        }]
                                                }).show();
                                            }
                                            else {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK'),
                                                        handler: function() { 
                                                            window.top.location.reload();
                                                            }
                                                        }]
                                                }).show();
                                            }
                                        });
                                    }
                                }, Zenoss.dialog.CANCEL]
                            }]
                        });
                        win.show();
                    }
                });
            });
        }()
);

