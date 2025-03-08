# scm/models/objects/__init__.py

from .address import (
    AddressCreateModel,
    AddressUpdateModel,
    AddressResponseModel,
)
from .address_group import (
    AddressGroupResponseModel,
    AddressGroupCreateModel,
    AddressGroupUpdateModel,
)
from .syslog_server_profiles import (
    SyslogServerProfileCreateModel,
    SyslogServerProfileUpdateModel,
    SyslogServerProfileResponseModel,
)
from .application import (
    ApplicationCreateModel,
    ApplicationResponseModel,
    ApplicationUpdateModel,
)
from .application_filters import (
    ApplicationFiltersCreateModel,
    ApplicationFiltersResponseModel,
    ApplicationFiltersUpdateModel,
)
from .application_group import (
    ApplicationGroupCreateModel,
    ApplicationGroupResponseModel,
    ApplicationGroupUpdateModel,
)
from .dynamic_user_group import (
    DynamicUserGroupCreateModel,
    DynamicUserGroupResponseModel,
    DynamicUserGroupUpdateModel,
)
from .external_dynamic_lists import (
    ExternalDynamicListsCreateModel,
    ExternalDynamicListsResponseModel,
    ExternalDynamicListsUpdateModel,
)
from .hip_object import (
    HIPObjectCreateModel,
    HIPObjectResponseModel,
    HIPObjectUpdateModel,
)
from .hip_profile import (
    HIPProfileCreateModel,
    HIPProfileResponseModel,
    HIPProfileUpdateModel,
)
from .http_server_profiles import (
    HTTPServerProfileCreateModel,
    HTTPServerProfileResponseModel,
    HTTPServerProfileUpdateModel,
    ServerModel,
)
from .log_forwarding_profile import (
    LogForwardingProfileCreateModel,
    LogForwardingProfileResponseModel,
    LogForwardingProfileUpdateModel,
    MatchListItem,
)
from .regions import (
    RegionCreateModel,
    RegionResponseModel,
    RegionUpdateModel,
    GeoLocation,
)
from .schedules import (
    ScheduleCreateModel,
    ScheduleResponseModel,
    ScheduleUpdateModel,
)
from .service import (
    ServiceCreateModel,
    ServiceResponseModel,
    ServiceUpdateModel,
)
from .service_group import (
    ServiceGroupResponseModel,
    ServiceGroupCreateModel,
    ServiceGroupUpdateModel,
)
from .tag import (
    TagCreateModel,
    TagResponseModel,
    TagUpdateModel,
)
from .quarantined_devices import (
    QuarantinedDevicesCreateModel,
    QuarantinedDevicesResponseModel,
    QuarantinedDevicesListParamsModel,
)
from .syslog_server_profiles import (
    SyslogServerProfileCreateModel,
    SyslogServerProfileResponseModel,
    SyslogServerProfileUpdateModel,
    SyslogServerModel,
    FormatModel,
    EscapingModel,
)

"""
# these are pydantic implementations created by not currently implemented in the API
# these will all return a 403 status code until implemented
from .auto_tag_actions import (
    AutoTagActionCreateModel,
    AutoTagActionResponseModel,
    AutoTagActionUpdateModel,
)
"""
