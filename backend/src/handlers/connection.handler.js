import { add_user } from "../data/users.data";

export const connect = (req_type, snd_id, socket) => {
    if (req_type != 'cnn') return false;

    const snd = get_user(snd_id);

    console.log(`[${snd_id}]>[Request for registration]`);
    // check heart beat of registered user and the socket
    // Note: if user on heartbeat and sockets doesn match, send confirmation/warning to the user on heartbeat!
    if (snd && snd.sck != socket /*&& false*/) {
        console.log(`[${snd_id}]>[sockets: ${snd.sck != socket}]>[Warning! User has no heartbeat or sockets doesnt match]`);
    }
    add_user({ snd_id, sck: socket });
    return true;
}