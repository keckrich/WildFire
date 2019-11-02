var request = new XMLHttpRequest()



request.open('GET', '/api', true)
request.onload = function() {
	

  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
  console.log(data)
    
}

request.send()