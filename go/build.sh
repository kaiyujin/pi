#!/bin/bash
if [ $# -le 1 ]; then
    echo "require arguments. go fileName and hostname"
    exit 1
fi

if [ ! -e $1 ]; then
    echo "error. not exists file"
    exit 1
fi
GOOS=linux GOARCH=arm GOARM=7 go build $1

HOST=$2
USER=pi
PASS=raspberry
SRC_PATH=./`echo $1 |sed -e s/.go$//`
DEST_PATH=/home/pi/

expect -c "
set timeout -1
spawn scp -C ${SRC_PATH} ${USER}@${HOST}:${DEST_PATH}
expect {
  \" Are you sure you want to continue connecting (yes/no)? \" {
    send \"yse\r\"
    expect \"password:\"
    send \"${PASS}\r\"
  } \"password:\" {
    send \"${PASS}\r\"
  }
}
interact
"
rm $SRC_PATH
