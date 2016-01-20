$(document).ready(function(){
  console.log("hello")
  });
var latitude = "";
var longitude = "";
function getLocation(){
      console.log("funciont works")
      if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showPosition);
      } else {
        html+"Geolocaion is not supported by this browser"
      }
    function showPosition(position){
      latitude=position.coords.latitude;
      longitude = position.coords.longitude;
      location={
        'latitude':latitude,
        'location':location
      }
    }
    }