const users = {};
/*
    users list, will include PER USER: 
    user id certificate: {
        socket,              // < sck
        connceted_since,     // < cnn_snc
        expired_heartrate,   // < xphrt
        last_seen,           // < ls
    }
*/
export const get_user = (user_id) => users[user_id];

export const add_user = (user_data) => {
    const { snd_id, sck } = user_data;

    // < must include user_data harsh values validation

    const date = Date.now()

    users[snd_id] = { sck, cnn_snc: date, xphrt: date + (5 * 1000), }

    return true;
}

export const rmv_user = (user_id) => delete users[user_id];

export const upd_xphrt = (user_id) => users[user_id].xphrt = Date.now() + (5 * 1000);

export const upd_sck = (user_id, socket) => users[user_id].sck = socket;
