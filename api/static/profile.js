import { create_flash, post, get } from "./modfunc.js";

const response = await get("/getUser");
console.log(response);
if (response.message == "success") {
    for (const key in response.data) {
        document.getElementById(key + "Card").innerText = response.data[key];
    }
}

