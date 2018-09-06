$(document).ready(function() {
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");
        var teamname = $('#teamName').val();
        var sup = $('#chooseSup').val();
        
        var members = [];
        $.each($("input[name='user_group']:checked"), function() {
            members.push($(this).val());            
        });        

        $.ajax({
            url : "", 
            type : "POST", 
            data : { 'team_name' : teamname, 'team_sup' : sup , 'team_members' : JSON.stringify(members) },
    
            // handle a successful response
            success : function(res) {                
                if(res.error){
                   $("#ifError").text(res.error).show();     
                }else if(res.status === "good"){
                   window.location.replace("/teams");     
                }             
            }           
        });
    });

    
  
  
});