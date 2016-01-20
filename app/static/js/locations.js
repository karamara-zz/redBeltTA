$(document).ready(function(){
    var latitude = "dd";
var longitude = "dd";
  console.log("hello")
    getLocation();
  });

function getLocation(){
      console.log("funciont works")
      if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showPosition);
      } else {
        html+"Geolocaion is not supported by this browser"
      }
    function showPosition(position){

      latitude=position.coords.latitude;
      var position = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude
      }
      console.log(latitude);
      $.post('/users/location',position,function(res){
        console.log(res)
      } )
      }
    }