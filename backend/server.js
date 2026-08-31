import express from 'express'
import cors from 'cors'

import { wss_init } from './websockets-server.js';

const app = express();
const port = process.env.PORT || 5000;

app.use(cors({
    origin: [
        `http://localhost:5173`,
    ],
    credentials: true
}));
app.use(express.json());

const server = app.listen(port, () => {
    if (port == 5000) console.log(`Server started at http://localhost:${port}`);
    else console.log(`Server started at port: ${port}`);
});

wss_init(server);