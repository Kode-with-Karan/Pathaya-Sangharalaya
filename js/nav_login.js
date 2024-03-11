try {
    let log_name = document.querySelector(".log_btn>a");
    if(localStorage.getItem("userloginData")){
        log_name.innerHTML = "Profile";
        log_name.href = "profile.html";
    }else{
        log_name.innerHTML = "Login";
        log_name.href = "login.html";
        
    }
} catch (error) {
    console.log(error)
}





function logOut() {
    console.log("Erase");
    localStorage.removeItem("userloginData");
}
