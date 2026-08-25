const users = {};

export const get_users = () => users

export const add_user = () => { }

export const rmv_user = () => { }

/*
    users list, will include PER USER: 
    user id certificate: {
        ipv4/ipv6, 
        local_port,
        last_seen,
        heartbit_time_until,
    }
*/