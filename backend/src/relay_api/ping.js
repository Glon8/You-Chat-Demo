export const ping = async (link) => {
    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

    console.log(`[Ping sent] ${String(link)}`);

    try {
        const res = await fetch('https://' + String(link) + '/api/ping', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '' });

        console.log(`[Ping res code] ${res.status}`);

        return res.ok;
    }
    catch (error) { console.log(`[Ping res code] 500\r\n${error.message}`); return false; }
}