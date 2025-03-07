from abc import ABC, abstractmethod

from neurionpy.protos.cosmos.distribution.v1beta1.query_pb2 import (
    QueryCommunityPoolResponse,
    QueryDelegationRewardsRequest,
    QueryDelegationRewardsResponse,
    QueryDelegationTotalRewardsRequest,
    QueryDelegationTotalRewardsResponse,
    QueryDelegatorValidatorsRequest,
    QueryDelegatorValidatorsResponse,
    QueryDelegatorWithdrawAddressRequest,
    QueryDelegatorWithdrawAddressResponse,
    QueryParamsResponse,
    QueryValidatorCommissionRequest,
    QueryValidatorCommissionResponse,
    QueryValidatorOutstandingRewardsRequest,
    QueryValidatorOutstandingRewardsResponse,
    QueryValidatorSlashesRequest,
    QueryValidatorSlashesResponse,
)


class Distribution(ABC):
    """Distribution abstract class."""

    @abstractmethod
    def CommunityPool(self) -> QueryCommunityPoolResponse:
        """
        CommunityPool queries the community pool coins.

        :return: a QueryCommunityPoolResponse instance
        """

    @abstractmethod
    def DelegationTotalRewards(
        self, request: QueryDelegationTotalRewardsRequest
    ) -> QueryDelegationTotalRewardsResponse:
        """
        DelegationTotalRewards queries the total rewards accrued by each validator.

        :param request: a QueryDelegationTotalRewardsRequest instance
        :return: a QueryDelegationTotalRewardsResponse instance
        """

    @abstractmethod
    def DelegationRewards(
        self, request: QueryDelegationRewardsRequest
    ) -> QueryDelegationRewardsResponse:
        """
        DelegationRewards queries the total rewards accrued by a delegation.

        :param request: a QueryDelegationRewardsRequest instance
        :return: a QueryDelegationRewardsResponse instance
        """

    @abstractmethod
    def DelegatorValidators(
        self, request: QueryDelegatorValidatorsRequest
    ) -> QueryDelegatorValidatorsResponse:
        """
        DelegatorValidators queries the validators of a delegator.

        :param request: a QueryDelegatorValidatorsRequest instance
        :return: a QueryDelegatorValidatorsResponse instance
        """

    @abstractmethod
    def DelegatorWithdrawAddress(
        self, request: QueryDelegatorWithdrawAddressRequest
    ) -> QueryDelegatorWithdrawAddressResponse:
        """
        DelegatorWithdrawAddress queries withdraw address of a delegator.

        :param request: a QueryDelegatorWithdrawAddressRequest instance
        :return: a QueryDelegatorWithdrawAddressResponse instance
        """

    @abstractmethod
    def Params(self) -> QueryParamsResponse:
        """
        Params queries params of the distribution module.

        :return: a QueryParamsResponse instance
        """

    @abstractmethod
    def ValidatorCommission(
        self, request: QueryValidatorCommissionRequest
    ) -> QueryValidatorCommissionResponse:
        """
        ValidatorCommission queries accumulated commission for a validator.

        :param request: QueryValidatorCommissionRequest
        :return: QueryValidatorCommissionResponse
        """

    @abstractmethod
    def ValidatorOutstandingRewards(
        self, request: QueryValidatorOutstandingRewardsRequest
    ) -> QueryValidatorOutstandingRewardsResponse:
        """
        ValidatorOutstandingRewards queries rewards of a validator address.

        :param request: QueryValidatorOutstandingRewardsRequest
        :return: QueryValidatorOutstandingRewardsResponse
        """

    @abstractmethod
    def ValidatorSlashes(
        self, request: QueryValidatorSlashesRequest
    ) -> QueryValidatorSlashesResponse:
        """
        ValidatorSlashes queries slash events of a validator.

        :param request: QueryValidatorSlashesRequest
        :return: QueryValidatorSlashesResponse
        """
