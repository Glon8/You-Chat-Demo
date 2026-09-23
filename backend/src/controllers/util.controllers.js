import { get_user, upd_rel_sync } from '../data/users.data.js'
import { get_relays, add_relay } from '../data/relays.data.js';

export const ping = (req, res) => {
    console.log('[Ping received]')

    const { snd_id } = req.body ?? {};

    const snd = get_user(snd_id);

    if (!snd) { res.sendStatus(200); return; }

    const snd_sync = snd.rel_sync;

    if (snd_sync && Date.now() < snd_sync + 1000 * 60 * 60) res.sendStatus(200);
    else { res.json({ sync_stat: true }); }
}

export const rel_upd = (req, res) => {
    console.log('[Relay Update received]');

    const { snd_id, data } = req.body ?? {};

    const relays = get_relays();

    if (data && data.length > 0) data.forEach(it => { if (!relays.has(it)) add_relay(it); });

    if (get_user(snd_id)) upd_rel_sync(snd_id);

    res.sendStatus(204);
}