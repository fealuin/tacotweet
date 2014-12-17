
var locations = [
      ['Macul', -33.507200, -70.590300, 1],
      ['Tobalaba', -33.473962, -70.554444, 2]
    ];

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

	// geocoding
	/*var geocoding = new google.maps.Geocoder();
	$("#submit_button_geocoding").click(function(){
		codeAddress(geocoding);
	});
	$("#submit_button_reverse").click(function(){
		codeLatLng(geocoding);
	});*/
}

/*
function codeLatLng(geocoding){
	var input = $('#search_box_reverse').val();
	console.log(input);
	var latlngbounds = new google.maps.LatLngBounds();
	var listener;
	var regex = /([1-9])+\.([1-9])+\,([1-9])+\.([1-9])+/g;

	if(regex.test(input)) {

		var latLngStr = input.split(",",2);
		var lat = parseFloat(latLngStr[0]);
		var lng = parseFloat(latLngStr[1]);
		var latLng = new google.maps.LatLng(lat, lng);

		geocoding.geocode({'latLng': latLng}, function(results, status) {
			console.log(results);
			console.log(status);
			if (status == google.maps.GeocoderStatus.OK){
				if(locations.length > 0){
					//map.setZoom(11);
					var marker;
					var i;

					map.setCenter(locations[1].geometry.location);
					info = new google.maps.InfoWindow();

					for(i = 0; i < locations.length; i++){
						//latlngbounds.extend(locations[i].geometry.location);
						marker = new google.maps.Marker({
							map: map,
							position: new google.maps.LatLng(locations[i][1], locations[i][2])
						});
						google.maps.event.addListener(marker, 'click', (function(marker,i) {
							return function() {
								info.setContent(locations[i][0]);
								info.open(map,marker);
							}
						})(marker,i));
					}

					map.fitBounds(latlngbounds);
					listener = google.maps.event.addListener(map, "idle", function() {
						if (map.getZoom() > 16) map.setZoom(16);
						google.maps.event.removeListener(listener);
					});
				}
			}
			else{
				alert("Geocoder failed due to: " + status);
			}
		});
	}else{
		alert("Wrong lat,lng format!");
	}
}

function codeAddress(geocoding){
	var address = $("#search_box_geocoding").val();
	if(address.length > 0){
		geocoding.geocode({'address': address},function(results, status){
			if(status == google.maps.GeocoderStatus.OK){
				map.setCenter(locations[0].geometry.location);
					var marker = new google.maps.Marker({
					map: map,
					position: locations[0].geometry.location
				});
			}else{
				alert("Geocode was not successful for the following reason: " + status);
			}
		});
	}else{
		alert("Search field can't be blank");
	}
}*/

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