var flag = true;
document.getElementById("send").onclick = function () {
    if (flag) {
        flag = true;
        let cal = {
            time: 7,
            counter: 1
        };
        let interval = setInterval(function () {
            send = document.getElementById("send");
            send.innerHTML = cal.time - cal.counter + "s后可以重新发送";
            send.removeAttribute("href");
            cal.counter += 1;
            if (cal.time - cal.counter <= 0) {
                send.innerHTML = "发送";
                send.herf = 'javascript:void(0)';
                clearInterval(interval);
            }
        }, 1000);

        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {

        };
        xhr.open("POST", "/api/email/", true);
        let cookies = document.cookie.split(',');

        let pattern = /csrftoken=(.*)/m;
        let csrf;
        for (let j = 0; j < cookies.length; j++) {
            if (pattern.test(cookies[j])) {
                csrf = pattern.exec(cookies[j])[1];
            }
        }
        xhr.setRequestHeader("X-CSRFToken", csrf);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
        let data = {
            email: document.getElementById("email"),
            subject: "注册邮箱验证"
        };
        xhr.send("email=" + data.email + "&" + "subject=" + data.subject);
        flag = false;
    }


};


function check(self = null) {
    if (self != null) {
        if (self.id !== "confirm") {
            let cls = {
                email: 1,
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

    if (danger) {  // 如果查找到danger

        for (let i = 0; i < danger.length; i++) {
            if (!danger[i].hidden) {  // 存在danger是显示的，那么btn不能点击
                flag = false;
            }
        }

        if (flag && verify) {
            btn.removeAttribute("disabled");
        } else {
            btn.disabled = "disable";
        }
    }
}