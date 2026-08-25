import express from 'express'

import cnn_router from './src/routes/connection.routes'
import msg_router from './src/routes/messaging.routes';

const app = express();
const port = process.env.PORT || 5000;


app.use(cors({
    origin: [
        `http://localhost:5173`,
    ],
    credentals: true
}));
app.use(express.json());

app.use('/api/cnn', cnn_router); // < connection
app.use('/api/msg', msg_router); // < messaging

app.listen(port, () => {
    if(port == 5000) console.log(`Server started at http://localhost:${port}`);
    else console.log(`Server started at port: ${port}`);
})