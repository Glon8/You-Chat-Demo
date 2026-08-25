import { get_user } from "../data/users.data";

export const snd_msg = (req, res) => {
    const { snd_id, rcv_id, dt, rst_routes } = req.data;
    /*
    message data:
    {
        snd_id,     // < sender_identifier
        rcv_id,     // < reciever_identifier
        dt: {       // < data
            msg,    // < message
            img,    // < image
            fl,     // < file
            etc
            ...
        }
        rst_routes, // < restricted_routes,
    }

    // < verify msg_data fields, eg strict verification
    // < verify sender and reciever identifiers < must be in a relay list < ip must match as long as sender or a reciever has a positive heartbeat
    // < verify if it is a valid route > if not pass it to another relay
    // < pass the message to the reciever    
    */

    // < strict verification

    const snd = get_user[snd_id];
    const rcv = get_user[rcv_id];

    if (!snd || !rcv) {
        // < ask another relay < if found, transfer
        return;
    }

    // < heartbeat verification for snd and rcv

    // < sending data to the reciever, after all checks, preferebly on ip6
}