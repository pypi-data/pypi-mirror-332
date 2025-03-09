"""
Python module generated from Java source file java.security.AccessController

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.ref import Reference
from java.security import *
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import Reflection
from jdk.internal.vm.annotation import DontInline
from jdk.internal.vm.annotation import ForceInline
from jdk.internal.vm.annotation import Hidden
from jdk.internal.vm.annotation import ReservedStackAccess
from sun.security.util import Debug
from sun.security.util import SecurityConstants
from typing import Any, Callable, Iterable, Tuple


class AccessController:

    @staticmethod
    def doPrivileged(action: "PrivilegedAction"["T"]) -> "T":
        ...


    @staticmethod
    def doPrivilegedWithCombiner(action: "PrivilegedAction"["T"]) -> "T":
        """
        Performs the specified `PrivilegedAction` with privileges
        enabled. The action is performed with *all* of the permissions
        possessed by the caller's protection domain.
        
         If the action's `run` method throws an (unchecked)
        exception, it will propagate through this method.
        
         This method preserves the current AccessControlContext's
        DomainCombiner (which may be null) while the action is performed.
        
        Type `<T>`: the type of the value returned by the PrivilegedAction's
                         `run` method.

        Arguments
        - action: the action to be performed.

        Returns
        - the value returned by the action's `run` method.

        Raises
        - NullPointerException: if the action is `null`

        See
        - java.security.DomainCombiner

        Since
        - 1.6
        """
        ...


    @staticmethod
    def doPrivileged(action: "PrivilegedAction"["T"], context: "AccessControlContext") -> "T":
        """
        Performs the specified `PrivilegedAction` with privileges
        enabled and restricted by the specified `AccessControlContext`.
        The action is performed with the intersection of the permissions
        possessed by the caller's protection domain, and those possessed
        by the domains represented by the specified `AccessControlContext`.
        
        If the action's `run` method throws an (unchecked) exception,
        it will propagate through this method.
        
        If a security manager is installed and the specified
        `AccessControlContext` was not created by system code and the
        caller's `ProtectionDomain` has not been granted the
        "createAccessControlContext"
        java.security.SecurityPermission, then the action is performed
        with no permissions.
        
        Type `<T>`: the type of the value returned by the PrivilegedAction's
                         `run` method.

        Arguments
        - action: the action to be performed.
        - context: an *access control context*
                       representing the restriction to be applied to the
                       caller's domain's privileges before performing
                       the specified action.  If the context is
                       `null`, then no additional restriction is applied.

        Returns
        - the value returned by the action's `run` method.

        Raises
        - NullPointerException: if the action is `null`

        See
        - .doPrivileged(PrivilegedExceptionAction,AccessControlContext)
        """
        ...


    @staticmethod
    def doPrivileged(action: "PrivilegedAction"["T"], context: "AccessControlContext", *perms: Tuple["Permission", ...]) -> "T":
        """
        Performs the specified `PrivilegedAction` with privileges
        enabled and restricted by the specified
        `AccessControlContext` and with a privilege scope limited
        by specified `Permission` arguments.
        
        The action is performed with the intersection of the permissions
        possessed by the caller's protection domain, and those possessed
        by the domains represented by the specified
        `AccessControlContext`.
        
        If the action's `run` method throws an (unchecked) exception,
        it will propagate through this method.
        
        If a security manager is installed and the specified
        `AccessControlContext` was not created by system code and the
        caller's `ProtectionDomain` has not been granted the
        "createAccessControlContext"
        java.security.SecurityPermission, then the action is performed
        with no permissions.
        
        Type `<T>`: the type of the value returned by the PrivilegedAction's
                         `run` method.

        Arguments
        - action: the action to be performed.
        - context: an *access control context*
                       representing the restriction to be applied to the
                       caller's domain's privileges before performing
                       the specified action.  If the context is
                       `null`,
                       then no additional restriction is applied.
        - perms: the `Permission` arguments which limit the
                     scope of the caller's privileges. The number of arguments
                     is variable.

        Returns
        - the value returned by the action's `run` method.

        Raises
        - NullPointerException: if action or perms or any element of
                perms is `null`

        See
        - .doPrivileged(PrivilegedExceptionAction,AccessControlContext)

        Since
        - 1.8
        """
        ...


    @staticmethod
    def doPrivilegedWithCombiner(action: "PrivilegedAction"["T"], context: "AccessControlContext", *perms: Tuple["Permission", ...]) -> "T":
        """
        Performs the specified `PrivilegedAction` with privileges
        enabled and restricted by the specified
        `AccessControlContext` and with a privilege scope limited
        by specified `Permission` arguments.
        
        The action is performed with the intersection of the permissions
        possessed by the caller's protection domain, and those possessed
        by the domains represented by the specified
        `AccessControlContext`.
        
        If the action's `run` method throws an (unchecked) exception,
        it will propagate through this method.
        
         This method preserves the current AccessControlContext's
        DomainCombiner (which may be null) while the action is performed.
        
        If a security manager is installed and the specified
        `AccessControlContext` was not created by system code and the
        caller's `ProtectionDomain` has not been granted the
        "createAccessControlContext"
        java.security.SecurityPermission, then the action is performed
        with no permissions.
        
        Type `<T>`: the type of the value returned by the PrivilegedAction's
                         `run` method.

        Arguments
        - action: the action to be performed.
        - context: an *access control context*
                       representing the restriction to be applied to the
                       caller's domain's privileges before performing
                       the specified action.  If the context is
                       `null`,
                       then no additional restriction is applied.
        - perms: the `Permission` arguments which limit the
                     scope of the caller's privileges. The number of arguments
                     is variable.

        Returns
        - the value returned by the action's `run` method.

        Raises
        - NullPointerException: if action or perms or any element of
                perms is `null`

        See
        - java.security.DomainCombiner

        Since
        - 1.8
        """
        ...


    @staticmethod
    def doPrivileged(action: "PrivilegedExceptionAction"["T"]) -> "T":
        """
        Performs the specified `PrivilegedExceptionAction` with
        privileges enabled.  The action is performed with *all* of the
        permissions possessed by the caller's protection domain.
        
         If the action's `run` method throws an *unchecked*
        exception, it will propagate through this method.
        
         Note that any DomainCombiner associated with the current
        AccessControlContext will be ignored while the action is performed.
        
        Type `<T>`: the type of the value returned by the
                         PrivilegedExceptionAction's `run` method.

        Arguments
        - action: the action to be performed

        Returns
        - the value returned by the action's `run` method

        Raises
        - PrivilegedActionException: if the specified action's
                `run` method threw a *checked* exception
        - NullPointerException: if the action is `null`

        See
        - java.security.DomainCombiner
        """
        ...


    @staticmethod
    def doPrivilegedWithCombiner(action: "PrivilegedExceptionAction"["T"]) -> "T":
        """
        Performs the specified `PrivilegedExceptionAction` with
        privileges enabled.  The action is performed with *all* of the
        permissions possessed by the caller's protection domain.
        
         If the action's `run` method throws an *unchecked*
        exception, it will propagate through this method.
        
         This method preserves the current AccessControlContext's
        DomainCombiner (which may be null) while the action is performed.
        
        Type `<T>`: the type of the value returned by the
                         PrivilegedExceptionAction's `run` method.

        Arguments
        - action: the action to be performed.

        Returns
        - the value returned by the action's `run` method

        Raises
        - PrivilegedActionException: if the specified action's
                `run` method threw a *checked* exception
        - NullPointerException: if the action is `null`

        See
        - java.security.DomainCombiner

        Since
        - 1.6
        """
        ...


    @staticmethod
    def doPrivileged(action: "PrivilegedExceptionAction"["T"], context: "AccessControlContext") -> "T":
        """
        Performs the specified `PrivilegedExceptionAction` with
        privileges enabled and restricted by the specified
        `AccessControlContext`.  The action is performed with the
        intersection of the permissions possessed by the caller's
        protection domain, and those possessed by the domains represented by the
        specified `AccessControlContext`.
        
        If the action's `run` method throws an *unchecked*
        exception, it will propagate through this method.
        
        If a security manager is installed and the specified
        `AccessControlContext` was not created by system code and the
        caller's `ProtectionDomain` has not been granted the
        "createAccessControlContext"
        java.security.SecurityPermission, then the action is performed
        with no permissions.
        
        Type `<T>`: the type of the value returned by the
                         PrivilegedExceptionAction's `run` method.

        Arguments
        - action: the action to be performed
        - context: an *access control context*
                       representing the restriction to be applied to the
                       caller's domain's privileges before performing
                       the specified action.  If the context is
                       `null`, then no additional restriction is applied.

        Returns
        - the value returned by the action's `run` method

        Raises
        - PrivilegedActionException: if the specified action's
                `run` method threw a *checked* exception
        - NullPointerException: if the action is `null`

        See
        - .doPrivileged(PrivilegedAction,AccessControlContext)
        """
        ...


    @staticmethod
    def doPrivileged(action: "PrivilegedExceptionAction"["T"], context: "AccessControlContext", *perms: Tuple["Permission", ...]) -> "T":
        """
        Performs the specified `PrivilegedExceptionAction` with
        privileges enabled and restricted by the specified
        `AccessControlContext` and with a privilege scope limited by
        specified `Permission` arguments.
        
        The action is performed with the intersection of the permissions
        possessed by the caller's protection domain, and those possessed
        by the domains represented by the specified
        `AccessControlContext`.
        
        If the action's `run` method throws an (unchecked) exception,
        it will propagate through this method.
        
        If a security manager is installed and the specified
        `AccessControlContext` was not created by system code and the
        caller's `ProtectionDomain` has not been granted the
        "createAccessControlContext"
        java.security.SecurityPermission, then the action is performed
        with no permissions.
        
        Type `<T>`: the type of the value returned by the
                         PrivilegedExceptionAction's `run` method.

        Arguments
        - action: the action to be performed.
        - context: an *access control context*
                       representing the restriction to be applied to the
                       caller's domain's privileges before performing
                       the specified action.  If the context is
                       `null`,
                       then no additional restriction is applied.
        - perms: the `Permission` arguments which limit the
                     scope of the caller's privileges. The number of arguments
                     is variable.

        Returns
        - the value returned by the action's `run` method.

        Raises
        - PrivilegedActionException: if the specified action's
                `run` method threw a *checked* exception
        - NullPointerException: if action or perms or any element of
                perms is `null`

        See
        - .doPrivileged(PrivilegedAction,AccessControlContext)

        Since
        - 1.8
        """
        ...


    @staticmethod
    def doPrivilegedWithCombiner(action: "PrivilegedExceptionAction"["T"], context: "AccessControlContext", *perms: Tuple["Permission", ...]) -> "T":
        """
        Performs the specified `PrivilegedExceptionAction` with
        privileges enabled and restricted by the specified
        `AccessControlContext` and with a privilege scope limited by
        specified `Permission` arguments.
        
        The action is performed with the intersection of the permissions
        possessed by the caller's protection domain, and those possessed
        by the domains represented by the specified
        `AccessControlContext`.
        
        If the action's `run` method throws an (unchecked) exception,
        it will propagate through this method.
        
         This method preserves the current AccessControlContext's
        DomainCombiner (which may be null) while the action is performed.
        
        If a security manager is installed and the specified
        `AccessControlContext` was not created by system code and the
        caller's `ProtectionDomain` has not been granted the
        "createAccessControlContext"
        java.security.SecurityPermission, then the action is performed
        with no permissions.
        
        Type `<T>`: the type of the value returned by the
                         PrivilegedExceptionAction's `run` method.

        Arguments
        - action: the action to be performed.
        - context: an *access control context*
                       representing the restriction to be applied to the
                       caller's domain's privileges before performing
                       the specified action.  If the context is
                       `null`,
                       then no additional restriction is applied.
        - perms: the `Permission` arguments which limit the
                     scope of the caller's privileges. The number of arguments
                     is variable.

        Returns
        - the value returned by the action's `run` method.

        Raises
        - PrivilegedActionException: if the specified action's
                `run` method threw a *checked* exception
        - NullPointerException: if action or perms or any element of
                perms is `null`

        See
        - java.security.DomainCombiner

        Since
        - 1.8
        """
        ...


    @staticmethod
    def getContext() -> "AccessControlContext":
        ...


    @staticmethod
    def checkPermission(perm: "Permission") -> None:
        ...
