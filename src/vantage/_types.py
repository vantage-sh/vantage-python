"""Auto-generated Pydantic models from OpenAPI schema."""

from __future__ import annotations

from typing import Any, Optional, List, Dict

from pydantic import BaseModel, Field


class AccessGrants(BaseModel):
    """AccessGrants model"""

    links: Optional[Links] = Field(default=None)
    access_grants: List[AccessGrant]


class Links(BaseModel):
    self: Optional[str] = Field(default=None, description="The URL of the current page of results.")
    first: Optional[str] = Field(default=None, description="The URL of the first page of results.")
    next: Optional[str] = Field(default=None, description="The URL of the next page of results, if one exists.")
    last: Optional[str] = Field(default=None, description="The URL of the last page of results, if one exists.")
    prev: Optional[str] = Field(default=None, description="The URL of the previous page of results, if one exists.")


class AccessGrant(BaseModel):
    """AccessGrant model"""

    token: str
    resource_token: str = Field(description="The token for any resource the AccessGrant is applied to.")
    access: str = Field(description="The access status of the AccessGrant.")
    team_token: Optional[str] = Field(description="The Team token for which an AccessGrant is applied to.")
    created_at: str = Field(description="The date and time, in UTC, the AccessGrant was created. ISO 8601 Formatted.")
    created_by: Optional[str] = Field(description="The token for the User who created the AccessGrant.")


class Errors(BaseModel):
    """Errors model"""

    links: Optional[Links] = Field(default=None)
    errors: List[str]


class CreateAccessGrant(BaseModel):
    """Create an Access Grant."""

    resource_token: str = Field(description="The token of the resource for which you are granting access.")
    team_token: str = Field(description="The token of the Team you want to grant access to.")
    access: Optional[str] = Field(default=None, description="The access level you want to grant. Defaults to 'allowed'.")


class UpdateAccessGrant(BaseModel):
    """Update an AccessGrant."""

    access: str = Field(description="Allowed or denied access to resource.")


class AnomalyAlerts(BaseModel):
    """AnomalyAlerts model"""

    links: Optional[Links] = Field(default=None)
    anomaly_alerts: List[AnomalyAlert]


class AnomalyAlert(BaseModel):
    """AnomalyAlert model"""

    token: str
    created_at: str = Field(description="The date and time, in UTC, the AnomalyAlert was created. ISO 8601 Formatted.")
    alerted_at: Optional[str] = Field(default=None, description="The date and time, in UTC, the AnomalyAlert is sent. ISO 8601 Formatted.")
    category: Optional[str] = Field(description="The category of the AnomalyAlert.")
    service: str = Field(description="The provider service causing the AnomalyAlert.")
    provider: str = Field(description="The provider of the service causing the AnomalyAlert.")
    amount: str = Field(description="The amount observed.")
    previous_amount: str = Field(description="The previous amount observed.")
    seven_day_average: str = Field(description="The seven day average of the amount observed.")
    status: str = Field(description="The status of the AnomalyAlert.")
    feedback: Optional[str] = Field(default=None, description="The user-provided feedback of why alert was ignored/archived.")
    resources: List[str] = Field(description="The names of the resources the AnomalyAlert was attributed to.")
    resource_tokens: List[str] = Field(description="The tokens of the Resources the AnomalyAlert was attributed to.")
    cost_report_token: str = Field(description="The token of the Report associated with the AnomalyAlert.")


class UpdateAnomalyAlert(BaseModel):
    """Update an AnomalyAlert."""

    status: str = Field(description="The status of the Anomaly Alert.")
    feedback: Optional[str] = Field(default=None, description="Optional additional comments for why this alert is ignored.")


class AnomalyNotifications(BaseModel):
    """AnomalyNotifications model"""

    links: Optional[Links] = Field(default=None)
    anomaly_notifications: List[AnomalyNotification]


class AnomalyNotification(BaseModel):
    """AnomalyNotification model"""

    token: str
    cost_report_token: str = Field(description="The token for the CostReport the AnomalyNotification is associated with.")
    created_at: str = Field(description="The date and time, in UTC, the AnomalyNotification was created. ISO 8601 Formatted.")
    updated_at: str = Field(description="The date and time, in UTC, the AnomalyNotification was last updated at. ISO 8601 Formatted.")
    threshold: int = Field(description="The threshold amount that must be met for the notification to fire.")
    user_tokens: List[str] = Field(description="The tokens of the users that receive the notification.")
    recipient_channels: List[str] = Field(description="The channels that the notification is sent to.")


class CreateAnomalyNotification(BaseModel):
    """Create an Anomaly Notification for a Cost Report."""

    cost_report_token: str = Field(description="The token of the Cost Report that has the notification.")
    threshold: Optional[int] = Field(default=None, description="The threshold amount that must be met for the notification to fire.")
    user_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the Users that receive the notification.")
    recipient_channels: Optional[List[str]] = Field(default=None, description="The Slack/MS Teams channels that receive the notification.")


class UpdateAnomalyNotification(BaseModel):
    """Update an Anomaly Notification."""

    threshold: Optional[int] = Field(default=None, description="The threshold amount that must be met for the notification to fire.")
    user_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the users that receive the notification.")
    recipient_channels: Optional[List[str]] = Field(default=None, description="The Slack/MS Teams channels that receive the notification.")


class AuditLogs(BaseModel):
    """AuditLogs model"""

    links: Optional[Links] = Field(default=None)
    audit_logs: List[AuditLog]


class AuditLog(BaseModel):
    """AuditLog model"""

    token: str = Field(description="The unique token identifying the audit log.")
    object_token: Optional[str] = Field(description="The token of the audited object.")
    object_type: str = Field(description="The type of the audited object.")
    object_title: Optional[str] = Field(description="The title of the audited object.")
    event: str = Field(description="The event type of the audit log.")
    source: str = Field(description="The source of the action (console, api, developer).")
    user: Optional[str] = Field(default=None, description="The name of the user who performed the action.")
    workspace_title: Optional[str] = Field(default=None, description="The name of the workspace associated with the audit log.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the workspace associated with the audit log.")
    created_at: str = Field(description="The date and time, in UTC, the audit log was created. ISO 8601 Formatted.")
    changed_values: Dict[str, Any] = Field(description="The changed values of the object.")
    unchanged_values: Dict[str, Any] = Field(description="The unchanged values of the object.")


class BillingProfiles(BaseModel):
    """BillingProfiles model"""

    links: Optional[Links] = Field(default=None)
    billing_profiles: List[BillingProfile]


class BillingProfile(BaseModel):
    """BillingProfile model"""

    token: str
    nickname: str = Field(description="Display name for the billing profile")
    created_at: str = Field(description="The date and time, in UTC, the billing profile was created. ISO 8601 formatted.")
    updated_at: str = Field(description="The date and time, in UTC, the billing profile was last updated. ISO 8601 formatted.")
    billing_information_attributes: BillingInformation
    business_information_attributes: BusinessInformation
    banking_information_attributes: Optional[BankingInformation] = Field(default=None)
    invoice_adjustment_attributes: InvoiceAdjustment
    managed_accounts_count: str = Field(description="Number of managed accounts using this billing profile")


class BillingInformation(BaseModel):
    token: str
    company_name: Optional[str] = Field(description="Company name for billing")
    country_code: Optional[str] = Field(description="ISO country code")
    address_line_1: Optional[str] = Field(description="First line of billing address")
    address_line_2: Optional[str] = Field(description="Second line of billing address")
    city: Optional[str] = Field(description="City for billing address")
    state: Optional[str] = Field(description="State or province for billing address")
    postal_code: Optional[str] = Field(description="Postal or ZIP code")
    billing_email: Optional[List[str]] = Field(description="Array of billing email addresses")


class BusinessInformation(BaseModel):
    token: str
    metadata: Optional[BusinessInformationMetadata] = Field(default=None)


class BusinessInformationMetadata(BaseModel):
    custom_fields: Optional[List[BusinessInformationCustomField]] = Field(default=None, description="Array of custom field objects")


class BusinessInformationCustomField(BaseModel):
    name: str = Field(description="Custom field name")
    value: Optional[str] = Field(description="Custom field value")


class BankingInformation(BaseModel):
    token: str
    bank_name: Optional[str] = Field(description="Name of the bank")
    beneficiary_name: Optional[str] = Field(description="Name of the account beneficiary")
    tax_id: Optional[str] = Field(description="Tax identification number")
    secure_data: Optional[BankingInformationSecureData] = Field(default=None)


class BankingInformationSecureData(BaseModel):
    account_number: Optional[str] = Field(description="Bank account number (US)")
    routing_number: Optional[str] = Field(description="Bank routing number (US)")
    iban: Optional[str] = Field(description="International Bank Account Number (EU)")
    swift_bic: Optional[str] = Field(description="SWIFT/BIC code (EU)")


class InvoiceAdjustment(BaseModel):
    token: str
    adjustment_items: List[AdjustmentItem] = Field(description="Array of adjustment items (taxes, fees, etc.)")


class AdjustmentItem(BaseModel):
    name: str = Field(description="Name of the adjustment (e.g., 'State Tax', 'Processing Fee')")
    adjustment_type: str = Field(description="Type of adjustment")
    calculation_type: str = Field(description="How the adjustment is calculated")
    amount: str = Field(description="Amount or percentage value for the adjustment")


class CreateBillingProfile(BaseModel):
    """Create a billing profile (MSP invoicing required)."""

    nickname: str = Field(description="Display name for the billing profile")
    billing_information_attributes: Optional[BillingInformation] = Field(default=None, description="Billing address and contact information")
    business_information_attributes: Optional[BusinessInformation] = Field(default=None, description="Business information and custom fields")
    banking_information_attributes: Optional[BankingInformation] = Field(default=None, description="Banking details (MSP accounts only)")
    invoice_adjustment_attributes: Optional[InvoiceAdjustment] = Field(default=None, description="Invoice adjustments (taxes, fees, etc.)")


class UpdateBillingProfile(BaseModel):
    """Update a billing profile (MSP invoicing required)."""

    nickname: Optional[str] = Field(default=None, description="Display name for the billing profile")
    billing_information_attributes: Optional[BillingInformation] = Field(default=None, description="Billing address and contact information")
    business_information_attributes: Optional[BusinessInformation] = Field(default=None, description="Business information and custom fields")
    banking_information_attributes: Optional[BankingInformation] = Field(default=None, description="Banking details (MSP accounts only)")
    invoice_adjustment_attributes: Optional[InvoiceAdjustment] = Field(default=None, description="Invoice adjustments (taxes, fees, etc.)")


class BillingRules(BaseModel):
    """BillingRules model"""

    links: Optional[Links] = Field(default=None)
    billing_rules: List[BillingRule]


class BillingRule(BaseModel):
    """BillingRule model"""

    token: str
    title: str = Field(description="The title of the BillingRule.")
    type: str = Field(description="The type of the BillingRule.")
    start_date: Optional[str] = Field(default=None, description="The start date of the BillingRule.")
    end_date: Optional[str] = Field(default=None, description="The end date of the BillingRule.")
    apply_to_all: Optional[bool] = Field(description="Whether the BillingRule applies to all future managed accounts.")
    created_by_token: str = Field(description="The token of the Creator of the BillingRule.")
    created_at: str = Field(description="The date and time, in UTC, the BillingRule was created. ISO 8601 Formatted.")
    service: Optional[str] = Field(default=None, description="The service for the BillingRule (Charge).")
    category: Optional[str] = Field(default=None, description="The category for the BillingRule (Charge).")
    percentage: Optional[str] = Field(default=None, description="The percentage of the cost shown for the BillingRule (Adjustment).")
    charge_type: Optional[str] = Field(default=None, description="The charge type for the BillingRule.")
    sub_category: Optional[str] = Field(default=None, description="The subcategory for the BillingRule (Charge).")
    start_period: Optional[str] = Field(default=None, description="The start period for the BillingRule (Charge).")
    amount: Optional[str] = Field(default=None, description="The amount for the BillingRule (Charge).")
    sql_query: Optional[str] = Field(default=None, description="The SQL query for the BillingRule (Custom).")


class CreateBillingRule(BaseModel):
    """Create a BillingRule."""

    type: str = Field(description="The type of the BillingRule. Note: the values are case insensitive.")
    title: str = Field(description="The title of the BillingRule.")
    start_period: Optional[str] = Field(default=None, description="The start period of the BillingRule. DEPRECATED: use start_date instead.")
    start_date: Optional[str] = Field(default=None, description="The start date of the BillingRule. ISO 8601 formatted.")
    end_date: Optional[str] = Field(default=None, description="The end date of the BillingRule. ISO 8601 formatted.")
    apply_to_all: Optional[bool] = Field(default=None, description="Determines if the BillingRule applies to all current and future managed accounts.")
    charge_type: Optional[str] = Field(default=None, description="The charge type of the BillingRule. Required for Exclusion rules.")
    percentage: Optional[float] = Field(default=None, description="The percentage of the cost shown. Required for Adjustment rules. Example value: 75.0")
    service: Optional[str] = Field(default=None, description="The service of the BillingRule. Required for Charge and Credit rules.")
    category: Optional[str] = Field(default=None, description="The category of the BillingRule. Required for Charge and Credit rules.")
    sub_category: Optional[str] = Field(default=None, description="The subcategory of the BillingRule. Required for Charge and Credit rules.")
    amount: Optional[float] = Field(default=None, description="The amount for the BillingRule. Required for Charge and Credit rules. Example value: 300")
    sql_query: Optional[str] = Field(default=None, description="The SQL query for the BillingRule. Required for Custom rules. Example value: UPDATE costs SET costs.amount = costs.amount * 0.95")


class UpdateBillingRule(BaseModel):
    """Update a BillingRule."""

    title: Optional[str] = Field(default=None, description="The title of the BillingRule.")
    charge_type: Optional[str] = Field(default=None, description="The charge type of the BillingRule.")
    percentage: Optional[float] = Field(default=None, description="The percentage of the cost shown. Example value: 75.0")
    service: Optional[str] = Field(default=None, description="The service of the BillingRule.")
    category: Optional[str] = Field(default=None, description="The category of the BillingRule.")
    sub_category: Optional[str] = Field(default=None, description="The subcategory of the BillingRule.")
    start_period: Optional[str] = Field(default=None, description="The start period of the BillingRule.")
    amount: Optional[float] = Field(default=None, description="The credit amount for the BillingRule. Example value: 300")
    start_date: Optional[str] = Field(default=None, description="The start date of the BillingRule. ISO 8601 formatted.")
    end_date: Optional[str] = Field(default=None, description="The end date of the BillingRule. ISO 8601 formatted.")
    apply_to_all: Optional[bool] = Field(default=None, description="Determines if the BillingRule applies to all current and future managed accounts.")
    sql_query: Optional[str] = Field(default=None, description="The SQL query of the BillingRule.")


class BudgetAlerts(BaseModel):
    """BudgetAlerts model"""

    links: Optional[Links] = Field(default=None)
    budget_alerts: List[BudgetAlert]


class BudgetAlert(BaseModel):
    """BudgetAlert model"""

    token: str
    budget_tokens: List[str] = Field(description="The tokens for the Budgets that the Budget Alert is monitoring to trigger alerts on.")
    created_at: str = Field(description="The date and time, in UTC, the Budget Alert was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the ResourceReport is a part of.")
    user_token: Optional[str] = Field(default=None, description="The token for the User who created this BudgetAlert.")
    user_tokens: List[str] = Field(description="The Users that receive the alert.")
    duration_in_days: Optional[int] = Field(description="The number of days from the start or end of the month to trigger the alert if the threshold is reached.")
    threshold: int = Field(description="Alerts only send if they reach this number (as a percentage). When threshold is 100, that means alerts are triggered once costs reach 100% of the budget.")
    period_to_track: Optional[str] = Field(description="The period tracked on the alert. Used with duration_in_days to determine the time window of the alert. Possible values: start_of_the_month, end_of_the_month.")
    integration_provider: Optional[str] = Field(default=None, description="The provider used for sending alerts. This must be configured in the console. Possible values are: slack, microsoft_graph.")
    recipient_channels: Optional[List[str]] = Field(description="The channels receiving the alerts. Requires an integration provider to be connected.")


class CreateBudgetAlert(BaseModel):
    """Create a Budget Alert."""

    budget_tokens: List[str] = Field(description="The tokens of the Budget that has the alert.")
    threshold: int = Field(description="The threshold amount that must be met for the alert to fire.")
    user_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the users that receive the alert.")
    duration_in_days: str = Field(description="The number of days from the start or end of the month to trigger the alert if the threshold is reached.  For the full month, pass an empty value.")
    period_to_track: Optional[str] = Field(default=None, description="The period tracked on the alert. Used with duration_in_days to determine the time window of the alert. Defaults to start_of_the_month if not passed. Possible values: start_of_the_month, end_of_the_month.")
    recipient_channels: Optional[List[str]] = Field(default=None, description="The channels receiving the alerts. Requires an integration provider to be connected.")


class UpdateBudgetAlert(BaseModel):
    """Updates an existing BudgetAlert."""

    budget_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the Budget that has the alert.")
    threshold: Optional[int] = Field(default=None, description="The threshold amount that must be met for the alert to fire.")
    user_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the users that receive the alert.")
    duration_in_days: Optional[str] = Field(default=None, description="The number of days from the start or end of the month to trigger the alert if the threshold is reached. For the full month, pass an empty value.")
    period_to_track: Optional[str] = Field(default=None, description="The period tracked on the alert. Used with duration_in_days to determine the time window of the alert. Defaults to start_of_the_month if not passed. Possible values: start_of_the_month, end_of_the_month.")
    recipient_channels: Optional[List[str]] = Field(default=None, description="The channels receiving the alerts. Requires an integration provider to be connected.")


class Budgets(BaseModel):
    """Budgets model"""

    links: Optional[Links] = Field(default=None)
    budgets: List[Budget]


class Budget(BaseModel):
    """Budget model"""

    token: str
    name: Optional[str] = Field(description="The name of the Budget.")
    workspace_token: str = Field(description="The token for the Workspace the Budget is a part of.")
    user_token: Optional[str] = Field(default=None, description="The token for the User who created this Budget.")
    created_by_token: Optional[str] = Field(default=None, description="The token of the Creator of the Budget.")
    cost_report_token: Optional[str] = Field(default=None, description="The token of the Report associated with the Budget.")
    created_at: str = Field(description="The date and time, in UTC, the Budget was created. ISO 8601 Formatted.")
    budget_alert_tokens: List[str] = Field(description="The tokens of the BudgetAlerts associated with the Budget.")
    child_budget_tokens: List[str] = Field(description="The tokens of the child Budgets associated with the hierarchical Budget.")
    periods: List[BudgetPeriod] = Field(description="The budget periods associated with the Budget.")
    performance: Optional[List[BudgetPerformance]] = Field(default=None, description="The historical performance of the Budget.")


class BudgetPeriod(BaseModel):
    start_at: str = Field(description="The date and time, in UTC, the Budget was created. ISO 8601 Formatted.")
    end_at: str = Field(description="The date and time, in UTC, the Budget was created. ISO 8601 Formatted.")
    amount: str = Field(description="The amount of the Budget Period as a string to ensure precision.")


class BudgetPerformance(BaseModel):
    date: str = Field(description="The date and time, in UTC, the Budget was created. ISO 8601 Formatted.")
    actual: str = Field(description="The date and time, in UTC, the Budget was created. ISO 8601 Formatted.")
    amount: str = Field(description="The amount of the Budget Period as a string to ensure precision.")


class CreateBudget(BaseModel):
    """Create a Budget."""

    name: str = Field(description="The name of the Budget.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to add the Budget to.")
    cost_report_token: Optional[str] = Field(default=None, description="The CostReport token. Ignored for hierarchical Budgets.")
    child_budget_tokens: Optional[List[str]] = Field(default=None, description="The tokens of any child Budgets when creating a hierarchical Budget.")
    periods: Optional[List[BudgetPeriod]] = Field(default=None, description="The periods for the Budget. The start_at and end_at must be iso8601 formatted e.g. YYYY-MM-DD. Ignored for hierarchical Budgets.")


class UpdateBudget(BaseModel):
    """Update a Budget."""

    name: Optional[str] = Field(default=None, description="The name of the Budget.")
    cost_report_token: Optional[str] = Field(default=None, description="The CostReport token. Ignored for hierarchical Budgets.")
    child_budget_tokens: Optional[List[str]] = Field(default=None, description="The tokens of any child Budgets when creating a hierarchical Budget.")
    periods: Optional[List[BudgetPeriod]] = Field(default=None, description="The periods for the Budget. The start_at and end_at must be iso8601 formatted e.g. YYYY-MM-DD. Ignored for hierarchical Budgets.")


class BusinessMetrics(BaseModel):
    """BusinessMetrics model"""

    business_metrics: List[BusinessMetric]


class BusinessMetric(BaseModel):
    """BusinessMetric model"""

    token: str = Field(description="The token of the BusinessMetric.")
    title: str = Field(description="The title of the BusinessMetric.")
    created_by_token: Optional[str] = Field(default=None, description="The token of the Creator of the BusinessMetric.")
    cost_report_tokens_with_metadata: List[AttachedCostReportForBusinessMetric] = Field(description="The tokens for any CostReports that use the BusinessMetric, the unit scale, and label filter.")
    import_type: Optional[str] = Field(description="The type of import for the BusinessMetric.")
    integration_token: Optional[str] = Field(description="The Integration token used to import the BusinessMetric.")
    cloudwatch_fields: Optional[CloudwatchFields] = Field(default=None)
    datadog_metric_fields: Optional[DatadogMetricFields] = Field(default=None)


class AttachedCostReportForBusinessMetric(BaseModel):
    cost_report_token: Optional[str] = Field(description="The token of the CostReport the BusinessMetric is attached to.")
    unit_scale: str = Field(description="Determines the scale of the BusinessMetric's values within a particular CostReport.")
    label_filter: Optional[List[str]] = Field(default=None, description="The labels that the BusinessMetric is filtered by within a particular CostReport.")


class CloudwatchFields(BaseModel):
    stat: str = Field(description="The time aggregation function used to import Cloudwatch metrics.")
    region: str = Field(description="The region used to import Cloudwatch metrics.")
    namespace: str = Field(description="The namespace used to import Cloudwatch metrics.")
    metric_name: str = Field(description="The metric name used to import Cloudwatch metrics.")
    dimensions: List[CloudwatchDimension] = Field(description="The dimensions used to pull specific statistical data for Cloudwatch metrics.")
    label_dimension: Optional[str] = Field(description="The dimension used to aggregate the Cloudwatch metrics.")


class CloudwatchDimension(BaseModel):
    name: str
    value: str


class DatadogMetricFields(BaseModel):
    query: str = Field(description="The query used to import Datadog metrics.")


class BusinessMetricValues(BaseModel):
    """BusinessMetricValues model"""

    values: List[BusinessMetricValue]


class BusinessMetricValue(BaseModel):
    date: str = Field(description="The date of the Business Metric Value. ISO 8601 formatted.")
    amount: str = Field(description="The amount of the Business Metric Value as a string to ensure precision.")
    label: Optional[str] = Field(default=None, description="The label of the Business Metric Value.")


class CreateBusinessMetric(BaseModel):
    """Create a new BusinessMetric."""

    title: str = Field(description="The title of the BusinessMetrics.")
    cost_report_tokens_with_metadata: Optional[List[AttachedCostReportForBusinessMetric]] = Field(default=None, description="The tokens for any CostReports that use the BusinessMetric, the unit scale, and label filter.")
    values: Optional[List[BusinessMetricValue]] = Field(default=None, description="The dates, amounts, and (optional) labels for the BusinessMetric.")
    forecasted_values: Optional[List[BusinessMetricValue]] = Field(default=None, description="The dates, amounts, and (optional) labels for forecasted BusinessMetric values.")
    datadog_metric_fields: Optional[CreateBusinessMetricOrUpdateBusinessMetricDatadogMetricFields] = Field(default=None, description="Datadog metric configuration fields")
    cloudwatch_fields: Optional[CreateBusinessMetricOrUpdateBusinessMetricCloudwatchFields] = Field(default=None, description="Cloudwatch configuration fields.")


class UpdateBusinessMetric(BaseModel):
    """Updates an existing BusinessMetric."""

    title: Optional[str] = Field(default=None, description="The title of the BusinessMetric.")
    cost_report_tokens_with_metadata: Optional[List[AttachedCostReportForBusinessMetric]] = Field(default=None, description="The tokens for any CostReports that use the BusinessMetric, and the unit scale.")
    values: Optional[List[BusinessMetricValue]] = Field(default=None, description="The dates, amounts, and (optional) labels for the BusinessMetric.")
    forecasted_values: Optional[List[BusinessMetricValue]] = Field(default=None, description="The dates, amounts, and (optional) labels for forecasted BusinessMetric values.")
    datadog_metric_fields: Optional[CreateBusinessMetricOrUpdateBusinessMetricDatadogMetricFields] = Field(default=None, description="Datadog metric configuration fields")
    cloudwatch_fields: Optional[CreateBusinessMetricOrUpdateBusinessMetricCloudwatchFields] = Field(default=None, description="Cloudwatch configuration fields.")


class CostAlertEvents(BaseModel):
    """CostAlertEvents model"""

    links: Optional[Links] = Field(default=None)
    cost_alert_events: List[CostAlertEvent]


class CostAlertEvent(BaseModel):
    """CostAlertEvent model"""

    token: str
    created_at: str = Field(description="The date and time, in UTC, the CostAlertEvent was created. ISO 8601 Formatted.")
    triggered_at: str = Field(description="The date and time, in UTC, the CostAlertEvent is sent. ISO 8601 Formatted.")
    description: str = Field(description="The description of the CostAlertEvent.")
    alert_type: str = Field(description="The type of the CostAlertEvent.")
    metadata: Dict[str, Any] = Field(description="The metadata of the CostAlertEvent.")
    report_token: str = Field(description="The token of the report associated with the CostAlertEvent.")
    alert_token: str = Field(description="The token of the alert associated with the CostAlertEvent.")


class CostAlerts(BaseModel):
    """CostAlerts model"""

    links: Optional[Links] = Field(default=None)
    cost_alerts: List[CostAlert]


class CostAlert(BaseModel):
    """CostAlert model"""

    token: str
    title: str
    email_recipients: List[str] = Field(description="The email addresses that will receive the alert.")
    slack_channels: List[str] = Field(description="The Slack channels that will receive the alert. Make sure your slack integration is connected at https://console.vantage.sh/settings/slack.")
    teams_channels: List[str] = Field(description="The Microsoft Teams channels that will receive the alert. Make sure your teams integration is connected at https://console.vantage.sh/settings/microsoft_teams.")
    created_at: str = Field(description="The date and time, in UTC, for when the alert was created. ISO 8601 Formatted.")
    updated_at: str = Field(description="The date and time, in UTC, for when the alert was last updated. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The ID of the organization that owns the CostAlert.")
    interval: str = Field(description="The period of time used to compare costs. Options are 'day', 'week', 'month', 'quarter'.")
    threshold: float = Field(description="The cost change threshold to alert on.")
    unit_type: str = Field(description="The unit type used to compare costs. Options are 'currency' or 'percentage'.")
    minimum_threshold: Optional[float] = Field(description="The minimum monetary amount threshold for percentage-based alerts. When set, alerts will only trigger if the cost change meets this minimum, even if the percentage threshold is exceeded.")
    report_tokens: List[str] = Field(description="The tokens of the reports to alert on.")


class CreateCostAlert(BaseModel):
    """Create a new Cost Alert"""

    title: str = Field(description="The title of the Cost Alert.")
    interval: str = Field(description="The period of time used to compare costs. Options are 'day', 'week', 'month', 'quarter'.")
    threshold: float = Field(description="The threshold value for the Cost Alert.")
    unit_type: str = Field(description="The unit type used to compare costs. Options are 'currency' or 'percentage'.")
    workspace_token: str = Field(description="The token of the Workspace to add the Cost Alert to.")
    report_tokens: List[str] = Field(description="The tokens of the reports to alert on.")
    email_recipients: Optional[List[str]] = Field(default=None, description="The email recipients for the Cost Alert.")
    slack_channels: Optional[List[str]] = Field(default=None, description="The Slack channels that will receive the alert.")
    teams_channels: Optional[List[str]] = Field(default=None, description="The Microsoft Teams channels that will receive the alert.")
    minimum_threshold: Optional[float] = Field(default=None, description="The minimum monetary amount threshold for percentage-based alerts. Only applicable when unit_type is 'percentage'.")


class UpdateCostAlert(BaseModel):
    """Update a Cost Alert"""

    title: Optional[str] = Field(default=None, description="The title of the Cost Alert.")
    email_recipients: Optional[List[str]] = Field(default=None, description="The email recipients for the Cost Alert.")
    interval: Optional[str] = Field(default=None, description="The period of time used to compare costs. Options are 'day', 'week', 'month', 'quarter'.")
    threshold: Optional[float] = Field(default=None, description="The threshold value for the Cost Alert.")
    slack_channels: Optional[List[str]] = Field(default=None, description="The Slack channels that will receive the alert. Make sure your slack integration is connected at https://console.vantage.sh/settings/slack.")
    teams_channels: Optional[List[str]] = Field(default=None, description="The Microsoft Teams channels that will receive the alert. Make sure your teams integration is connected at https://console.vantage.sh/settings/microsoft_teams.")
    unit_type: Optional[str] = Field(default=None, description="The unit type used to compare costs. Options are 'currency' or 'percentage'.")
    report_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the reports to alert on.")
    minimum_threshold: Optional[float] = Field(default=None, description="The minimum monetary amount threshold for percentage-based alerts. Only applicable when unit_type is 'percentage'.")


class CostProviderAccounts(BaseModel):
    """CostProviderAccounts model"""

    links: Optional[Links] = Field(default=None)
    cost_provider_accounts: List[CostProviderAccount]


class CostProviderAccount(BaseModel):
    title: str = Field(description="The display name of the provider account.")
    account_id: str = Field(description="The provider account identifier (e.g., AWS account ID, Azure subscription ID).")
    provider_uuid: str = Field(description="The provider-specific unique identifier.")
    provider: str = Field(description="The provider type (aws, azure, gcp, etc.).")


class CostReports(BaseModel):
    """CostReports model"""

    links: Optional[Links] = Field(default=None)
    cost_reports: List[CostReport]


class CostReport(BaseModel):
    """CostReport model"""

    token: str
    title: str = Field(description="The title of the CostReport.")
    folder_token: Optional[str] = Field(default=None, description="The token for the Folder the CostReport is a part of.")
    saved_filter_tokens: Optional[List[str]] = Field(default=None, description="The tokens for the SavedFilters assigned to the CostReport.")
    business_metric_tokens_with_metadata: List[AttachedBusinessMetricForCostReport] = Field(description="The tokens for the BusinessMetrics assigned to the CostReport, the unit scale, and label filter.")
    filter: Optional[str] = Field(description="The filter applied to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.")
    groupings: Optional[str] = Field(default=None, description="The grouping aggregations applied to the filtered data.")
    settings: Optional[Settings] = Field(default=None, description="Report settings.")
    created_at: str = Field(description="The date and time, in UTC, the report was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the CostReport is a part of.")
    previous_period_start_date: Optional[str] = Field(default=None, description="The previous period start date of the CostReport. ISO 8601 Formatted.")
    previous_period_end_date: Optional[str] = Field(default=None, description="The previous period end date of the CostReport. ISO 8601 Formatted.")
    start_date: Optional[str] = Field(default=None, description="The start date of the CostReports. ISO 8601 Formatted. Overwrites 'date_interval' if set.")
    end_date: Optional[str] = Field(default=None, description="The end date of the CostReports. ISO 8601 Formatted. Overwrites 'date_interval' if set.")
    date_interval: str = Field(description="The date interval of the CostReport.")
    chart_type: str = Field(description="The chart type of the CostReport.")
    date_bin: str = Field(description="The date bin of the CostReport.")
    chart_settings: ChartSettings


class AttachedBusinessMetricForCostReport(BaseModel):
    business_metric_token: str = Field(description="The token of the BusinessMetric that's attached to the CostReport.")
    unit_scale: str = Field(description="Determines the scale of the BusinessMetric's values within a particular CostReport.")
    label_filter: Optional[List[str]] = Field(default=None, description="The labels that the BusinessMetric is filtered by within a particular CostReport.")


class ChartSettings(BaseModel):
    y_axis_dimension: str = Field(description="The metric or measure displayed on the chart’s y-axis. Possible values: 'cost', 'usage'. Defaults to 'cost'.")
    x_axis_dimension: List[str] = Field(description="The dimension used to group or label data along the x-axis (e.g., by date, region, or service). NOTE: Only one value is allowed at this time. Defaults to ['date'].")


class ForecastedCosts(BaseModel):
    """ForecastedCosts model"""

    links: Optional[Links] = Field(default=None)
    forecasted_costs: List[ForecastedCost]
    currency: Optional[str] = Field(description="The currency of the forecasted costs.")


class ForecastedCost(BaseModel):
    links: Optional[Links] = Field(default=None)
    date: str = Field(description="The date the forecasted cost is projected to accrue. ISO 8601 Formatted.")
    amount: str = Field(description="The amount of the forecasted cost.")
    provider: str = Field(description="The cost provider which incurred the cost. Will be 'all' for all combined providers.")
    service: str = Field(description="The service for the forecasted cost. Will be 'all' for all combined services")


class CreateCostReport(BaseModel):
    """Create a CostReport."""

    title: str = Field(description="The title of the CostReport.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to add the Cost Report to. Ignored if 'folder_token' is set. Required if the API token is associated with multiple Workspaces.")
    groupings: Optional[str] = Field(default=None, description="Grouping values for aggregating costs on the report. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.")
    saved_filter_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the SavedFilters to apply to the CostReport.")
    business_metric_tokens_with_metadata: Optional[List[AttachedBusinessMetricForCostReport]] = Field(default=None, description="The tokens for any BusinessMetrics to attach to the CostReport, and the unit scale.")
    folder_token: Optional[str] = Field(default=None, description="The token of the Folder to add the CostReport to. Determines the Workspace the report is assigned to.")
    settings: Optional[Settings] = Field(default=None, description="Report settings.")
    previous_period_start_date: Optional[str] = Field(default=None, description="The previous period start date of the CostReport. ISO 8601 Formatted.")
    previous_period_end_date: str = Field(description="The previous period end date of the CostReport. ISO 8601 Formatted. Required when previous_period_start_date is provided.")
    start_date: Optional[str] = Field(default=None, description="The start date of the CostReport. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    end_date: str = Field(description="The end date of the CostReport. ISO 8601 Formatted. Required when start_date is provided. Incompatible with 'date_interval' parameter.")
    date_interval: Optional[str] = Field(default=None, description="The date interval of the CostReport. Incompatible with 'start_date' and 'end_date' parameters. Defaults to 'this_month' if start_date and end_date are not provided.")
    chart_type: Optional[str] = Field(default="line", description="The chart type of the CostReport.")
    date_bin: Optional[str] = Field(default="cumulative", description="The date bin of the CostReport.")
    chart_settings: Optional[ChartSettings] = Field(default=None, description="Report chart settings.")


class UpdateCostReport(BaseModel):
    """Update a CostReport."""

    title: Optional[str] = Field(default=None, description="The title of the CostReport.")
    groupings: Optional[str] = Field(default=None, description="Grouping values for aggregating costs on the report. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.")
    saved_filter_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the SavedFilters to apply to the CostReport.")
    business_metric_tokens_with_metadata: Optional[List[AttachedBusinessMetricForCostReport]] = Field(default=None, description="The tokens for any BusinessMetrics to attach to the CostReport, and the unit scale.")
    folder_token: Optional[str] = Field(default=None, description="The token of the Folder to add the CostReport to. Determines the Workspace the report is assigned to.")
    settings: Optional[Settings] = Field(default=None, description="Report settings.")
    chart_settings: Optional[ChartSettings] = Field(default=None, description="Report chart settings.")
    previous_period_start_date: Optional[str] = Field(default=None, description="The previous period start date of the CostReport. ISO 8601 Formatted.")
    previous_period_end_date: Optional[str] = Field(default=None, description="The previous period end date of the CostReport. ISO 8601 Formatted. Required when previous_period_start_date is provided.")
    start_date: Optional[str] = Field(default=None, description="The start date of the CostReport. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date of the CostReport. ISO 8601 Formatted. Required when start_date is provided. Incompatible with 'date_interval' parameter.")
    date_interval: Optional[str] = Field(default=None, description="The date interval of the CostReport. Incompatible with 'start_date' and 'end_date' parameters. Defaults to 'this_month' if start_date and end_date are not provided.")
    chart_type: Optional[str] = Field(default="line", description="The chart type of the CostReport.")
    date_bin: Optional[str] = Field(default="cumulative", description="The date bin of the CostReport.")


class CreateCostExport(BaseModel):
    """Generate a DataExport of costs."""

    cost_report_token: Optional[str] = Field(default=None, description="The CostReport token.")
    filter: Optional[str] = Field(default=None, description="The VQL filter to apply to the costs. If this is supplied you do not need cost_report_token.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to query costs from. Ignored if 'cost_report_token' is set. Required if the API token is associated with multiple Workspaces.")
    start_date: Optional[str] = Field(default=None, description="First date you would like to filter costs from. ISO 8601 formatted.")
    end_date: Optional[str] = Field(default=None, description="Last date you would like to filter costs to. ISO 8601 formatted.")
    date_bin: Optional[str] = Field(default=None, description="The date bin of the costs. Defaults to the report's default or day.")
    schema_: Optional[str] = Field(alias="schema", default="vntg", description="The schema of the data export.")


class Costs(BaseModel):
    """Costs model"""

    links: Optional[Links] = Field(default=None)
    total_cost: CostPartial
    total_usage: Optional[List[UsagePartial]] = Field(default=None, description="The sum of all usage for the CostReport for the requested period, rounded to 2 decimal places, grouped by usage unit.")
    costs: List[Cost]


class CostPartial(BaseModel):
    amount: str = Field(description="The amount of the cost.")
    currency: str = Field(description="The currency of the cost.")


class UsagePartial(BaseModel):
    amount: str = Field(description="The sum of the usage.")
    unit: str = Field(description="The unit of the usage.")


class Cost(BaseModel):
    """Cost model"""

    links: Optional[Links] = Field(default=None)
    accrued_at: str = Field(description="The date the cost was accrued. ISO 8601 Formatted.")
    amount: str = Field(description="The amount of the cost.")
    currency: str = Field(description="The currency of the cost.")
    usage: Optional[Dict[str, Any]] = Field(default=None, description="The usage amount and unit incurred by the cost.")
    provider: Optional[str] = Field(default=None, description="The cost provider which incurred the cost.")
    billing_account_id: Optional[str] = Field(default=None, description="The cost provider's billing account id that incurred the cost.")
    account_id: Optional[str] = Field(default=None, description="The cost provider's account id that incurred the cost.")
    service: Optional[str] = Field(default=None, description="The service which incurred the cost.")
    region: Optional[str] = Field(default=None, description="The region which incurred the cost.")
    resource_id: Optional[str] = Field(default=None, description="The resource id which incurred the cost.")
    tag: Optional[str] = Field(default=None, description="The tag attached to the cost that was incurred. DEPRECATED: does not support multiple tags.")
    tags: Optional[List[str]] = Field(default=None, description="The tag pairs attached to the cost that was incurred.")
    cost_category: Optional[str] = Field(default=None, description="The category for the cost.")
    cost_subcategory: Optional[str] = Field(default=None, description="The subcategory for the cost.")
    segment: Optional[str] = Field(default=None, description="The segment name for segment report costs.")


class Dashboards(BaseModel):
    """Dashboards model"""

    links: Optional[Links] = Field(default=None)
    dashboards: List[Dashboard]


class Dashboard(BaseModel):
    """Dashboard model"""

    token: str
    title: str = Field(description="The title of the Dashboard.")
    widgets: List[DashboardWidget]
    saved_filter_tokens: List[str] = Field(description="The tokens of the Saved Filters used in the Dashboard.")
    date_bin: Optional[str] = Field(description="Determines how to group costs in the Dashboard.")
    date_interval: Optional[str] = Field(description="Determines the date range for Reports in the Dashboard. Guaranteed to be set to 'custom' if 'start_date' and 'end_date' are set.")
    start_date: Optional[str] = Field(default=None, description="The start date for the date range for Reports in the Dashboard. ISO 8601 Formatted. Overwrites 'date_interval' if set.")
    end_date: Optional[str] = Field(default=None, description="The end date for the date range for Reports in the Dashboard. ISO 8601 Formatted. Overwrites 'date_interval' if set.")
    created_at: str = Field(description="The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted.")
    updated_at: str = Field(description="The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the Dashboard is a part of.")


class DashboardWidget(BaseModel):
    widgetable_token: str
    title: str = Field(description="The title of the Widget.")
    settings: DashboardWidgetSettings


class DashboardWidgetSettings(BaseModel):
    display_type: str


class CreateDashboard(BaseModel):
    """Create a Dashboard."""

    title: str = Field(description="The title of the Dashboard.")
    widgets: Optional[List[DashboardWidget]] = Field(default=None, description="The widgets to add to the Dashboard. Currently supports CostReport, ResourceReport, KubernetesEfficiencyReport, and FinancialCommitmentReport.")
    saved_filter_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the Saved Filters used in the Dashboard.")
    date_bin: Optional[str] = Field(default=None, description="Determines how to group costs in the Dashboard.")
    date_interval: Optional[str] = Field(default=None, description="Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.")
    start_date: Optional[str] = Field(default=None, description="The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to add the Dashboard to. Required if the API token is associated with multiple Workspaces.")


class UpdateDashboard(BaseModel):
    """Update a Dashboard."""

    title: Optional[str] = Field(default=None, description="The title of the Dashboard.")
    widgets: Optional[List[DashboardWidget]] = Field(default=None, description="The widgets to add to the Dashboard. Currently supports CostReport, ResourceReport, KubernetesEfficiencyReport, and FinancialCommitmentReport.")
    saved_filter_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the Saved Filters used in the Dashboard.")
    date_bin: Optional[str] = Field(default=None, description="Determines how to group costs in the Dashboard.")
    date_interval: Optional[str] = Field(default=None, description="Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.")
    start_date: Optional[str] = Field(default=None, description="The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace the Dashboard belongs to. Required if the API token is associated with multiple Workspaces.")


class DataExport(BaseModel):
    """DataExport model"""

    token: str
    status: str
    created_at: str
    export_type: str
    manifest: DataExportManifest
    attributes: Dict[str, Any]


class DataExportManifest(BaseModel):
    files: List[str]
    completed_at: Optional[str]
    valid_until: Optional[str]


class ExchangeRates(BaseModel):
    """ExchangeRates model"""

    links: Optional[Links] = Field(default=None)
    exchange_rates: List[ExchangeRate]


class ExchangeRate(BaseModel):
    base_currency_code: str
    currency_code: str
    rate: str
    effective_date: str
    updated_at: str


class FinancialCommitmentReports(BaseModel):
    """FinancialCommitmentReports model"""

    links: Optional[Links] = Field(default=None)
    financial_commitment_reports: List[FinancialCommitmentReport]


class FinancialCommitmentReport(BaseModel):
    """FinancialCommitmentReport model"""

    token: str
    title: str = Field(description="The title of the FinancialCommitmentReport.")
    default: bool = Field(description="Indicates whether the FinancialCommitmentReport is the default report.")
    created_at: str = Field(description="The date and time, in UTC, the report was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the FinancialCommitmentReport is a part of.")
    user_token: Optional[str] = Field(default=None, description="The token for the User who created this FinancialCommitmentReport.")
    start_date: Optional[str] = Field(description="The start date for the FinancialCommitmentReport. Only set for custom date ranges. ISO 8601 Formatted.")
    end_date: Optional[str] = Field(description="The end date for the FinancialCommitmentReport. Only set for custom date ranges. ISO 8601 Formatted.")
    date_interval: Optional[str] = Field(description="The date range for the FinancialCommitmentReport. Only present if a custom date range is not specified.")
    date_bucket: str = Field(description="How costs are grouped and displayed in the FinancialCommitmentReport. Possible values: day, week, month.")
    groupings: Optional[str] = Field(description="The grouping aggregations applied to the filtered data.")
    on_demand_costs_scope: str = Field(description="The scope for the costs. Possible values: discountable, all.")
    filter: Optional[str] = Field(description="The filter applied to the FinancialCommitmentReport. Additional documentation available at https://docs.vantage.sh/vql.")


class CreateFinancialCommitmentReport(BaseModel):
    """Create a FinancialCommitmentReport."""

    workspace_token: str = Field(description="The Workspace in which the FinancialCommitmentReport will be created.")
    title: str = Field(description="The title of the FinancialCommitmentReport.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the FinancialCommitmentReport. Additional documentation available at https://docs.vantage.sh/vql.")
    start_date: Optional[str] = Field(default=None, description="The start date of the FinancialCommitmentReport. YYYY-MM-DD formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date of the FinancialCommitmentReport. YYYY-MM-DD formatted. Incompatible with 'date_interval' parameter.")
    date_interval: Optional[str] = Field(default=None, description="The date interval of the FinancialCommitmentReport. Unless 'custom' is used, this is incompatible with 'start_date' and 'end_date' parameters. Defaults to 'last_3_months'.")
    date_bucket: Optional[str] = Field(default=None, description="The date bucket of the FinancialCommitmentReport.")
    on_demand_costs_scope: Optional[str] = Field(default=None, description="The scope for the costs. Possible values: discountable, all.")
    groupings: Optional[List[str]] = Field(default=None, description="Grouping values for aggregating costs on the FinancialCommitmentReport. Valid groupings: cost_type, commitment_type, commitment_id, service, resource_account_id, provider_account_id, region, cost_category, cost_sub_category, instance_type, tag, tag:<label_name>.")


class UpdateFinancialCommitmentReport(BaseModel):
    """Update a FinancialCommitmentReport."""

    title: Optional[str] = Field(default=None, description="The title of the FinancialCommitmentReport.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the FinancialCommitmentReport. Additional documentation available at https://docs.vantage.sh/vql.")
    start_date: Optional[str] = Field(default=None, description="The start date of the FinancialCommitmentReport. YYYY-MM-DD formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date of the FinancialCommitmentReport. YYYY-MM-DD formatted. Incompatible with 'date_interval' parameter.")
    date_interval: Optional[str] = Field(default=None, description="The date interval of the FinancialCommitmentReport. Unless 'custom' is used, this is incompatible with 'start_date' and 'end_date' parameters. Defaults to 'last_3_months'.")
    date_bucket: Optional[str] = Field(default=None, description="The date bucket of the FinancialCommitmentReport.")
    on_demand_costs_scope: Optional[str] = Field(default=None, description="The scope for the costs. Possible values: discountable, all.")
    groupings: Optional[List[str]] = Field(default=None, description="Grouping values for aggregating costs on the FinancialCommitmentReport. Valid groupings: cost_type, commitment_type, commitment_id, service, resource_account_id, provider_account_id, region, cost_category, cost_sub_category, instance_type, tag, tag:<label_name>.")


class FinancialCommitments(BaseModel):
    """FinancialCommitments model"""

    links: Optional[Links] = Field(default=None)
    financial_commitments: List[FinancialCommitment]


class FinancialCommitment(BaseModel):
    commitment_type: str = Field(description="The commitment type (eg Savings Plan or Reserved Instance).")
    service: str = Field(description="The service this commitment applies towards.")
    account: str = Field(description="The account for this financial commitment.")
    type: str = Field(description="The type of financial commitment.")
    amount: Optional[int] = Field(description="The number of instances for the financial commitment.")
    term: Optional[str] = Field(description="The duration in years of the financial commitment.")
    payment_type: Optional[str] = Field(description="The type of payment for the financial commitment.")
    region: Optional[str] = Field(description="The region for the financial commitment.")
    purchase_date: str = Field(description="The purchase date of the financial commitment. ISO 8601 Formatted.")
    expiration_date: str = Field(description="The expiration date of the financial commitment. ISO 8601 Formatted.")
    commitment: str = Field(description="The amount of the financial commitment.")
    status: Optional[str] = Field(description="The status of the financial commitment (e.g. active vs expired).")
    created_at: str = Field(description="The date and time, in UTC, the Financial Commitment was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the FinancialCommitment is a part of.")


class Folders(BaseModel):
    """Folders model"""

    links: Optional[Links] = Field(default=None)
    folders: List[Folder]


class Folder(BaseModel):
    """Folder model"""

    token: str
    title: Optional[str] = Field(description="The title of the Folder.")
    parent_folder_token: Optional[str] = Field(default=None, description="The token for the parent Folder, if any.")
    saved_filter_tokens: List[str] = Field(description="The tokens for the SavedFilters assigned to the Folder.")
    created_at: str = Field(description="The date and time, in UTC, the Folder was created. ISO 8601 Formatted.")
    updated_at: str = Field(description="The date and time, in UTC, the Folder was last updated at. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the Folder is a part of.")


class CreateFolder(BaseModel):
    """Create a Folder for CostReports."""

    title: str = Field(description="The title of the Folder.")
    parent_folder_token: Optional[str] = Field(default=None, description="The token of the parent Folder.")
    saved_filter_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the SavedFilters to apply to any Cost Report contained within the Folder.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to add the Folder to. Ignored if 'parent_folder_token' is set. Required if the API token is associated with multiple Workspaces.")


class UpdateFolder(BaseModel):
    """Update a Folder for CostReports."""

    title: Optional[str] = Field(default=None, description="The title of the Folder.")
    parent_folder_token: Optional[str] = Field(default=None, description="The token of the parent Folder.")
    saved_filter_tokens: Optional[List[str]] = Field(default=None, description="The tokens of the SavedFilters to apply to any Cost Report contained within the Folder.")


class Integrations(BaseModel):
    """Integrations model"""

    links: Optional[Links] = Field(default=None)
    integrations: List[Integration]


class Integration(BaseModel):
    """Integration model"""

    token: str
    provider: str = Field(description="The name of the Integration.")
    account_identifier: Optional[str] = Field(description="The account identifier. For GCP this is the billing Account ID, for Azure this is the account ID")
    status: str = Field(description="The status of the Integration. Can be 'connected', 'error', 'pending', 'importing', 'imported', or 'disconnected'.")
    last_updated: Optional[str] = Field(default=None, description="The date and time, in UTC, when the Integration was last updated. ISO 8601 Formatted.")
    workspace_tokens: List[str] = Field(description="The tokens for any Workspaces that the account belongs to.")
    created_at: str = Field(description="The date and time, in UTC, the Integration was created. ISO 8601 Formatted.")
    managed_account_tokens: List[str] = Field(description="The tokens for any Managed Accounts that are associated with the Integration.")


class CreateCustomProviderIntegration(BaseModel):
    """Create a Custom Provider Integration"""

    name: str = Field(description="Name of the Custom Provider Integration.")
    description: Optional[str] = Field(default=None, description="Description of the Custom Provider Integration.")


class UserCostsUpload(BaseModel):
    """UserCostsUpload model"""

    token: str = Field(description="The token of the UserCostsUpload.")
    filename: str = Field(description="The filename of the uploaded costs UserCostsUpload.")
    amount: str = Field(description="The total amount of the costs in the UserCostsUpload.")
    start_date: str = Field(description="The start date of the costs in the UserCostsUpload.")
    end_date: str = Field(description="The end date of the costs in the UserCostsUpload.")
    import_status: str = Field(description="Import status of the UserCostsUpload.")
    created_by_token: str = Field(description="The token of the Creator of the UserCostsUpload.")
    created_at: str = Field(description="When the UserCostsUpload was uploaded.")


class UserCostsUploads(BaseModel):
    """UserCostsUploads model"""

    links: Optional[Links] = Field(default=None)
    user_costs_uploads: List[UserCostsUpload]


class CreateGcpIntegration(BaseModel):
    """Create a GCP Integration"""

    billing_account_id: str = Field(description="GCP billing account ID.")
    project_id: str = Field(description="GCP project ID.")
    dataset_name: str = Field(description="BigQuery dataset name.")


class CreateAzureIntegration(BaseModel):
    """Create an Azure Integration"""

    tenant: str = Field(description="Azure AD Tenant ID.")
    app_id: str = Field(description="Service Principal Application ID.")
    password: str = Field(description="Service Principal Password.")


class UpdateIntegration(BaseModel):
    """Update an Integration."""

    workspace_tokens: Optional[List[str]] = Field(default=None, description="The Workspace tokens to associate to the Integration.")


class Invoices(BaseModel):
    """Invoices model"""

    links: Optional[Links] = Field(default=None)
    invoices: List[Invoice]


class Invoice(BaseModel):
    """Invoice model"""

    token: str
    invoice_number: str = Field(description="Sequential invoice number for the MSP account")
    total: Optional[str] = Field(description="Total amount for the invoice period")
    billing_period_start: str = Field(description="Start date of the billing period. ISO 8601 formatted.")
    billing_period_end: str = Field(description="End date of the billing period. ISO 8601 formatted.")
    status: str = Field(description="Current status of the invoice")
    created_at: str = Field(description="The date and time, in UTC, the invoice was created. ISO 8601 formatted.")
    updated_at: str = Field(description="The date and time, in UTC, the invoice was last updated. ISO 8601 formatted.")
    account_token: str = Field(description="Token of the managed account this invoice belongs to")
    account_name: str = Field(description="Name of the managed account this invoice belongs to")
    msp_account_token: str = Field(description="Token of the MSP account that owns this invoice")


class CreateInvoice(BaseModel):
    """Create an invoice (MSP accounts only)."""

    billing_period_start: str = Field(description="Start date of billing period (YYYY-MM-DD)")
    billing_period_end: str = Field(description="End date of billing period (YYYY-MM-DD)")
    account_token: str = Field(description="Token of the managed account to invoice")


class DownloadInvoiceRequest(BaseModel):
    """Download invoice file (PDF or CSV)."""

    file_type: str = Field(description="Type of file to download (pdf or csv)")


class DownloadInvoice(BaseModel):
    """DownloadInvoice model"""

    download_url: str = Field(description="The URL to download the invoice file.")


class SendInvoice(BaseModel):
    """SendInvoice model"""

    recipients: List[str]


class CostReportUrl(BaseModel):
    """CostReportUrl model"""

    cost_report_url: str = Field(description="The URL of the cost report.")


class KubernetesEfficiencyReports(BaseModel):
    """KubernetesEfficiencyReports model"""

    links: Optional[Links] = Field(default=None)
    kubernetes_efficiency_reports: List[KubernetesEfficiencyReport]


class KubernetesEfficiencyReport(BaseModel):
    """KubernetesEfficiencyReport model"""

    token: str
    title: str = Field(description="The title of the KubernetesEfficiencyReport.")
    default: bool = Field(description="Indicates whether the KubernetesEfficiencyReport is the default report.")
    created_at: str = Field(description="The date and time, in UTC, the report was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the KubernetesEfficiencyReport is a part of.")
    user_token: Optional[str] = Field(default=None, description="The token for the User who created this KubernetesEfficiencyReport.")
    start_date: Optional[str] = Field(description="The start date for the KubernetesEfficiencyReport. Only set for custom date ranges. ISO 8601 Formatted.")
    end_date: Optional[str] = Field(description="The end date for the KubernetesEfficiencyReport. Only set for custom date ranges. ISO 8601 Formatted.")
    date_interval: Optional[str] = Field(description="The date range for the KubernetesEfficiencyReport. Only present if a custom date range is not specified.")
    date_bucket: str = Field(description="How costs are grouped and displayed in the KubernetesEfficiencyReport. Possible values: day, week, month.")
    aggregated_by: str = Field(description="How costs are aggregated by. Possible values: idle_cost, amount, cost_efficiency.")
    groupings: Optional[str] = Field(description="Grouping values for aggregating costs on the KubernetesEfficiencyReport. Valid groupings: cluster_id, namespace, labeled, category, pod, label, label:<label_name>.")
    filter: Optional[str] = Field(description="The filter applied to the KubernetesEfficiencyReport. Additional documentation available at https://docs.vantage.sh/vql.")


class CreateKubernetesEfficiencyReportExport(BaseModel):
    """Generate a DataExport of Kubernetes efficiency data."""

    kubernetes_efficiency_report_token: Optional[str] = Field(default=None, description="The KubernetesEfficiencyReport token. If not provided, the default report for the workspace will be used.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the KubernetesEfficiencyReport. Additional documentation available at https://docs.vantage.sh/vql.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to export data from. Ignored if 'kubernetes_efficiency_report_token' is set. Required if the API token is associated with multiple Workspaces.")
    start_date: Optional[str] = Field(default=None, description="First date you would like to filter data from. ISO 8601 formatted.")
    end_date: Optional[str] = Field(default=None, description="Last date you would like to filter data to. ISO 8601 formatted.")
    date_bin: Optional[str] = Field(default=None, description="The date bin of the data. Defaults to the report's default or day.")


class CreateKubernetesEfficiencyReport(BaseModel):
    """Create a KubernetesEfficiencyReport."""

    workspace_token: str = Field(description="The Workspace in which the KubernetesEfficiencyReport will be created.")
    title: str = Field(description="The title of the KubernetesEfficiencyReport.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the KubernetesEfficiencyReport. Additional documentation available at https://docs.vantage.sh/vql.")
    start_date: Optional[str] = Field(default=None, description="The start date of the KubernetesEfficiencyReport. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date of the KubernetesEfficiencyReport. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    date_interval: Optional[str] = Field(default=None, description="The date interval of the KubernetesEfficiencyReport. Incompatible with 'start_date' and 'end_date' parameters. Defaults to 'this_month' if start_date and end_date are not provided.")
    aggregated_by: Optional[str] = Field(default=None, description="The column by which the costs are aggregated.")
    date_bucket: Optional[str] = Field(default=None, description="The date bucket of the KubernetesEfficiencyReport.")
    groupings: Optional[List[str]] = Field(default=None, description="Grouping values for aggregating costs on the KubernetesEfficiencyReport. Valid groupings: cluster_id, namespace, labeled, category, pod, label, label:<label_name>.")


class UpdateKubernetesEfficiencyReport(BaseModel):
    """Update a KubernetesEfficiencyReport."""

    title: Optional[str] = Field(default=None, description="The title of the KubernetesEfficiencyReport.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the KubernetesEfficiencyReport. Additional documentation available at https://docs.vantage.sh/vql.")
    start_date: Optional[str] = Field(default=None, description="The start date of the KubernetesEfficiencyReport. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date of the KubernetesEfficiencyReport. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.")
    date_interval: Optional[str] = Field(default=None, description="The date interval of the KubernetesEfficiencyReport. Incompatible with 'start_date' and 'end_date' parameters. Defaults to 'this_month' if start_date and end_date are not provided.")
    aggregated_by: Optional[str] = Field(default=None, description="The column by which the costs are aggregated.")
    date_bucket: Optional[str] = Field(default=None, description="The date bucket of the KubernetesEfficiencyReport.")
    groupings: Optional[List[str]] = Field(default=None, description="Grouping values for aggregating costs on the KubernetesEfficiencyReport. Valid groupings: cluster_id, namespace, labeled, category, pod, label, label:<label_name>.")


class ManagedAccounts(BaseModel):
    """ManagedAccounts model"""

    links: Optional[Links] = Field(default=None)
    managed_accounts: List[ManagedAccount]


class ManagedAccount(BaseModel):
    """ManagedAccount model"""

    token: str
    name: str
    contact_email: str
    parent_account_token: str = Field(description="The token for the parent Account.")
    access_credential_tokens: List[str] = Field(description="The tokens for the Access Credentials assigned to the Managed Account.")
    billing_rule_tokens: List[str] = Field(description="The tokens for the Billing Rules assigned to the Managed Account.")
    email_domain: Optional[str] = Field(default=None, description="Email domain associated with this Managed Account for SSO.")
    msp_billing_profile_token: Optional[str] = Field(default=None, description="Token of the MSP billing profile used for this managed account (MSP invoicing accounts only)")
    billing_information_attributes: Optional[BillingInformation] = Field(default=None)
    business_information_attributes: Optional[BusinessInformation] = Field(default=None)


class CreateManagedAccount(BaseModel):
    """Create a Managed Account."""

    name: str = Field(description="The name of the Managed Account.")
    contact_email: str = Field(description="The contact email address for the Managed Account.")
    access_credential_tokens: Optional[List[str]] = Field(default=None, description="Access Credential (aka Integrations) tokens to assign to the Managed Account.")
    billing_rule_tokens: Optional[List[str]] = Field(default=None, description="Billing Rule tokens to assign to the Managed Account.")
    email_domain: Optional[str] = Field(default=None, description="Email domain to associate with this Managed Account for SSO.")


class UpdateManagedAccount(BaseModel):
    """Update a Managed Account."""

    name: Optional[str] = Field(default=None, description="The name of the Managed Account.")
    contact_email: Optional[str] = Field(default=None, description="The contact email address for the Managed Account.")
    access_credential_tokens: Optional[List[str]] = Field(default=None, description="Access Credential (aka Integrations) tokens to assign to the Managed Account.")
    billing_rule_tokens: Optional[List[str]] = Field(default=None, description="Billing Rule tokens to assign to the Managed Account.")
    email_domain: Optional[str] = Field(default=None, description="Email domain to associate with this Managed Account for SSO.")
    msp_billing_profile_token: Optional[str] = Field(default=None, description="Token of the MSP billing profile to use for this managed account (MSP invoicing accounts only).")
    billing_information_attributes: Optional[BillingInformationAttributes] = Field(default=None, description="Billing address and contact information (MSP invoicing accounts only)")
    business_information_attributes: Optional[BusinessInformationAttributes] = Field(default=None, description="Business information and custom fields (MSP invoicing accounts only)")


class CreateSsoConnectionForManagedAccount(BaseModel):
    """Configure SSO for a Managed Account."""

    type: str = Field(description="The type of SSO connection. Currently supported: saml.")
    saml_metadata_url: Optional[str] = Field(default=None, description="The SAML metadata URL for the identity provider. Required when type is saml.")
    additional_domains: Optional[List[str]] = Field(default=None, description="Additional email domains to associate with this SSO configuration. The account's SSO domain is always included.")


class UpdateSsoConnectionForManagedAccount(BaseModel):
    """Update SSO configuration for a Managed Account."""

    saml_metadata_url: Optional[str] = Field(default=None, description="The SAML metadata URL for the identity provider.")
    additional_domains: Optional[List[str]] = Field(default=None, description="Additional email domains to associate with this SSO configuration. Replaces existing additional domains. The account's SSO domain is always preserved.")


class Me(BaseModel):
    """Me model"""

    default_workspace_token: Optional[str]
    workspaces: List[Workspace]
    bearer_token: BearerToken


class Workspace(BaseModel):
    """Workspace model"""

    token: str
    name: str = Field(description="The name of the Workspace.")
    created_at: str = Field(description="The date and time, in UTC, the Workspace was created. ISO 8601 Formatted.")
    enable_currency_conversion: bool = Field(description="Whether or not currency conversion is enabled for the Workspace.")
    currency: str = Field(description="The currency code for the Workspace that will be used for currency conversion.")
    exchange_rate_date: str = Field(description="The exchange rate date that will be used to convert currency for your cost data.")


class BearerToken(BaseModel):
    description: str = Field(description="The user supplied description of this BearerToken")
    created_at: str = Field(description="The date and time, in UTC, the BearerToken was created. ISO 8601 Formatted.")
    scope: List[str] = Field(description="The scopes applied to the BearerToken used to authenticate this request.")


class CostProviders(BaseModel):
    """CostProviders model"""

    links: Optional[Links] = Field(default=None)
    cost_providers: List[CostProvider]


class CostProvider(BaseModel):
    name: str = Field(description="The name of the CostProvider.")
    key: str = Field(description="The key of the CostProvider, useful for filtering Costs.")


class CostServices(BaseModel):
    """CostServices model"""

    links: Optional[Links] = Field(default=None)
    cost_services: List[CostService]


class CostService(BaseModel):
    name: str = Field(description="The name of the CostService.")
    provider: str = Field(description="The key value of the CostProvider.")


class CreateUserFeedback(BaseModel):
    """Provide UserFeedback for our product and features."""

    message: str = Field(description="UserFeedback message")


class UserFeedback(BaseModel):
    """UserFeedback model"""

    token: str = Field(description="Token of the feedback")
    message: str = Field(description="User feedback message")
    created_by_token: Optional[str] = Field(default=None, description="Token of the creator of the feedback")
    created_at: str = Field(description="Feedback creation timestamp")


class NetworkFlowReports(BaseModel):
    """NetworkFlowReports model"""

    links: Optional[Links] = Field(default=None)
    network_flow_reports: List[NetworkFlowReport]


class NetworkFlowReport(BaseModel):
    """NetworkFlowReport model"""

    token: str
    title: str = Field(description="The title of the NetworkFlowReport.")
    default: bool = Field(description="Indicates whether the NetworkFlowReport is the default report.")
    created_at: str = Field(description="The date and time, in UTC, the report was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the NetworkFlowReport is a part of.")
    created_by_token: Optional[str] = Field(default=None, description="The token for the User or Team that created this NetworkFlowReport.")
    start_date: Optional[str] = Field(description="The start date for the NetworkFlowReport. Only set for custom date ranges. ISO 8601 Formatted.")
    end_date: Optional[str] = Field(description="The end date for the NetworkFlowReport. Only set for custom date ranges. ISO 8601 Formatted.")
    date_interval: Optional[str] = Field(description="The date range for the NetworkFlowReport. Only present if a custom date range is not specified.")
    groupings: Optional[str] = Field(description="The grouping aggregations applied to the filtered data.")
    flow_direction: Optional[str] = Field(description="The flow weight of the NetworkFlowReport. Possible values: costs, bytes.")
    flow_weight: str = Field(description="The flow weight of the NetworkFlowReport. Possible values: costs, bytes.")
    filter: Optional[str] = Field(description="The filter applied to the NetworkFlowReport. Additional documentation available at https://docs.vantage.sh/vql.")


class CreateNetworkFlowReport(BaseModel):
    """Create a NetworkFlowReport."""

    workspace_token: str = Field(description="The Workspace in which the NetworkFlowReport will be created.")
    title: str = Field(description="The title of the NetworkFlowReport.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the NetworkFlowReport. Additional documentation available at https://docs.vantage.sh/vql.")
    start_date: Optional[str] = Field(default=None, description="The start date of the NetworkFlowReport. YYYY-MM-DD formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date of the NetworkFlowReport. YYYY-MM-DD formatted. Incompatible with 'date_interval' parameter.")
    date_interval: Optional[str] = Field(default=None, description="The date interval of the NetworkFlowReport. Unless 'custom' is used, this is incompatible with 'start_date' and 'end_date' parameters. Defaults to 'last_7_days'.")
    groupings: Optional[List[str]] = Field(default=None, description="Grouping values for aggregating data on the NetworkFlowReport. Valid groupings: account_id, az_id, dstaddr, dsthostname, flow_direction, interface_id, instance_id, peer_resource_uuid, peer_account_id, peer_vpc_id, peer_region, peer_az_id, peer_subnet_id, peer_interface_id, peer_instance_id, region, resource_uuid, srcaddr, srchostname, subnet_id, traffic_category, traffic_path, vpc_id.")
    flow_direction: Optional[str] = Field(default=None, description="The flow direction of the NetworkFlowReport.")
    flow_weight: Optional[str] = Field(default=None, description="The dimension by which the logs in the report are sorted. Defaults to costs.")


class UpdateNetworkFlowReport(BaseModel):
    """Update a NetworkFlowReport."""

    title: Optional[str] = Field(default=None, description="The title of the NetworkFlowReport.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the NetworkFlowReport. Additional documentation available at https://docs.vantage.sh/vql.")
    start_date: Optional[str] = Field(default=None, description="The start date of the NetworkFlowReport. YYYY-MM-DD formatted. Incompatible with 'date_interval' parameter.")
    end_date: Optional[str] = Field(default=None, description="The end date of the NetworkFlowReport. YYYY-MM-DD formatted. Incompatible with 'date_interval' parameter.")
    date_interval: Optional[str] = Field(default=None, description="The date interval of the NetworkFlowReport. Unless 'custom' is used, this is incompatible with 'start_date' and 'end_date' parameters. Defaults to 'last_7_days'.")
    groupings: Optional[List[str]] = Field(default=None, description="Grouping values for aggregating data on the NetworkFlowReport. Valid groupings: account_id, az_id, dstaddr, dsthostname, flow_direction, interface_id, instance_id, peer_resource_uuid, peer_account_id, peer_vpc_id, peer_region, peer_az_id, peer_subnet_id, peer_interface_id, peer_instance_id, region, resource_uuid, srcaddr, srchostname, subnet_id, traffic_category, traffic_path, vpc_id.")
    flow_direction: Optional[str] = Field(default=None, description="The flow direction of the NetworkFlowReport.")
    flow_weight: Optional[str] = Field(default=None, description="The dimension by which the logs in the report are sorted. Defaults to costs.")


class Prices(BaseModel):
    """Prices model"""

    links: Optional[Links] = Field(default=None)
    prices: List[Price]


class Price(BaseModel):
    """Price model"""

    id: str
    unit: str = Field(description="The unit in which the amount is billed.")
    region: str = Field(description="The region the price is specific to.")
    rate_type: str = Field(description="The part of the product the price applies to. (compute, transfer, etc..)")
    currency: str = Field(description="The currency of the amount.")
    amount: float = Field(description="The amount of money this specific product price costs.")
    details: Dict[str, Any] = Field(description="Service specific metadata.")


class Products(BaseModel):
    """Products model"""

    links: Optional[Links] = Field(default=None)
    products: List[Product]


class Product(BaseModel):
    """Product model"""

    id: str
    category: str = Field(description="The category of the cloud product")
    name: str = Field(description="The common name of the product.")
    service_id: str = Field(description="A unique slug for the service the product belongs to.")
    provider_id: str = Field(description="A unique slug for the provider the product belongs to.")
    details: Dict[str, Any] = Field(description="An object of metadata about the product.")


class Recommendations(BaseModel):
    """Recommendations model"""

    links: Optional[Links] = Field(default=None)
    recommendations: List[Recommendation]


class Recommendation(BaseModel):
    """Recommendation model"""

    token: str
    type: str = Field(description="The type of the Recommendation. This is analogous to category, but with a uniform format.")
    category: str = Field(description="The category of the Recommendation.")
    workspace_token: str = Field(description="The token for the Workspace the Recommendation is a part of.")
    provider: str = Field(description="The provider the Recommendation is for.")
    provider_account_id: Optional[str] = Field(description="The account ID of the provider. For Azure, this is the subscription ID.")
    description: str
    potential_savings: Optional[str] = Field(description="The monthly potential savings of the Recommendation, converted to the organization's selected currency.")
    service: str = Field(description="The service the Recommendation is for.")
    created_at: str = Field(description="The date and time, in UTC, the Recommendation was created. ISO 8601 Formatted.")
    resources_affected_count: int = Field(description="The number of ProviderResources related to the Recommendation. Use the `recommendations/:token/resources` endpoint to get the full list of resources.")
    currency_code: Optional[str] = Field(default=None, description="The currency code used by the Workspace to which this Recommendation belongs.")
    currency_symbol: Optional[str] = Field(default=None, description="The currency symbol used by the Workspace to which this Recommendation belongs.")


class RecommendationProviderResources(BaseModel):
    """RecommendationProviderResources model"""

    links: Optional[Links] = Field(default=None)
    resources: List[ProviderResource]


class ProviderResource(BaseModel):
    """ProviderResource model"""

    token: str
    resource_id: str = Field(description="The unique identifier of the Active Resource.")
    recommendation_actions: Optional[List[RecommendationAction]] = Field(default=None, description="The actions to take to implement the Recommendation.")


class RecommendationAction(BaseModel):
    action: str
    description: str
    potential_savings: str = Field(description="Potential savings in dollars")
    instance_type: Optional[str] = Field(default=None)
    containers: Optional[str] = Field(default=None)
    remediation_cli_command: Optional[str] = Field(default=None, description="CLI command to remediate this recommendation")


class RecommendationViews(BaseModel):
    """RecommendationViews model"""

    links: Optional[Links] = Field(default=None)
    recommendation_views: Optional[List[RecommendationView]] = Field(default=None)


class RecommendationView(BaseModel):
    """RecommendationView model"""

    token: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None, description="The title of the RecommendationView.")
    workspace_token: Optional[str] = Field(default=None, description="The token for the Workspace the RecommendationView is a part of.")
    start_date: Optional[str] = Field(default=None, description="Filter recommendations created on/after this YYYY-MM-DD date.")
    end_date: Optional[str] = Field(default=None, description="Filter recommendations created on/before this YYYY-MM-DD date.")
    provider_ids: Optional[List[str]] = Field(default=None, description="Filter by one or more providers.")
    billing_account_ids: Optional[List[str]] = Field(default=None, description="Filter by billing account identifiers.")
    account_ids: Optional[List[str]] = Field(default=None, description="Filter by cloud account identifiers.")
    regions: Optional[List[str]] = Field(default=None, description="Filter by region slugs (e.g. us-east-1, eastus, asia-east1).")
    tag_key: Optional[str] = Field(default=None, description="Filter by tag key (must be used with tag_value).")
    tag_value: Optional[str] = Field(default=None, description="Filter by tag value (requires tag_key).")
    created_at: Optional[str] = Field(default=None, description="The date and time, in UTC, the view was created. ISO 8601 Formatted.")
    created_by: Optional[str] = Field(default=None, description="The token for the Creator of this RecommendationView.")


class CreateRecommendationView(BaseModel):
    """Create a RecommendationView."""

    title: str = Field(description="The title of the RecommendationView.")
    workspace_token: str = Field(description="The Workspace to associate the RecommendationView with.")
    provider_ids: Optional[List[str]] = Field(default=None, description="Filter by one or more providers (e.g. aws, gcp, azure, kubernetes, datadog).")
    billing_account_ids: Optional[List[str]] = Field(default=None, description="Filter by billing account identifiers.")
    account_ids: Optional[List[str]] = Field(default=None, description="Filter by cloud account identifiers.")
    regions: Optional[List[str]] = Field(default=None, description="Filter by region slugs (e.g. us-east-1, eastus, asia-east1).")
    tag_key: Optional[str] = Field(default=None, description="Filter by tag key (must be used with tag_value).")
    tag_value: Optional[str] = Field(default=None, description="Filter by tag value (requires tag_key).")
    start_date: Optional[str] = Field(default=None, description="Filter recommendations created on/after this YYYY-MM-DD date.")
    end_date: Optional[str] = Field(default=None, description="Filter recommendations created on/before this YYYY-MM-DD date.")


class UpdateRecommendationView(BaseModel):
    """Update a RecommendationView."""

    title: Optional[str] = Field(default=None, description="The title of the RecommendationView.")
    provider_ids: Optional[List[str]] = Field(default=None, description="Filter by one or more providers (e.g. aws, gcp, azure, kubernetes, datadog).")
    billing_account_ids: Optional[List[str]] = Field(default=None, description="Filter by billing account identifiers.")
    account_ids: Optional[List[str]] = Field(default=None, description="Filter by cloud account identifiers.")
    regions: Optional[List[str]] = Field(default=None, description="Filter by region slugs (e.g. us-east-1, eastus, asia-east1).")
    tag_key: Optional[str] = Field(default=None, description="Filter by tag key (must be used with tag_value).")
    tag_value: Optional[str] = Field(default=None, description="Filter by tag value (requires tag_key).")
    start_date: Optional[str] = Field(default=None, description="Filter recommendations created on/after this YYYY-MM-DD date.")
    end_date: Optional[str] = Field(default=None, description="Filter recommendations created on/before this YYYY-MM-DD date.")


class ReportNotifications(BaseModel):
    """ReportNotifications model"""

    links: Optional[Links] = Field(default=None)
    report_notifications: List[ReportNotification]


class ReportNotification(BaseModel):
    """ReportNotification model"""

    token: str
    title: str = Field(description="The title of the ReportNotification.")
    cost_report_token: str = Field(description="The token for a CostReport the ReportNotification is applied to.")
    user_tokens: List[str] = Field(description="The Users that receive the notification.")
    recipient_channels: List[str] = Field(description="The Slack or Microsoft Teams channels that receive the notification.")
    frequency: str = Field(description="The frequency the ReportNotification is sent.")
    change: str = Field(description="The type of change the ReportNotification is tracking.")


class CreateReportNotification(BaseModel):
    """Create a ReportNotification."""

    title: str = Field(description="The title of the ReportNotification.")
    cost_report_token: str = Field(description="The CostReport token.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to add the ReportNotification to. Required if the API token is associated with multiple Workspaces.")
    user_tokens: Optional[List[str]] = Field(default=None, description="The Users that receive the notification.")
    recipient_channels: Optional[List[str]] = Field(default=None, description="The Slack or Microsoft Teams channels that receive the notification.")
    frequency: str = Field(description="The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.")
    change: str = Field(description="The type of change the ReportNotification is tracking. Possible values: percentage, dollars.")


class UpdateReportNotification(BaseModel):
    """Update a ReportNotification."""

    title: Optional[str] = Field(default=None, description="The title of the ReportNotification.")
    cost_report_token: Optional[str] = Field(default=None, description="The CostReport token.")
    user_tokens: Optional[List[str]] = Field(default=None, description="The Users that receive the notification.")
    recipient_channels: Optional[List[str]] = Field(default=None, description="The Slack or Microsoft Teams channels that receive the notification.")
    frequency: Optional[str] = Field(default=None, description="The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.")
    change: Optional[str] = Field(default=None, description="The type of change the ReportNotification is tracking. Possible values: percentage, dollars.")


class ResourceReportColumns(BaseModel):
    """ResourceReportColumns model"""

    columns: List[str] = Field(description="Array of available column names for the specified resource type.")


class ResourceReports(BaseModel):
    """ResourceReports model"""

    links: Optional[Links] = Field(default=None)
    resource_reports: List[ResourceReport]


class ResourceReport(BaseModel):
    """ResourceReport model"""

    token: str
    title: str = Field(description="The title of the ResourceReport.")
    filter: Optional[str] = Field(description="The filter applied to the ResourceReport. Additional documentation available at https://docs.vantage.sh/vql.")
    created_at: str = Field(description="The date and time, in UTC, the report was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the ResourceReport is a part of.")
    user_token: Optional[str] = Field(description="The token for the User who created this ResourceReport.")
    created_by_token: Optional[str] = Field(description="The token for the User or Team who created this ResourceReport.")
    columns: List[str] = Field(description="Array of column names configured for the ResourceReport table display.")


class CreateResourceReport(BaseModel):
    """Create a ResourceReport."""

    workspace_token: str = Field(description="The token of the Workspace to add the ResourceReport to.")
    title: Optional[str] = Field(default=None, description="The title of the ResourceReport.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the ResourceReport. Additional documentation available at https://docs.vantage.sh/vql.")
    columns: Optional[List[str]] = Field(default=None, description="Array of column names to display in the table. Column names should match those returned by the /resource_reports/columns endpoint. The order determines the display order. Only available for reports with a single resource type filter.")


class UpdateResourceReport(BaseModel):
    """Update a ResourceReport."""

    title: Optional[str] = Field(default=None, description="The title of the ResourceReport.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the ResourceReport. Additional documentation available at https://docs.vantage.sh/vql.")
    columns: Optional[List[str]] = Field(default=None, description="Array of column names to display in the table. Column names should match those returned by the /resource_reports/columns endpoint. The order determines the display order. Only available for reports with a single resource type filter.")


class Resources(BaseModel):
    """Resources model"""

    links: Optional[Links] = Field(default=None)
    resources: List[Resource]


class Resource(BaseModel):
    """Resource model"""

    token: str
    uuid: str = Field(description="The unique identifier for the resource.")
    type: str = Field(description="The kind of resource.")
    label: Optional[str]
    metadata: Optional[Dict[str, Any]] = Field(description="Type-specific attributes of the resource.")
    account_id: Optional[str] = Field(description="The provider account where the resource is located.")
    billing_account_id: Optional[str] = Field(description="The provider billing account this resource is charged to.")
    provider: str = Field(description="The provider of the resource.")
    region: Optional[str] = Field(description="The region where the resource is located. Region values are specific to each provider.")
    costs: Optional[List[ResourceCost]] = Field(default=None, description="The cost of the resource broken down by category.")
    created_at: str = Field(description="The date and time when Vantage first observed the resource.")


class ResourceCost(BaseModel):
    category: str = Field(description="The category of the cost.")
    amount: float = Field(description="The cost amount.")


class SavedFilters(BaseModel):
    """SavedFilters model"""

    links: Optional[Links] = Field(default=None)
    saved_filters: List[SavedFilter]


class SavedFilter(BaseModel):
    """SavedFilter model"""

    token: str
    title: str = Field(description="The title of the SavedFilter.")
    cost_report_tokens: List[str] = Field(description="The tokens for any CostReports the SavedFilter is applied to.")
    filter: Optional[str] = Field(description="The SavedFilter's filter, applied to any relevant CostReports. Additional documentation available at https://docs.vantage.sh/vql.")
    created_at: str = Field(description="The date and time, in UTC, the report was created. ISO 8601 Formatted.")
    created_by: Optional[str] = Field(description="The token for the Creator of this SavedFilter.")
    workspace_token: str = Field(description="The token for the Workspace the SavedFilter is a part of.")


class CreateSavedFilter(BaseModel):
    """Create a SavedFilter for CostReports."""

    title: str = Field(description="The title of the SavedFilter.")
    workspace_token: Optional[str] = Field(default=None, description="The Workspace to associate the SavedFilter with. Required if the API token is associated with multiple Workspaces.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the SavedFilter, which subsequently gets applied to a CostReport. Additional documentation available at https://docs.vantage.sh/vql.")


class UpdateSavedFilter(BaseModel):
    """Update a SavedFilter for CostReports."""

    title: Optional[str] = Field(default=None, description="The title of the SavedFilter.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the SavedFilter, which subsequently gets applied to a CostReport. Additional documentation available at https://docs.vantage.sh/vql.")


class Segments(BaseModel):
    """Segments model"""

    links: Optional[Links] = Field(default=None)
    segments: List[Segment]


class Segment(BaseModel):
    """Segment model"""

    token: str
    title: str = Field(description="The title of the Segment.")
    parent_segment_token: Optional[str] = Field(description="The token of the parent Segment of this Segment.")
    description: str = Field(description="The description of the Segment.")
    track_unallocated: bool = Field(description="Track Unallocated Costs which are not assigned to any of the created Segments.")
    report_settings: Optional[ReportSettings] = Field(default=None, description="Report settings configurable on top-level Segments.")
    priority: int = Field(description="Costs are assigned in priority order across all Segments with assigned filters.")
    filter: Optional[str] = Field(description="The filter applied to the Segment. Additional documentation available at https://docs.vantage.sh/vql.")
    created_at: str = Field(description="The date and time, in UTC, the Segment was created. ISO 8601 Formatted.")
    workspace_token: str = Field(description="The token for the Workspace the Segment is a part of.")
    report_token: Optional[str] = Field(description="The token for the Report the Segment has generated.")


class CreateSegment(BaseModel):
    """Create a Segment."""

    title: str = Field(description="The title of the Segment.")
    description: Optional[str] = Field(default=None, description="The description of the Segment.")
    priority: Optional[int] = Field(default=None, description="The priority of the Segment.")
    track_unallocated: Optional[bool] = Field(default=False, description="Track Unallocated Costs which are not assigned to any of the created Segments.")
    report_settings: Optional[ReportSettings] = Field(default=None, description="Report settings configurable on top-level Segments.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to add the Segment to. Ignored if 'segment_token' is set. Required if the API token is associated with multiple Workspaces.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.")
    parent_segment_token: Optional[str] = Field(default=None, description="The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.")


class UpdateSegment(BaseModel):
    """Update a Segment."""

    title: Optional[str] = Field(default=None, description="The title of the Segment.")
    description: Optional[str] = Field(default=None, description="The description of the Segment.")
    priority: Optional[int] = Field(default=None, description="The priority of the Segment.")
    track_unallocated: Optional[bool] = Field(default=False, description="Track Unallocated Costs which are not assigned to any of the created Segments.")
    report_settings: Optional[ReportSettings] = Field(default=None, description="Report settings configurable on top-level Segments.")
    filter: Optional[str] = Field(default=None, description="The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.")
    parent_segment_token: Optional[str] = Field(default=None, description="The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.")


class Tags(BaseModel):
    """Tags model"""

    links: Optional[Links] = Field(default=None)
    tags: List[Tag]


class Tag(BaseModel):
    tag_key: str = Field(description="The Tag key.")
    hidden: bool = Field(description="Whether the Tag has been hidden from the Vantage UI.")
    providers: List[str] = Field(description="The unique providers that are covered by the Tag key.")


class TagValues(BaseModel):
    """TagValues model"""

    links: Optional[Links] = Field(default=None)
    tag_values: List[TagValue]


class TagValue(BaseModel):
    tag_value: str = Field(description="The TagValue.")
    providers: List[str] = Field(description="The unique providers that are covered by the TagValue.")


class UpdateTag(BaseModel):
    """Updates an existing Tag."""

    tag_key: Optional[str] = Field(default=None)
    tag_keys: Optional[List[str]] = Field(default=None)
    hidden: bool = Field(description="Whether the Tag is hidden from the Vantage UI.")


class Teams(BaseModel):
    """Teams model"""

    links: Optional[Links] = Field(default=None)
    teams: List[Team]


class Team(BaseModel):
    """Team model"""

    token: str
    name: str = Field(description="The name of the Team.")
    description: Optional[str] = Field(description="The description of the Team.")
    workspace_tokens: List[str] = Field(description="The tokens for any Workspaces that the Team belongs to")
    user_emails: List[str] = Field(description="The email addresses for Users that belong to the Team")
    user_tokens: List[str] = Field(description="The tokens for Users that belong to the Team")


class CreateTeam(BaseModel):
    """Create a new Team."""

    name: str = Field(description="The name of the Team.")
    description: Optional[str] = Field(default=None, description="The description of the Team.")
    workspace_tokens: Optional[List[str]] = Field(default=None, description="The Workspace tokens to associate to the Team.")
    user_tokens: Optional[List[str]] = Field(default=None, description="The User tokens to associate to the Team.")
    user_emails: Optional[List[str]] = Field(default=None, description="The User emails to associate to the Team.")
    role: Optional[str] = Field(default=None, description="The role to assign to the provided Users. Defaults to 'editor' which has editor permissions.")


class UpdateTeam(BaseModel):
    """Update a Team."""

    name: Optional[str] = Field(default=None, description="The name of the Team.")
    description: Optional[str] = Field(default=None, description="The description of the Team.")
    workspace_tokens: Optional[List[str]] = Field(default=None, description="The Workspace tokens to associate to the Team.")
    user_tokens: Optional[List[str]] = Field(default=None, description="The User tokens to associate to the Team.")
    user_emails: Optional[List[str]] = Field(default=None, description="The User emails to associate to the Team.")
    role: Optional[str] = Field(default=None, description="The role to assign to the provided Users. Defaults to 'editor' which has editor permissions.")


class TeamMembers(BaseModel):
    """TeamMembers model"""

    links: Optional[Links] = Field(default=None)
    members: List[TeamMember]


class TeamMember(BaseModel):
    """TeamMember model"""

    name: str = Field(description="The name of the team member.")
    email: str = Field(description="The email address of the team member.")
    user_token: str = Field(description="The token of the team member.")
    role: str = Field(description="The role of the team member in the team.")


class AddTeamMember(BaseModel):
    """Add a member to a Team."""

    user_email: str = Field(description="The email address of the user to add to the Team.")
    role: Optional[str] = Field(default="editor", description="The role to assign to the user. Defaults to 'editor'.")


class CreateUnitCostsExport(BaseModel):
    """Generate a DataExport of unit costs."""

    cost_report_token: str = Field(description="The CostReport token.")
    workspace_token: Optional[str] = Field(default=None, description="The token of the Workspace to query costs from. Required if the API token is associated with multiple Workspaces.")
    start_date: Optional[str] = Field(default=None, description="First date you would like to filter unit costs from. Defaults to the report's default. ISO 8601 formatted.")
    end_date: Optional[str] = Field(default=None, description="Last date you would like to filter unit costs to. Defaults to the report's default. ISO 8601 formatted.")
    date_bin: Optional[str] = Field(default=None, description="The date bin of the unit costs. Defaults to the report's default or day.")


class UnitCosts(BaseModel):
    """UnitCosts model"""

    links: Optional[Links] = Field(default=None)
    unit_costs: List[UnitCost]


class UnitCost(BaseModel):
    links: Optional[Links] = Field(default=None)
    business_metric_token: str = Field(description="The token of the BusinessMetric for which the unit cost was calculated.")
    business_metric_title: str = Field(description="The title of the BusinessMetric for which the unit cost was calculated.")
    unit_cost_amount: str = Field(description="The amount of the unit cost.")
    business_metric_amount: str = Field(description="The amount of the business metric.")
    scale: float = Field(description="The scale of the BusinessMetric's values within a particular CostReport.")
    date: str = Field(description="The date for which the unit cost was calculated. ISO 8601 Formatted.")


class Users(BaseModel):
    """Users model"""

    links: Optional[Links] = Field(default=None)
    users: List[User]


class User(BaseModel):
    """User model"""

    token: str
    name: Optional[str] = Field(description="The name of the User.")
    email: str = Field(description="The email of the User.")
    role: str = Field(description="The role of the User.")
    last_seen_at: Optional[str] = Field(default=None, description="The last time the User logged in.")


class VirtualTagConfigs(BaseModel):
    """VirtualTagConfigs model"""

    virtual_tag_configs: List[VirtualTagConfig]


class VirtualTagConfig(BaseModel):
    """VirtualTagConfig model"""

    token: str = Field(description="The token of the VirtualTagConfig.")
    created_by_token: Optional[str] = Field(description="The token of the Creator of the VirtualTagConfig.")
    key: str = Field(description="The key of the VirtualTagConfig.")
    overridable: bool = Field(description="Whether the VirtualTagConfig can override a provider-supplied tag on a matching Cost.")
    backfill_until: str = Field(description="The earliest month VirtualTagConfig should be backfilled to.")
    collapsed_tag_keys: Optional[List[VirtualTagConfigCollapsedTagKey]] = Field(default=None, description="Tag keys to collapse values for.")
    values: List[VirtualTagConfigValue] = Field(description="Values for the VirtualTagConfig, with match precedence determined by their relative order in the list.")


class VirtualTagConfigCollapsedTagKey(BaseModel):
    key: str = Field(description="The tag key to collapse values for.")
    providers: List[str] = Field(description="The providers this collapsed tag key applies to. Defaults to all providers.")


class VirtualTagConfigValue(BaseModel):
    filter: Optional[str] = Field(description="The filter VQL for the Value.")
    name: Optional[str] = Field(default=None, description="The name of the Value.")
    business_metric_token: Optional[str] = Field(default=None, description="The token of the associated BusinessMetric.")
    cost_metric: Optional[VirtualTagConfigValueCostMetric] = Field(default=None)
    percentages: Optional[List[VirtualTagConfigValuePercentage]] = Field(default=None, description="Labeled percentage allocations for matching costs.")
    date_ranges: Optional[List[VirtualTagConfigValueDateRange]] = Field(default=None, description="Date ranges restricting when this value applies.")


class VirtualTagConfigValueCostMetric(BaseModel):
    filter: Optional[str] = Field(description="The filter VQL for the cost metric.")
    aggregation: VirtualTagConfigValueCostMetricAggregation


class VirtualTagConfigValueCostMetricAggregation(BaseModel):
    tag: Optional[str] = Field(default=None, description="The tag to aggregate on.")


class VirtualTagConfigValuePercentage(BaseModel):
    value: str = Field(description="The tag value associated with a percentage of matched costs.")
    pct: float = Field(description="The percentage of matched costs associated with the value.")


class VirtualTagConfigValueDateRange(BaseModel):
    start_date: Optional[str] = Field(description="The start date of the range (inclusive), or null for unbounded.")
    end_date: Optional[str] = Field(description="The end date of the range (inclusive), or null for unbounded.")


class VirtualTagConfigStatus(BaseModel):
    """VirtualTagConfigStatus model"""

    token: str = Field(description="The token of the VirtualTagConfig.")
    processing: bool = Field(description="Whether the VirtualTagConfig is currently processing. True if any provider has not completed processing.")
    providers: List[VirtualTagConfigProviderStatus] = Field(description="Processing status broken down by provider.")


class VirtualTagConfigProviderStatus(BaseModel):
    provider: str = Field(description="The provider name.")
    status: str = Field(description="The processing status for this provider. Possible values: queued, processing, complete, failed.")


class CreateVirtualTagConfig(BaseModel):
    """Create a new VirtualTagConfig."""

    key: str = Field(description="The key of the VirtualTagConfig.")
    overridable: bool = Field(description="Whether the VirtualTagConfig can override a provider-supplied tag on a matching Cost.")
    backfill_until: Optional[str] = Field(default=None, description="The earliest month the VirtualTagConfig should be backfilled to.")
    collapsed_tag_keys: Optional[List[VirtualTagConfigCollapsedTagKey]] = Field(default=None, description="Tag keys to collapse values for.")
    values: Optional[List[VirtualTagConfigValue]] = Field(default=None, description="Values for the VirtualTagConfig, with match precedence determined by order in the list.")


class UpdateVirtualTagConfig(BaseModel):
    """Updates an existing VirtualTagConfig."""

    key: Optional[str] = Field(default=None, description="The key of the VirtualTagConfig.")
    overridable: Optional[bool] = Field(default=None, description="Whether the VirtualTagConfig can override a provider-supplied tag on a matching Cost.")
    backfill_until: Optional[str] = Field(default=None, description="The earliest month the VirtualTagConfig should be backfilled to.")
    collapsed_tag_keys: Optional[List[VirtualTagConfigCollapsedTagKey]] = Field(default=None, description="Tag keys to collapse values for.")
    values: Optional[List[VirtualTagConfigValue]] = Field(default=None, description="Values for the VirtualTagConfig, with match precedence determined by order in the list.")


class UpdateAsyncVirtualTagConfig(BaseModel):
    """Asynchronously updates an existing VirtualTagConfig."""

    key: Optional[str] = Field(default=None, description="The key of the VirtualTagConfig.")
    overridable: Optional[bool] = Field(default=None, description="Whether the VirtualTagConfig can override a provider-supplied tag on a matching Cost.")
    backfill_until: Optional[str] = Field(default=None, description="The earliest month the VirtualTagConfig should be backfilled to.")
    collapsed_tag_keys: Optional[List[VirtualTagConfigCollapsedTagKey]] = Field(default=None, description="Tag keys to collapse values for.")
    values: Optional[List[VirtualTagConfigValue]] = Field(default=None, description="Values for the VirtualTagConfig, with match precedence determined by order in the list.")


class AsyncVirtualTagConfigUpdate(BaseModel):
    """AsyncVirtualTagConfigUpdate model"""

    request_id: str = Field(description="The request ID of the async virtual tag config update.")
    status_url: str = Field(description="The status path of the async virtual tag config update.")


class Workspaces(BaseModel):
    """Workspaces model"""

    links: Optional[Links] = Field(default=None)
    workspaces: List[Workspace]


class CreateWorkspace(BaseModel):
    """Create a workspace"""

    name: str = Field(description="Name of the workspace.")
    enable_currency_conversion: Optional[bool] = Field(default=True, description="Enable currency conversion for the workspace.")
    currency: Optional[str] = Field(default=None, description="Currency code for the workspace.")
    exchange_rate_date: Optional[str] = Field(default="daily_rate", description="The date to use for currency conversion.")


class UpdateWorkspace(BaseModel):
    """Update a workspace"""

    name: Optional[str] = Field(default=None, description="Name of the workspace.")
    enable_currency_conversion: Optional[bool] = Field(default=True, description="Enable currency conversion for the workspace.")
    currency: Optional[str] = Field(default=None, description="Currency code for the workspace.")
    exchange_rate_date: Optional[str] = Field(default="daily_rate", description="The date to use for currency conversion.")


class CreateBusinessMetricOrUpdateBusinessMetricDatadogMetricFields(BaseModel):
    """Datadog metric configuration fields"""

    integration_token: Optional[str] = Field(default=None, description="Integration token for the account from which you would like to fetch metrics.")
    query: Optional[str] = Field(default=None, description="Datadog metrics query string. e.g. sum:aws.applicationelb.request_count{region:us-east-1}.rollup(avg,daily)")


class CreateBusinessMetricOrUpdateBusinessMetricCloudwatchFields(BaseModel):
    """Cloudwatch configuration fields."""

    integration_token: Optional[str] = Field(default=None, description="Integration token for the account from which you would like to fetch metrics.")
    stat: Optional[str] = Field(default=None)
    region: Optional[str] = Field(default=None)
    namespace: Optional[str] = Field(default=None)
    metric_name: Optional[str] = Field(default=None)
    label_dimension: Optional[str] = Field(default=None)
    dimensions: Optional[List[BusinessInformationCustomField]] = Field(default=None)


class Settings(BaseModel):
    """Report settings."""

    include_credits: Optional[bool] = Field(default=False, description="Report will include credits.")
    include_refunds: Optional[bool] = Field(default=False, description="Report will include refunds.")
    include_discounts: Optional[bool] = Field(default=True, description="Report will include discounts.")
    include_tax: Optional[bool] = Field(default=True, description="Report will include tax.")
    amortize: Optional[bool] = Field(default=True, description="Report will amortize.")
    unallocated: Optional[bool] = Field(default=False, description="Report will show unallocated costs.")
    aggregate_by: Optional[str] = Field(default="cost", description="Report will aggregate by cost or usage.")
    show_previous_period: Optional[bool] = Field(default=True, description="Report will show previous period costs or usage comparison.")


class BillingInformationAttributes(BaseModel):
    """Billing address and contact information (MSP invoicing accounts only)"""

    id: Optional[int] = Field(default=None)
    token: Optional[str] = Field(default=None)
    company_name: Optional[str] = Field(default=None, description="Company name for billing")
    country_code: Optional[str] = Field(default=None, description="ISO country code")
    address_line_1: Optional[str] = Field(default=None, description="First line of billing address")
    address_line_2: Optional[str] = Field(default=None, description="Second line of billing address")
    city: Optional[str] = Field(default=None, description="City for billing address")
    state: Optional[str] = Field(default=None, description="State or province for billing address")
    postal_code: Optional[str] = Field(default=None, description="Postal or ZIP code")
    billing_email: Optional[List[str]] = Field(default=None, description="Array of billing email addresses")


class BusinessInformationAttributes(BaseModel):
    """Business information and custom fields (MSP invoicing accounts only)"""

    id: Optional[int] = Field(default=None)
    token: Optional[str] = Field(default=None)
    metadata: Optional[BusinessInformationMetadata] = Field(default=None, description="Business metadata including custom fields")


class ReportSettings(BaseModel):
    """Report settings configurable on top-level Segments."""

    include_credits: Optional[bool] = Field(default=None, description="Reports created under this Segment will include credits.")
    include_refunds: Optional[bool] = Field(default=None, description="Reports created under this Segment will include refunds.")
    include_discounts: Optional[bool] = Field(default=None, description="Reports created under this Segment will include discounts.")
    include_tax: Optional[bool] = Field(default=None, description="Reports created under this Segment will include tax.")
    amortize: Optional[bool] = Field(default=None, description="Reports created under this Segment will amortize.")

