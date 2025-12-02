# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

from .. import Control, NotifyEvent, Object

class WebView(Control):
    """ This control may be used to render web (HTML / CSS / javascript)
documents.

        Source: https://docs.wxpython.org/wx.html2.WebView.html
    """
    def AddScriptMessageHandler(self, name) -> None:
        """ Add a script message handler with the given name.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def AddUserScript(self, javascript, injectionTime=WEBVIEW_INJECT_AT_DOCUMENT_START) -> None:
        """ Injects the specified script into the webpageâs content.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanCopy(self) -> None:
        """ Returns True if the current selection can be copied.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanCut(self) -> None:
        """ Returns True if the current selection can be cut.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanGoBack(self) -> None:
        """ Returns True if it is possible to navigate backward in the history of visited pages.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanGoForward(self) -> None:
        """ Returns True if it is possible to navigate forward in the history of visited pages.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanPaste(self) -> None:
        """ Returns True if data can be pasted.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanRedo(self) -> None:
        """ Returns True if there is an action to redo.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanSetZoomType(self, type) -> None:
        """ Retrieve whether the current HTML engine supports a zoom type.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanUndo(self) -> None:
        """ Returns True if there is an action to undo.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def ClearHistory(self) -> None:
        """ Clear the history, this will also remove the visible page.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def ClearSelection(self) -> None:
        """ Clears the current selection.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Copy(self) -> None:
        """ Copies the current selection.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Create(self, parent, id=ID_ANY, url=WebViewDefaultURLStr, pos=DefaultPosition, size=DefaultSize, style=0, name=WebViewNameStr) -> None:
        """ Creation function for two-step creation.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Cut(self) -> None:
        """ Cuts the current selection.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def DeleteSelection(self) -> None:
        """ Deletes the current selection.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def EnableAccessToDevTools(self, enable=True) -> None:
        """ Enable or disable access to dev tools for the user.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def EnableContextMenu(self, enable=True) -> None:
        """ Enable or disable the right click context menu.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def EnableHistory(self, enable=True) -> None:
        """ Enable or disable the history.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Find(self, text, flags=WEBVIEW_FIND_DEFAULT) -> None:
        """ Finds a phrase on the current page and if found, the control will scroll the phrase into view and select it.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def GetBackendVersionInfo(backend=WebViewBackendDefault) -> None:
        """ Retrieve the version information about the backend implementation.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetBackwardHistory(self) -> None:
        """ Returns a list of items in the back history.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL) -> None:
        """ variant (WindowVariant)

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetCurrentTitle(self) -> None:
        """ Get the title of the current web page, or its URL/path if title is not available.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetCurrentURL(self) -> None:
        """ Get the URL of the currently displayed document.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetForwardHistory(self) -> None:
        """ Returns a list of items in the forward history.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetNativeBackend(self) -> None:
        """ Return the pointer to the native backend used by this control.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetPageSource(self) -> None:
        """ Get the HTML source code of the currently displayed document.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetPageText(self) -> None:
        """ Get the text of the current page.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetSelectedSource(self) -> None:
        """ Returns the currently selected source, if any.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetSelectedText(self) -> None:
        """ Returns the currently selected text, if any.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetUserAgent(self) -> None:
        """ Returns the current user agent string for the web view.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetZoom(self) -> None:
        """ Get the zoom level of the page.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetZoomFactor(self) -> None:
        """ Get the zoom factor of the page.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetZoomType(self) -> None:
        """ Get how the zoom factor is currently interpreted.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GoBack(self) -> None:
        """ Navigate back in the history of visited pages.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GoForward(self) -> None:
        """ Navigate forward in the history of visited pages.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def HasSelection(self) -> None:
        """ Returns True if there is a current selection.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def IsAccessToDevToolsEnabled(self) -> None:
        """ Returns True if dev tools are available to the user.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def IsBackendAvailable(backend) -> None:
        """ Allows to check if a specific backend is currently available.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def IsBusy(self) -> None:
        """ Returns whether the web control is currently busy (e.g. loading a page).

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def IsContextMenuEnabled(self) -> None:
        """ Returns True if a context menu will be shown on right click.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def IsEditable(self) -> None:
        """ Returns whether the web control is currently editable.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def LoadURL(self, url) -> None:
        """ Load a web page from a URL.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def MSWSetEmulationLevel(level=WEBVIEWIE_EMU_IE11) -> None:
        """ Sets emulation level.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def MSWSetModernEmulationLevel(modernLevel=True) -> None:
        """ Please explicitly specify emulation level with MSWSetEmulationLevel .

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def New(*args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Paste(self) -> None:
        """ Pastes the current data.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Print(self) -> None:
        """ Opens a print dialog so that the user may print the currently displayed page.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Redo(self) -> None:
        """ Redos the last action.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def RegisterFactory(backend, factory) -> None:
        """ Allows the registering of new backend for   wx.html2.WebView.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RegisterHandler(self, handler) -> None:
        """ Registers a custom scheme handler.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Reload(self, flags=WEBVIEW_RELOAD_DEFAULT) -> None:
        """ Reload the currently displayed URL.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RemoveAllUserScripts(self) -> None:
        """ Removes all user scripts from the web view.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RemoveScriptMessageHandler(self, name) -> None:
        """ Remove a script message handler with the given name that was previously added via AddScriptMessageHandler .

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RunScript(self, javascript) -> None:
        """ Runs the given JavaScript code.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RunScriptAsync(self, javascript, clientData=None) -> None:
        """ Runs the given JavaScript code asynchronously and returns the result via a  wxEVT_WEBVIEW_SCRIPT_RESULT .

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SelectAll(self) -> None:
        """ Selects the entire page.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetEditable(self, enable=True) -> None:
        """ Set the editable property of the web control.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetPage(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetUserAgent(self, userAgent) -> None:
        """ Specify a custom user agent string for the web view.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetZoom(self, zoom) -> None:
        """ Set the zoom level of the page.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetZoomFactor(self, zoom) -> None:
        """ Set the zoom factor of the page.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetZoomType(self, zoomType) -> None:
        """ Set how to interpret the zoom factor.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Stop(self) -> None:
        """ Stop the current page loading process, if any.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Undo(self) -> None:
        """ Undos the last action.

            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    BackwardHistory: None  # See GetBackwardHistory
    CurrentTitle: None  # See GetCurrentTitle
    CurrentURL: None  # See GetCurrentURL
    ForwardHistory: None  # See GetForwardHistory
    NativeBackend: None  # See GetNativeBackend
    PageSource: None  # See GetPageSource
    PageText: None  # See GetPageText
    SelectedSource: None  # See GetSelectedSource
    SelectedText: None  # See GetSelectedText
    UserAgent: None  # See GetUserAgent and SetUserAgent
    Zoom: None  # See GetZoom and SetZoom
    ZoomFactor: None  # See GetZoomFactor and SetZoomFactor
    ZoomType: None  # See GetZoomType and SetZoomType



EVT_WEBVIEW_NAVIGATING: int  # Process a  wxEVT_WEBVIEW_NAVIGATING   event, generated before trying to get a resource. This event may be vetoed to prevent navigating to this resource. Note that if the displayed HTML document has several frames, one such event will be generated per frame.

EVT_WEBVIEW_NAVIGATED: int  # Process a  wxEVT_WEBVIEW_NAVIGATED   event generated after it was confirmed that a resource would be requested. This event may not be vetoed. Note that if the displayed HTML document has several frames, one such event will be generated per frame.

EVT_WEBVIEW_LOADED: int  # Process a  wxEVT_WEBVIEW_LOADED   event generated when the document is fully loaded and displayed. Note that if the displayed HTML document has several frames, one such event will be generated per frame.

EVT_WEBVIEW_ERROR: int  # Process a  wxEVT_WEBVIEW_ERROR   event generated when a navigation error occurs. The integer associated with this event will be a WebNavigationError item. The string associated with this event may contain a backend-specific more precise error message/code.

EVT_WEBVIEW_NEWWINDOW: int  # Process a  wxEVT_WEBVIEW_NEWWINDOW   event, generated when a new window is created. You must handle this event if you want anything to happen, for example to load the page in a new window or tab.

EVT_WEBVIEW_TITLE_CHANGED: int  # Process a  wxEVT_WEBVIEW_TITLE_CHANGED   event, generated when the page title changes. Use GetString to get the title.

EVT_WEBVIEW_FULLSCREEN_CHANGED: int  # Process a  wxEVT_WEBVIEW_FULLSCREEN_CHANGED   event, generated when the page wants to enter or leave fullscreen. Use GetInt to get the status. Not implemented for the IE backend and is only available in wxWidgets 3.1.5 or later.

EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED: int  # Process a  wxEVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED   event only available in wxWidgets 3.1.5 or later. For usage details see  AddScriptMessageHandler.

wxEVT_WEBVIEW_SCRIPT_RESULT: int  # Process a  wxEVT_WEBVIEW_SCRIPT_RESULT   event only available in wxWidgets 3.1.6 or later. For usage details see  RunScriptAsync.

WEBVIEW_INJECT_AT_DOCUMENT_START: int

class WebViewEvent(NotifyEvent):
    """ A navigation event holds information about events associated with
WebView objects.

        Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def GetMessageHandler(self) -> None:
        """ Get the name of the script handler.

            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def GetNavigationAction(self) -> None:
        """ Get the type of navigation action.

            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def GetTarget(self) -> None:
        """ Get the name of the target frame which the url of this event has been or will be loaded into.

            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def GetURL(self) -> None:
        """ Get the URL being visited.

            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def IsError(self) -> None:
        """ Returns True the script execution failed.

            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    MessageHandler: None  # See GetMessageHandler
    NavigationAction: None  # See GetNavigationAction
    Target: None  # See GetTarget
    URL: None  # See GetURL



class WebViewFactory(Object):
    """ An abstract factory class for creating WebView backends.

        Source: https://docs.wxpython.org/wx.html2.WebViewFactory.html
    """
    def Create(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.html2.WebViewFactory.html
        """

    def GetVersionInfo(self) -> None:
        """ Retrieve the version information about this backend implementation.

            Source: https://docs.wxpython.org/wx.html2.WebViewFactory.html
        """

    def IsAvailable(self) -> None:
        """ Function to check if the backend is available at runtime.

            Source: https://docs.wxpython.org/wx.html2.WebViewFactory.html
        """

    VersionInfo: None  # See GetVersionInfo



class WebViewHandler:
    """ The base class for handling custom schemes in WebView, for example
to allow virtual file system support.

        Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
    """
    def __init__(self, scheme) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    def GetFile(self, uri) -> None:
        """ uri (string)

            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    def GetName(self) -> None:
        """ str

            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    def GetSecurityURL(self) -> None:
        """ str

            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    def SetSecurityURL(self, url) -> None:
        """ Sets a custom security URL.

            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    Name: None  # See GetName
    SecurityURL: None  # See GetSecurityURL and SetSecurityURL



class WebViewFSHandler(WebViewHandler):
    """ A WebView file system handler to support standard FileSystem
protocols of the form  example:page.htm  The handler allows WebView
to use FileSystem in a similar fashion to its use with Html.

        Source: https://docs.wxpython.org/wx.html2.WebViewFSHandler.html
    """
    def __init__(self, scheme) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.html2.WebViewFSHandler.html
        """

    def GetFile(self, uri) -> None:
        """ uri (string)

            Source: https://docs.wxpython.org/wx.html2.WebViewFSHandler.html
        """



class WebViewArchiveHandler(WebViewHandler):
    """ A custom handler for the file scheme which also supports loading from
archives.

        Source: https://docs.wxpython.org/wx.html2.WebViewArchiveHandler.html
    """
    def __init__(self, scheme) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.html2.WebViewArchiveHandler.html
        """

    def GetFile(self, uri) -> None:
        """ uri (string)

            Source: https://docs.wxpython.org/wx.html2.WebViewArchiveHandler.html
        """



WebViewUserScriptInjectionTime: TypeAlias = int  # Enumeration

WEBVIEW_INJECT_AT_DOCUMENT_END: int

WebViewZoomType: TypeAlias = int  # Enumeration

WEBVIEW_ZOOM_TYPE_LAYOUT: int

WEBVIEW_ZOOM_TYPE_TEXT: int

WebViewFindFlags: TypeAlias = int  # Enumeration

WEBVIEW_FIND_WRAP: int

WEBVIEW_FIND_ENTIRE_WORD: int

WEBVIEW_FIND_MATCH_CASE: int

WEBVIEW_FIND_HIGHLIGHT_RESULT: int

WEBVIEW_FIND_BACKWARDS: int

WEBVIEW_FIND_DEFAULT: int

WebViewZoom: TypeAlias = int  # Enumeration

WEBVIEW_ZOOM_TINY: int

WEBVIEW_ZOOM_SMALL: int

WEBVIEW_ZOOM_MEDIUM: int

WEBVIEW_ZOOM_LARGE: int

WEBVIEW_ZOOM_LARGEST: int

WEBVIEWIE_EMU_DEFAULT: int

WEBVIEWIE_EMU_IE7: int

WEBVIEWIE_EMU_IE8: int

WEBVIEWIE_EMU_IE8_FORCE: int

WEBVIEWIE_EMU_IE9: int

WEBVIEWIE_EMU_IE9_FORCE: int

WEBVIEWIE_EMU_IE10: int

WEBVIEWIE_EMU_IE10_FORCE: int

WEBVIEWIE_EMU_IE11: int

WEBVIEWIE_EMU_IE11_FORCE: int

WebViewReloadFlags: TypeAlias = int  # Enumeration

WEBVIEW_RELOAD_DEFAULT: int

WEBVIEW_RELOAD_NO_CACHE: int

WebViewNavigationError: TypeAlias = int  # Enumeration

WEBVIEW_NAV_ERR_CONNECTION: int

WEBVIEW_NAV_ERR_CERTIFICATE: int

WEBVIEW_NAV_ERR_AUTH: int

WEBVIEW_NAV_ERR_SECURITY: int

WEBVIEW_NAV_ERR_NOT_FOUND: int

WEBVIEW_NAV_ERR_REQUEST: int

WEBVIEW_NAV_ERR_USER_CANCELLED: int

WEBVIEW_NAV_ERR_OTHER: int

WebViewNavigationActionFlags: TypeAlias = int  # Enumeration

WEBVIEW_NAV_ACTION_NONE: int

WEBVIEW_NAV_ACTION_USER: int

WEBVIEW_NAV_ACTION_OTHER: int

WebViewIE_EmulationLevel: TypeAlias = int

