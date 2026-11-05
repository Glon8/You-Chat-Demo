import { get_user, upd_ls } from "../data/users.data.js"
import { ping_check } from "./heartbeat.handler.js"
import { get_relays } from "../data/relays.data.js";
import { ping } from "../relay_api/ping.js";
import { msg_trans } from "../relay_api/message_transfer.js";
/*
    3 phases:
        * Last, must return boolean, if the cnt_id, is found in its client list. <=== LookUp func
        * Middle, ll return pre last TTL (that received the boolean) and return, associated link. <=== LookUp func
        * First, relay with TTL 0 ll send the package to associated link. <=== transfer func
*/
export const transfer = async (data) => {
    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

    // unpack data
    const { snd_id, rcv_id, req_type } = JSON.parse(data.toString());
    // check if request is valid
    if (!['msg', 'upd'].includes(req_type)) return false;
    // get the receiver info
    const rcv = get_user(rcv_id);
    // inform
    console.log(`[${snd_id}]>[${rcv_id}]>[Request for message transfer]`);
    // checking if reciever exists
    if (!rcv) {
        // inform
        console.log(`[${rcv_id}]>[Warning! Receiver not registred]\r\n[Attempt to transfer to another relay]`);
        /*
            transfer to another relay
            * send request for look up
            * message transfer
        */
        // get relays info
        const relays = get_relays();
        // create a black list
        const bList = [];
        // get through relay list
        for (const relay of relays) {
            // check if the relay is alive
            const alive = Boolean(await ping(relay));
            // inform
            console.log(`[Relay] ${relay}\r\n[Alive] ${alive}`);
            // abort + inform
            if (!alive) { console.log(`[Status] Abort`); continue; }
            // add relay to black list
            bList.push(String(relay));
            // attempt to lookup through relay
            try {
                // call the relay
                const response = await fetch('https://' + String(relay) + '/api/lookup', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ rcv_id, curTTL: 0, bList })
                });

                if (response) {
                    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

                    // unpack
                    const { link } = response.body;
                    //transfer the message
                    msg_trans(link, data);
                    // inform
                    console.log(console.log(`[Status] Transfered`));
                    // break the lookup
                    break;
                }
            } catch (error) {
                // inform
                console.log(`[Status] Failed\r\n${error}`);
            }
        }

        return true;
    }

    let ping_state = true;
    // checking if reciever has positive heartbeat
    if (rcv && Date.now() > 5 * 1000 + rcv.ls) {
        // inform
        console.log(`[Starting Ping-Pong]>[${rcv_id}]`);
        // check socket being alive
        ping_state = await ping_check(rcv.sck, 5);

        if (ping_state) {
            // last seen update
            upd_ls(rcv_id);
            // inform
            console.log(`[${rcv_id}]>[Pong received]`);
        }
        else {
            // inform
            console.log(`[${rcv_id}]>[No Pong]`);
            return true;
        }
    }
    // transfer data routed to reciever
    rcv.sck.send(data);

    return true;
}