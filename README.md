# Student Online Time Converter | ⏱️ 學生上線時間換算工具

A Streamlit web application that converts student online hours and minutes to seconds for tracking purposes.

這是一個方便的網頁應用程式，用於將學生的上線時間轉換成總秒數，並可匯出為 Excel 檔案。

## Live Demo | 線上示範

🌐 [**Try it online now! | 立即線上試用！**](https://student-online-time-converter.streamlit.app/)

## Project Screenshot | 專案畫面

![Student Online Time Converter Screenshot](screenshots/app_screenshot.png)

## Features | 功能說明
- Convert time format to seconds | 將時間格式轉換為秒數
- Process multiple student data at once | 一次處理多位學生資料
- Export results to Excel file | 匯出結果至 Excel 檔案
- Clean and intuitive user interface | 簡潔明了的使用者介面

## Supported Input Formats | 支援的輸入格式

1. `姓名 小時數 小時 分鐘數 分鐘`，例如：`王小明 2 小時 30 分鐘`
2. `姓名 登入次數 小時數時分鐘數分`，例如：`李小華 36 13時22分`

## How to Use | 如何使用

1. Copy and paste student data into the input box | 將學生資料複製到輸入框中
2. Click the "Convert" button | 點擊「轉換」按鈕
3. View the results table | 查看結果表格
4. Download the generated Excel file | 下載產生的 Excel 檔案

## Technical Implementation | 技術實現

This project is developed using Python and the Streamlit framework, with main features including:
- Regular expression pattern matching | 正則表達式模式匹配
- Data processing and conversion | 資料處理與轉換
- Excel file generation | Excel 檔案生成

## Usage | 使用方法

```bash
# Install dependencies | 安裝相依套件
pip install -r requirements.txt
# or install manually | 或者手動安裝
pip install streamlit pandas openpyxl

# Launch application | 啟動應用程式
streamlit run app.py
```

© 2025 Student Online Time Converter | 版本 1.0