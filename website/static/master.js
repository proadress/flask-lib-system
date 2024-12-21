import { create_flash, post, get } from "./modfunc.js";

document.addEventListener("DOMContentLoaded", function () {
    // 获取当前页面的路径
    const currentURL = window.location.pathname;
    const linkElement = document.getElementById(currentURL); // 请替换为实际的元素ID
    if (linkElement) {
        setTimeout(function () {
            linkElement.className = "sidebar-item active";
        }, 0);
    }
});

const response = await get("/getUser");
if (response.message && response.message == "success") {
    document.getElementById("nav-user").innerText = response.data["name"];
    document.getElementById("nav-id").innerText = response.data["_id"];
    document.getElementById("login-show-nav").hidden = true;
    document.getElementById("login-show-side").hidden = true;
    document.getElementById("login-hide-nav").hidden = false;
    document.getElementById("login-hide-side").hidden = false;
    if (response.data["type"] == "admin")
        document.getElementById("admin-hide-side").hidden = false;
}
else {
    document.getElementById("nav-user").innerText = "Login";
    document.getElementById("nav-id").innerText = "require";
}