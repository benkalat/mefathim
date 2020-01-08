
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

//check_connect();


function buildnavbar(){

    objects=[];
    r="";
    $.get("scripts/user_data.py", function(result){
        var user_data = JSON.parse(result);
        if (user_data.ok == false) {
            window.location.href = "login.html";
        }
        var data = user_data.data.nickname + "<br>" + user_data.data.email;
        r=data;        
        objects[0]=user_data["data"]["nickname"];
        f();
    });

    function f(){
        ourlocation = location.href.split("/").slice(-1)[0];
        objects[1]="preferences.html";
        objects[2]="שינוי סיסמה";
        objects[3]="change_password.html";
        objects[4] = "דף הבית";
        objects[5] = "home_page.html";
        
        navbar='';
        logo="<a class='navbar-brand'href='home_page.html'><img src='img/logo.png'alt='logo'id='logo' style='width:400px;height: 120px;'></a>";
        exit="<ul class='navbar-nav ml-auto'><li class='nav-item'><a class='nav-link active'href='scripts/logged_out.py'>יציאה</a></li>";
    
        navbar+=logo+exit;
    
        for(i=0; i<objects.length; i+=2){
            if(objects[i+1]==ourlocation){
                continue;
            }
            navbar+="<li class='nav-item'><a class='nav-link'href="+objects[i+1]+">"+objects[i]+"</a></li>";
        }

        face="</ul><div id='profile'><img src='img/face.png'id='face'><div id='user'class='title'>"+r+"</div></div>";

        navbar+=face;
    
        var navigation = document.getElementById("nav");   
        navigation.innerHTML = navbar;
    }
}

function get_connected_users(){
    $.get("scripts/users_get.py", function(result){
        var users = JSON.parse(result);
        
        if (users.ok == false) {
          window.location.href = "login.html";
        }else {
            var faces = "<div class='.container float-right'><ul class='list-group'><li class='list-group-item users' style='text-align: center'>רשימת מחוברים</li>";
            for (x in users.data) {
                sel = users.data[x];
                faces += "<li class='list-group-item users'><div class='float-right'>"+ sel.nickname +"</div><div class='float-left'><img src='img/face.png' style='width: 50px;' class='users_face'></div></li>";
            }
            faces += "</ul></div>"
            $("#now_logged").html(faces);
        }
    });
}
