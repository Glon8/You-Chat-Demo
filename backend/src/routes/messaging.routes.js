import express from 'express'

import { snd_msg } from '../controllers/messaging.contollers';

const msg_router = express.Router();

msg_router.post('/snd', snd_msg); // < send a message

export default msg_router;