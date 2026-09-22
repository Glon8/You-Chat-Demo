import express from 'express'
import { ping, rel_upd } from '../controllers/util.controllers.js'

const utilRouter = express.Router();

utilRouter.post('/ping', ping);
utilRouter.post('/rel-upd', rel_upd);

export default utilRouter;