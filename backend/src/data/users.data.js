const users = {};
/*
    users list, will include PER USER: 
    user id certificate: {
        ipv4/ipv6, 
        local_port,
        last_seen,
        heartbit_time_until,
    }
*/
export const get_user = (user_cer) => users[user_cer];

export const add_user = (user_data) => {
    const { user, ip6, ip4, lp } = user_data;

    // < must include user_data harsh values validation

    const date = Date.now()

    users[user] = {
        ip6: ip6 ?? null,
        ip4: ip4 ?? null,
        lp: lp ?? null,
        ls: date,
        hbu: date + (5 * 60 * 1000), // < estimated five minutes for heart beat > upon IDLE connection
    }
}

export const rmv_user = (user_cer) => delete users[user_cer];