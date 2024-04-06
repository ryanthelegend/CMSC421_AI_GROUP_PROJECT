const express = require('express')
const axios = require('axios')
const app = express()

app.get("/api", (req, res) => {
    res.json({"users" : ["Document Summary", "URL Summary", "data3", "new data"]})
})

app.post('/api/summarize',async(req,res)=>{
    const{text,url,pdf_path,max_tokens} = req.body;

    try {
        const flaskResponse = await axios.post('http://localhost:5002/generate',{
            text,
            url,
            pdf_path,
            max_tokens
        });
        res.json(flaskResponse.data)
    }catch (error){
        console.error('Error calling Flask server:',error)
        res.status(500).send('Internal Server Error')
    }
})


app.listen(5001, () => {console.log("server started on port 5000")})
