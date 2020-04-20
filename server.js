const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 3030 });

var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: true
});

rl.on('line', (line) => {
    wss.clients.forEach((client) => {
        client.send(line)
    })
})

wss.on('connection', function connection(ws) {
    ws.on('message', function incoming(data) {
        console.log(data);
    });
});
