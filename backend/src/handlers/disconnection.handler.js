import { rmv_user } from "../data/users.data";
export const disconnect = (req_type, snd_id, socket) => {
    const snd = get_user(snd_id);
    // known/unknown user sends disconnection request
    // Note: remove the user, only if sockets match and saved user on heartbeat!
    if (req_type != 'dsc' || snd.sck != socket || false) return false;

    console.log(`[${snd_id}]>[Request for disconnect]`);

    rmv_user(snd_id);

    socket.close();

    return true;
}