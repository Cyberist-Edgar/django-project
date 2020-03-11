"use strict";
const profile = document.getElementById('profile');
const n = document.getElementsByTagName("nav")[0];


// 对nav bar上面的点击用户头像弹出信息进行处理
if (profile) {  // 说明用户已经登录
    let nav = document.getElementsByClassName("dropdown-menu")[0];


    profile.onclick = function () {
        if (nav.style.display === 'none') {
            nav.style.display = 'block';
            nav.style.marginTop = 12 + "px";
        } else
            nav.style.display = 'none';
    };

    profile.onmouseout = function () {
        document.onclick = function (ev) {
            if (ev.target.className !== 'dropdown-menu' && ev.target.id !== 'profile') {
                nav.style.display = 'none';
            }
        }
    }

}


// 对用户的登出进行处理
if (document.getElementById('loginout')) {
    document.getElementById('loginout').onclick = function () {
        let xmlhttp = new XMLHttpRequest();

        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
                location.reload();
            }
        };
        xmlhttp.open('GET', '/user/loginout', true);
        xmlhttp.send();
    }
}

