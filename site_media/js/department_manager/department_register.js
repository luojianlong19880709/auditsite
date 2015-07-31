function isEmpty(){
        var pattern = /^([\.a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/; 
        if(cycasForm.department.value==""){
                alert("请输入部门名称");
                cycasForm.department.focus();
                return false;
        }
        
        if(cycasForm.leader.value==""){
                alert("请输入部门负责人");
                cycasForm.leader.focus();
                return false;
        }
        
/*
        if(isNaN(cycasForm.leader_mobile.value)){
                alert("手机号只能为数字");
                cycasForm.leader_mobile.focus();
                return false;
        }
        if(!pattern.test(cycasForm.leader_email.value)){
                alert("请输入正确的邮箱格式");
                cycasForm.leader_mail.focus();
                return false;
        }
	if(!pattern.test(cycasForm.depart_mail.value)){
                alert("请输入正确的邮箱格式");
                cycasForm.depart_mail.focus();
                return false;
        }
	
*/      

        return true;
}
