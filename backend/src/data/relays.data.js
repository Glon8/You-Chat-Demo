const relays = new Set();
/*
    relays list may include just a set of keys of relay_cnn_crt for each relay
    relay_cnn_crt - is a link/ip that the relay can be reached by
*/
export const get_relays = () => relays;

export const add_relay = (relay_cnn_crt) => {
    // < relay connection(cnn) certificate(crt) harsh verification

    relays.add(relay_cnn_crt);
}

export const rmv_relay = (relay_cnn_crt) => relays.delete(relay_cnn_crt);