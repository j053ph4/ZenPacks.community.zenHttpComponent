#!/bin/bash
###################################
#
#       check-http-wrapper.sh
#
#		wrapper for check-http plugin 
#		to handle optional arguments
#		
###################################

HOST=$1;
URL=$2;
PORT=$3;
USER=$4;
PASS=$5;
STRING=$6;
POST=$7;

COMMAND="/opt/zenoss/libexec/check_http"

if [ "$HOST" ] ; then
	COMMAND=$COMMAND" -H "$HOST
fi

if [ "$PORT" ] ; then
	COMMAND=$COMMAND" -p "$PORT
fi

if [ "$URL" ] ; then
	COMMAND=$COMMAND" -u "'"'$URL'"'
fi

if [ "$USER" ] ; then
	COMMAND=$COMMAND" -a "$USER
fi

if [ "$PASS" ] ; then
	COMMAND=$COMMAND":"$PASS
fi

if [ "$STRING" ] ; then
	COMMAND=$COMMAND" -s "'"'$STRING'"'
fi

if [ "$POST" ] ; then
	COMMAND=$COMMAND" -P "'"'$POST'"'
fi

/bin/sh -c "$COMMAND"

