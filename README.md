# practice
## localhost server
The file is writen in app.js. It will open a web that can send message to database. Enter these instruction to run the server. It is implemented by socket.
To build the server: 
```
~$ npm install
~$ node app.js
```
Open your browser, and enter "localhost".
## 開啟網頁
若沒有要架server可以直接點開index.html，firebase的也可以正常運作。
## Go button function
放在sendBox.html中，function中有set database，若有要改傳送格式可從此做修改。

## index.html
(可忽略) To make the web be split. Somthing goes wrong when it is opened by app.js.
## room
(可忽略)Used for placing history message. It should be connected to firebase too.
## Dir/script
Useless.
## Dir/style
Store the format in sendBox.html.