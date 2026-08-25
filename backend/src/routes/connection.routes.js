import express from 'express'

const cnn_router = express.Router();

cnn_router.post('/dsc', func); // < disconnect
cnn_router.post('/cnn', func); // < connect

export default cnn_router;