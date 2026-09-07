const users = {};
/*
    users list, will include PER USER: 
    user id certificate: {
        socket,              // < sck
        last_seen,           // < ls
        expired_heartrate,   // < xphrt
    }
*/
export const get_user = (user_id) => users[user_id];

export const add_user = (user_data) => {
    const { snd_id, sck } = user_data;

    // < must include user_data harsh values validation

    const date = Date.now()

    users[snd_id] = { sck, ls: date, xphrt: date + (5 * 1000), }

    return true;
}

export const rmv_user = (user_id) => delete users[user_id];

export const upd_xphrt = (user_id) => users[user_id].xphrt = Date.now() + (5 * 1000);
