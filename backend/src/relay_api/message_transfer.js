export const msg_trans = async (link, data) => {
    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

    try {
        const res = await fetch('https://' + String(link) + '/api/msg-rcv', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: { data } });
    }
    catch (error) {
        console.log(`[Status] Failed\r\n${error}`);
    }
}