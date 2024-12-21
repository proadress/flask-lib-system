const s = [document.getElementById('switch1'),
document.getElementById('switch2'),
document.getElementById('switch3')];

// 添加事件監聽器
for (const item of s)
    item.addEventListener('change', () => { Switch(item); });

// 通用的開關變化處理函數
function Switch(item) {
    for (const i of s)
        if (!i.checked) {
            return;
        }

    while (true) {
        const n = s[Math.floor(Math.random() * s.length)];
        if (n != item) {
            n.checked = false;
            break;
        }
    }
}