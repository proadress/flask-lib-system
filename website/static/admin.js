import { create_flash, post, get } from "./modfunc.js";

const userForm = document.getElementById("userForm");
const uForm = document.getElementById("uForm");
const card = document.getElementById("card");
const switchButton = document.getElementById("switchButton");
const arr = ["_id", "name", "type"]


switchButton.addEventListener('click', () => {
  if (!userForm.hidden) {
    userForm.hidden = true;
    uForm.hidden = false;
    card.hidden = false;
  }
  else {
    userForm.hidden = false;
    uForm.hidden = true;
    card.hidden = true;
  }
})

userForm.addEventListener("submit", async (event) => {
  event.preventDefault(); // 阻止表单默认提交
  const formData = new FormData(userForm); // 创建一个表单数据对象
  formData.append("type", document.getElementById("basicSelect").value)
  const response = await post("/admin/signup", formData);
  if (response.message == "success") {
    console.log(response.message)
    switchButton.click();
    document.getElementById("checkSid").value = userForm["sid"].value;
    document.getElementById("checkSubmit").click();
  } else {
    create_flash(response.message);
  }
});


uForm.addEventListener("submit", async (event) => {
  event.preventDefault(); // 阻止表单默认提交
  const formData = new FormData(uForm); // 创建一个表单数据对象
  const response = await post('/admin/check', formData);
  arr.forEach(element => {
    document.getElementById(element + "Card").innerText = response.message == "success" ? response.data[element] : "...";
  })
});

document.getElementById("deleteButton").addEventListener("click", async () => {
  const formData = new FormData(uForm); // 创建一个表单数据对象
  const response = await post('/admin/delete', formData);
  if (response.message == "success") {
    arr.forEach(element => {
      document.getElementById(element + "Card").innerText = "...";
    });
    create_flash("delete " + response.message);
  }
  else {
    create_flash(response.message);
  }
})