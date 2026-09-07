import express from 'express'
import { ping } from '../controllers/util.controllers.js'

const utilRouter = express.Router();

utilRouter.get('/ping', ping);

export default utilRouter;