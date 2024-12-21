import { create_flash, post, get } from "./modfunc.js";
const codeReader = new ZXing.BrowserMultiFormatReader();
const sourceSelectPanel = document.getElementById("sourceSelectPanel");
const vedioPanel = document.getElementById("demo-content");
const sourceSelect = document.getElementById("sourceSelect");
const barcodeInput = document.getElementById("barcodeInput");
const stopButton = document.getElementById("stopButton");
const scaneButton = document.getElementById("scaneButton");
const submitButton = document.getElementById("submitButton");

scaneButton.addEventListener("click", () => {
    stopButton.hidden = false;
    scaneButton.hidden = true;
    vedioPanel.hidden = false;
    decodeContinuously(sourceSelect.value);
});
stopButton.addEventListener("click", () => {
    stopButton.hidden = true;
    scaneButton.hidden = false;
    vedioPanel.hidden = true;
    codeReader.reset();
});

function decodeContinuously(selectedDeviceId) {
    let temp_result = "";
    let temp_err = "";
    codeReader.decodeFromInputVideoDeviceContinuously(
        selectedDeviceId,
        "video",
        async (result, err) => {
            if (result && result.text != temp_result) {
                temp_result = result.text;
                if (temp_result.length == 7 || temp_result.length == 59 || temp_result.length == 61) {
                    barcodeInput.value = temp_result;
                    vedioPanel.hidden = true;
                    stopButton.click();
                    submitButton.click();
                } else {
                    temp_result = "not barcode " + temp_result;
                    create_flash(temp_result);
                }
            } else if (err) {
                let errMsg = "";
                if (err instanceof ZXing.ChecksumException)
                    errMsg = "A code was found, but it's read value was not valid.";
                else if (err instanceof ZXing.FormatException)
                    errMsg = "A code was found, but it was in a invalid format.";
                if (errMsg != temp_err) {
                    temp_err = errMsg;
                    create_flash(errMsg);
                }
            }
        }
    );
}

codeReader.getVideoInputDevices().then((videoInputDevices) => {
    if (videoInputDevices.length > 1) {
        videoInputDevices.forEach((element) => {
            const sourceOption = document.createElement("option");
            sourceOption.text = element.label;
            sourceOption.value = element.deviceId;
            sourceSelect.appendChild(sourceOption);
        });
        sourceSelect.addEventListener("change", function () {
            // 獲取所選選項的值
            decodeContinuously(sourceSelect.value);
        });
    } else {
        sourceSelectPanel.hidden = true;
    }
}).catch((err) => {
    console.error(err);
});
