#!/bin/bash
if [ "`hostname`" == "hsldz" ]; then
    chown -R d33tah:d33tah /home/d33tah/workspace/hs/gnujdb
    cd /home/d33tah/workspace/hs/gnujdb && docker-compose build
    cd /home/d33tah/workspace/hs/gnujdb && docker-compose up -d
else
    rsync -ra --progress --exclude ".git" --exclude "db.sqlite3" --exclude "deploy.sh" --exclude "media/" ./* root@hs-ldz.pl:/home/d33tah/workspace/hs/gnujdb/
    ssh root@hs-ldz.pl "chown -R d33tah:d33tah /home/d33tah/workspace/hs/gnujdb"
    ssh root@hs-ldz.pl "cd /home/d33tah/workspace/hs/gnujdb && docker-compose build"
    ssh root@hs-ldz.pl "cd /home/d33tah/workspace/hs/gnujdb && docker-compose up -d"
fi
