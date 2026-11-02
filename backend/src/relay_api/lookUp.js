import { get_user } from "../data/users.data.js"
import { get_relays } from "../data/relays.data.js"
import { ping } from "./ping.js"
import { sleep } from "../controllers/util.controllers.js"
/*
    3 phases:
        * Last, must return boolean, if the cnt_id, is found in its client list. <=== LookUp func
        * Middle, ll return pre last TTL (that received the boolean) and return, associated link. <=== LookUp func
        * First, ll check, whether the TTL is 0, and if its so, ll send the package to associated number. 
*/
export const lookUp = async (req, res) => {
    const { cnt_id, curTTL } = req.data;

    const TTL = 1 + curTTL[0];
    const maxTTL = curTTL[1];
    // Last phase
    if (!!get_user(cnt_id)) { res.sendStatus(200); return; }
    // Middle phase
    if (TTL > maxTTL) { res.sendStatus(429); return; }

    get_relays().forEach(async (link) => {
        let ping_state = await ping(link);

        if (!ping_state) { await sleep(5000); ping_state = await ping(link); }

        if (ping_state) {
            try {
                response = await fetch(String(link) + '/api/lookup', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: { cnt_id, curTTL: [TTL, maxTTL] } });

                if (response.ok) { res.json({ TTL, link }); return; }
            }
            catch (error) { res.sendStatus(500); console.log(`[Look Up] 500\r\n${error}`); }
        }
    });
}