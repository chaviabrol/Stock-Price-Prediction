const express = require("express");
const ejs = require("ejs");
const {  spawn } = require('child_process');
// const { title } = require("process");
// var plotly = require('plotly')("chavi123", "PtVwlLfJmIn3C3UbCSZ2")
const app = express();


// const childPython = spawn('python', ['--version']);
// const childPython = spawn('python', ['applepickle.py']);
// childPython.stdout.on('data',(data) =>{
//     console.log('stdout:'+ data);
// });
// childPython.stderr.on('data',(data) =>{
//     console.error('stderr:' +data);
// });

app.set('view engine', 'ejs');
app.use(express.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/",function(req,res){
    res.render("main");
});
app.get("/company",function(req,res){
    res.render("company");
});
app.get("/company/:postId", function(req, res){

    const requestedPostId = req.params.postId;
        res.render(requestedPostId, {title:requestedPostId});
    
});   

app.listen("3000", function(){
    console.log("Server started at port 3000");
});