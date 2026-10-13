from typing import Any, Dict, List


def transform_to_silver(raw_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Silver Layer Transformation: Cleanses, deduplicates, and validates data."""
    silver = []
    seen_ids = set()

    for r in raw_records:
        rec_id = r.get("event_id")
        amount = r.get("amount")

        # Validation rules: unique event_id, positive amount, non-empty user_id
        if not rec_id or rec_id in seen_ids:
            continue
        if amount is None or float(amount) < 0:
            continue
        if not r.get("user_id"):
            continue

        seen_ids.add(rec_id)
        silver.append({
            "event_id": str(rec_id),
            "user_id": str(r["user_id"]),
            "event_type": str(r.get("event_type", "unknown")).upper(),
            "amount": round(float(amount), 2),
            "timestamp": str(r.get("timestamp", "")),
        })

    return silver


def aggregate_to_gold(silver_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Gold Layer Transformation: Computes aggregated user-level business KPIs."""
    user_metrics: Dict[str, Dict[str, Any]] = {}

    for r in silver_records:
        u_id = r["user_id"]
        if u_id not in user_metrics:
            user_metrics[u_id] = {
                "user_id": u_id,
                "total_events": 0,
                "total_revenue": 0.0,
            }

        user_metrics[u_id]["total_events"] += 1
        user_metrics[u_id]["total_revenue"] += r["amount"]

    for metrics in user_metrics.values():
        metrics["total_revenue"] = round(metrics["total_revenue"], 2)

    return list(user_metrics.values())
