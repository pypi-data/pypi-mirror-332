from collections import defaultdict
from enum import StrEnum

import mcp.server.stdio
from mcp.server.models import InitializationOptions
from mcp.types import TextContent, Tool
from mcp.server import NotificationOptions, Server
from pydantic import BaseModel, Field

from .load import load_hch_service_details_info, load_hch_service_price_info


class HchTools(StrEnum):
    GREETS = "get_greetings"
    RES_SERVICES = "get_residential_services"
    SERVICE_DETAILS_INFO = "get_service_details_info"
    SERVICE_PRICE_INFO = "get_service_price_info"


class HchResidentialServices(StrEnum):
    DETAIL = "Detail Cleaning"
    MOVE_IN = "Move In Cleaning"
    MOVE_OUT = "Move Out Cleaning"
    POST_RENOVATION = "Post-Renovation Cleaning"
    SPRING = "Spring Cleaning (Occupied Unit)"
    FLOOR = "Floor Cleaning or Floor Care"
    FORMALDEHYDE = "Formaldehyde (VOC)"
    DISINFECTING = "Disinfecting"
    HOUSEHOLD_ACCESSORY = "Household Accessory Cleaning (e.g. Sofa, Mattress, Carpet, Curtains)"
    CUSTOMISED = "Customised or Combination Cleaning"


class HchCommercialServices(StrEnum):
    Commercial = "Commercial Cleaning"


class HchGetGreetings(BaseModel):
    pass


class HchGetResidentialServices(BaseModel):
    pass


class HchGetServiceDetailsInfo(BaseModel):
    service: HchResidentialServices | HchCommercialServices = Field(description="Home clean home(hch) service.")


class HchGetServicePriceInfo(BaseModel):
    service: HchResidentialServices | HchCommercialServices = Field(description="Home clean home(hch) service.")


server = Server("home-clean-home")
service2details_info = load_hch_service_details_info()
service2price_info = load_hch_service_price_info()


def get_greetings() -> str:
    """Get greetings message.

    Returns:
        str: Greetings message.
    """
    return (
        "Hi, I'm Minnie from Home Clean Home. Thanks for meessaging us!\n\n"
        "May I check if you're enquiring for residential cleaning services or commercial cleaning services?"
    )


def get_res_services() -> list[str]:
    """Retrieve all residential cleaning services.

    Returns:
        list[str]: A list of residential cleaning services.
    """
    return [service.value for service in HchResidentialServices]


def get_service_details_info(service: HchResidentialServices | HchCommercialServices) -> str:
    """Get details info with respect to the selected cleaning service.

    Args:
        service (HchResidentialServices | HchCommercialServices): Home clean home(hch) residential/commercial service.

    Returns:
        str: Details information for the selected service.
    """
    details_info = service2details_info.get(service, None)
    if not details_info:
        return f"No details information found for {service}."

    return f"{'='*50}\n".join(details_info)


def get_service_price_info(service: HchResidentialServices | HchCommercialServices) -> str:
    """Get price info with respect to the selected cleaning service.

    Args:
        service (HchResidentialServices | HchCommercialServices): Home clean home(hch) residential/commercial service.

    Returns:
        str: Price information for the selected service.
    """
    price_info = service2price_info.get(service, None)
    if not price_info:
        return f"No price information found for {service}."

    return f"{'='*50}\n".join(price_info)


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available tools. Each tool specifies its arguments using JSON Schema validation.

    Returns:
        list[Tool]: A list of tools available for the server.
    """
    return [
        Tool(
            name=HchTools.GREETS,
            description="Get greetings message.",
            inputSchema=HchGetGreetings.model_json_schema(),
        ),
        Tool(
            name=HchTools.RES_SERVICES,
            description="Get all residential cleaning services.",
            inputSchema=HchGetResidentialServices.model_json_schema(),
        ),
        Tool(
            name=HchTools.SERVICE_DETAILS_INFO,
            description="Get details info with respect to the selected cleaning service.",
            inputSchema=HchGetServiceDetailsInfo.model_json_schema(),
        ),
        Tool(
            name=HchTools.SERVICE_PRICE_INFO,
            description="Get price info with respect to the selected cleaning service.",
            inputSchema=HchGetServicePriceInfo.model_json_schema(),
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool execution requests. Tools can modify server state and notify clients of changes.

    Args:
        name (str): Tool name.
        arguments (dict): Tool arguments.

    Returns:
        list[TextContent]: A list of text content to be sent to the client.
    """
    match name:
        case HchTools.GREETS:
            greetings = get_greetings()
            return [TextContent(type="text", text=greetings)]

        case HchTools.RES_SERVICES:
            services = get_res_services()
            formatted_output = "\n".join(f"{index+1}. {service}" for index, service in enumerate(services))
            return [TextContent(type="text", text=f"Available services:\n{formatted_output}")]

        case HchTools.SERVICE_DETAILS_INFO:
            service = arguments["service"]
            service_details_info = get_service_details_info(service=service)
            return [
                TextContent(
                    type="text",
                    text=f"{service_details_info}",
                )
            ]

        case HchTools.SERVICE_PRICE_INFO:
            service = arguments["service"]
            price_info = get_service_price_info(service=service)
            return [
                TextContent(
                    type="text",
                    text=f"{price_info}",
                )
            ]

        case _:
            raise ValueError(f"Unknown tool: {name}")


async def main():
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="home-clean-home",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
