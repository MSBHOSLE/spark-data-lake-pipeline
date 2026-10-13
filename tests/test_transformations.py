import unittest
from src.transformations import aggregate_to_gold, transform_to_silver


class TestMedallionPipeline(unittest.TestCase):
    def test_bronze_to_silver_deduplication_and_cleansing(self):
        raw = [
            {"event_id": "EV-1", "user_id": "U100", "amount": 50.0, "event_type": "purchase"},
            {"event_id": "EV-1", "user_id": "U100", "amount": 50.0, "event_type": "purchase"},  # Duplicate
            {"event_id": "EV-2", "user_id": "", "amount": 30.0, "event_type": "view"},          # Invalid user
            {"event_id": "EV-3", "user_id": "U101", "amount": -10.0, "event_type": "refund"},    # Negative
            {"event_id": "EV-4", "user_id": "U100", "amount": 100.5, "event_type": "purchase"},
        ]

        silver = transform_to_silver(raw)
        self.assertEqual(len(silver), 2)
        self.assertEqual(silver[0]["event_id"], "EV-1")
        self.assertEqual(silver[1]["event_id"], "EV-4")

    def test_silver_to_gold_aggregation(self):
        silver = [
            {"event_id": "EV-1", "user_id": "U100", "amount": 50.0, "event_type": "PURCHASE"},
            {"event_id": "EV-4", "user_id": "U100", "amount": 100.5, "event_type": "PURCHASE"},
            {"event_id": "EV-5", "user_id": "U200", "amount": 25.0, "event_type": "PURCHASE"},
        ]

        gold = aggregate_to_gold(silver)
        self.assertEqual(len(gold), 2)

        u100 = next(g for g in gold if g["user_id"] == "U100")
        self.assertEqual(u100["total_events"], 2)
        self.assertEqual(u100["total_revenue"], 150.5)


if __name__ == "__main__":
    unittest.main()
