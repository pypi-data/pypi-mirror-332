from __future__ import annotations

import logging
from typing import List

from langchain_core.tools import BaseTool
from langchain_core.tools.base import BaseToolkit

from zmp_zcp_toolkit.models.operation import ZmpAPIOperation
from zmp_zcp_toolkit.tools.tool import ZmpTool
from zmp_zcp_toolkit.wrapper.api_wrapper import ZmpAPIWrapper

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class ZmpToolkit(BaseToolkit):
    tools: List[BaseTool] = []

    @classmethod
    def from_zmp_api_wrapper(cls, *, zmp_api_wrapper: ZmpAPIWrapper) -> "ZmpToolkit":
        """Create ZMP toolkit from ZMP API wrapper.

        Args:
            zmp_api_wrapper (BaseAPIWrapper): ZMP API wrapper

        Returns:
            ZmpToolkit: ZMP toolkit
        """
        operations: List[ZmpAPIOperation] = zmp_api_wrapper.get_operations()

        tools = [
            ZmpTool(
                name=operation.name,
                description=operation.description,
                args_schema=operation.args_schema,
                method=operation.method,
                path=operation.path,
                path_params=operation.path_params,
                query_params=operation.query_params,
                request_body=operation.request_body,
                api_wrapper=zmp_api_wrapper,
            )
            for operation in operations
        ]

        logger.debug(f"Tools: {tools}")

        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        return self.tools
