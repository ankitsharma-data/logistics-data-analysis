import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("data/logistics_data.csv")
FIG = Path("reports/figures")
FIG.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)

# Basic cleaning
df = df.drop_duplicates()
df["order_date"] = pd.to_datetime(df["order_date"])

# KPIs
on_time_rate = (1 - df["delay_flag"].mean()) * 100
avg_delivery_time = df["delivery_days"].mean()
cost_per_shipment = df["shipping_cost"].sum() / df["shipment_count"].sum()
delay_rate = df["delay_flag"].mean() * 100

print("LOGISTICS KPI SUMMARY")
print(f"On-Time Delivery Rate: {on_time_rate:.2f}%")
print(f"Average Delivery Time: {avg_delivery_time:.2f} days")
print(f"Cost per Shipment: ₹{cost_per_shipment:.2f}")
print(f"Delay Rate: {delay_rate:.2f}%")

# Route/warehouse performance
warehouse_perf = (
    df.groupby("warehouse")
      .agg(shipments=("shipment_id", "count"),
           avg_delivery_days=("delivery_days", "mean"),
           delay_rate=("delay_flag", "mean"),
           avg_cost=("shipping_cost", "mean"))
      .sort_values("delay_rate", ascending=False)
)
warehouse_perf["delay_rate"] *= 100
print("\nWAREHOUSE PERFORMANCE")
print(warehouse_perf.round(2))

# Visualization 1: delay rate by warehouse
warehouse_perf["delay_rate"].plot(kind="bar", title="Delay Rate by Warehouse",
                                  xlabel="Warehouse", ylabel="Delay Rate (%)")
plt.tight_layout()
plt.savefig(FIG / "delay_rate_by_warehouse.png", dpi=150)
plt.close()

# Visualization 2: distance vs delivery time
df.plot.scatter(x="distance_km", y="delivery_days",
                title="Distance vs Delivery Time")
plt.tight_layout()
plt.savefig(FIG / "distance_vs_delivery_time.png", dpi=150)
plt.close()
