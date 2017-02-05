@ stdcall AssociateColorProfileWithDeviceA(ptr ptr ptr)
@ stdcall AssociateColorProfileWithDeviceW(ptr ptr ptr)
@ stdcall CheckBitmapBits(ptr ptr ptr long long long ptr ptr long)
@ stdcall CheckColors(ptr ptr long long ptr)
@ stdcall CloseColorProfile(ptr)
@ stdcall ConvertColorNameToIndex(ptr ptr ptr long)
@ stdcall ConvertIndexToColorName(ptr ptr ptr long)
@ stdcall CreateColorTransformA(ptr ptr ptr long)
@ stdcall CreateColorTransformW(ptr ptr ptr long)
@ stdcall CreateDeviceLinkProfile(ptr long ptr long long ptr long)
@ stdcall CreateMultiProfileTransform(ptr long ptr long long long)
@ stdcall CreateProfileFromLogColorSpaceA(ptr ptr)
@ stdcall CreateProfileFromLogColorSpaceW(ptr ptr)
@ stdcall DeleteColorTransform(ptr)
@ stdcall DisassociateColorProfileFromDeviceA(ptr ptr ptr)
@ stdcall DisassociateColorProfileFromDeviceW(ptr ptr ptr)
@ stdcall EnumColorProfilesA(ptr ptr ptr ptr ptr)
@ stdcall EnumColorProfilesW(ptr ptr ptr ptr ptr)
@ stdcall GenerateCopyFilePaths(wstr wstr ptr long ptr ptr ptr ptr long)
@ stdcall GetCMMInfo(ptr long)
@ stdcall GetColorDirectoryA(ptr ptr ptr)
@ stdcall GetColorDirectoryW(ptr ptr ptr)
@ stdcall GetColorProfileElement(ptr long long ptr ptr ptr)
@ stdcall GetColorProfileElementTag(ptr long ptr)
@ stdcall GetColorProfileFromHandle(ptr ptr ptr)
@ stdcall GetColorProfileHeader(ptr ptr)
@ stdcall GetCountColorProfileElements(ptr ptr)
@ stdcall GetNamedProfileInfo(ptr ptr)
@ stdcall GetPS2ColorRenderingDictionary(ptr long ptr ptr ptr)
@ stdcall GetPS2ColorRenderingIntent(ptr long ptr ptr)
@ stdcall GetPS2ColorSpaceArray(ptr long long ptr ptr ptr)
@ stdcall GetStandardColorSpaceProfileA(ptr long ptr ptr)
@ stdcall GetStandardColorSpaceProfileW(ptr long ptr ptr)
@ stdcall InstallColorProfileA(ptr ptr)
@ stdcall InstallColorProfileW(ptr ptr)
@ stub InternalGetDeviceConfig
@ stub InternalGetPS2CSAFromLCS
@ stub InternalGetPS2ColorRenderingDictionary
@ stub InternalGetPS2ColorSpaceArray
@ stub InternalGetPS2PreviewCRD
@ stub InternalSetDeviceConfig
@ stdcall IsColorProfileTagPresent(ptr long ptr)
@ stdcall IsColorProfileValid(ptr ptr)
@ stdcall OpenColorProfileA(ptr long long long)
@ stdcall OpenColorProfileW(ptr long long long)
@ stdcall RegisterCMMA(ptr long ptr)
@ stdcall RegisterCMMW(ptr long ptr)
@ stdcall SelectCMM(long)
@ stdcall SetColorProfileElement(ptr long long ptr ptr)
@ stdcall SetColorProfileElementReference(ptr long long)
@ stdcall SetColorProfileElementSize(ptr long long)
@ stdcall SetColorProfileHeader(ptr ptr)
@ stdcall SetStandardColorSpaceProfileA(ptr long ptr)
@ stdcall SetStandardColorSpaceProfileW(ptr long ptr)
@ stdcall SpoolerCopyFileEvent(wstr wstr long)
@ stdcall TranslateBitmapBits(ptr ptr long long long long ptr long long ptr long)
@ stdcall TranslateColors(ptr ptr long long ptr long)
@ stdcall UninstallColorProfileA(ptr ptr long)
@ stdcall UninstallColorProfileW(ptr ptr long)
@ stdcall UnregisterCMMA(ptr long)
@ stdcall UnregisterCMMW(ptr long)
