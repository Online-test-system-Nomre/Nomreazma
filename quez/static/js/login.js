function validateFormLogin(){
    var UserName = document.forms["contact"]["user"].value;
    var Password = document.forms["contact"]["pass"].value;
    if (UserName == null || UserName == ""){
        if (Password == null || Password == ""){
            alert("نام کاربری و رمز عبور نباید خالی باشند!");
        }
        else{
            alert("نام کاربری نباید خالی باشد!");
        }
        return false;
      }
    else if (Password == null || Password == ""){
        alert("رمز عبور نباید خالی باشد!");
        return false;
    }
    delete UserName, Password;
}
function validateFormSignUp(){
    var UserName = document.forms["contact"]["user"].value;
    var Email = document.forms["contact"]["email"].value;
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var Password = document.forms["contact"]["pass"].value;
    var Password2 = document.forms["contact"]["pass2"].value;
    if (UserName == null || UserName == ""){
        alert("نام کاربری نباید خالی باشد!");
        return false;
    }
    else if (Email == null || Email == "" || reg.test(Email) == false){
        alert("ایمیل نباید خالی باشد!");
        return false;
    }
    else if (Password == null || Password == ""){
        alert("رمز عبور نباید خالی باشد!");
        return false;
    }
    else if (Password2 == null || Password2 == ""){
        alert("تکرار رمز عبور نباید خالی باشد!");
        return false;
    }
    else if (Password != Password2){
        alert("رمز عبور ها با هم یکسان نیستند! لطفا درست وارد نمایید!")
        return false;
    }
}
function validateFormForgetPassword(){
    var Email = document.forms["recovery"]["email"].value;
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if (Email == null || Email == "" || reg.test(Email) == false){
        alert("لطفا ایمیل خود را به درستی وارد نمایید!")
        return false;
    }
}