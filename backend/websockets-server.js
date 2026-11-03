import { WebSocketServer } from "ws"

import { get_user } from "./src/data/users.data.js"
import { connect } from "./src/handlers/connection.handler.js"
import { disconnect } from "./src/handlers/disconnection.handler.js"
import { transfer } from "./src/handlers/transition.handler.js"

export let wss = null;

export const wss_init = (server) => {
    wss = new WebSocketServer({ server });

    wss.on('connection', (socket) => {
        console.log(`[Connection detected]`);
        socket.on('message', async (data) => {
            const { snd_id, req_type } = JSON.parse(data.toString());

            console.log(`[${snd_id}]>[Request: ${req_type}]`);

            // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

            // check if request is valid
            if (!['cnn', 'dsc', 'msg', 'upd'].includes(req_type)) return;
            // get user by id
            const snd = get_user(snd_id);
            // known/unknown user sends a connection request
            if (await connect(req_type, snd_id, socket)) return;
            // check that user have been registered
            if (!snd) { console.log(`[${snd_id}]>[Warning! User not registrated!]`); return; }
            // user sends a disconnection request
            if (await disconnect(req_type, snd_id, socket)) return;
            // user sends a transfer package
            if (await transfer(data)) return;
        });
    });

    wss.on('error', () => {
        console.log('some error occured');
    });
}