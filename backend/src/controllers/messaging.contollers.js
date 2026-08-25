export const snd_msg = (req, res) => {
    const msg_data = req.data;

    /*
    message data:
    {
        sender_identifier,
        reciever_identifier,
        data: {
            message,
            image,
            files,
            etc
            ...
        }
        restricted_routes,
    }
    */

    // verify msg_data fields, eg strict verification
    // verify sender and reciever identifiers > must be in a relay list > ip must match as long as sender or a reciever has a positive heartbeat
    // verify if it is a valid route > if not pass it to another relay
    // pass the message to the reciever
}