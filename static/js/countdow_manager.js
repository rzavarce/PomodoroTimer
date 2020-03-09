$(document).ready(function(){

 var audio = $("audio")[0]; 
  
 var countTime = 0;
 var breakTime = 0;
 var pomodoros_laps = 0
 var longBreakTime = 0;

 var pause = false;
 var seconds = 0;
 var minutes = 0;

 var counting;

 $('.timer').html(minutes + ":00");
  

 //FUNCTION COUNTDOWN CONTROLLER 
 function countdown(){
    
    
    if(minutes === 0 && seconds === 1){
      //play the sound on both
      audio.play();
    }
   
   if(minutes === 0 && seconds === 0){

      if($('.title').text() === 'Pomodoro'){
        pomodoros_laps++;
        if(pomodoros_laps<3){
          $('.title').text('Break');
          minutes = breakTime;
          $('.timer').html(minutes + ":0" + seconds);
        }else{
          $('.title').text('Long Break');
          minutes = longBreakTime;
          $('.timer').html(minutes + ":0" + seconds);
          pomodoros_laps=0;
        }
      }
      else if($('.title').text() === 'Break'){
          $('.title').text('Pomodoro');
          minutes = countTime;
          $('.timer').html(minutes + ":0" + seconds);
      }
      else if($('.title').text() === 'Long Break'){
        $('.title').text('Pomodoro');
        minutes = countTime;
        $('.timer').html(minutes + ":0" + seconds);
      }
   }
   else{
      if(seconds === 0){seconds = 60; minutes--}
      seconds--;
      if(seconds < 10){$('.timer').html(minutes + ":0" + seconds);}
      else{
      $('.timer').html(minutes + ":" + seconds);
      }
   }
  }
  
  //for all, if we are paused, change our timer displays and reset text so clock is completely reset
  $('#minusBreak').click(function(){
    if(pause === false){
    if(breakTime > 1){
      breakTime--; 
      $("#break").html(breakTime); 
      $('.title').text('Pomodoro'); 
      $(".timer").html(countTime + ":00");
       //reset times
       seconds = 0;
       minutes = countTime;}
    }
  });
  $('#plusBreak').click(function(){
    if(pause === false){
      breakTime++; 
      $("#break").html(breakTime);
      $('.title').text('Pomodoro');
      $(".timer").html(countTime + ":00");
    //reset times
       seconds = 0;
       minutes = countTime;
    }
  });
  $('#minusLongBreak').click(function(){
    if(pause === false){
    if(longBreakTime > 1){
      longBreakTime--; 
      $("#long_break").html(longBreakTime); 
      $('.title').text('Pomodoro'); 
      $(".timer").html(countTime + ":00");
       //reset times
       seconds = 0;
       minutes = countTime;}
    }
  });
  $('#plusLongBreak').click(function(){
    if(pause === false){
      longBreakTime++; 
      $("#long_break").html(longBreakTime);
      $('.title').text('Pomodoro');
      $(".timer").html(countTime + ":00");
      //reset times
       seconds = 0;
       minutes = countTime;
    }
  });
   $('#minusCount').click(function(){
     if(pause === false){
        if(countTime > 1){
          countTime--; 
          $("#count").html(countTime); 
          $(".timer").html(countTime + ":00");        
          $('.title').text('Pomodoro');
        }
       //reset times
       seconds = 0;
       minutes = countTime;
     }
  });
  $('#plusCount').click(function(){
    if(pause === false){
    countTime++; $("#count").html(countTime);
      $(".timer").html(countTime + ":00");
      $('.title').text('Pomodoro');

      //reset times
      seconds = 0;
      minutes = countTime;
    }
  });
  

//FUNCTION START/STOP POMODORO
  $('#pomodoro_controller').click(function(){
    
   if(pause === false && $(this).is(':checked')){
     counting = setInterval(countdown, 1000);
     pause = true;
   }
   else if(pause === true && !$(this).is(':checked')){
     clearInterval(counting);
     pause = false;
   }
  });


  //FUNCTION ACTIVE POMODORO IF A TASK PENDINT EXISTS
  $('#id_task').change(function(){
    //console.log($('#id_task').val());
   if($('#id_task').val()=="Null"){
      
      $("#pomodoro_controller").prop('checked', false);
      $(".pomodoro_controller_content").hide( "slow" );

      if(countTime > 1){
          $("#count").html(countTime); 
          $(".timer").html(countTime + ":00");        
          $('.title').text('Pomodoro');
        }
       //reset times
       seconds = 0;
       minutes = countTime;

       if(pause === true && !$(this).is(':checked')){
         clearInterval(counting);
         pause = false;
       }

      //console.log('ssssssss');

   }else{
      console.log('zzzzzzz');
      $(".pomodoro_controller_content").show( "slow" );
      config_setting();

   }
  });


//FUNCTION API TASK CONTROLER
function config_setting() {
  task_active = $("#id_task").val()
  $.ajax({
    url : "http://localhost:8000/tasks/"+task_active,
    dataType: "json",
    success : function (data) {

        console.log(data['tsk_config']['cnf_lap_time']);

        countTime = data['tsk_config']['cnf_lap_time']

        if(countTime > 0){
          $("#count").html(countTime); 
          $(".timer").html(countTime + ":00");        
          $('.title').text('Pomodoro');
        }

        breakTime = data['tsk_config']['cnf_time_short_brake']
        $("#break").html(data['tsk_config']['cnf_time_short_brake']);


        longBreakTime = data['tsk_config']['cnf_time_long_brake']
        $("#long_break").html(data['tsk_config']['cnf_time_long_brake']);


        //reset times
        seconds = 0;
        minutes = countTime;

        $('#pomodoro_controller').prop('checked', false);

      }
   });
}





//FUNCTION API TASK CONTROLER
  function task_update() {
    $.ajax({
      url : "http://localhost:8000/tasks",
      dataType: "json",
      success : function (data) {
          

          task_active = $("#id_task").val()

          var firstOption = $("#id_task option:first-child");
          $("#id_task").empty().append(firstOption);

          $.each(data['results'], function(i, item) {
              //console.log(item);

              if(item.id == task_active){
                $("#id_task").append('<option value="'+ item.id +'" selected>'+ item.tsk_title +'</option>')
              }else{
                $("#id_task").append('<option value="'+ item.id +'">'+ item.tsk_title +'</option>')
              }

              
          });



        }
     });
  }
  setInterval(task_update, 3000);



});








