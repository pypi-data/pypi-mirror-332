# pylint: disable
# flake8: noqa
from __future__ import annotations
from enum import Enum
from typing import Annotated, Dict, List, Optional, Union

from pydantic import BaseModel, Field

from llamazure.azrest.models import AzList, ReadOnly, Req, default_list, default_dict



class AzureEntityResource(BaseModel):
	"""The resource model definition for an Azure Resource Manager resource with an etag."""

	etag: ReadOnly[str] = None
	rid: ReadOnly[str] = Field(alias="id", default=None)
	name: ReadOnly[str] = None
	type: ReadOnly[str] = None
	systemData: Optional[SystemData] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.systemData == o.systemData
		)



class CheckNameAvailabilityRequest(BaseModel):
	"""The check availability request body."""

	name: Optional[str] = None
	type: Optional[str] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.name == o.name
			and self.type == o.type
		)



class CheckNameAvailabilityResponse(BaseModel):
	"""The check availability result."""

	nameAvailable: Optional[bool] = None
	reason: Optional[str] = None
	message: Optional[str] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.nameAvailable == o.nameAvailable
			and self.reason == o.reason
			and self.message == o.message
		)



class ErrorAdditionalInfo(BaseModel):
	"""The resource management error additional info."""

	type: ReadOnly[str] = None
	info: ReadOnly[dict] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
		)



class ErrorDetail(BaseModel):
	"""The error detail."""

	code: ReadOnly[str] = None
	message: ReadOnly[str] = None
	target: ReadOnly[str] = None
	details: Annotated[List[ErrorDetail],default_list] = []
	additionalInfo: Annotated[List[ErrorAdditionalInfo],default_list] = []

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.details == o.details
			and self.additionalInfo == o.additionalInfo
		)



class ErrorResponse(BaseModel):
	"""Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.)."""

	error: Optional[ErrorDetail] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.error == o.error
		)



class Identity(BaseModel):
	"""Identity for the resource."""

	principalId: ReadOnly[str] = None
	tenantId: ReadOnly[str] = None
	type: Optional[str] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.type == o.type
		)



class Operation(BaseModel):
	"""Details of a REST API operation, returned from the Resource Provider Operations API"""
	class Display(BaseModel):
		"""Localized display information for this particular operation."""

		provider: ReadOnly[str] = None
		resource: ReadOnly[str] = None
		operation: ReadOnly[str] = None
		description: ReadOnly[str] = None

		def __eq__(self, o) -> bool:
			return (
				isinstance(o, self.__class__)
			)


	name: ReadOnly[str] = None
	isDataAction: ReadOnly[bool] = None
	display: Optional[Display] = None
	origin: ReadOnly[str] = None
	actionType: ReadOnly[str] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.display == o.display
		)



class OperationStatusResult(BaseModel):
	"""The current status of an async operation."""

	rid: Optional[str] = Field(alias="id", default=None)
	resourceId: ReadOnly[str] = None
	name: Optional[str] = None
	status: str
	percentComplete: Optional[float] = None
	startTime: Optional[str] = None
	endTime: Optional[str] = None
	operations: Annotated[List[OperationStatusResult],default_list] = []
	error: Optional[ErrorDetail] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.rid == o.rid
			and self.name == o.name
			and self.status == o.status
			and self.percentComplete == o.percentComplete
			and self.startTime == o.startTime
			and self.endTime == o.endTime
			and self.operations == o.operations
			and self.error == o.error
		)



class Plan(BaseModel):
	"""Plan for the resource."""

	name: str
	publisher: str
	product: str
	promotionCode: Optional[str] = None
	version: Optional[str] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.name == o.name
			and self.publisher == o.publisher
			and self.product == o.product
			and self.promotionCode == o.promotionCode
			and self.version == o.version
		)



class Resource(BaseModel):
	"""Common fields that are returned in the response for all Azure Resource Manager resources"""

	rid: ReadOnly[str] = Field(alias="id", default=None)
	name: ReadOnly[str] = None
	type: ReadOnly[str] = None
	systemData: Optional[SystemData] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.systemData == o.systemData
		)



class ResourceModelWithAllowedPropertySet(BaseModel):
	"""The resource model definition containing the full set of allowed properties for a resource. Except properties bag, there cannot be a top level property outside of this set."""

	managedBy: Optional[str] = None
	kind: Optional[str] = None
	etag: ReadOnly[str] = None
	identity: Optional[Identity] = None
	sku: Optional[Sku] = None
	plan: Optional[Plan] = None
	tags: Annotated[Optional[Dict[str, str]],default_dict] = {}
	location: str
	rid: ReadOnly[str] = Field(alias="id", default=None)
	name: ReadOnly[str] = None
	type: ReadOnly[str] = None
	systemData: Optional[SystemData] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.managedBy == o.managedBy
			and self.kind == o.kind
			and self.identity == o.identity
			and self.sku == o.sku
			and self.plan == o.plan
			and self.tags == o.tags
			and self.location == o.location
			and self.systemData == o.systemData
		)



class Sku(BaseModel):
	"""The resource model definition representing SKU"""

	name: str
	tier: Optional[SkuTier] = None
	size: Optional[str] = None
	family: Optional[str] = None
	capacity: Optional[int] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.name == o.name
			and self.tier == o.tier
			and self.size == o.size
			and self.family == o.family
			and self.capacity == o.capacity
		)



class TrackedResource(BaseModel):
	"""The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'"""

	tags: Annotated[Optional[Dict[str, str]],default_dict] = {}
	location: str
	rid: ReadOnly[str] = Field(alias="id", default=None)
	name: ReadOnly[str] = None
	type: ReadOnly[str] = None
	systemData: Optional[SystemData] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.tags == o.tags
			and self.location == o.location
			and self.systemData == o.systemData
		)



class LocationData(BaseModel):
	"""Metadata pertaining to the geographic location of the resource."""

	name: str
	city: Optional[str] = None
	district: Optional[str] = None
	countryOrRegion: Optional[str] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.name == o.name
			and self.city == o.city
			and self.district == o.district
			and self.countryOrRegion == o.countryOrRegion
		)



class SystemData(BaseModel):
	"""Metadata pertaining to creation and last modification of the resource."""

	createdBy: Optional[str] = None
	createdByType: Optional[str] = None
	createdAt: Optional[str] = None
	lastModifiedBy: Optional[str] = None
	lastModifiedByType: Optional[str] = None
	lastModifiedAt: Optional[str] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.createdBy == o.createdBy
			and self.createdByType == o.createdByType
			and self.createdAt == o.createdAt
			and self.lastModifiedBy == o.lastModifiedBy
			and self.lastModifiedByType == o.lastModifiedByType
			and self.lastModifiedAt == o.lastModifiedAt
		)



OperationListResult = AzList[Operation]

class SkuTier(Enum):
	"""This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT."""
	Free = "Free"
	Basic = "Basic"
	Standard = "Standard"
	Premium = "Premium"


AzureEntityResource.model_rebuild()

CheckNameAvailabilityRequest.model_rebuild()

CheckNameAvailabilityResponse.model_rebuild()

ErrorAdditionalInfo.model_rebuild()

ErrorDetail.model_rebuild()

ErrorResponse.model_rebuild()

Identity.model_rebuild()

Operation.model_rebuild()

OperationStatusResult.model_rebuild()

Plan.model_rebuild()

Resource.model_rebuild()

ResourceModelWithAllowedPropertySet.model_rebuild()

Sku.model_rebuild()

TrackedResource.model_rebuild()

LocationData.model_rebuild()

SystemData.model_rebuild()

OperationListResult.model_rebuild()


