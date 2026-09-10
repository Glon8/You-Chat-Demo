import { get_user, upd_xphrt } from "../data/users.data.js";
import { ping_check } from "./heartbeat.handler.js";

export const transfer = async (req_type, data) => {
    if (req_type != 'msg' && req_type != 'upd') return false;

    const { snd_id, rcv_id, trn_dt, tm_stm } = JSON.parse(data.toString());

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
    if (rcv && Date.now() > rcv.xphrt) {
        console.log(`[Starting Ping-Pong]>[${rcv_id}]`);
        
        ping_state = await ping_check(rcv.sck, 5);

        if (ping_state) { upd_xphrt(rcv_id); console.log(`[${rcv_id}]>[Pong received]`); }
        else { console.log(`[${rcv_id}]>[No Pong]`); return true; }
    }
    // transfer data routed to reciever
    rcv.sck.send(JSON.stringify({ snd_id, rcv_id, req_type, trn_dt, tm_stm }));

    return true;
}