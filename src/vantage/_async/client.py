"""Auto-generated asynchronous client for Vantage API."""

from __future__ import annotations

from typing import Any, Optional, Dict, List
from urllib.parse import quote

import httpx

from .._base import (
    VantageAPIError,
    DEFAULT_BASE_URL,
    build_query_string,
    is_multipart_route,
)
from .._types import *  # noqa: F401, F403


class AsyncClient:
    """Asynchronous HTTP client for Vantage API."""

    def __init__(
        self,
        bearer_token: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
    ) -> None:
        self._bearer_token = bearer_token
        self._base_url = base_url.rstrip('/')
        self._http = httpx.AsyncClient(
            headers={"Authorization": f"Bearer {bearer_token}"},
            timeout=30.0,
        )

        # Initialize resource APIs
        self.access_grants = AccessGrantsAsyncApi(self)
        self.anomaly_alerts = AnomalyAlertsAsyncApi(self)
        self.anomaly_notifications = AnomalyNotificationsAsyncApi(self)
        self.audit_logs = AuditLogsAsyncApi(self)
        self.billing_profiles = BillingProfilesAsyncApi(self)
        self.billing_rules = BillingRulesAsyncApi(self)
        self.budget_alerts = BudgetAlertsAsyncApi(self)
        self.budgets = BudgetsAsyncApi(self)
        self.business_metrics = BusinessMetricsAsyncApi(self)
        self.cost_alerts = CostAlertsAsyncApi(self)
        self.cost_provider_accounts = CostProviderAccountsAsyncApi(self)
        self.cost_providers = CostProvidersAsyncApi(self)
        self.cost_reports = CostReportsAsyncApi(self)
        self.cost_services = CostServicesAsyncApi(self)
        self.costs = CostsAsyncApi(self)
        self.dashboards = DashboardsAsyncApi(self)
        self.data_exports = DataExportsAsyncApi(self)
        self.exchange_rates = ExchangeRatesAsyncApi(self)
        self.financial_commitment_reports = FinancialCommitmentReportsAsyncApi(self)
        self.financial_commitments = FinancialCommitmentsAsyncApi(self)
        self.folders = FoldersAsyncApi(self)
        self.integrations = IntegrationsAsyncApi(self)
        self.invoices = InvoicesAsyncApi(self)
        self.kubernetes_efficiency_reports = KubernetesEfficiencyReportsAsyncApi(self)
        self.managed_accounts = ManagedAccountsAsyncApi(self)
        self.me = MeAsyncApi(self)
        self.network_flow_reports = NetworkFlowReportsAsyncApi(self)
        self.ping = PingAsyncApi(self)
        self.products = ProductsAsyncApi(self)
        self.recommendation_views = RecommendationViewsAsyncApi(self)
        self.recommendations = RecommendationsAsyncApi(self)
        self.report_notifications = ReportNotificationsAsyncApi(self)
        self.resource_reports = ResourceReportsAsyncApi(self)
        self.resources = ResourcesAsyncApi(self)
        self.saved_filters = SavedFiltersAsyncApi(self)
        self.segments = SegmentsAsyncApi(self)
        self.tags = TagsAsyncApi(self)
        self.teams = TeamsAsyncApi(self)
        self.unit_costs = UnitCostsAsyncApi(self)
        self.user_feedback = UserFeedbackAsyncApi(self)
        self.users = UsersAsyncApi(self)
        self.virtual_tag_configs = VirtualTagConfigsAsyncApi(self)
        self.workspaces = WorkspacesAsyncApi(self)

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._http.aclose()

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Make a raw API request."""
        url = self._base_url + path

        if method.upper() == 'GET' and params:
            url += build_query_string(params)
            params = None

        if is_multipart_route(path, method):
            response = await self._http.request(
                method,
                url,
                data=body,
            )
        else:
            response = await self._http.request(
                method,
                url,
                params=params,
                json=body,
            )

        if not response.is_success:
            raise VantageAPIError(
                status=response.status_code,
                status_text=response.reason_phrase,
                body=response.text,
            )

        try:
            data = response.json()
        except Exception:
            data = None

        return data


class AccessGrantsAsyncApi:
    """Async API methods for access_grants resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> AccessGrants:
        """
        Get all access grants
        
        Return all Access Grants that the current API token has access to.
        """
        path = "/access_grants"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateAccessGrant) -> AccessGrant:
        """
        Create access grant
        
        Create an Access Grant.
        """
        path = "/access_grants"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, access_grant_token: str) -> AccessGrant:
        """
        Get access grant by token
        
        Return a specific Access Grant.
        """
        path = f"/access_grants/{quote(str(access_grant_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, access_grant_token: str, body: UpdateAccessGrant) -> AccessGrant:
        """
        Update access grant
        
        Update an AccessGrant.
        """
        path = f"/access_grants/{quote(str(access_grant_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, access_grant_token: str) -> Any:
        """
        Delete access grant
        
        Delete an Access Grant.
        """
        path = f"/access_grants/{quote(str(access_grant_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class AnomalyAlertsAsyncApi:
    """Async API methods for anomaly_alerts resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None, start_date: Optional[str] = None, end_date: Optional[str] = None, provider: Optional[str] = None, service: Optional[str] = None, cost_category: Optional[str] = None, cost_report_token: Optional[str] = None) -> AnomalyAlerts:
        """
        Get all anomaly alerts
        
        Return all Anomaly Alerts that the current API token has access to.
        """
        path = "/anomaly_alerts"
        params = {
            "page": page,
            "limit": limit,
            "start_date": start_date,
            "end_date": end_date,
            "provider": provider,
            "service": service,
            "cost_category": cost_category,
            "cost_report_token": cost_report_token,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get(self, anomaly_alert_token: str) -> AnomalyAlert:
        """
        Get anomaly alert by token
        
        Return an AnomalyAlert that the current API token has access to.
        """
        path = f"/anomaly_alerts/{quote(str(anomaly_alert_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, anomaly_alert_token: str, body: UpdateAnomalyAlert) -> AnomalyAlert:
        """
        Update anomaly alert
        
        Update an AnomalyAlert.
        """
        path = f"/anomaly_alerts/{quote(str(anomaly_alert_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)


class AnomalyNotificationsAsyncApi:
    """Async API methods for anomaly_notifications resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> AnomalyNotifications:
        """
        Get all anomaly notifications
        
        Return all Anomaly Notifications.
        """
        path = "/anomaly_notifications"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateAnomalyNotification) -> AnomalyNotification:
        """
        Create anomaly notification
        
        Create an Anomaly Notification for a Cost Report.
        """
        path = "/anomaly_notifications"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, anomaly_notification_token: str) -> AnomalyNotification:
        """
        Get anomaly notification by token
        
        Return an Anomaly Notification that the current API token has access to.
        """
        path = f"/anomaly_notifications/{quote(str(anomaly_notification_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, anomaly_notification_token: str, body: UpdateAnomalyNotification) -> AnomalyNotification:
        """
        Update anomaly notification
        
        Update an Anomaly Notification.
        """
        path = f"/anomaly_notifications/{quote(str(anomaly_notification_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, anomaly_notification_token: str) -> Any:
        """
        Delete anomaly notification
        
        Delete an Anomaly Notification.
        """
        path = f"/anomaly_notifications/{quote(str(anomaly_notification_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class AuditLogsAsyncApi:
    """Async API methods for audit_logs resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None, user: Optional[int] = None, workspace_token: Optional[str] = None, action: Optional[str] = None, object_name: Optional[str] = None, source: Optional[str] = None, object_type: Optional[str] = None, token: Optional[str] = None, object_token: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None) -> AuditLogs:
        """
        Get all audit logs
        
        Return all AuditLogs.
        """
        path = "/audit_logs"
        params = {
            "page": page,
            "limit": limit,
            "user": user,
            "workspace_token": workspace_token,
            "action": action,
            "object_name": object_name,
            "source": source,
            "object_type": object_type,
            "token": token,
            "object_token": object_token,
            "start_date": start_date,
            "end_date": end_date,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get(self, audit_log_token: str) -> AuditLog:
        """
        Get audit log by token
        
        Return a specific AuditLog.
        """
        path = f"/audit_logs/{quote(str(audit_log_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class BillingProfilesAsyncApi:
    """Async API methods for billing_profiles resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> BillingProfiles:
        """
        Get all billing profiles
        
        Returns a list of billing profiles (MSP invoicing required).
        """
        path = "/billing_profiles"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateBillingProfile) -> BillingProfile:
        """
        Create billing profile
        
        Create a billing profile (MSP invoicing required).
        """
        path = "/billing_profiles"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, billing_profile_token: str) -> BillingProfile:
        """
        Get billing profile by token
        
        Requires MSP invoicing to be enabled on the account.
        """
        path = f"/billing_profiles/{quote(str(billing_profile_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, billing_profile_token: str, body: UpdateBillingProfile) -> BillingProfile:
        """
        Update billing profile
        
        Requires MSP invoicing to be enabled on the account.
        """
        path = f"/billing_profiles/{quote(str(billing_profile_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, billing_profile_token: str) -> Any:
        """
        Delete billing profile
        
        Requires MSP invoicing to be enabled on the account.
        """
        path = f"/billing_profiles/{quote(str(billing_profile_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class BillingRulesAsyncApi:
    """Async API methods for billing_rules resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> BillingRules:
        """
        Get all billing rules
        
        Returns a list of billing rules.
        """
        path = "/billing_rules"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateBillingRule) -> BillingRule:
        """
        Create billing rule
        
        Create a BillingRule.
        """
        path = "/billing_rules"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, billing_rule_token: str) -> BillingRule:
        """
        Get billing rule by token
        
        Return a BillingRule.
        """
        path = f"/billing_rules/{quote(str(billing_rule_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, billing_rule_token: str, body: UpdateBillingRule) -> BillingRule:
        """
        Update billing rule
        
        Update a BillingRule.
        """
        path = f"/billing_rules/{quote(str(billing_rule_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, billing_rule_token: str) -> Any:
        """
        Delete billing rule
        
        Delete a BillingRule.
        """
        path = f"/billing_rules/{quote(str(billing_rule_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class BudgetAlertsAsyncApi:
    """Async API methods for budget_alerts resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> BudgetAlerts:
        """
        Get all budget alerts
        
        Return all BudgetAlerts.
        """
        path = "/budget_alerts"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateBudgetAlert) -> BudgetAlert:
        """
        Create budget alert
        
        Create a Budget Alert.
        """
        path = "/budget_alerts"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, budget_alert_token: str) -> BudgetAlert:
        """
        Get budget alert by token
        
        Return a BudgetAlert.
        """
        path = f"/budget_alerts/{quote(str(budget_alert_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, budget_alert_token: str, body: UpdateBudgetAlert) -> BudgetAlert:
        """
        Update budget alert
        
        Updates an existing BudgetAlert.
        """
        path = f"/budget_alerts/{quote(str(budget_alert_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, budget_alert_token: str) -> Any:
        """
        Delete budget alert
        
        Delete a BudgetAlert.
        """
        path = f"/budget_alerts/{quote(str(budget_alert_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class BudgetsAsyncApi:
    """Async API methods for budgets resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> Budgets:
        """
        Get all budgets
        
        Return all Budgets.
        """
        path = "/budgets"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateBudget) -> Budget:
        """
        Create budget
        
        Create a Budget.
        """
        path = "/budgets"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, budget_token: str, *, include_performance: Optional[bool] = None) -> Budget:
        """
        Get budget by token
        
        Return a Budget.
        """
        path = f"/budgets/{quote(str(budget_token), safe='')}"
        params = {
            "include_performance": include_performance,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, budget_token: str, body: UpdateBudget) -> Budget:
        """
        Update budget
        
        Update a Budget.
        """
        path = f"/budgets/{quote(str(budget_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, budget_token: str) -> Any:
        """
        Delete budget
        
        Delete a Budget.
        """
        path = f"/budgets/{quote(str(budget_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class BusinessMetricsAsyncApi:
    """Async API methods for business_metrics resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> BusinessMetrics:
        """
        Get all business metrics
        
        Return all BusinessMetrics that the current API token has access to.
        """
        path = "/business_metrics"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateBusinessMetric) -> BusinessMetric:
        """
        Create business metric
        
        Create a new BusinessMetric.
        """
        path = "/business_metrics"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, business_metric_token: str) -> BusinessMetric:
        """
        Get business metric by token
        
        Return a BusinessMetric.
        """
        path = f"/business_metrics/{quote(str(business_metric_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, business_metric_token: str, body: UpdateBusinessMetric) -> BusinessMetric:
        """
        Update business metric
        
        Updates an existing BusinessMetric.
        """
        path = f"/business_metrics/{quote(str(business_metric_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, business_metric_token: str) -> Any:
        """
        Delete business metric
        
        Deletes an existing BusinessMetric.
        """
        path = f"/business_metrics/{quote(str(business_metric_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)

    async def get_values(self, business_metric_token: str, *, page: Optional[int] = None, limit: Optional[int] = None, start_date: Optional[str] = None) -> BusinessMetricValues:
        """
        Get business metric values
        
        Return values of a BusinessMetric
        """
        path = f"/business_metrics/{quote(str(business_metric_token), safe='')}/values"
        params = {
            "page": page,
            "limit": limit,
            "start_date": start_date,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get_forecasted_values(self, business_metric_token: str, *, page: Optional[int] = None, limit: Optional[int] = None, start_date: Optional[str] = None) -> BusinessMetricValues:
        """
        Get business metric forecasted values
        
        Return forecasted values of a BusinessMetric
        """
        path = f"/business_metrics/{quote(str(business_metric_token), safe='')}/forecasted_values"
        params = {
            "page": page,
            "limit": limit,
            "start_date": start_date,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update_values_csv(self, business_metric_token: str, body: dict[str, Any]) -> BusinessMetric:
        """
        Update business metric values from CSV
        
        Updates the values for an existing BusinessMetric from a CSV file.
        """
        path = f"/business_metrics/{quote(str(business_metric_token), safe='')}/values.csv"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)


class CostAlertsAsyncApi:
    """Async API methods for cost_alerts resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def get_events(self, cost_alert_token: str, *, report_token: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> CostAlertEvents:
        """
        Get all cost alert events
        
        Get all CostAlertEvents
        """
        path = f"/cost_alerts/{quote(str(cost_alert_token), safe='')}/events"
        params = {
            "report_token": report_token,
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get_event(self, cost_alert_token: str, event_token: str) -> CostAlertEvent:
        """
        Get cost alert event by token
        
        Get a CostAlertEvent
        """
        path = f"/cost_alerts/{quote(str(cost_alert_token), safe='')}/events/{quote(str(event_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def list(self) -> CostAlerts:
        """
        Get all cost alerts
        
        List all Cost Alerts
        """
        path = "/cost_alerts"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateCostAlert) -> CostAlert:
        """
        Create cost alert
        
        Create a new Cost Alert
        """
        path = "/cost_alerts"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, cost_alert_token: str) -> CostAlert:
        """
        Get cost alert by token
        
        Get a Cost Alert
        """
        path = f"/cost_alerts/{quote(str(cost_alert_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, cost_alert_token: str, body: UpdateCostAlert) -> CostAlert:
        """
        Update cost alert
        
        Update a Cost Alert
        """
        path = f"/cost_alerts/{quote(str(cost_alert_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, cost_alert_token: str) -> Any:
        """
        Delete cost alert
        
        Delete a Cost Alert
        """
        path = f"/cost_alerts/{quote(str(cost_alert_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class CostProviderAccountsAsyncApi:
    """Async API methods for cost_provider_accounts resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, workspace_token: Optional[str] = None, provider: Optional[str] = None, account_id: Optional[str] = None, account_name: Optional[str] = None) -> CostProviderAccounts:
        """
        Get all cost provider accounts
        
        List CostProviderAccounts available in a given Workspace.
        """
        path = "/cost_provider_accounts"
        params = {
            "workspace_token": workspace_token,
            "provider": provider,
            "account_id": account_id,
            "account_name": account_name,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class CostProvidersAsyncApi:
    """Async API methods for cost_providers resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, workspace_token: Optional[str] = None) -> CostProviders:
        """
        Get cost providers
        
        List CostProviders available to query in a given Workspace.
        """
        path = "/cost_providers"
        params = {
            "workspace_token": workspace_token,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class CostReportsAsyncApi:
    """Async API methods for cost_reports resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None, folder_token: Optional[str] = None) -> CostReports:
        """
        Get all cost reports
        
        Return all CostReports.
        """
        path = "/cost_reports"
        params = {
            "page": page,
            "limit": limit,
            "folder_token": folder_token,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateCostReport) -> CostReport:
        """
        Create cost report
        
        Create a CostReport.
        """
        path = "/cost_reports"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, cost_report_token: str) -> CostReport:
        """
        Get cost report by token
        
        Return a CostReport.
        """
        path = f"/cost_reports/{quote(str(cost_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, cost_report_token: str, body: UpdateCostReport) -> CostReport:
        """
        Update cost report
        
        Update a CostReport.
        """
        path = f"/cost_reports/{quote(str(cost_report_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, cost_report_token: str) -> Any:
        """
        Delete cost report
        
        Delete a CostReport.
        """
        path = f"/cost_reports/{quote(str(cost_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)

    async def get_forecasted_costs(self, cost_report_token: str, *, start_date: Optional[str] = None, end_date: Optional[str] = None, provider: Optional[str] = None, service: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> ForecastedCosts:
        """
        Get forecasted costs for a cost report
        
        Return all ForecastedCosts.
        """
        path = f"/cost_reports/{quote(str(cost_report_token), safe='')}/forecasted_costs"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "provider": provider,
            "service": service,
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class CostServicesAsyncApi:
    """Async API methods for cost_services resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, workspace_token: Optional[str] = None) -> CostServices:
        """
        Get cost services
        
        List CostServices available to query in a given Workspace.
        """
        path = "/cost_services"
        params = {
            "workspace_token": workspace_token,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class CostsAsyncApi:
    """Async API methods for costs resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def create_export(self, body: CreateCostExport, *, groupings: Optional[List[str]] = None) -> Any:
        """
        Generate cost data export
        
        Generate a DataExport of costs.
        """
        path = "/costs/data_exports"
        params = {
            "groupings": groupings,
        }
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def list(self, *, cost_report_token: Optional[str] = None, filter: Optional[str] = None, workspace_token: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None, groupings: Optional[List[str]] = None, order: Optional[str] = None, limit: Optional[int] = None, page: Optional[int] = None, date_bin: Optional[str] = None, settings_include_credits: Optional[bool] = None, settings_include_refunds: Optional[bool] = None, settings_include_discounts: Optional[bool] = None, settings_include_tax: Optional[bool] = None, settings_amortize: Optional[bool] = None, settings_unallocated: Optional[bool] = None, settings_aggregate_by: Optional[str] = None, settings_show_previous_period: Optional[bool] = None) -> Costs:
        """
        Get costs for cost report or VQL filter
        
        Return all Costs for a CostReport or VQL filter.
        """
        path = "/costs"
        params = {
            "cost_report_token": cost_report_token,
            "filter": filter,
            "workspace_token": workspace_token,
            "start_date": start_date,
            "end_date": end_date,
            "groupings": groupings,
            "order": order,
            "limit": limit,
            "page": page,
            "date_bin": date_bin,
            "settings[include_credits]": settings_include_credits,
            "settings[include_refunds]": settings_include_refunds,
            "settings[include_discounts]": settings_include_discounts,
            "settings[include_tax]": settings_include_tax,
            "settings[amortize]": settings_amortize,
            "settings[unallocated]": settings_unallocated,
            "settings[aggregate_by]": settings_aggregate_by,
            "settings[show_previous_period]": settings_show_previous_period,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class DashboardsAsyncApi:
    """Async API methods for dashboards resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> Dashboards:
        """
        Get all dashboards
        
        Return all Dashboards.
        """
        path = "/dashboards"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateDashboard) -> Dashboard:
        """
        Create dashboard
        
        Create a Dashboard.
        """
        path = "/dashboards"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, dashboard_token: str) -> Dashboard:
        """
        Get dashboard by token
        
        Return a specific Dashboard.
        """
        path = f"/dashboards/{quote(str(dashboard_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, dashboard_token: str, body: UpdateDashboard) -> Dashboard:
        """
        Update dashboard
        
        Update a Dashboard.
        """
        path = f"/dashboards/{quote(str(dashboard_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, dashboard_token: str) -> Any:
        """
        Delete dashboard
        
        Delete a Dashboard.
        """
        path = f"/dashboards/{quote(str(dashboard_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class DataExportsAsyncApi:
    """Async API methods for data_exports resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def get(self, data_export_token: str) -> DataExport:
        """
        Get status of data export
        
        Get the status of a data export.
        """
        path = f"/data_exports/{quote(str(data_export_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class ExchangeRatesAsyncApi:
    """Async API methods for exchange_rates resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> ExchangeRates:
        """
        Get all exchange rates
        
        Return all Exchange Rates.
        """
        path = "/exchange_rates"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create_via_csv(self, body: dict[str, Any]) -> Any:
        """
        Upload exchange rates via CSV
        
        Upload Exchange Rates via CSV.
        """
        path = "/exchange_rates/csv"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)


class FinancialCommitmentReportsAsyncApi:
    """Async API methods for financial_commitment_reports resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> FinancialCommitmentReports:
        """
        Get all financial commitment reports
        
        Return all FinancialCommitmentReports.
        """
        path = "/financial_commitment_reports"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateFinancialCommitmentReport) -> FinancialCommitmentReport:
        """
        Create financial commitment report
        
        Create a FinancialCommitmentReport.
        """
        path = "/financial_commitment_reports"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, financial_commitment_report_token: str) -> FinancialCommitmentReport:
        """
        Get financial commitment report by token
        
        Return a FinancialCommitmentReport.
        """
        path = f"/financial_commitment_reports/{quote(str(financial_commitment_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, financial_commitment_report_token: str, body: UpdateFinancialCommitmentReport) -> FinancialCommitmentReport:
        """
        Update financial commitment report
        
        Update a FinancialCommitmentReport.
        """
        path = f"/financial_commitment_reports/{quote(str(financial_commitment_report_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, financial_commitment_report_token: str) -> Any:
        """
        Delete financial commitment report
        
        Delete a FinancialCommitmentReport.
        """
        path = f"/financial_commitment_reports/{quote(str(financial_commitment_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class FinancialCommitmentsAsyncApi:
    """Async API methods for financial_commitments resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> FinancialCommitments:
        """
        Get all financial commitments
        
        Return all FinancialCommitments.
        """
        path = "/financial_commitments"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class FoldersAsyncApi:
    """Async API methods for folders resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> Folders:
        """
        Get all folders
        
        Return all Folders for CostReports.
        """
        path = "/folders"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateFolder) -> Folder:
        """
        Create folder
        
        Create a Folder for CostReports.
        """
        path = "/folders"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, folder_token: str) -> Folder:
        """
        Get folder by token
        
        Return a specific Folder for CostReports.
        """
        path = f"/folders/{quote(str(folder_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, folder_token: str, body: UpdateFolder) -> Folder:
        """
        Update folder
        
        Update a Folder for CostReports.
        """
        path = f"/folders/{quote(str(folder_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, folder_token: str) -> Any:
        """
        Delete folder
        
        Delete a Folder for CostReports.
        """
        path = f"/folders/{quote(str(folder_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class IntegrationsAsyncApi:
    """Async API methods for integrations resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, provider: Optional[str] = None, account_identifier: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Integrations:
        """
        Get all integrations
        
        Return all Integrations.
        """
        path = "/integrations"
        params = {
            "provider": provider,
            "account_identifier": account_identifier,
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get(self, integration_token: str) -> Integration:
        """
        Get integration by token
        
        Return an Integration.
        """
        path = f"/integrations/{quote(str(integration_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, integration_token: str, body: UpdateIntegration) -> Integration:
        """
        Update integration
        
        Update an Integration.
        """
        path = f"/integrations/{quote(str(integration_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, integration_token: str) -> Any:
        """
        Delete integration
        
        Delete an Integration.
        """
        path = f"/integrations/{quote(str(integration_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)

    async def create_custom_provider(self, body: CreateCustomProviderIntegration) -> Integration:
        """
        Create custom provider integration
        
        Create a Custom Provider Integration
        """
        path = "/integrations/custom_provider"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def create_user_costs_upload_via_csv(self, integration_token: str, body: dict[str, Any]) -> UserCostsUpload:
        """
        Upload custom provider costs
        
        Create UserCostsUpload via CSV for a Custom Provider Integration.
        """
        path = f"/integrations/{quote(str(integration_token), safe='')}/costs.csv"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def delete_user_costs_upload(self, integration_token: str, user_costs_upload_token: int) -> Any:
        """
        Delete user costs upload
        
        Delete a UserCostsUpload.
        """
        path = f"/integrations/{quote(str(integration_token), safe='')}/costs/{quote(str(user_costs_upload_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)

    async def get_user_costs_uploads(self, integration_token: str) -> UserCostsUploads:
        """
        Get all user costs uploads
        
        List UserCostUploads.
        """
        path = f"/integrations/{quote(str(integration_token), safe='')}/costs"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create_gcp(self, body: CreateGcpIntegration) -> Integration:
        """
        Create GCP integration
        
        Create a GCP Integration
        """
        path = "/integrations/gcp"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def create_azure(self, body: CreateAzureIntegration) -> Integration:
        """
        Create Azure integration
        
        Create an Azure Integration
        """
        path = "/integrations/azure"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)


class InvoicesAsyncApi:
    """Async API methods for invoices resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None, managed_account_token: Optional[str] = None) -> Invoices:
        """
        Get all invoices
        
        Returns a list of invoices (MSP invoicing required).
        """
        path = "/invoices"
        params = {
            "page": page,
            "limit": limit,
            "managed_account_token": managed_account_token,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateInvoice) -> Invoice:
        """
        Create invoice
        
        Create an invoice (MSP accounts only).
        """
        path = "/invoices"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, invoice_token: str) -> Invoice:
        """
        Get invoice by token
        
        Return an invoice.
        """
        path = f"/invoices/{quote(str(invoice_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def download(self, invoice_token: str, body: DownloadInvoice) -> Any:
        """
        Get invoice file
        
        Download invoice file (PDF or CSV).
        """
        path = f"/invoices/{quote(str(invoice_token), safe='')}/download"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def send(self, invoice_token: str) -> SendInvoice:
        """
        Send invoice
        
        Send invoice via email.
        """
        path = f"/invoices/{quote(str(invoice_token), safe='')}/send"
        params = None
        body_data = None
        return await self._client.request("POST", path, params=params, body=body_data)

    async def send_and_approve(self, invoice_token: str) -> SendInvoice:
        """
        Send and approve invoice
        
        Send and approve invoice via email (MSP accounts only).
        """
        path = f"/invoices/{quote(str(invoice_token), safe='')}/send_and_approve"
        params = None
        body_data = None
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get_cost_report(self, invoice_token: str) -> CostReportUrl:
        """
        Get cost report URL
        
        Get cost report URL for invoice period.
        """
        path = f"/invoices/{quote(str(invoice_token), safe='')}/cost_report"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def regenerate(self, invoice_token: str) -> Invoice:
        """
        Regenerate invoice
        
        Regenerate an existing invoice (MSP accounts only).
        """
        path = f"/invoices/{quote(str(invoice_token), safe='')}/regenerate"
        params = None
        body_data = None
        return await self._client.request("POST", path, params=params, body=body_data)


class KubernetesEfficiencyReportsAsyncApi:
    """Async API methods for kubernetes_efficiency_reports resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> KubernetesEfficiencyReports:
        """
        Get all Kubernetes efficiency reports
        
        Return all KubernetesEfficiencyReports.
        """
        path = "/kubernetes_efficiency_reports"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateKubernetesEfficiencyReport) -> KubernetesEfficiencyReport:
        """
        Create Kubernetes efficiency report
        
        Create a KubernetesEfficiencyReport.
        """
        path = "/kubernetes_efficiency_reports"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def create_export(self, body: CreateKubernetesEfficiencyReportExport, *, groupings: Optional[List[str]] = None) -> DataExport:
        """
        Generate Kubernetes efficiency data export
        
        Generate a DataExport of Kubernetes efficiency data.
        """
        path = "/kubernetes_efficiency_reports/data_exports"
        params = {
            "groupings": groupings,
        }
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, kubernetes_efficiency_report_token: str) -> KubernetesEfficiencyReport:
        """
        Get Kubernetes efficiency report by token
        
        Return a KubernetesEfficiencyReport.
        """
        path = f"/kubernetes_efficiency_reports/{quote(str(kubernetes_efficiency_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, kubernetes_efficiency_report_token: str, body: UpdateKubernetesEfficiencyReport) -> KubernetesEfficiencyReport:
        """
        Update Kubernetes efficiency report
        
        Update a KubernetesEfficiencyReport.
        """
        path = f"/kubernetes_efficiency_reports/{quote(str(kubernetes_efficiency_report_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, kubernetes_efficiency_report_token: str) -> Any:
        """
        Delete Kubernetes efficiency report
        
        Delete a KubernetesEfficiencyReport.
        """
        path = f"/kubernetes_efficiency_reports/{quote(str(kubernetes_efficiency_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class ManagedAccountsAsyncApi:
    """Async API methods for managed_accounts resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> ManagedAccounts:
        """
        Get all managed accounts
        
        Returns a list of managed accounts.
        """
        path = "/managed_accounts"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateManagedAccount) -> ManagedAccount:
        """
        Create managed account
        
        Create a Managed Account.
        """
        path = "/managed_accounts"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, managed_account_token: str) -> ManagedAccount:
        """
        Get managed account by token
        
        Return a Managed Account.
        """
        path = f"/managed_accounts/{quote(str(managed_account_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, managed_account_token: str, body: UpdateManagedAccount) -> ManagedAccount:
        """
        Update managed account
        
        Update a Managed Account.
        """
        path = f"/managed_accounts/{quote(str(managed_account_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, managed_account_token: str) -> Any:
        """
        Delete managed account
        
        Delete a Managed Account.
        """
        path = f"/managed_accounts/{quote(str(managed_account_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)

    async def update_sso_connection_for(self, managed_account_token: str, body: UpdateSsoConnectionForManagedAccount) -> ManagedAccount:
        """
        Update SSO configuration for managed account
        
        Update SSO configuration for a Managed Account.
        """
        path = f"/managed_accounts/{quote(str(managed_account_token), safe='')}/sso_connection"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def create_sso_connection_for(self, managed_account_token: str, body: CreateSsoConnectionForManagedAccount) -> ManagedAccount:
        """
        Configure SSO for managed account
        
        Configure SSO for a Managed Account.
        """
        path = f"/managed_accounts/{quote(str(managed_account_token), safe='')}/sso_connection"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)


class MeAsyncApi:
    """Async API methods for me resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def get(self) -> Me:
        """
        Get authenticated user info
        
        Get information about the authenticated BearerToken.
        """
        path = "/me"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class NetworkFlowReportsAsyncApi:
    """Async API methods for network_flow_reports resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> NetworkFlowReports:
        """
        Get all network flow reports
        
        Return all NetworkFlowReports.
        """
        path = "/network_flow_reports"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateNetworkFlowReport) -> NetworkFlowReport:
        """
        Create network flow report
        
        Create a NetworkFlowReport.
        """
        path = "/network_flow_reports"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, network_flow_report_token: str) -> NetworkFlowReport:
        """
        Get network flow report by token
        
        Return a NetworkFlowReport.
        """
        path = f"/network_flow_reports/{quote(str(network_flow_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, network_flow_report_token: str, body: UpdateNetworkFlowReport) -> NetworkFlowReport:
        """
        Update network flow report
        
        Update a NetworkFlowReport.
        """
        path = f"/network_flow_reports/{quote(str(network_flow_report_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, network_flow_report_token: str) -> Any:
        """
        Delete network flow report
        
        Delete a NetworkFlowReport.
        """
        path = f"/network_flow_reports/{quote(str(network_flow_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class PingAsyncApi:
    """Async API methods for ping resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def ping(self) -> Any:
        """This is a health check endpoint that can be used to determine Vantage API healthiness. It will return 200 if everything is running smoothly."""
        path = "/ping"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class ProductsAsyncApi:
    """Async API methods for products resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def get_prices(self, product_id: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> Prices:
        """
        Get prices for a product
        
        Return available Prices across all Regions for a Product.
        """
        path = f"/products/{quote(str(product_id), safe='')}/prices"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get_price(self, product_id: str, id: str) -> Price:
        """
        Get price by ID
        
        Returns a price
        """
        path = f"/products/{quote(str(product_id), safe='')}/prices/{quote(str(id), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def list(self, *, provider_id: Optional[str] = None, service_id: Optional[str] = None, name: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Products:
        """
        Get all products
        
        Return available Products for a Service. For example, with a Provider of AWS and a Service of EC2, Products will be a list of all EC2 Instances. By default, this endpoint returns all Products across all Services and Providers but has optional query parameters for filtering listed below.
        """
        path = "/products"
        params = {
            "provider_id": provider_id,
            "service_id": service_id,
            "name": name,
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get(self, id: str) -> Product:
        """
        Get product by ID
        
        Return a product
        """
        path = f"/products/{quote(str(id), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class RecommendationViewsAsyncApi:
    """Async API methods for recommendation_views resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> RecommendationViews:
        """
        Get all recommendation views
        
        Return all RecommendationViews.
        """
        path = "/recommendation_views"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateRecommendationView) -> RecommendationView:
        """
        Create recommendation view
        
        Create a RecommendationView.
        """
        path = "/recommendation_views"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, recommendation_view_token: str) -> RecommendationView:
        """
        Get recommendation view by token
        
        Return a specific RecommendationView.
        """
        path = f"/recommendation_views/{quote(str(recommendation_view_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, recommendation_view_token: str, body: UpdateRecommendationView) -> RecommendationView:
        """
        Update recommendation view
        
        Update a RecommendationView.
        """
        path = f"/recommendation_views/{quote(str(recommendation_view_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, recommendation_view_token: str) -> Any:
        """
        Delete recommendation view
        
        Delete a RecommendationView.
        """
        path = f"/recommendation_views/{quote(str(recommendation_view_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class RecommendationsAsyncApi:
    """Async API methods for recommendations resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, provider_ids: Optional[List[str]] = None, billing_account_ids: Optional[List[str]] = None, account_ids: Optional[List[str]] = None, regions: Optional[List[str]] = None, tag_key: Optional[str] = None, tag_value: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None, status: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, workspace_token: Optional[str] = None, provider_account_id: Optional[str] = None, category: Optional[str] = None, type: Optional[str] = None, provider: Optional[str] = None) -> Recommendations:
        """
        Get all recommendations
        
        Return all Recommendations. Use the `type` query parameter with a fuzzy fragment to filter recommendation type case-insensitively (for example: aws, aws:ec2, aws:ec2:rightsizing).
        """
        path = "/recommendations"
        params = {
            "provider_ids": provider_ids,
            "billing_account_ids": billing_account_ids,
            "account_ids": account_ids,
            "regions": regions,
            "tag_key": tag_key,
            "tag_value": tag_value,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "page": page,
            "limit": limit,
            "workspace_token": workspace_token,
            "provider_account_id": provider_account_id,
            "category": category,
            "type": type,
            "provider": provider,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get(self, recommendation_token: str) -> Recommendation:
        """
        Get recommendation by token
        
        Return a Recommendation.
        """
        path = f"/recommendations/{quote(str(recommendation_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get_resources(self, recommendation_token: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> RecommendationProviderResources:
        """
        Get all resources for a recommendation
        
        Return all Active Resources, including Recommendation Actions, referenced in this Recommendation.
        """
        path = f"/recommendations/{quote(str(recommendation_token), safe='')}/resources"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get_resource(self, recommendation_token: str, resource_token: str) -> ProviderResource:
        """
        Get specific resource for a recommendation
        
        Return an Active Resource, including Recommendation Actions, referenced in this Recommendation.
        """
        path = f"/recommendations/{quote(str(recommendation_token), safe='')}/resources/{quote(str(resource_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get_type_resources(self, type: str, *, provider_ids: Optional[List[str]] = None, billing_account_ids: Optional[List[str]] = None, account_ids: Optional[List[str]] = None, regions: Optional[List[str]] = None, tag_key: Optional[str] = None, tag_value: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None, status: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, workspace_token: str) -> RecommendationProviderResources:
        """
        Get all resources for a recommendation type
        
        Return all Active Resources associated with recommendations of the specified type.
        """
        path = f"/recommendations/by_type/{quote(str(type), safe='')}/resources"
        params = {
            "provider_ids": provider_ids,
            "billing_account_ids": billing_account_ids,
            "account_ids": account_ids,
            "regions": regions,
            "tag_key": tag_key,
            "tag_value": tag_value,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "page": page,
            "limit": limit,
            "workspace_token": workspace_token,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class ReportNotificationsAsyncApi:
    """Async API methods for report_notifications resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> ReportNotifications:
        """
        Get all report notifications
        
        Return all ReportNotifications.
        """
        path = "/report_notifications"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateReportNotification) -> ReportNotification:
        """
        Create report notification
        
        Create a ReportNotification.
        """
        path = "/report_notifications"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, report_notification_token: str) -> ReportNotification:
        """
        Get report notification by token
        
        Return a ReportNotification.
        """
        path = f"/report_notifications/{quote(str(report_notification_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, report_notification_token: str, body: UpdateReportNotification) -> ReportNotification:
        """
        Update report notification
        
        Update a ReportNotification.
        """
        path = f"/report_notifications/{quote(str(report_notification_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, report_notification_token: str) -> Any:
        """
        Delete report notification
        
        Delete a ReportNotification.
        """
        path = f"/report_notifications/{quote(str(report_notification_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class ResourceReportsAsyncApi:
    """Async API methods for resource_reports resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def get_columns(self, *, resource_type: str) -> ResourceReportColumns:
        """
        Get resource report columns
        
        List available columns for a resource type.
        """
        path = "/resource_reports/columns"
        params = {
            "resource_type": resource_type,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> ResourceReports:
        """
        Get all resource reports
        
        Return all ResourceReports.
        """
        path = "/resource_reports"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateResourceReport) -> ResourceReport:
        """
        Create resource report
        
        Create a ResourceReport.
        """
        path = "/resource_reports"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, resource_report_token: str) -> ResourceReport:
        """
        Get resource report by token
        
        Return a ResourceReport.
        """
        path = f"/resource_reports/{quote(str(resource_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, resource_report_token: str, body: UpdateResourceReport) -> ResourceReport:
        """
        Update resource report
        
        Update a ResourceReport.
        """
        path = f"/resource_reports/{quote(str(resource_report_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, resource_report_token: str) -> Any:
        """
        Delete resource report
        
        Delete a ResourceReport.
        """
        path = f"/resource_reports/{quote(str(resource_report_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class ResourcesAsyncApi:
    """Async API methods for resources resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def get_report(self, *, resource_report_token: Optional[str] = None, filter: Optional[str] = None, workspace_token: Optional[str] = None, include_cost: Optional[bool] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Resources:
        """
        Get resources
        
        Return Resources contained in a ResourceReport
        """
        path = "/resources"
        params = {
            "resource_report_token": resource_report_token,
            "filter": filter,
            "workspace_token": workspace_token,
            "include_cost": include_cost,
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get(self, resource_token: str, *, include_cost: Optional[bool] = None) -> Resource:
        """
        Get resource by token
        
        Return a single Resource
        """
        path = f"/resources/{quote(str(resource_token), safe='')}"
        params = {
            "include_cost": include_cost,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class SavedFiltersAsyncApi:
    """Async API methods for saved_filters resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> SavedFilters:
        """
        Get all saved filters
        
        Return all SavedFilters that can be applied to a CostReport.
        """
        path = "/saved_filters"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateSavedFilter) -> SavedFilter:
        """
        Create saved filter
        
        Create a SavedFilter for CostReports.
        """
        path = "/saved_filters"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, saved_filter_token: str) -> SavedFilter:
        """
        Get saved filter by token
        
        Return a specific SavedFilter.
        """
        path = f"/saved_filters/{quote(str(saved_filter_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, saved_filter_token: str, body: UpdateSavedFilter) -> SavedFilter:
        """
        Update saved filter
        
        Update a SavedFilter for CostReports.
        """
        path = f"/saved_filters/{quote(str(saved_filter_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, saved_filter_token: str) -> Any:
        """
        Delete saved filter
        
        Delete a SavedFilter for CostReports.
        """
        path = f"/saved_filters/{quote(str(saved_filter_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class SegmentsAsyncApi:
    """Async API methods for segments resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> Segments:
        """
        Get all segments
        
        Return all Segments.
        """
        path = "/segments"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateSegment) -> Segment:
        """
        Create segment
        
        Create a Segment.
        """
        path = "/segments"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, segment_token: str) -> Segment:
        """
        Get segment by token
        
        Return a Segment.
        """
        path = f"/segments/{quote(str(segment_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, segment_token: str, body: UpdateSegment) -> Segment:
        """
        Update segment
        
        Update a Segment.
        """
        path = f"/segments/{quote(str(segment_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, segment_token: str) -> Any:
        """
        Delete segment
        
        Delete a Segment.
        """
        path = f"/segments/{quote(str(segment_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class TagsAsyncApi:
    """Async API methods for tags resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, providers: Optional[List[str]] = None, search_query: Optional[str] = None, sort_direction: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Tags:
        """
        Get all tags
        
        Return all Tags that the current API token has access to.
        """
        path = "/tags"
        params = {
            "providers": providers,
            "search_query": search_query,
            "sort_direction": sort_direction,
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, body: UpdateTag) -> Tags:
        """
        Update tag
        
        Updates an existing Tag.
        """
        path = "/tags"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def get_values(self, key: str, *, providers: Optional[List[str]] = None, sort_direction: Optional[str] = None, search_query: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> TagValues:
        """
        Get tag values
        
        Returns corresponding TagValues for a given Tag.
        """
        path = f"/tags/{quote(str(key), safe='')}/values"
        params = {
            "providers": providers,
            "sort_direction": sort_direction,
            "search_query": search_query,
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class TeamsAsyncApi:
    """Async API methods for teams resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> Teams:
        """
        Get all teams
        
        Return all Teams that the current API token has access to.
        """
        path = "/teams"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateTeam) -> Team:
        """
        Create team
        
        Create a new Team.
        """
        path = "/teams"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, team_token: str) -> Team:
        """
        Get team by token
        
        Return a specific Team.
        """
        path = f"/teams/{quote(str(team_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, team_token: str, body: UpdateTeam) -> Team:
        """
        Update team
        
        Update a Team.
        """
        path = f"/teams/{quote(str(team_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, team_token: str) -> Any:
        """
        Delete team
        
        Delete a Team.
        """
        path = f"/teams/{quote(str(team_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)

    async def get_members(self, team_token: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> TeamMembers:
        """
        Get team members
        
        Return all members of a Team.
        """
        path = f"/teams/{quote(str(team_token), safe='')}/members"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def add_member(self, team_token: str, body: AddTeamMember) -> TeamMember:
        """
        Add team member
        
        Add a member to a Team.
        """
        path = f"/teams/{quote(str(team_token), safe='')}/members"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def remove_member(self, team_token: str, user_token: str) -> Any:
        """
        Remove team member
        
        Remove a member from a Team.
        """
        path = f"/teams/{quote(str(team_token), safe='')}/members/{quote(str(user_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)


class UnitCostsAsyncApi:
    """Async API methods for unit_costs resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def create_export(self, body: CreateUnitCostsExport) -> DataExport:
        """
        Generate data export of unit costs
        
        Generate a DataExport of unit costs.
        """
        path = "/unit_costs/data_exports"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def list(self, *, cost_report_token: str, start_date: Optional[str] = None, end_date: Optional[str] = None, date_bin: Optional[str] = None, order: Optional[str] = None, limit: Optional[int] = None, page: Optional[int] = None) -> UnitCosts:
        """
        Get all unit costs for a cost report
        
        Return all UnitCosts for a CostReport.
        """
        path = "/unit_costs"
        params = {
            "cost_report_token": cost_report_token,
            "start_date": start_date,
            "end_date": end_date,
            "date_bin": date_bin,
            "order": order,
            "limit": limit,
            "page": page,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class UserFeedbackAsyncApi:
    """Async API methods for user_feedback resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def create(self, body: CreateUserFeedback) -> UserFeedback:
        """
        Submit user feedback
        
        Provide UserFeedback for our product and features.
        """
        path = "/user_feedback"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)


class UsersAsyncApi:
    """Async API methods for users resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> Users:
        """
        Get all users
        
        Return all Users that the current API token has access to.
        """
        path = "/users"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def get(self, user_token: str) -> User:
        """
        Get user by token
        
        Return a specific User.
        """
        path = f"/users/{quote(str(user_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class VirtualTagConfigsAsyncApi:
    """Async API methods for virtual_tag_configs resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self) -> VirtualTagConfigs:
        """
        Get all virtual tag configs
        
        Return all VirtualTagConfigs that the current API token has access to.
        """
        path = "/virtual_tag_configs"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateVirtualTagConfig) -> VirtualTagConfig:
        """
        Create virtual tag config
        
        Create a new VirtualTagConfig.
        """
        path = "/virtual_tag_configs"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, token: str) -> VirtualTagConfig:
        """
        Get virtual tag config by token
        
        Return a specific VirtualTagConfig.
        """
        path = f"/virtual_tag_configs/{quote(str(token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, token: str, body: UpdateVirtualTagConfig) -> VirtualTagConfig:
        """
        Update virtual tag config
        
        Updates an existing VirtualTagConfig.
        """
        path = f"/virtual_tag_configs/{quote(str(token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def delete(self, token: str) -> Any:
        """
        Delete virtual tag config
        
        Deletes an existing VirtualTagConfig.
        """
        path = f"/virtual_tag_configs/{quote(str(token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("DELETE", path, params=params, body=body_data)

    async def get_status(self, token: str) -> VirtualTagConfigStatus:
        """
        Get virtual tag config processing status
        
        Return the processing status of a specific VirtualTagConfig.
        """
        path = f"/virtual_tag_configs/{quote(str(token), safe='')}/status"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update_async(self, token: str, body: UpdateAsyncVirtualTagConfig) -> Any:
        """
        Update virtual tag config asynchronously
        
        Asynchronously updates an existing VirtualTagConfig.
        """
        path = f"/virtual_tag_configs/{quote(str(token), safe='')}/async"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

    async def get_async_virtual_tag_config_status(self, request_id: str) -> Any:
        """
        Get async virtual tag config update status
        
        Check the status of an async VirtualTagConfig update.
        """
        path = f"/virtual_tag_configs/async/{quote(str(request_id), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)


class WorkspacesAsyncApi:
    """Async API methods for workspaces resource."""

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def list(self, *, page: Optional[int] = None, limit: Optional[int] = None) -> Workspaces:
        """
        Get all workspaces
        
        Return all Workspaces that the current API token has access to.
        """
        path = "/workspaces"
        params = {
            "page": page,
            "limit": limit,
        }
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def create(self, body: CreateWorkspace) -> Workspace:
        """
        Create workspace
        
        Create a workspace
        """
        path = "/workspaces"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("POST", path, params=params, body=body_data)

    async def get(self, workspace_token: str) -> Workspace:
        """
        Get workspace by token
        
        Return a specific Workspace.
        """
        path = f"/workspaces/{quote(str(workspace_token), safe='')}"
        params = None
        body_data = None
        return await self._client.request("GET", path, params=params, body=body_data)

    async def update(self, workspace_token: str, body: UpdateWorkspace) -> Workspace:
        """
        Update workspace
        
        Update a workspace
        """
        path = f"/workspaces/{quote(str(workspace_token), safe='')}"
        params = None
        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body
        return await self._client.request("PUT", path, params=params, body=body_data)

