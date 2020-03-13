function check(self=null) {
    if(self!=null) {
        if (self.id !== "confirm") {
            let cls = {
                username: 1,
                password: 2,
            };
            let el = document.getElementById(self.id);
            let id = cls[el.id];
            let small = document.getElementById(id);
            small.hidden = self.value.length >= 6;
            if (el.id === 'password' && document.getElementById('confirm').value !== '') {
                let passwd = document.getElementById("password");
                let confirm = document.getElementById("confirm");
                let small = document.getElementById("3");
                small.hidden = (passwd.value === confirm.value);
            }
        } else {
            let passwd = document.getElementById("password");
            let confirm = document.getElementById("confirm");
            let small = document.getElementById("3");
            small.hidden = (passwd.value === confirm.value);
        }
    }

    let btn = document.getElementById("btn");
    let danger = document.getElementsByClassName("text-danger");
    let verify = document.getElementById("verify").value;

    let flag = true;  // 判断是否有错误

    if (danger){  // 如果查找到danger

        for(let i=0; i<danger.length; i++){
            if (!danger[i].hidden){  // 存在danger是显示的，那么btn不能点击
                flag = false;
            }
        }

        if (flag&&verify){
            btn.removeAttribute("disabled");
        }
        else{
            btn.disabled = "disable";
        }
    }


}
