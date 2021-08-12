const express = require('express')
var request = require('then-request');
const http = require('http');
const expressHandlebars = require('express-handlebars')

const app = express()

const port = process.env.PORT || 3000

var options = {
  host: '127.0.0.1',
  port: 8080,
  path: '/country',
  method: 'GET'
};
// custom 404 page
//app.use((req, res) => {
//  res.type('text/plain')
//  res.status(404)
//  res.send('404 - Not Found')
//})

// custom 500 page
//app.use((err, req, res, next) => {
 // console.error(err.message)
 // res.type('text/plain')
 // res.status(500)
 // res.send('500 - Server Error')
//})
let countryList = [];
let stateList = [];
let dict = {};

app.engine('handlebars', expressHandlebars({
  defaultLayout: 'main',
}))
app.set('view engine', 'handlebars');
app.get('/', (req, res) => res.render('form', {countries : countryList}));
http.request(options, function(response) {
	var str = '';
	response.on('data', function (chunk) {
    	str += chunk;
	});
	console.log(str);
	response.on('end', function () {
		//console.log(str);
		//console.log(typeof str);
		let countries = JSON.parse(str);
		//console.log(countries);
		//console.log(typeof countries);
		countries.forEach(function(country) {
			countryList.push(country.name);			
			dict[country.name] = country.phonecode;
		});
		app.listen(port, () => console.log(
  `Express started on http://localhost:${port}; ` +
  `press Ctrl-C to terminate.`));
	console.log(countryList);
	});
}).end();

