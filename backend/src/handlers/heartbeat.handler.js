export const ping_check = (socket, timeout, user_id) => {
    return new Promise((resolve) => {
        const pong_state = () => {
            clearTimeout(timer);
            resolve(true);
        }

        socket.once('pong', pong_state);
        socket.ping();

        const timer = setTimeout(() => {
            socket.off('pong', pong_state);
            resolve(false);
        }, timeout * 1000);
    });
}


