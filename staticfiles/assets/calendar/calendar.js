
var today = new Date();
year = today.getFullYear();
month = today.getMonth();
day = today.getDate();
// var calendar = $('#myEvent').fullCalendar({
//   height: 'auto',
//   defaultView: 'month',
//   editable: true,
//   selectable: true,
//   header: {
//     left: 'prev,next today',
//     center: 'title',
//     right: 'month,agendaWeek,agendaDay,listMonth'
//   },
//   events: [{
//     title: "Palak Jani",
//     start: new Date(year, month, day, 11, 30),

//     // backgroundColor: "#00bcd4"
//   }, ]
// });
$(document).ready(function(){


  var author = $('#author').val();
  console.log(author);

  $.ajax({
    
    // url:"../videre/timetabledata.php",
    url:"{% url 'calendar-data' author %}",
    type : "GET",
    // data:$(this).serialize(),
    dataType:"json",
    beforeSend: function(){
    // Show image container
    $("#loadcal").show();
  // $('#myEvent').html("loading.....")
  // alert("loading");
   },
    success : function(data){
      console.log(data);
    $("#loadcal").hide();
      
var calendar = $('#myEvent').fullCalendar({
  height: 'auto',
  defaultView: 'month',
  editable: true,
  selectable: true,
  header: {
    left: 'prev,next today',
    center: 'title',
    right: 'month,agendaWeek,agendaDay,listMonth'
  },
  events: data

});
// $("#myEvent").fullCalendar({
//   height: 'auto',
//   header: {
//     left: 'prev,next today',
//     center: 'title',
//     right: 'month,agendaWeek,agendaDay,listWeek'
//   },
//   editable: false,
//   events:[data],
//   // events: [
//   //   {
//   //     title: 'Conferences',
//   //     start: '2020-07-10 11:30:00',

//   //     // backgroundColor: "#00bcd4",
//   //     // borderColor: "#fff",
//   //     // textColor: '#000'
//   //   },
//   //   {
//   //     title: "John's Birthday",
//   //     start: '2018-01-14',
//   //     backgroundColor: "#007bff",
//   //     borderColor: "#007bff",
//   //     textColor: '#fff'
//   //   },
//   //   {
//   //     title: 'Reporting',
//   //     start: '2018-01-10T11:30:00',
//   //     backgroundColor: "#f56954",
//   //     borderColor: "#f56954",
//   //     textColor: '#fff'
//   //   },
//   //   {
//   //     title: 'Starting New Project',
//   //     start: '2018-01-11',
//   //     backgroundColor: "#ffc107",
//   //     borderColor: "#ffc107",
//   //     textColor: '#fff'
//   //   },
//   //   {
//   //     title: 'Social Distortion Concert',
//   //     start: '2018-01-24',
//   //     end: '2018-01-27',
//   //     backgroundColor: "#000",
//   //     borderColor: "#000",
//   //     textColor: '#fff'
//   //   },
//   //   {
//   //     title: 'Lunch',
//   //     start: '2020-07-10T13:15:00',
//   //     backgroundColor: "#84646",
//   //     borderColor: "#fff",
//   //     textColor: '#000',
//   //   },
//   //   {
//   //     title: 'Company Trip',
//   //     start: '2018-01-28',
//   //     end: '2018-01-31',
//   //     backgroundColor: "#fff",
//   //     borderColor: "#fff",
//   //     textColor: '#000',
//   //   },
//   // ]

// });
    }
  });
});
