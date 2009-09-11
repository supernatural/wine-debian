/* OLE DB Initialization
 *
 * Copyright 2009 Huw Davies
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

#include <stdarg.h>

#define COBJMACROS
#define NONAMELESSUNION
#define NONAMELESSSTRUCT

#include "windef.h"
#include "winbase.h"
#include "ole2.h"

#include "initguid.h"
#include "msdaguid.h"

#include "oledb_private.h"

#include "wine/debug.h"

WINE_DEFAULT_DEBUG_CHANNEL(oledb);

BOOL WINAPI DllMain(HINSTANCE hinst, DWORD reason, LPVOID lpv)
{
    switch(reason)
    {
    case DLL_PROCESS_ATTACH:
        DisableThreadLibraryCalls(hinst);
        break;

    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

/******************************************************************************
 * ClassFactory
 */
typedef struct
{
    const IClassFactoryVtbl *lpVtbl;
    HRESULT (*create_object)( IUnknown*, LPVOID* );
} cf;

static HRESULT WINAPI CF_QueryInterface(IClassFactory *iface, REFIID riid, void **obj)
{
    cf *This = (cf *)iface;

    TRACE("(%p, %s, %p)\n", This, debugstr_guid(riid), obj);

    if( IsEqualCLSID( riid, &IID_IUnknown ) ||
        IsEqualCLSID( riid, &IID_IClassFactory ) )
    {
        IClassFactory_AddRef( iface );
        *obj = iface;
        return S_OK;
    }
    return E_NOINTERFACE;
}

static ULONG WINAPI CF_AddRef(IClassFactory *iface)
{
    return 2;
}

static ULONG WINAPI CF_Release(IClassFactory *iface)
{
    return 1;
}

static HRESULT WINAPI CF_CreateInstance(IClassFactory *iface, IUnknown *pOuter, REFIID riid, void **obj)
{
    cf *This = (cf *)iface;
    IUnknown *unk = NULL;
    HRESULT r;

    TRACE("(%p, %p, %s, %p)\n", This, pOuter, debugstr_guid(riid), obj);

    r = This->create_object( pOuter, (void **) &unk );
    if (SUCCEEDED(r))
    {
        r = IUnknown_QueryInterface( unk, riid, obj );
        IUnknown_Release( unk );
    }
    return r;
}

static HRESULT WINAPI CF_LockServer(IClassFactory *iface, BOOL dolock)
{
    FIXME("(%p, %d): stub\n", iface, dolock);
    return S_OK;
}

static const IClassFactoryVtbl CF_Vtbl =
{
    CF_QueryInterface,
    CF_AddRef,
    CF_Release,
    CF_CreateInstance,
    CF_LockServer
};

static cf oledb_convert_cf = { &CF_Vtbl, create_oledb_convert };

/******************************************************************
 * DllGetClassObject
 */
HRESULT WINAPI DllGetClassObject(REFCLSID rclsid, REFIID riid, void **obj)
{
    TRACE("(%s, %s, %p)\n", debugstr_guid(rclsid), debugstr_guid(riid), obj);

    if ( IsEqualCLSID (rclsid, &CLSID_OLEDB_CONVERSIONLIBRARY) )
    {
        *obj = &oledb_convert_cf;
        return S_OK;
    }

    return CLASS_E_CLASSNOTAVAILABLE;
}
