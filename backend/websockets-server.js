import { WebSocketServer } from "ws";

import { get_user } from "./src/data/users.data.js";
import { connect } from "./src/handlers/connection.handler.js";
import { disconnect } from "./src/handlers/disconnection.handler.js";
import { message } from "./src/handlers/messaging.handler.js";

export let wss = null;

export const wss_init = (server) => {
    wss = new WebSocketServer({ server });

    wss.on('connection', (socket) => {
        console.log(`[Connection detected]`);
        socket.on('message', (data) => {
            const { snd_id, req_type } = JSON.parse(data.toString());

            // < verify data fields, eg strict verification

            const req_types = ['cnn', 'dsc', 'msg', 'upd'];
            // check if request is valid
            if (!req_types.includes(req_type)) return;

            const snd = get_user(snd_id);
            // known/unknown user sends connection request
            if (connect(req_type, snd_id, socket)) return;

            // check that user have been registered
            if (!snd) {
                console.log(`[${snd_id}]>[Warning! User not registrated!]`);
                return;
            }
            // known/unknown user sends disconnection request
            // Note: remove the user, only if sockets match and saved user on heartbeat!
            if (disconnect(req_type, snd_id, socket)) return;

            if (message(data, req_type)) return;
        });
    });

    wss.on('error', () => {
        console.log('some error occured')
    });
}