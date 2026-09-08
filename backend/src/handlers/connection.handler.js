import { add_user, get_user, upd_xphrt } from "../data/users.data.js";
import { ping_check } from "./heartbeat.handler.js";

export const connect = async (req_type, snd_id, socket) => {
    if (req_type != 'cnn') return false;

    console.log(`[${snd_id}]>[Request for registration]`);

    const snd = get_user(snd_id);

    let ping_state = true;
    let sck_mismatch = false;

    if (snd && Date.now() > snd.xphrt) {
        ping_state = await ping_check(snd.sck, 5);

        if (ping_state) upd_xphrt(snd_id);
    }

    // check heart beat of registered user and the socket
    // Note: if user on heartbeat and sockets doesn match, send confirmation/warning to the user on heartbeat!
    if (snd && snd.sck != socket) { sck_mismatch = true; console.log(`[${snd_id}]>[Warning! Sockets mismatch!]`); }
    if (ping_state && sck_mismatch) { console.log(`[${snd_id}]>[Warning! Takeover attempt, original user has heartbeat!]`); return true; }
    add_user({ snd_id, sck: socket });
    return true;
}