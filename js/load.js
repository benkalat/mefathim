function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}



function check_connect(){
    connect = getCookie("LoggedIn");
    if (connect == undefined) {
        window.location.href = "login.html";
    }
    else{
        $.post( "scripts/check_connect.py", JSON.stringify({ "cookie": connect }))
        .done(function( data ) {
            myObj = JSON.parse(data);
            if (myObj.ok == false){
                window.location.href = "login.html";
            }
        });
    }
}



user_id = "";

function buildnavbar(){

    objects=[];

    $.get("scripts/user_data.py", function(result){
        user_data = JSON.parse(result);
        if (user_data.ok == false) {
            window.location.href = "login.html";
        }
        user_id = user_data.data.id;
        picture_number = user_data.data.picture_number;
        if (picture_number == ""){
            picture_number = "22";
        }
        objects[0]=user_data["data"]["nickname"];
        f();
    });

    function f(){
        ourlocation = location.href.split("/").slice(-1)[0];
        objects[1]="העדפות"
        objects[2]="preferences.html";
        objects[3]="שינוי סיסמה";
        objects[4]="change_password.html";


        navbar='';
        logo="<a class='navbar-brand'href='home_page.html'><img src='img/logo.png'alt='logo'id='logo' style='width:400px;height: 120px;'></a>";
        exit="<ul class='navbar-nav ml-auto'><li class='nav-item'><a class='nav-link active'href='scripts/logged_out.py'>יציאה</a></li>";
        profile='<li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'+objects[0]+'</a><div class="dropdown-menu dropdown-menu-right" style="text-align: center">';
        
        navbar+=logo+exit;
    
        for(i=1; i<objects.length-1; i+=2){
            if(objects[i+1]==ourlocation.split("?")[0]){
                continue;
            }
            profile+="<a class='dropdown-item' href="+objects[i+1]+">"+objects[i]+"</a>";
        }

        profile+="</div></li>"

        face="<div id='profile'><img src='img/avatars/"+picture_number+".png'id='face'><div id='user'class='title'></div>";

        navbar+=profile+face;
    
        var navigation = document.getElementById("nav");   
        navigation.innerHTML = navbar;
    }
}


function get_connected_users(){
    
    $.get("scripts/users_get.py", function(result){
       // console.log(result);
        var users = JSON.parse(result);
        if (users.ok == false) {
          window.location.href = "login.html";
        }else {
            var faces = "<div class=''><ul class='list-group'><li class='list-group-item users' style='text-align: center'>כרגע באתר</li>";
            for (x in users.data) {
                sel = users.data[x];
                img_num = sel.picture_number;
                if (img_num == null){
                    img_num = "22";
                }
                if (sel.id == user_id) {

                    
                    faces += "<li class=' list-group-item users'><div class='float-right' style='margin-top:25px;'>"
                    + "את \/ אתה " +"</div><div class='float-left'><img src='img/avatars/"
                    +img_num+".png' style=' border-radius:50%;' class='users_face' id='face'></div></li>";
                } else {
                    faces += "<li class=' list-group-item users'><div class='float-right' style='margin-top:25px;'>"
                    + sel.nickname +"</div><div class='float-left'><img src='img/avatars/"
                    +img_num+".png' style=' border-radius:50%;' class='users_face' id='face'></div></li>";
                }
            }
            faces += "</ul></div>"
            $("#now_logged").html(faces);
        }
    });
}
function print_post() {
			
        $.get("scripts/get_posts.py", function(data){
        var all_posts = JSON.parse(data);
        
        var i = 0;
        var btn_more = "";
        var posts = "";
        
        for (x in all_posts)
        {
            
            sel = all_posts[x];
            
            posts += "<div class=' show_posts' style='background-color: "  +";'><p class='details'>    מאת: "+
             sel.user +"  |   "+ sel.writing_time +"</p><p class='post'> "+ sel.text +
            "</p></div>";
            
            
            
        }
    //    console.log(data);
        $(".posts").html(posts);
        $("#text").val('');
    });
}