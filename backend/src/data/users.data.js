const users = {};
/*
    users list, will include PER USER: 
    user id certificate: {
        socket,              // < sck
        last_seen,           // < ls
        heartbit_time_until, // < hbu
    }
*/
export const get_user = (user_id) => users[user_id];

export const add_user = (user_data) => {
    const { snd_id, sck } = user_data;

    // < must include user_data harsh values validation

    const date = Date.now()

    users[snd_id] = {
        sck,
        ls: date,
        hbu: date + (5 * 60 * 1000), // < estimated five minutes for heart beat > upon IDLE connection
    }

    return true;
}

export const rmv_user = (user_id) => delete users[user_id];