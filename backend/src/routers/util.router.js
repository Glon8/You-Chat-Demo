import express from 'express'
import { ping, rel_upd } from '../controllers/util.controllers.js'

const utilRouter = express.Router();

utilRouter.get('/ping', ping);
utilRouter.get('/rel-upd', rel_upd);

export default utilRouter;