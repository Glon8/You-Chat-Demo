import { WebSocketServer } from "ws";

import { get_user } from "./src/data/users.data.js";
import { connect } from "./src/handlers/connection.handler.js";
import { disconnect } from "./src/handlers/disconnection.handler.js";
import { transfer } from "./src/handlers/transition.handler.js";

export let wss = null;

export const wss_init = (server) => {
    wss = new WebSocketServer({ server });

    wss.on('connection', (socket) => {
        console.log(`[Connection detected]`);
        socket.on('message', async (data) => {
            const { snd_id, req_type } = JSON.parse(data.toString());

            // < verify data fields, eg strict verification

            const req_types = ['cnn', 'dsc', 'msg', 'upd'];
            // check if request is valid
            if (!req_types.includes(req_type)) return;

            const snd = get_user(snd_id);
            // known/unknown user sends connection request
            if (await connect(req_type, snd_id, socket)) return;

            // check that user have been registered
            if (!snd) {
                console.log(`[${snd_id}]>[Warning! User not registrated!]`);
                return;
            }
            // known/unknown user sends disconnection request
            if (await disconnect(req_type, snd_id, socket)) return;

            if (await transfer(req_type, data)) return;
        });

        socket.on('pong', (item) => {
            console.log(`[GLOBAL PONG] ${item}`);
        });
    });

    wss.on('error', () => {
        console.log('some error occured')
    });
}