$(document).ready(function(){
    $('#eye').click(function(){
        $(this).toggleClass('open');
        $(this).children('i').toggleClass('fa-eye-slash fa-eye');
        if($(this).hasClass('open')){
            $(this).prev().attr('type', 'text');
        }else{
            $(this).prev().attr('type', 'password');
        }
    });

    $('#eye_confirm').click(function(){
        $(this).toggleClass('open');
        $(this).children('i').toggleClass('fa-eye-slash fa-eye');
        if($(this).hasClass('open')){
            $(this).prev().attr('type', 'text');
        }else{
            $(this).prev().attr('type', 'password');
        }
    });

    function Register(){
        let Email_Address = document.getElementById('Email_Address').value;
        let User_Name = document.getElementById('User_Name').value;
        let Password = document.getElementById('Password').value;
        let Confirm_Password = document.getElementById('Confirm_Password').value;
        if(User_Name == "")
        {
            Swal.fire({
                icon: 'error',
                title: 'Lỗi',
                text: 'Vui lòng nhập First Name',
              })
        }
    }
});