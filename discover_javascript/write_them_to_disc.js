var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_school',
	'Authorization': 'token bda95ce68a968bacccce67f5d2ce34c5c5657a3f'
    }
}

var callback1 = function(res) { 
  streamToString(res, write  );
}

var req = https.request( options,callback1 );

function streamToString(stream, cb) {
 const chunks = [];
 stream.on('data', (chunk) => {
   chunks.push(chunk);
 });
 stream.on('end', () => {
   cb(chunks.join(''));
 });
}

var write = function(jsonString){
var fs = require('fs');
fs.writeFile("/tmp/16", jsonString, function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
}); 
}

req.end();

req.on('error', function(e) {
 console.error(e);
});

var longString = function(jsonString){                   
   console.log(typeof jsonString);
   console.log(jsonString);
}

