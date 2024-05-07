#!/bin/bash
PROJPATH=/opt/hsl-services/gnujdb
if [ "`hostname`" == "hsldz" ]; then
    cd $PROJPATH && docker-compose build
    cd $PROJPATH && docker-compose up -d
else
    mkdir backup
    scp root@hs-ldz.pl:$PROJPATH/db.sqlite3 ./backup/db.$(date +%Y-%m-%d).$(date +%s).sqlite3
    rsync -ra --progress --exclude ".git" --exclude "db.sqlite3" --exclude "deploy.sh" --exclude "media/" ./* root@hs-ldz.pl:$PROJPATH/
    ssh root@hs-ldz.pl "cd $PROJPATH && docker compose build"
    ssh root@hs-ldz.pl "cd $PROJPATH && docker compose up -d"
fi
