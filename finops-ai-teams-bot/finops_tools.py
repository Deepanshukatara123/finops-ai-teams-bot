# placeholder for usage analyzer function

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import QueryDefinition, QueryTimePeriod, QueryDataset, QueryAggregation
from datetime import datetime, timedelta
import os

SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
cost_client = CostManagementClient(credential)

def analyze_usage():
    underutilized_resources = []
    resources = resource_client.resources.list()

    for resource in resources:
        if "virtualMachines" in resource.type.lower():
            underutilized_resources.append({
                "name": resource.name,
                "type": resource.type,
                "location": resource.location,
                "id": resource.id
            })

    time_period = QueryTimePeriod(
        from_property=(datetime.utcnow() - timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        to=(datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%SZ')
    )

    query_definition = QueryDefinition(
        type="Usage",
        timeframe="Custom",
        time_period=time_period,
        dataset=QueryDataset(
            granularity="None",
            aggregation={
                "totalCost": QueryAggregation(
                    name="PreTaxCost",
                    function="Sum"
                )
            }
        )
    )

    scope = f"/subscriptions/{SUBSCRIPTION_ID}"
    cost_data = cost_client.query.usage(scope, query_definition)

    for item in cost_data.rows:
        resource_id = item[0]
        cost = item[1]
        try:
            cost = float(cost)
            if cost < 10:
                underutilized_resources.append({
                    "name": resource_id.split('/')[-1],
                    "type": "Unknown",
                    "location": "Unknown",
                    "id": resource_id,
                    "cost": cost
                })
        except:
            continue

    return underutilized_resources
