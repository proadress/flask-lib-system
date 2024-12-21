import { create_flash, post } from "./modfunc.js";

const barcodeInput = document.getElementById("barcodeInput");
const keys = ["_id", "name", "type"]

document.getElementById("submitButton").addEventListener("click", async () => {
  const form = new FormData();
  form.append("random_code", barcodeInput.value);
  const response = await post("/admin/qrpost", form);
  if (response.message == "success") {
    keys.forEach(key => {
      document.getElementById(key + "Card").innerText = response.data[key];
    });
  }
  else create_flash(response.message);
});


