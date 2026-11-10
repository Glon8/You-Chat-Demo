export const msg_trans = async (link, data) => {
    // <<<<<<<<<<<<<<<<<<<<<<< STRICT DATA VERIFICATION REQUIRED

    let converted;

    try {
        JSON.parse(data);

        converted = data;
    }
    catch (error) {
        converted = JSON.stringify(data);
    }

    try {
        const res = await fetch('https://' + String(link) + '/api/msg-rcv', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: converted });
    }
    catch (error) {
        console.log(`[Status] Failed\r\n${error}`);
    }
}