from abc import ABC, abstractmethod

from neurionpy.protos.cosmos.base.tendermint.v1beta1.query_pb2 import (
    GetBlockByHeightRequest,
    GetBlockByHeightResponse,
    GetLatestBlockRequest,
    GetLatestBlockResponse,
    GetLatestValidatorSetRequest,
    GetLatestValidatorSetResponse,
    GetNodeInfoRequest,
    GetNodeInfoResponse,
    GetSyncingRequest,
    GetSyncingResponse,
    GetValidatorSetByHeightRequest,
    GetValidatorSetByHeightResponse,
)


class CosmosBaseTendermint(ABC):
    """Cosmos Base Tendermint abstract class."""

    @abstractmethod
    def GetNodeInfo(self, request: GetNodeInfoRequest) -> GetNodeInfoResponse:
        """
        GetNodeInfo queries the current node info.

        :param request: GetNodeInfoRequest
        :return: GetNodeInfoResponse
        """

    @abstractmethod
    def GetSyncing(self, request: GetSyncingRequest) -> GetSyncingResponse:
        """
        GetSyncing queries node syncing.

        :param request: GetSyncingRequest
        :return: GetSyncingResponse
        """

    @abstractmethod
    def GetLatestBlock(self, request: GetLatestBlockRequest) -> GetLatestBlockResponse:
        """
        GetLatestBlock returns the latest block.

        :param request: GetLatestBlockRequest
        :return: GetLatestBlockResponse
        """

    @abstractmethod
    def GetBlockByHeight(
        self, request: GetBlockByHeightRequest
    ) -> GetBlockByHeightResponse:
        """
        GetBlockByHeight queries block for given height.

        :param request: GetBlockByHeightRequest
        :return: GetBlockByHeightResponse
        """

    @abstractmethod
    def GetLatestValidatorSet(
        self, request: GetLatestValidatorSetRequest
    ) -> GetLatestValidatorSetResponse:
        """
        GetLatestValidatorSet queries latest validator-set.

        :param request: GetLatestValidatorSetRequest
        :return: GetLatestValidatorSetResponse
        """

    @abstractmethod
    def GetValidatorSetByHeight(
        self, request: GetValidatorSetByHeightRequest
    ) -> GetValidatorSetByHeightResponse:
        """
        GetValidatorSetByHeight queries validator-set at a given height.

        :param request: GetValidatorSetByHeightRequest
        :return: GetValidatorSetByHeightResponse
        """
