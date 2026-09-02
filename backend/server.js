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

const server = app.listen(port, '0.0.0.0', () => { console.log(`Server started at port: ${port}`) });

wss_init(server);