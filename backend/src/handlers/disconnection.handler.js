import { rmv_user, get_user, upd_xphrt } from "../data/users.data.js";
import { ping_check } from "./heartbeat.handler.js";

export const disconnect = async (req_type, snd_id, socket) => {
    if (req_type != 'dsc') return false;

    const snd = get_user(snd_id);
    // known/unknown user sends disconnection request
    // Note: remove the user, only if sockets match and saved user on heartbeat!
    let ping_state = true;
    // checking if reciever has positive heartbeat
    if (snd && Date.now() > snd.xphrt) {
        ping_state = await ping_check(snd.sck, 5);

        if (ping_state) upd_xphrt(snd_id);
    }

    console.log(`[${snd_id}]>[Request for disconnect]`);

    if (snd && snd.sck != socket) { console.log(`[${snd_id}]>[Warning! Sockets mismatch!]`); return true; }
    if (!ping_state) { console.log(`[${snd_id}]>[Warning! Takeover attempt, original user has no heartbeat!]`); return true; }

    rmv_user(snd_id);

    socket.close();

    return true;
}