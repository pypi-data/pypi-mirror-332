from __future__ import annotations

import logging
import re
from typing import List

from zmp_zcp_toolkit.models.mixed_spec import MethodSpec, MixedAPISpecConfig
from zmp_zcp_toolkit.models.operation import ZmpAPIOperation
from zmp_zcp_toolkit.openapi.fastapi_models import Operation
from zmp_zcp_toolkit.openapi.zmpapi_models import ZmpOpenAPI

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class OpenAPIHelper:
    """OpenAPIHelper for ZMP ApiWrapper"""

    def __init__(self, mixed_api_spec_config: MixedAPISpecConfig):
        self.mixed_api_spec_config = mixed_api_spec_config

    def generate_operations(self) -> List[ZmpAPIOperation]:
        operations = []

        for backend in self.mixed_api_spec_config.backends:
            zmp_openapi = ZmpOpenAPI.from_spec_file(backend.config.file_path)

            for api in backend.config.apis:
                for method in api.methods:
                    method_name = ""
                    description = ""

                    if isinstance(method, str):
                        method_name = method
                    elif isinstance(method, MethodSpec):
                        method_name = method.method
                        description = method.description
                    else:
                        raise ValueError(f"Invalid method type: {type(method)}")

                    operation: Operation = zmp_openapi.get_operation_by_path_method(
                        path=api.path,
                        method=method_name,
                    )
                    query_params, path_params, request_body = (
                        zmp_openapi.generate_models_by_path_and_method(
                            path=api.path,
                            method=method_name,
                        )
                    )

                    operations.append(
                        ZmpAPIOperation(
                            name=self._get_operation_name(
                                path=api.path, method=method_name
                            ),
                            description=description
                            if description
                            else operation.description
                            if operation.description
                            else "",
                            path=api.path,
                            method=method_name,
                            query_params=query_params,
                            path_params=path_params,
                            request_body=request_body,
                        )
                    )

        return operations

    def _get_operation_name(self, *, path: str, method: str) -> str:
        replaced_path = re.sub(r"[/{}_]", "-", path)  # remove path params brackets

        name = "".join(word.capitalize() for word in replaced_path.split("-"))

        return f"{method.capitalize()}{name}"
