@ stub BCryptAddContextFunction
@ stub BCryptAddContextFunctionProvider
@ stdcall BCryptCloseAlgorithmProvider(ptr long) bcrypt.BCryptCloseAlgorithmProvider
@ stub BCryptConfigureContext
@ stub BCryptConfigureContextFunction
@ stub BCryptCreateContext
@ stdcall BCryptCreateHash(ptr ptr ptr long ptr long long) bcrypt.BCryptCreateHash
@ stub BCryptDecrypt
@ stub BCryptDeleteContext
@ stub BCryptDeriveKey
@ stub BCryptDeriveKeyCapi
@ stub BCryptDeriveKeyPBKDF2
@ stdcall BCryptDestroyHash(ptr) bcrypt.BCryptDestroyHash
@ stub BCryptDestroyKey
@ stub BCryptDestroySecret
@ stub BCryptDuplicateHash
@ stub BCryptDuplicateKey
@ stub BCryptEncrypt
@ stdcall BCryptEnumAlgorithms(long ptr ptr long) bcrypt.BCryptEnumAlgorithms
@ stub BCryptEnumContextFunctionProviders
@ stub BCryptEnumContextFunctions
@ stub BCryptEnumContexts
@ stub BCryptEnumProviders
@ stub BCryptEnumRegisteredProviders
@ stub BCryptExportKey
@ stub BCryptFinalizeKeyPair
@ stdcall BCryptFinishHash(ptr ptr long long) bcrypt.BCryptFinishHash
@ stub BCryptFreeBuffer
@ stdcall BCryptGenRandom(ptr ptr long long) bcrypt.BCryptGenRandom
@ stub BCryptGenerateKeyPair
@ stub BCryptGenerateSymmetricKey
@ stdcall BCryptGetFipsAlgorithmMode(ptr) bcrypt.BCryptGetFipsAlgorithmMode
@ stdcall BCryptGetProperty(ptr wstr ptr long ptr long) bcrypt.BCryptGetProperty
@ stdcall BCryptHash(ptr ptr long ptr long ptr long) bcrypt.BCryptHash
@ stdcall BCryptHashData(ptr ptr long long) bcrypt.BCryptHashData
@ stub BCryptImportKey
@ stub BCryptImportKeyPair
@ stub BCryptKeyDerivation
@ stdcall BCryptOpenAlgorithmProvider(ptr wstr wstr long) bcrypt.BCryptOpenAlgorithmProvider
@ stub BCryptQueryContextConfiguration
@ stub BCryptQueryContextFunctionConfiguration
@ stub BCryptQueryContextFunctionProperty
@ stub BCryptQueryProviderRegistration
@ stub BCryptRegisterConfigChangeNotify
@ stub BCryptRegisterProvider
@ stub BCryptRemoveContextFunction
@ stub BCryptRemoveContextFunctionProvider
@ stub BCryptResolveProviders
@ stub BCryptSecretAgreement
@ stub BCryptSetAuditingInterface
@ stub BCryptSetContextFunctionProperty
@ stub BCryptSetProperty
@ stub BCryptSignHash
@ stub BCryptUnregisterConfigChangeNotify
@ stub BCryptUnregisterProvider
@ stub BCryptVerifySignature
@ stub GetIsolationServerInterface
@ stub GetKeyStorageInterface
@ stub GetSChannelInterface
@ stub NCryptCloseKeyProtector
@ stub NCryptCloseProtectionDescriptor
@ stub NCryptCreateClaim
@ stub NCryptCreatePersistedKey
@ stub NCryptCreateProtectionDescriptor
@ stub NCryptDecrypt
@ stub NCryptDeleteKey
@ stub NCryptDeriveKey
@ stub NCryptDuplicateKeyProtectorHandle
@ stub NCryptEncrypt
@ stub NCryptEnumAlgorithms
@ stub NCryptEnumKeys
@ stub NCryptEnumStorageProviders
@ stub NCryptExportKey
@ stub NCryptFinalizeKey
@ stub NCryptFreeBuffer
@ stub NCryptFreeObject
@ stub NCryptGetProperty
@ stub NCryptGetProtectionDescriptorInfo
@ stub NCryptImportKey
@ stub NCryptIsAlgSupported
@ stub NCryptIsKeyHandle
@ stub NCryptKeyDerivation
@ stub NCryptNotifyChangeKey
@ stub NCryptOpenKey
@ stub NCryptOpenKeyProtector
@ stub NCryptOpenStorageProvider
@ stub NCryptProtectKey
@ stub NCryptProtectSecret
@ stub NCryptQueryProtectionDescriptorName
@ stub NCryptRegisterProtectionDescriptorName
@ stub NCryptSecretAgreement
@ stub NCryptSetAuditingInterface
@ stub NCryptSetProperty
@ stub NCryptSignHash
@ stub NCryptStreamClose
@ stub NCryptStreamOpenToProtect
@ stub NCryptStreamOpenToUnprotect
@ stub NCryptStreamOpenToUnprotectEx
@ stub NCryptStreamUpdate
@ stub NCryptTranslateHandle
@ stub NCryptUnprotectKey
@ stub NCryptUnprotectSecret
@ stub NCryptVerifyClaim
@ stub NCryptVerifySignature
@ stub SslChangeNotify
@ stub SslComputeClientAuthHash
@ stub SslComputeEapKeyBlock
@ stub SslComputeFinishedHash
@ stub SslComputeSessionHash
@ stub SslCreateClientAuthHash
@ stub SslCreateEphemeralKey
@ stub SslCreateHandshakeHash
@ stub SslDecrementProviderReferenceCount
@ stub SslDecryptPacket
@ stub SslEncryptPacket
@ stub SslEnumCipherSuites
@ stub SslEnumEccCurves
@ stub SslEnumProtocolProviders
@ stub SslExportKey
@ stub SslExportKeyingMaterial
@ stub SslFreeBuffer
@ stub SslFreeObject
@ stub SslGenerateMasterKey
@ stub SslGeneratePreMasterKey
@ stub SslGenerateSessionKeys
@ stub SslGetCipherSuitePRFHashAlgorithm
@ stub SslGetKeyProperty
@ stub SslGetProviderProperty
@ stub SslHashHandshake
@ stub SslImportKey
@ stub SslImportMasterKey
@ stub SslIncrementProviderReferenceCount
@ stub SslLookupCipherLengths
@ stub SslLookupCipherSuiteInfo
@ stub SslOpenPrivateKey
@ stub SslOpenProvider
@ stub SslSignHash
@ stub SslVerifySignature
