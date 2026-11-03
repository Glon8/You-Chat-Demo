import express from 'express'

import { ping_mngr, rel_upd, HaSh_mngr, msg_rcv } from '../controllers/util.controllers.js'

import { lookUp } from '../relay_api/lookUp.js'

const utilRouter = express.Router();

utilRouter.post('/ping', ping_mngr);
utilRouter.post('/rel-upd', rel_upd);
utilRouter.post('/handshake', HaSh_mngr);
utilRouter.post('/msg-rcv', msg_rcv);

utilRouter.post('/lookup', lookUp);

export default utilRouter;