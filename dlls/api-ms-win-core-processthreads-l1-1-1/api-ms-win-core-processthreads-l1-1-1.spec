@ stdcall CreateProcessA(str str ptr ptr long long ptr str ptr ptr) kernel32.CreateProcessA
@ stdcall CreateProcessAsUserW(long wstr wstr ptr ptr long long ptr wstr ptr ptr) advapi32.CreateProcessAsUserW
@ stdcall CreateProcessW(wstr wstr ptr ptr long long ptr wstr ptr ptr) kernel32.CreateProcessW
@ stdcall CreateRemoteThread(long ptr long ptr long long ptr) kernel32.CreateRemoteThread
@ stub CreateRemoteThreadEx
@ stdcall CreateThread(ptr long ptr long long ptr) kernel32.CreateThread
@ stub DeleteProcThreadAttributeList
@ stdcall ExitProcess(long) kernel32.ExitProcess
@ stdcall ExitThread(long) kernel32.ExitThread
@ stdcall FlushInstructionCache(long long long) kernel32.FlushInstructionCache
@ stdcall FlushProcessWriteBuffers() kernel32.FlushProcessWriteBuffers
@ stdcall -norelay GetCurrentProcess() kernel32.GetCurrentProcess
@ stdcall -norelay GetCurrentProcessId() kernel32.GetCurrentProcessId
@ stdcall GetCurrentProcessorNumber() kernel32.GetCurrentProcessorNumber
@ stdcall GetCurrentProcessorNumberEx(ptr) kernel32.GetCurrentProcessorNumberEx
@ stdcall -norelay GetCurrentThread() kernel32.GetCurrentThread
@ stdcall -norelay GetCurrentThreadId() kernel32.GetCurrentThreadId
@ stub GetCurrentThreadStackLimits
@ stdcall GetExitCodeProcess(long ptr) kernel32.GetExitCodeProcess
@ stdcall GetExitCodeThread(long ptr) kernel32.GetExitCodeThread
@ stdcall GetPriorityClass(long) kernel32.GetPriorityClass
@ stdcall GetProcessHandleCount(long ptr) kernel32.GetProcessHandleCount
@ stdcall GetProcessId(long) kernel32.GetProcessId
@ stdcall GetProcessIdOfThread(long) kernel32.GetProcessIdOfThread
@ stub GetProcessMitigationPolicy
@ stdcall GetProcessTimes(long ptr ptr ptr ptr) kernel32.GetProcessTimes
@ stdcall GetProcessVersion(long) kernel32.GetProcessVersion
@ stdcall GetStartupInfoW(ptr) kernel32.GetStartupInfoW
@ stdcall GetThreadContext(long ptr) kernel32.GetThreadContext
@ stdcall GetThreadId(ptr) kernel32.GetThreadId
@ stub GetThreadIdealProcessorEx
@ stdcall GetThreadPriority(long) kernel32.GetThreadPriority
@ stdcall GetThreadPriorityBoost(long ptr) kernel32.GetThreadPriorityBoost
@ stdcall GetThreadTimes(long ptr ptr ptr ptr) kernel32.GetThreadTimes
@ stub InitializeProcThreadAttributeList
@ stdcall IsProcessorFeaturePresent(long) kernel32.IsProcessorFeaturePresent
@ stdcall OpenProcess(long long long) kernel32.OpenProcess
@ stdcall OpenProcessToken(long long ptr) advapi32.OpenProcessToken
@ stdcall OpenThread(long long long) kernel32.OpenThread
@ stdcall OpenThreadToken(long long long ptr) advapi32.OpenThreadToken
@ stdcall ProcessIdToSessionId(long ptr) kernel32.ProcessIdToSessionId
@ stub QueryProcessAffinityUpdateMode
@ stdcall QueueUserAPC(ptr long long) kernel32.QueueUserAPC
@ stdcall ResumeThread(long) kernel32.ResumeThread
@ stdcall SetPriorityClass(long long) kernel32.SetPriorityClass
@ stub SetProcessAffinityUpdateMode
@ stub SetProcessMitigationPolicy
@ stdcall SetProcessShutdownParameters(long long) kernel32.SetProcessShutdownParameters
@ stdcall SetThreadContext(long ptr) kernel32.SetThreadContext
@ stub SetThreadIdealProcessorEx
@ stdcall SetThreadPriority(long long) kernel32.SetThreadPriority
@ stdcall SetThreadPriorityBoost(long long) kernel32.SetThreadPriorityBoost
@ stdcall SetThreadStackGuarantee(ptr) kernel32.SetThreadStackGuarantee
@ stdcall SetThreadToken(ptr ptr) advapi32.SetThreadToken
@ stdcall SuspendThread(long) kernel32.SuspendThread
@ stdcall SwitchToThread() kernel32.SwitchToThread
@ stdcall TerminateProcess(long long) kernel32.TerminateProcess
@ stdcall TerminateThread(long long) kernel32.TerminateThread
@ stdcall TlsAlloc() kernel32.TlsAlloc
@ stdcall TlsFree(long) kernel32.TlsFree
@ stdcall TlsGetValue(long) kernel32.TlsGetValue
@ stdcall TlsSetValue(long ptr) kernel32.TlsSetValue
@ stub UpdateProcThreadAttribute
