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
                                items: [
                {
                xtype: 'textfield',
                name: 'port',
                fieldLabel: _t('Port'),
                id: "portField",
                width: 260,
                allowBlank: false,
                },
                
                {
                xtype: 'checkbox',
                name: 'ssl',
                fieldLabel: _t('SSL'),
                id: "sslField",
                width: 260,
                allowBlank: false,
                },
                
                {
                xtype: 'textfield',
                name: 'eventComponent',
                fieldLabel: _t('Alias'),
                id: "eventComponentField",
                width: 260,
                allowBlank: false,
                },
                
                {
                xtype: 'textfield',
                name: 'url',
                fieldLabel: _t('URL'),
                id: "urlField",
                width: 260,
                allowBlank: false,
                },
                ],
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
                                                        text: _t('OK')
                                                    }]
                                                }).show();
                                            }
                                            else {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK')
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

