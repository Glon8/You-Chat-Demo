export const ping = (req, res) => {
    console.log('[Ping received]')
    res.sendStatus(200);
} 