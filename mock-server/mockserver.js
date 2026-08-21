import http from 'node:http';
import path from 'node:path';
import fs from 'node:fs/promises';

function getExt(ext){
    const types = {
        ".js":"text/javascript",
        ".css":"text/css",
        ".json":"application/json",
        ".png":"image/png",
        ".jpg":"image/jpeg",
        ".jpeg":"image/jpeg",
        ".gif":"image/gif",
        ".svg":"image/svg+xml"
    }

    return types[ext.toLowerCase()] || "text/html"
}

const mypath = import.meta.dirname;
const folder = './Path/file'; // Change this to the folder you want to serve
const dest = path.join(mypath,folder);

const server = http.createServer(async (req,res)=>{
    const filepaths = path.join(dest, req.url == "/"? "index.html":req.url);
    const fileext = path.extname(filepaths);
    const ext = getExt(fileext);

    try{
        const content = await fs.readFile(filepaths);
        res.statusCode = 200;
        res.setHeader("Content-type", ext)
        res.end(content)
    }catch(err){
        res.statusCode = 404;
        res.setHeader("Content-Type", "text/plain");
        res.end("Page not found!")
        console.log("404")
    }
});

server.listen(3000, console.log("Server is running on port 3000"))