export const message = (data, req_type) => {
    if (req_type != 'msg') return false;

    const { snd_id, rcv_id, trn_dt, tm_stm } = JSON.parse(data.toString());

    const rcv = get_user(rcv_id);

    console.log(`[${snd_id}]>[Request for message transfer]`);
    // checking if reciever exists
    if (!rcv) {
        console.log(`[${rcv_id}]>[Warning! Receiver not registred]`);
        // < transfer to another relay
        console.log('[Data transferred to another relay]')
        return true;
    }
    // checking if reciever on heartbeat
    if (!true) {
        console.log(`[${rcv_id}]>[Receiver has no heartbeat]`);
        return true;
    }
    // transfer data routed to reciever
    rcv.sck.send(JSON.stringify({ snd_id, rcv_id, req_type, trn_dt, tm_stm }));

    return true;
}