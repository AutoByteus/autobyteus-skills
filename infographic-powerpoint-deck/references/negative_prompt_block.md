# Negative prompt block (avoid common generator failures)

Paste this block into every slide prompt to prevent unwanted artifacts.

```text
负面约束（必须避免）：
- 不要出现：水印、logo、品牌标识、二维码、网址、UI界面元素、按钮、应用窗口、字幕条。
- 不要出现：任何未指定的英文单词、字母串、随机字符、无意义的符号。
- 不要出现：照片上的街牌/海报文字、书页上可读文字（全部必须是无字纹理）。
- 不要出现：过度复杂背景导致文字区难读；不要让背景高对比纹理穿过文字面板。
- 不要出现：恐怖血腥元素；不要出现真实人物肖像（尤其是名人脸）。
- 不要出现：不一致的多种画风混杂（例如同时出现卡通+写实摄影+3D）。
```
