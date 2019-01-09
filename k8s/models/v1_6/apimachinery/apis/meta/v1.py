#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import absolute_import

import datetime

import six

from k8s.base import Model
from k8s.fields import Field, ListField, ReadOnlyField, RequiredField
from k8s.models.v1_6.apimachinery.runtime import RawExtension


###############################################################################
# This file is auto-generated! Do not edit!
#
# Codestyle checking is disabled for this file
# flake8: noqa
###############################################################################


class WatchEvent(Model):
    """
    Event represents a single event to a watched resource.
    """

    object = RequiredField(RawExtension)
    type = RequiredField(six.text_type)


class StatusCause(Model):
    """
    StatusCause provides more information about an api.Status failure, including
    cases when multiple errors are encountered.
    """

    field = Field(six.text_type)
    message = Field(six.text_type)
    reason = Field(six.text_type)


class StatusDetails(Model):
    """
    StatusDetails is a set of additional properties that MAY be set by the server
    to provide additional information about a response. The Reason field of a
    Status object defines what attributes will be set. Clients must ignore fields
    that do not match the defined type of each attribute, and should assume that
    any attribute may be empty, invalid, or under defined.
    """

    causes = ListField(StatusCause)
    group = Field(six.text_type)
    name = Field(six.text_type)
    retryAfterSeconds = Field(int)


class ServerAddressByClientCIDR(Model):
    """
    ServerAddressByClientCIDR helps the client to determine the server address that
    they should use, depending on the clientCIDR that they match.
    """

    clientCIDR = RequiredField(six.text_type)
    serverAddress = RequiredField(six.text_type)


class APIVersions(Model):
    """
    APIVersions lists the versions that are available, to allow clients to discover
    the API at /api, which is the root path of the legacy v1 API.
    """

    serverAddressByClientCIDRs = ListField(ServerAddressByClientCIDR)
    versions = ListField(six.text_type)


class Preconditions(Model):
    """
    Preconditions must be fulfilled before an operation (update, delete, etc.) is
    carried out.
    """

    uid = Field(six.text_type)


class DeleteOptions(Model):
    """
    DeleteOptions may be provided when deleting an API object.
    """

    gracePeriodSeconds = Field(int)
    orphanDependents = Field(bool)
    preconditions = Field(Preconditions)
    propagationPolicy = Field(six.text_type)


class OwnerReference(Model):
    """
    OwnerReference contains enough information to let you identify an owning
    object. Currently, an owning object must be in the same namespace, so there is
    no namespace field.
    """

    blockOwnerDeletion = Field(bool)
    controller = Field(bool)
    name = RequiredField(six.text_type)
    uid = RequiredField(six.text_type)


class ObjectMeta(Model):
    """
    ObjectMeta is metadata that all persisted resources must have, which includes
    all objects users must create.
    """

    annotations = Field(dict)
    clusterName = Field(six.text_type)
    creationTimestamp = ReadOnlyField(datetime.datetime)
    deletionGracePeriodSeconds = ReadOnlyField(int)
    deletionTimestamp = ReadOnlyField(datetime.datetime)
    finalizers = ListField(six.text_type)
    generateName = Field(six.text_type)
    generation = ReadOnlyField(int)
    labels = Field(dict)
    name = Field(six.text_type)
    namespace = Field(six.text_type)
    ownerReferences = ListField(OwnerReference)
    resourceVersion = ReadOnlyField(six.text_type)
    selfLink = ReadOnlyField(six.text_type)
    uid = ReadOnlyField(six.text_type)


class ListMeta(Model):
    """
    ListMeta describes metadata that synthetic resources must have, including lists
    and various status objects. A resource may have only one of {ObjectMeta,
    ListMeta}.
    """

    resourceVersion = ReadOnlyField(six.text_type)
    selfLink = ReadOnlyField(six.text_type)


class Status(Model):
    """
    Status is a return value for calls that don't return other objects.
    """

    code = Field(int)
    details = Field(StatusDetails)
    message = Field(six.text_type)
    metadata = Field(ListMeta)
    reason = Field(six.text_type)
    status = Field(six.text_type)


class LabelSelectorRequirement(Model):
    """
    A label selector requirement is a selector that contains values, a key, and an
    operator that relates the key and values.
    """

    key = RequiredField(six.text_type)
    operator = RequiredField(six.text_type)
    values = ListField(six.text_type)


class LabelSelector(Model):
    """
    A label selector is a label query over a set of resources. The result of
    matchLabels and matchExpressions are ANDed. An empty label selector matches all
    objects. A null label selector matches no objects.
    """

    matchExpressions = ListField(LabelSelectorRequirement)
    matchLabels = Field(dict)


class GroupVersionForDiscovery(Model):
    """
    GroupVersion contains the 'group/version' and 'version' string of a version. It
    is made a struct to keep extensibility.
    """

    groupVersion = RequiredField(six.text_type)
    version = RequiredField(six.text_type)


class APIGroup(Model):
    """
    APIGroup contains the name, the supported versions, and the preferred version
    of a group.
    """

    name = RequiredField(six.text_type)
    preferredVersion = Field(GroupVersionForDiscovery)
    serverAddressByClientCIDRs = ListField(ServerAddressByClientCIDR)
    versions = ListField(GroupVersionForDiscovery)


class APIGroupList(Model):
    """
    APIGroupList is a list of APIGroup, to allow clients to discover the API at
    /apis.
    """

    groups = ListField(APIGroup)


class APIResource(Model):
    """
    APIResource specifies the name of a resource and whether it is namespaced.
    """

    name = RequiredField(six.text_type)
    namespaced = RequiredField(bool)
    shortNames = ListField(six.text_type)
    verbs = ListField(six.text_type)


class APIResourceList(Model):
    """
    APIResourceList is a list of APIResource, it is used to expose the name of the
    resources supported in a specific group and version, and if the resource is
    namespaced.
    """

    groupVersion = RequiredField(six.text_type)
    resources = ListField(APIResource)
