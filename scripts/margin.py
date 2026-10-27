"""Margin math for a marketplace listing. Prices in reais."""
from __future__ import annotations

import argparse

COMMISSION = 0.115  # Mercado Livre "Clássico" at the time of writing; check the current rate


def min_price(cost: float, freight: float, margin: float = 0.20, commission: float = COMMISSION) -> float:
    """Lowest price that still leaves `margin` of the price as profit."""
    if cost < 0 or freight < 0:
        raise ValueError("custo e frete não podem ser negativos")
    if not 0 <= margin < 1 - commission:
        raise ValueError("margem + comissão deve ficar abaixo de 100%")
    return round((cost + freight) / (1 - commission - margin), 2)


def profit(price: float, cost: float, freight: float, commission: float = COMMISSION) -> tuple[float, float]:
    """Returns (profit in reais, margin over the price)."""
    if price <= 0:
        raise ValueError("preço deve ser positivo")
    net = round(price * (1 - commission) - freight - cost, 2)
    return net, round(net / price, 4)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cost", type=float)
    ap.add_argument("freight", type=float)
    ap.add_argument("--margin", type=float, default=0.20)
    ap.add_argument("--price", type=float, help="se informado, calcula lucro e margem desse preço")
    a = ap.parse_args()
    if a.price is not None:
        net, margin = profit(a.price, a.cost, a.freight)
        print(f"lucro: R$ {net:.2f}, margem: {margin:.1%}")
    else:
        print(f"preço mínimo para {a.margin:.0%}: R$ {min_price(a.cost, a.freight, a.margin):.2f}")


if __name__ == "__main__":
    main()
