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
    const { cnt_id, curTTL, bList } = req?.data ?? {};

    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

    const TTL = 1 + curTTL;
    const maxTTL = 2;
    // Last phase
    if (!!get_user(cnt_id)) return res.sendStatus(200);
    // Middle phase
    if (TTL > maxTTL) return res.sendStatus(429);

    const relays = get_relays().filter(link => !bList.includes(link));

    for (const link of relays) {
        if (await ping(link)) {
            bList.push(link);

            await sleep(100);

            try {
                const response = await fetch(String(link) + '/api/lookup',
                    {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ cnt_id, curTTL: TTL, bList })
                    });

                if (response.ok) {
                    const body = await response.json();

                    if (Object.keys(body).length == 0) { return res.status(200).json({ TTL, link }); }
                    else {
                        // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

                        return res.status(200).json(body);
                    }
                }
            }
            catch (error) { console.log(`[=== Look Up ===]\r\n[Link] ${link}\r\n[Status] 500\r\n${error}`); }
        }
    };

    return res.sendStatus(404);
}