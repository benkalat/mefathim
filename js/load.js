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

check_connect();

function buildnavbar(){
    navbar='';
    objects=["link 2","link 3"];
    logo="<a class='navbar-brand'href='home_page.html'><img src='img/logo.png'alt='logo'id='logo' style='width:400px;height: 120px;'></a>";
    exit="<ul class='navbar-nav ml-auto'><li class='nav-item'><a class='nav-link active'href='scripts/logged_out.py'>יציאה</a></li>";
    face="</ul><div id='profile'><img src='img/face.png'id='face'><div id='user'class='title'></div></div>";
    item="<li class='nav-item'><a class='nav-link'href='preferences.html'>שינוי העדפות</a></li>";

    navbar+=logo+exit;

    for(i=0; i<objects.length; i++){
        navbar+="<li class='nav-item'><a class='nav-link'href='#'>1"+ objects[i]+"</a></li>";
    }

    navbar+=face;

    var navigation = document.getElementById("nav");   
    navigation.innerHTML = navbar;  
}                 


    
