import { get_user, upd_rel_sync } from '../data/users.data.js'
import { get_relays, add_relay } from '../data/relays.data.js'
import { transfer } from '../handlers/transition.handler.js'

export const ping_mngr = (req, res) => {
    console.log('[Ping received]')

    const { snd_id } = req.body ?? {};

    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

    const snd = get_user(snd_id);

    if (!snd) return res.sendStatus(200);

    const snd_sync = snd.rel_sync;

    if (snd_sync && Date.now() <= snd_sync + 1000 * 60 * 60) return res.sendStatus(200);
    else { return res.json({ sync_stat: true }); }
}

export const rel_upd = (req, res) => {
    console.log('[Relay Update received]');

    const { snd_id, data } = req?.body ?? {};

    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

    const relays = get_relays();

    if (data && data.length > 0) data.forEach(it => { if (!relays.has(it)) add_relay(it); });

    if (get_user(snd_id)) upd_rel_sync(snd_id);
    //=================================== FOR DEBUG ONLY
    console.log('[Relay Peer List]');
    console.log(relays)

    return res.sendStatus(200);
}

export const HaSh_mngr = (req, res) => { }

export const sleep = async (ms) => new Promise(resolve => setTimeout(resolve, ms));

export const msg_rcv = async (req, res) => {
    // data_package full package, not only the encrypted message
    const { data } = req?.body ?? {};

    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED
    
    console.log(`[Outer message transfer]\r\n[From] ${link}\r\n[To] ${rcv_id}`);

    await transfer(data);

    return res.sendStatus(200);
}