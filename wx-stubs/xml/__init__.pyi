# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

from .. import Object

class XmlDocument(Object):
    """ This class holds XML data/document as parsed by XML parser in the root
node.

        Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def AppendToProlog(self, node) -> None:
        """ Appends a Process Instruction or Comment node to the document prologue.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def DetachDocumentNode(self) -> None:
        """ Detaches the document node and returns it.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def DetachRoot(self) -> None:
        """ Detaches the root entity node and returns it.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetDoctype(self) -> None:
        """ Returns the DOCTYPE declaration data for the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetDocumentNode(self) -> None:
        """ Returns the document node of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetEOL(self) -> None:
        """ Returns the output line ending string used for documents.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetFileEncoding(self) -> None:
        """ Returns encoding of document (may be empty).

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetFileType(self) -> None:
        """ Returns the output line ending format used for documents.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    @staticmethod
    def GetLibraryVersionInfo() -> None:
        """ Get expat library version information.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetRoot(self) -> None:
        """ Returns the root element node of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetVersion(self) -> None:
        """ Returns the version of document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def IsOk(self) -> None:
        """ Returns True if the document has been loaded successfully.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def Load(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def Save(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetDoctype(self, doctype) -> None:
        """ Sets the data which will appear in the DOCTYPE declaration when the document is saved.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetDocumentNode(self, node) -> None:
        """ Sets the document node of this document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetFileEncoding(self, encoding) -> None:
        """ Sets the encoding of the file which will be used to save the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetFileType(self, fileType) -> None:
        """ Sets the output line ending formats when the document is saved.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetRoot(self, node) -> None:
        """ Sets the root element node of this document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetVersion(self, version) -> None:
        """ Sets the version of the XML file which will be used to save the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    Doctype: None  # See GetDoctype and SetDoctype
    DocumentNode: None  # See GetDocumentNode and SetDocumentNode
    EOL: None  # See GetEOL
    FileEncoding: None  # See GetFileEncoding and SetFileEncoding
    FileType: None  # See GetFileType and SetFileType
    Root: None  # See GetRoot and SetRoot
    Version: None  # See GetVersion and SetVersion



XMLDOC_KEEP_WHITESPACE_NODES: int

class XmlNode:
    """ Represents a node in an XML document.

        Source: https://docs.wxpython.org/wx.xml.XmlNode.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def AddAttribute(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def AddChild(self, child) -> None:
        """ Adds node child  as the last child of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def DeleteAttribute(self, name) -> None:
        """ Removes the first attributes which has the given name  from the list of attributes for this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetAttribute(self, attrName, defaultVal='') -> None:
        """ Returns the value of the attribute named attrName  if it does exist.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetAttributes(self) -> None:
        """ Return a pointer to the first attribute of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetChildren(self) -> None:
        """ Returns the first child of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetContent(self) -> None:
        """ Returns the content of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetDepth(self, grandparent=None) -> None:
        """ Returns the number of nodes which separate this node from  grandparent .

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetLineNumber(self) -> None:
        """ Returns line number of the node in the input XML file or  -1   if it is unknown.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetName(self) -> None:
        """ Returns the name of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNext(self) -> None:
        """ Returns a pointer to the sibling of this node or None if there are no siblings.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNoConversion(self) -> None:
        """ Returns a flag indicating whether encoding conversion is necessary when saving.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNodeContent(self) -> None:
        """ Returns the content of the first child node of type  XML_TEXT_NODE   or   XML_CDATA_SECTION_NODE .

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetParent(self) -> None:
        """ Returns a pointer to the parent of this node or None if this node has no parent.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetType(self) -> None:
        """ Returns the type of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def HasAttribute(self, attrName) -> None:
        """ Returns True if this node has a attribute named attrName.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def InsertChild(self, child, followingNode) -> None:
        """ Inserts the child  node immediately before followingNode  in the children list.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def InsertChildAfter(self, child, precedingNode) -> None:
        """ Inserts the child  node immediately after precedingNode  in the children list.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def IsWhitespaceOnly(self) -> None:
        """ Returns True if the content of this node is a string containing only whitespaces (spaces, tabs, new lines, etc).

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def RemoveChild(self, child) -> None:
        """ Removes the given node from the children list.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetContent(self, con) -> None:
        """ Sets the content of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetName(self, name) -> None:
        """ Sets the name of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetNext(self, next) -> None:
        """ Sets as sibling the given node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetNoConversion(self, noconversion) -> None:
        """ Sets a flag to indicate whether encoding conversion is necessary when saving.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetParent(self, parent) -> None:
        """ Sets as parent the given node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetType(self, type) -> None:
        """ Sets the type of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    Attributes: None  # See GetAttributes
    Children: None  # See GetChildren
    Content: None  # See GetContent and SetContent
    Depth: None  # See GetDepth
    LineNumber: None  # See GetLineNumber
    Name: None  # See GetName and SetName
    Next: None  # See GetNext and SetNext
    NoConversion: None  # See GetNoConversion and SetNoConversion
    NodeContent: None  # See GetNodeContent
    Parent: None  # See GetParent and SetParent
    Type: None  # See GetType and SetType



class XmlAttribute:
    """ Represents a node attribute.

        Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetName(self) -> None:
        """ Returns the name of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetNext(self) -> None:
        """ Returns the sibling of this attribute or None if there are no siblings.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetValue(self) -> None:
        """ Returns the value of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetName(self, name) -> None:
        """ Sets the name of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetNext(self, next) -> None:
        """ Sets the sibling of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetValue(self, value) -> None:
        """ Sets the value of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    Name: None  # See GetName and SetName
    Next: None  # See GetNext and SetNext
    Value: None  # See GetValue and SetValue



class XmlDoctype:
    """ Represents a DOCTYPE Declaration.

        Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
    """
    def __init__(self, rootName='', systemId='', publicId='') -> None:
        """ Creates and possible initializes the DOCTYPE.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def Clear(self) -> None:
        """ Removes all the DOCTYPE values.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetFullString(self) -> None:
        """ Returns the formatted DOCTYPE contents.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetPublicId(self) -> None:
        """ Returns the public id of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetRootName(self) -> None:
        """ Returns the root name of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetSystemId(self) -> None:
        """ Returns the system id of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def IsValid(self) -> None:
        """ Returns True if the contents can produce a valid DOCTYPE string.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    FullString: None  # See GetFullString
    PublicId: None  # See GetPublicId
    RootName: None  # See GetRootName
    SystemId: None  # See GetSystemId



XmlNodeType: TypeAlias = int  # Enumeration

XML_ELEMENT_NODE: int

XML_ATTRIBUTE_NODE: int

XML_TEXT_NODE: int

XML_CDATA_SECTION_NODE: int

XML_ENTITY_REF_NODE: int

XML_ENTITY_NODE: int

XML_PI_NODE: int

XML_COMMENT_NODE: int

XML_DOCUMENT_NODE: int

XML_DOCUMENT_TYPE_NODE: int

XML_DOCUMENT_FRAG_NODE: int

XML_NOTATION_NODE: int

XML_HTML_DOCUMENT_NODE: int

