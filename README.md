# 取得JIRA單

### 配置
1. 先取得Atlassian的API key用來做資料存取
  https://id.atlassian.com/manage-profile/security/api-tokens

2. 依據目錄內的climbIssue.sample.ini設置climbIssue.ini配置

```
[DEFAULT]
server=https://sample.atlassian.net \\ jira的server路徑
user_name=                          \\ jira的使用者信箱
api_key=                            \\ jira的使用者API key
finish_text=Done                    \\ 完成的key word
```

### 開始測試
1. 主要檔案為climbIssue.py

2. 執行
```
py climbIssue.py
```

3. 依序填入專案名稱,專案spring,issue被指派人

```
Please enter project(ZRSH):
Please enter Sprint(openSprints()):
Please enter assignee people(self):
```

4. 完成後便會將jira issue寫入在同目錄底下的output.txt檔案

5. 修改完檔案後,使用`pyinstaller`指令打包成exe檔
```
pyinstaller -F climbIssue.py
```

### exe檔案操作
1. 先拿到.exe檔案後，取得Atlassian的API key用來做資料存取
  https://id.atlassian.com/manage-profile/security/api-tokens

2. 設置目錄內的climbIssue.ini配置

```
[DEFAULT]
server=https://sample.atlassian.net \\ jira的server路徑
user_name=                          \\ jira的使用者信箱
api_key=                            \\ jira的使用者API key
finish_text=Done                    \\ 完成的key word
```

3. 點擊.exe檔案,並依序填入專案名稱,專案spring,issue被指派人

```
Please enter project(ZRSH):           \\ 預設產品研發
Please enter Sprint(openSprints()):   \\ 預設啟動的Sprint
Please enter assignee people(self):   \\ 預設自己
```
