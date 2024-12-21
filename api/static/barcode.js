import { create_flash, post, get } from "./modfunc.js";

const barcodeInput = document.getElementById("barcodeInput");

document.getElementById("submitButton").addEventListener("click", async () => {
  const form = new FormData();
  form.append("barcode", barcodeInput.value);
  const response = await post("/checkBook", form);
  if (response.message == "success") {
    for (const key in response.data) {
      document.getElementById(key + "Card").innerText = response.data[key];
    }
  }
  else create_flash(response.message);
});

