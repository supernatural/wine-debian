2 stdcall SQLInstallDriver(str str str long ptr)
3 stdcall SQLInstallDriverManager(ptr long ptr)
4 stdcall SQLGetInstalledDrivers(str long ptr)
5 stdcall SQLGetAvailableDrivers(str ptr long ptr)
6 stdcall SQLConfigDataSource(ptr long str str)
7 stdcall SQLRemoveDefaultDataSource()
8 stdcall SQLWriteDSNToIni(str str)
9 stdcall SQLRemoveDSNFromIni(str)
10 stdcall SQLInstallODBC(ptr str str str)
11 stdcall SQLManageDataSources(ptr)
12 stdcall SQLCreateDataSource(ptr str)
13 stdcall SQLGetTranslator(ptr str long ptr ptr long ptr ptr)
14 stdcall SQLWritePrivateProfileString(str str str str)
15 stdcall SQLGetPrivateProfileString(str str str str long str)
16 stdcall SQLValidDSN(str)
17 stdcall SQLRemoveDriverManager(ptr)
18 stdcall SQLInstallTranslator(str str str ptr long ptr long ptr)
19 stdcall SQLRemoveTranslator(str ptr)
20 stdcall SQLRemoveDriver(str long ptr)
21 stdcall SQLConfigDriver(ptr long str str ptr long ptr)
22 stdcall SQLInstallerError(long ptr ptr long ptr)
23 stdcall SQLPostInstallerError(long ptr)
24 stdcall SQLReadFileDSN(str str str ptr long ptr)
25 stdcall SQLWriteFileDSN(str str str str)
26 stdcall SQLInstallDriverEx(str str str long ptr long ptr)
27 stdcall SQLGetConfigMode(ptr)
28 stdcall SQLSetConfigMode(long)
29 stdcall SQLInstallTranslatorEx(str str ptr long ptr long ptr)
30 stub SQLCreateDataSourceEx
101 stdcall ODBCCPlApplet( long long ptr ptr)
112 stub SelectTransDlg
202 stdcall SQLInstallDriverW(wstr wstr wstr long ptr)
203 stdcall SQLInstallDriverManagerW(ptr long ptr)
204 stdcall SQLGetInstalledDriversW(wstr long ptr)
205 stdcall SQLGetAvailableDriversW(wstr ptr long ptr)
206 stdcall SQLConfigDataSourceW(ptr long wstr wstr)
208 stdcall SQLWriteDSNToIniW(wstr wstr)
209 stdcall SQLRemoveDSNFromIniW(wstr)
210 stdcall SQLInstallODBCW(ptr wstr wstr wstr)
212 stdcall SQLCreateDataSourceW(ptr wstr)
213 stdcall SQLGetTranslatorW(ptr wstr long ptr ptr long ptr ptr)
214 stdcall SQLWritePrivateProfileStringW(wstr wstr wstr wstr)
215 stdcall SQLGetPrivateProfileStringW(wstr wstr wstr wstr long wstr)
216 stdcall SQLValidDSNW(wstr)
218 stdcall SQLInstallTranslatorW(wstr wstr wstr ptr long ptr long ptr)
219 stdcall SQLRemoveTranslatorW(wstr ptr)
220 stdcall SQLRemoveDriverW(wstr long ptr)
221 stdcall SQLConfigDriverW(ptr long wstr wstr ptr long ptr)
222 stdcall SQLInstallerErrorW(long ptr ptr long ptr)
223 stdcall SQLPostInstallerErrorW(long ptr)
224 stdcall SQLReadFileDSNW(wstr wstr wstr ptr long ptr)
225 stdcall SQLWriteFileDSNW(wstr wstr wstr wstr)
226 stdcall SQLInstallDriverExW(wstr wstr wstr long ptr long ptr)
229 stdcall SQLInstallTranslatorExW(wstr wstr ptr long ptr long ptr)
230 stub SQLCreateDataSourceExW
231 stub SQLLoadDriverListBox
232 stub SQLLoadDataSourcesListBox
