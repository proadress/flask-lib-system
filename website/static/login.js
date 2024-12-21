import { create_flash, post, get } from "./modfunc.js";

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async function (event) {
  event.preventDefault(); // 阻止表单默认提交
  const formData = new FormData(loginForm); // 创建一个表单数据对象
  const response = await post("/login/api", formData);
  console.log(response);
  if (response.message == "success") {
    window.location.href = "/";
  } else {
    create_flash(response.message);
  }
});
