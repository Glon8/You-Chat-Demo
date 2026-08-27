import { add_user, rmv_user, get_user } from "./src/data/users.data";

export let wss = null;

export const wss_init = (server) => {
    wss = new WebSocketServer({ server });

    wss.on('connection', (socket) => {
        socket.on('message', (data) => {
            const { snd_id, rcv_id, req_type, trn_dt } = JSON.parse(data.toString());

            // < verify data fields, eg strict verification

            const req_types = ['cnn', 'dsc', 'msg'];
            const snd = get_user(snd_id);
            // check if request is valid and sender in on heartbeat
            if (!req_types.includes(req_type) || false) return;
            // known/unknown user sends connection request
            if (req_type == 'cnn') {
                // check heart beat of registered user and the socket
                // Note: if user on heartbeat and sockets doesn match, send confirmation/warning to the sender on heartbeat!
                if (snd.sck == socket && false) { }
                add_user({ snd_id, socket });
                return;
            }

            // check that user have been registered
            if (!snd) return;
            // known/unknown user sends disconnection request
            // Note: remove the user, only if sockets match and saved user on heartbeat!
            if (req_type == 'dsc' && snd.sck == socket && true) {
                rmv_user(snd_id);
                socket.close();
                return;
            }

            const rcv = get_user(rcv_id);

            if (req_type != 'msg') return;
            // checking if reciever exists
            if (!rcv) {
                // < transfer to another relay
                return;
            }
            // checking if reciever on heartbeat
            if (!true) return;
            // transfer data routed to reciever
            rcv.sck.send(JSON.stringify({
                snd_id,
                trn_dt
            }));
        });

        socket.on('error', () => { });

        socket.on('close', () => {
            /*
                ** HANDLES ALL POSSIBLE DISCONNECTIONS!
    
                if socket closure triggered specifically by user, remove user from the users list!
            */
        });
    });

    wss.on('close', (sck) => { /* socket server is shut down */ });
}