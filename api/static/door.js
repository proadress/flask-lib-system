import { create_flash, post, get } from "./modfunc.js";

const codeWriter = new ZXing.BrowserQRCodeSvgWriter();
const result = document.getElementById("result");

generateQRCode();

result.addEventListener("click", (e) => {
  generateQRCode();
});

async function generateQRCode() {
  const ur = await get("/getDoor");
  result.innerHTML = "";
  codeWriter.writeToDom("#result", ur, 300, 300);
}
