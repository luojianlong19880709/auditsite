function isEmpty(){
        var pattern = /^([\.a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/; 
        if(cycasForm.user_name.value==""){
                alert("请输入用户名");
                cycasForm.user_name.focus();
                return false;
        }
        
        if(cycasForm.applicant.value==""){
                alert("请输入用户申请人");
                cycasForm.applicant.focus();
                return false;
        }
        
        if(cycasForm.department.value==""){
                alert("请输入所在部门");
                cycasForm.department.focus();
                return false;
        }

/*        if(isNaN(cycasForm.mobile_phone.value)){
                alert("手机号只能为数字");
                cycasForm.mobile_phone.focus();
                return false;

        }
        if(!pattern.test(cycasForm.email.value)){
                alert("请输入正确的邮箱格式");
                cycasForm.mobile_phone.focus();
                return false;
        }
        
*/
        return true;
}
