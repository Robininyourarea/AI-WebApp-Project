import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import axios from 'axios';
import pg from "pg";
import bcrypt from "bcrypt";
import env from "dotenv";


const app = express();
const port = 5000;
const saltRounds = 10;

env.config();

const db = new pg.Client({
    user: process.env.PG_USER,
    host: process.env.PG_HOST,
    database: process.env.PG_DATABASE,
    password: process.env.PG_PASSWORD,
    port: process.env.PG_PORT
});

db.connect()

app.use(cors());
app.use(express.json({ limit: '10mb' }));
app.use(bodyParser.urlencoded({ extend: true}));

app.get("/", (req, res) => {
    res.json({message: 'Hello from the server'})
})

// login endpoint
app.post("/login", async (req, res) => {
    // console.log(req.body);
    const email = req.body.email;
    const password = req.body.password;

    try {
        const result = await db.query("SELECT * FROM users WHERE email = $1", [email])
        if (result.rows.length > 0) {
            const user = result.rows[0];
            const storedHashedPassword = user.password;

            //verifying the password
            bcrypt.compare(password, storedHashedPassword, (err, result) => {
                if (err) {
                    console.log("Error comparing passwords:", err);
                } else {
                    if (result) {
                        res.json({ message: 'Login successful' });
                    } else {
                        res.json({ message: 'Incorrect password' });
                    }
                }
            })
        } else {
            res.json({ message: 'User not found' })
        }
    } catch (err) {
        console.log(err);
    }

});

// register endpoint
app.post("/register", async (req, res) => {
    
    const regEmail = req.body.email;
    const regPassword = req.body.password;
    try {
        const checkResult = await db.query("SELECT * FROM users WHERE email = $1", [regEmail])

        if (checkResult.rows.length > 0) {
            res.json({message: 'Email already exists. Try logging in.'});
        } else {
            bcrypt.hash(regPassword, saltRounds, async (err, hash) => {
                if (err) {
                    console.error("Error hashing password:", err);
                } else {
                    const result = await db.query("INSERT INTO users (email, password) VALUES ($1, $2)",
                        [regEmail, hash]
                    );
                    res.json({message: 'Your registration already successfully'});
                }
            })
        }    
    } catch (err) {
        console.log(err);
    }
    console.log(regEmail);
    console.log(regPassword);
})

// classify endpoint
app.post("/cls_upload-image", async (req, res) => {
    console.log('image has send to this endpoint');
    console.log(req.body);
    // res.json({message: 'predict successful'})
    try {
        const image = req.body.image;
        const model = req.body.model;
        console.log(model)
        // Forward image to aiserver.py
        const aiserverURL = 'http://localhost:3000/cls_predict'
        const response = await axios.post(aiserverURL, {image, model});

        // Return response from aiserver.py to the client
        res.json(response.data);
    } catch (error) {
        console.error('Error forwarding image to aiserver:', error);
        res.status(500).json({ error: 'Failed to forward image to aiserver' });
    }
})

// object detection endpoint
app.post("/obj_upload-image", async (req, res) => {
    console.log('image has send to this endpoint');
    console.log(req.body);
    // res.json({message: 'predict successful'})
    try {
        const {image} = req.body;
        // Forward image to aiserver.py
        const aiserverURL = 'http://localhost:3000/obj_predict'
        const response = await axios.post(aiserverURL, {image});

        // Return response from aiserver.py to the client
        res.json(response.data);
    } catch (error) {
        console.error('Error forwarding image to aiserver:', error);
        res.status(500).json({ error: 'Failed to forward image to aiserver' });
    }
})

// segment endpoint
app.post("/seg_upload-image", async (req, res) => {
    console.log('image has send to this endpoint');
    console.log(req.body);
    // res.json({message: 'predict successful'})
    try {
        const {image} = req.body;
        // Forward image to aiserver.py
        const aiserverURL = 'http://localhost:3000/seg_predict'
        const response = await axios.post(aiserverURL, {image});

        // Return response from aiserver.py to the client
        res.json(response.data);
    } catch (error) {
        console.error('Error forwarding image to aiserver:', error);
        res.status(500).json({ error: 'Failed to forward image to aiserver' });
    }
})

app.listen(port, () => {
    console.log(`Server running on port ${port}.`)
  });