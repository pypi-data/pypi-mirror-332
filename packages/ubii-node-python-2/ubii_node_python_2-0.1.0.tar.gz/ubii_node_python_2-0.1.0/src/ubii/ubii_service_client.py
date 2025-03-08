import aiohttp
import asyncio

from proto.services.serviceRequest_pb2 import ServiceRequest
from proto.services.serviceReply_pb2 import ServiceReply


class UbiiServiceClient:
    def __init__(self, endpoint, node):
        #print('UbiiServiceClient.endpoint: ' + endpoint)
        self.endpoint = endpoint
        self.node = node

    async def send(self, request: ServiceRequest, timeout=None) -> ServiceReply:
        return await self.sendProto(request, timeout)

    async def sendProto(self, request: ServiceRequest, timeout=None) -> ServiceReply:
        binary = request.SerializeToString()
        try:
            async with aiohttp.ClientSession(raise_for_status=True, trace_configs=[aiohttp.TraceConfig()],
                                             timeout=aiohttp.ClientTimeout(total=300)) as aiohttp_clientsession:
                async with aiohttp_clientsession.post(self.endpoint, data=binary, timeout=timeout) as response:
                    responseBinary = await asyncio.wait_for(response.read(), timeout=timeout)
                    msg = ServiceReply()
                    msg.ParseFromString(responseBinary)
                    return msg

        except aiohttp.ClientConnectionError as e:
            print('Connection Error while sending serviceRequest to masternode')
            self.node.events.onConnectionError(e)
            raise e
