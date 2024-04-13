express = require("express")
const app = express()

app.get("/api", (req, res) => {
    res.json({"users" : ["Document Summary", "URL Summary", "data3", "new data"]})
})

app.listen(5000, () => {console.log("server started on port 5000")})