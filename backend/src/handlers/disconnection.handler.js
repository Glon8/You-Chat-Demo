import { rmv_user, get_user } from "../data/users.data.js";

export const disconnect = async (req_type, snd_id, socket) => {
    if (req_type != 'dsc') return false;

    console.log(`[${snd_id}]>[Request for disconnect]`);

    const snd = get_user(snd_id);
    //check the sockets origins
    if (snd && snd.sck != socket) { console.log(`[${snd_id}]>[Warning! Takeover attempt, sockets mismatch!]`); return true; }

    rmv_user(snd_id);

    socket.close();

    return true;
}