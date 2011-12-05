(function() {

/**
* On the device details page the uid is
* Zenoss.env.device_uid and on most other pages it is set with
* the environmental variable PARENT_CONTEXT;
**/
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
                        items: [{
                            xtype: 'textfield',
                            name: 'httpPort',
                            fieldLabel: _t('Port'),
                            id: "httpPortField",
                            width: 260,
                            allowBlank: false
                        }, {
                            xtype: 'textfield',
                            name: 'httpUrl',
                            fieldLabel: _t('URL'),
                            id: "httpUrlField",
                            width: 260,
                            allowBlank: false
                        }, {
                            xtype: 'textfield',
                            name: 'httpAuthUser',
                            fieldLabel: _t('User'),
                            id: "httpAuthUserField",
                            width: 260,
                            allowBlank: true
                        }, {
                            xtype: 'textfield',
                            name: 'httpAuthPassword',
                            fieldLabel: _t('Password'),
                            id: "httpAuthPasswordField",
                            width: 260,
                            allowBlank: true
                        }, {
                            xtype: 'textfield',
                            name: 'httpJsonPost',
                            fieldLabel: _t('POST'),
                            id: "httpJsonPostField",
                            width: 260,
                            allowBlank: true
                        }, {
                            xtype: 'textfield',
                            name: 'httpFindString',
                            fieldLabel: _t('Find String'),
                            id: "httpFindStringField",
                            width: 260,
                            allowBlank: true
                        }],
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
                                            title: _t(' URL Added'),
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
}());
