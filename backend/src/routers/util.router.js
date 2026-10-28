import express from 'express'
import { ping_mngr, rel_upd, HaSh_mngr } from '../controllers/util.controllers.js'

const utilRouter = express.Router();

utilRouter.post('/ping', ping_mngr);
utilRouter.post('/rel-upd', rel_upd);
utilRouter.post('/handshake', HaSh_mngr);

export default utilRouter;