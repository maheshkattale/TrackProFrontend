$(document).ready(function(){
    $("#selectcountry").change(function () {
      var url = $("#User_form").attr("data-cities-url");
      var countryId = $(this).val();
      console.log(countryId)
      var html;
    
      $.ajax({
        type:'POST',
        url: 'http://127.0.0.1:8000/userApi/selectstate',
        data: {
          'country': countryId
        },
        success: function (response) {
          console.log(response)
          $(response).each(function(a,b){
           
            console.log(b.id)
            html += "<option value='"+b.id+"'>" + b.state +" </option>"
          });
          $("#selectstate").html(html);
        }
      });
      });  
    }) 
    
     
    $(document).ready(function(){
      select();
   });
      function  select(){
        var countryId = $('#selectcountry').val();
        var html;
  
        $.ajax({
          type:'POST',
          url: 'http://127.0.0.1:8000/userApi/selectstate',
          data: {
            'country': countryId
          },
          success: function (response) {
              
            $(response).each(function(states,cuntrys){
              html += "<option value='"+cuntrys.id+"'>" + cuntrys.state +" </option>"
            });
            $("#selectstate").html(html);
            $('#selectstate').val(selectstate);
          
          }
        });
        var selectstate;
        var studentformdata = JSON.parse(document.getElementById('User').textContent);
        $(studentformdata).each(function(ind,txt){
          selectstate = txt.state
        });
        };  



    