import re
import pandas as pd
import streamlit as st
import openpyxl
from io import BytesIO

# 設置頁面配置
st.set_page_config(
    page_title="學生上線時間換算工具",
    page_icon="⏱️",
    layout="centered"
)

# 頁面標題與介紹
st.title("學生上線時間換算工具 ⏱️")

# 使用說明區塊
with st.expander("📖 使用說明 (點擊展開)", expanded=True):
    st.markdown("""
    ### 如何使用本工具
    1. 在下方文字框中輸入學生姓名和上線時間
    2. 每位學生的資料可以放在同一行，或分行輸入
    3. 點擊「轉換」按鈕處理資料
    4. 查看結果並下載 Excel 檔案
    
    ### 支援的輸入格式
    
    **格式 1：**
    ```
    王小明 2 小時 30 分鐘
    李小華 1 小時 45 分鐘
    張三 3 小時 15 分鐘
    ```
    
    **格式 2：**
    ```
    王小明	36	3時2分
    李小華	34	2時38分
    """)

# 輸入區域
st.subheader("輸入學生資料")
data = st.text_area(
    "請輸入學生姓名和上線時間：",
    height=150,
    placeholder="例如：\n王小明 2 小時 30 分鐘\n李小華	34	2時38分"
)

# 處理按鈕
if st.button("轉換", type="primary", use_container_width=True):
    if not data.strip():
        st.error("❌ 請輸入資料！")
    else:
        # 使用正則表達式提取學生姓名和上線時間 (兩種格式)
        student_pattern1 = r'(\S+)\s+(\d+)\s*小時\s+(\d+)\s*分鐘'
        student_pattern2 = r'(\S+)\s+\d+\s+(\d+)時(\d+)分'
        
        matches1 = re.findall(student_pattern1, data)
        matches2 = re.findall(student_pattern2, data)
        
        students = []
        
        # 處理格式1的資料
        for match in matches1:
            name = match[0]
            hours = int(match[1])
            minutes = int(match[2])
            total_seconds = hours * 3600 + minutes * 60
            students.append({
                "姓名": name,
                "小時": hours,
                "分鐘": minutes,
                "總秒數": total_seconds
            })
        
        # 處理格式2的資料
        for match in matches2:
            name = match[0]
            hours = int(match[1])
            minutes = int(match[2])
            total_seconds = hours * 3600 + minutes * 60
            students.append({
                "姓名": name,
                "小時": hours,
                "分鐘": minutes,
                "總秒數": total_seconds
            })
        
        if not students:
            st.error("❌ 未找到符合格式的資料！請確認格式是否正確。")
        else:
            # 建立 DataFrame 顯示結果
            df = pd.DataFrame(students)
            
            # 成功訊息
            st.success(f"✅ 已成功處理 {len(students)} 位學生的資料！")
            
            # 顯示處理結果的表格
            st.subheader("處理結果")
            st.dataframe(df, use_container_width=True)
            
            # 準備 Excel 檔案下載
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "上線時間"
            
            # 寫入表頭
            ws.append(["姓名", "小時", "分鐘", "上線時間 (秒)"])
            
            # 寫入資料
            for student in students:
                ws.append([
                    student["姓名"], 
                    student["小時"], 
                    student["分鐘"], 
                    student["總秒數"]
                ])
            
            # 儲存為 BytesIO 以供下載
            output = BytesIO()
            wb.save(output)
            output.seek(0)
            
            # 下載按鈕
            st.download_button(
                label="📥 下載 Excel 檔案",
                data=output,
                file_name="上線時間.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

# 頁尾
st.markdown("---")
st.caption("© 2025 學生上線時間換算工具 | 版本 1.0")