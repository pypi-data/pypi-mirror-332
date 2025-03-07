from abc import ABC, abstractmethod

import neurionpy.protos.cosmos.tx.v1beta1.service_pb2 as svc


class TxInterface(ABC):
    """Tx abstract class."""

    @abstractmethod
    def Simulate(self, request: svc.SimulateRequest) -> svc.SimulateResponse:
        """
        Simulate executing a transaction to estimate gas usage.

        :param request: SimulateRequest
        :return: SimulateResponse
        """

    @abstractmethod
    def GetTx(self, request: svc.GetTxRequest) -> svc.GetTxResponse:
        """
        GetTx fetches a tx by hash.

        :param request: GetTxRequest
        :return: GetTxResponse
        """

    @abstractmethod
    def BroadcastTx(self, request: svc.BroadcastTxRequest) -> svc.BroadcastTxResponse:
        """
        BroadcastTx broadcast transaction.

        :param request: BroadcastTxRequest
        :return: BroadcastTxResponse
        """

    @abstractmethod
    def GetTxsEvent(self, request: svc.GetTxsEventRequest) -> svc.GetTxsEventResponse:
        """
        GetTxsEvent fetches txs by event.

        :param request: GetTxsEventRequest
        :return: GetTxsEventResponse
        """
