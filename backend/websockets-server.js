import { WebSocketServer } from "ws";

import { add_user, rmv_user, get_user } from "./src/data/users.data.js";

export let wss = null;

export const wss_init = (server) => {
    wss = new WebSocketServer({ server });

    wss.on('connection', (socket) => {
        console.log('[Connection detected]');
        socket.on('message', (data) => {
            const { snd_id, rcv_id, req_type, trn_dt } = JSON.parse(data.toString());

            // < verify data fields, eg strict verification

            const req_types = ['cnn', 'dsc', 'msg', 'upd'];
            // check if request is valid
            if (!req_types.includes(req_type)) return;
            const snd = get_user(snd_id);
            // known/unknown user sends connection request
            if (req_type == 'cnn') {
                console.log('[Request for registration]');
                // check heart beat of registered user and the socket
                // Note: if user on heartbeat and sockets doesn match, send confirmation/warning to the user on heartbeat!
                if (snd.sck != socket /*&& false*/) {
                    console.log('[Warning! User has no heartbeat or sockets doesnt match]');
                }
                add_user({ snd_id, socket });
                return;
            }

            // check that user have been registered
            if (!snd) {
                console.log('[Warning! No user id not registrated]');
                return;
            }
            // known/unknown user sends disconnection request
            // Note: remove the user, only if sockets match and saved user on heartbeat!
            if (req_type == 'dsc' && snd.sck == socket && true) {
                console.log('[Request for disconnect]');
                rmv_user(snd_id);
                socket.close();
                return;
            }

            const rcv = get_user(rcv_id);

            if (req_type != 'msg') return;
            console.log('[Request for message transfer]');
            // checking if reciever exists
            if (!rcv) {
                console.log('[Warning! Receiver not registred]');
                // < transfer to another relay
                console.log('[Data transferred to another relay]')
                return;
            }
            // checking if reciever on heartbeat
            if (!true) {
                console.log('[Receiver has no heartbeat]');
                return;
            }
            // transfer data routed to reciever
            rcv.sck.send(JSON.stringify({
                snd_id,
                trn_dt
            }));
        });
    });
}