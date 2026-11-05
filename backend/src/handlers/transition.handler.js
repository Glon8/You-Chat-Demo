import { get_user, upd_ls } from "../data/users.data.js"
import { ping_check } from "./heartbeat.handler.js"

export const transfer = async (data) => {
    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

    const { snd_id, rcv_id, req_type } = JSON.parse(data.toString());

    // check if request is valid
    if (!['msg', 'upd'].includes(req_type)) return false;

    const rcv = get_user(rcv_id);

    console.log(`[${snd_id}]>[${rcv_id}]>[Request for message transfer]`);
    // checking if reciever exists
    if (!rcv) {
        console.log(`[${rcv_id}]>[Warning! Receiver not registred]`);
        // < transfer to another relay
        console.log('[Data has been transferred to another relay]')
        return true;
    }

    let ping_state = true;
    // checking if reciever has positive heartbeat
    if (rcv && Date.now() > 5 * 1000 + rcv.ls) {
        console.log(`[Starting Ping-Pong]>[${rcv_id}]`);

        ping_state = await ping_check(rcv.sck, 5);

        if (ping_state) { upd_ls(rcv_id); console.log(`[${rcv_id}]>[Pong received]`); }
        else { console.log(`[${rcv_id}]>[No Pong]`); return true; }
    }
    // transfer data routed to reciever
    rcv.sck.send(data);

    return true;
}