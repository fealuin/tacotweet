/*
var locations = [
      ['Macul', -33.507200, -70.590300, 1],
      ['Tobalaba', -33.473962, -70.554444, 2]
    ];
*/

var map;
var info;

$(window).load(function() {
	loadScript();
});

function initialize() {
	var mapOptions = {
		center: new google.maps.LatLng(-33.4691199, -70.641997),
		//center: new google.maps.LatLng(-33.92, 151.25),
		zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		panControl: true,
		scaleControl: false,
		streetViewControl: true,
		overviewMapControl: true
	};
	// initializing map
	map = new google.maps.Map(document.getElementById("map-canvas"),mapOptions);

	var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }

	}

function loadScript() {
	console.log("map loading ...");
	var script = document.createElement('script');
	script.type = 'text/javascript';
	//'https://maps.googleapis.com/maps/api/js?v=3.exp&key=AIzaSyBJYFdplGeKUUEmGZ-vL4ydiSZ09Khsa_o&sensor=false&libraries=drawing'
	script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp' +
	//'&v=3.14'+
	//'&key=AIzaSyBJYFdplGeKUUEmGZ-vL4ydiSZ09Khsa_o'+
	'&libraries=drawing'+
	'&callback=initialize';
	document.body.appendChild(script);
}
