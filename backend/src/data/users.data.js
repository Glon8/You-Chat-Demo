const users = {};
/*
    users list, will include PER USER: 
    user id certificate: {
        socket,               // < sck
        last_seen,            // < ls
        relay_syncronisation, // < rel_sync
    }
*/
export const get_user = (user_id) => users[user_id];

export const add_user = (user_data) => {
    const { snd_id, sck } = user_data;

    // < must include user_data harsh values validation

    const date = Date.now()

    users[snd_id] = { sck, ls: date, rel_sync: date }

    return true;
}

export const rmv_user = (user_id) => delete users[user_id];

export const upd_ls = (user_id) => users[user_id].ls = Date.now();

export const upd_rel_sync = (user_id) => users[user_id].rel_sync = Date.now();

export const upd_sck = (user_id, socket) => users[user_id].sck = socket;
